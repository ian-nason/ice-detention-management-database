"""Small malformed-data regressions for the required DTM invariants."""
import unittest
import duckdb
from build_validation import validate_keys_and_dates,validate_criminality_totals

class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.con=duckdb.connect(config={'threads':'1','memory_limit':'128MiB','max_temp_directory_size':'0B'})
        self.con.execute('CREATE TABLE sample(key VARCHAR,date DATE,file_date DATE,pull_date DATE)')
        self.con.execute("INSERT INTO sample VALUES (NULL,'2026-01-01','2026-01-03','2026-01-02')")
    def tearDown(self):self.con.close()
    def check_dates(self):return validate_keys_and_dates(self.con,'sample',['key'],['date','file_date','pull_date'])
    def test_valid_nullable_key_and_dates(self):
        self.assertEqual(self.check_dates(),{'duplicate_key_groups':0,'file_before_pull_rows':0,'observation_after_pull_rows':0})
    def test_duplicate_nullable_key_rejected(self):
        self.con.execute('INSERT INTO sample SELECT * FROM sample')
        with self.assertRaisesRegex(ValueError,'Candidate-key duplicates'):self.check_dates()
    def test_file_before_pull_rejected(self):
        self.con.execute("UPDATE sample SET file_date='2026-01-01'")
        with self.assertRaisesRegex(ValueError,'File date before pull'):self.check_dates()
    def test_future_observation_rejected(self):
        self.con.execute("UPDATE sample SET date='2026-01-03'")
        with self.assertRaisesRegex(ValueError,'Observation date after pull'):self.check_dates()
    def criminality(self):
        self.con.execute('CREATE TABLE criminality(pull_date DATE,criminality VARCHAR,arresting_agency VARCHAR,n_detained INTEGER)')
        self.con.execute("INSERT INTO criminality VALUES ('2026-01-02','A','ICE',2),('2026-01-02','A','CBP',3),('2026-01-02','A','Total',5)")
    def test_criminality_total_matches_components(self):
        self.criminality()
        self.assertEqual(validate_criminality_totals(self.con,'criminality'),{'criminality_total_groups':1,'criminality_total_mismatches':0})
    def test_incorrect_total_rejected(self):
        self.criminality();self.con.execute("UPDATE criminality SET n_detained=6 WHERE arresting_agency='Total'")
        with self.assertRaisesRegex(ValueError,'Total must equal'):validate_criminality_totals(self.con,'criminality')
    def test_missing_component_rejected_even_when_sum_matches(self):
        self.criminality();self.con.execute("DELETE FROM criminality WHERE arresting_agency='CBP'");self.con.execute("UPDATE criminality SET n_detained=2 WHERE arresting_agency='Total'")
        with self.assertRaisesRegex(ValueError,'Total must equal'):validate_criminality_totals(self.con,'criminality')

if __name__=='__main__':unittest.main()
