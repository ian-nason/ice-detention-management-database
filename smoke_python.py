import importlib.metadata,json,sys
from pathlib import Path
from build_safety import require
import datapond,datapond.registry as registry,duckdb
registry.REGISTRY_URL=sys.argv[1]
registry.CACHE_DIR=Path(sys.argv[2]);registry.CACHE_FILE=registry.CACHE_DIR/'registry.json'
require(datapond.list()==['ice-detention-management'], "Smoke check failed")
con=datapond.connect('ice-detention-management',quiet=True)
try:
    con.execute("SET memory_limit='128MiB'");con.execute('SET threads=1');con.execute("SET max_temp_directory_size='0B'")
    for table,expected in {'dtm_adp_and_stay_length_by_agency_fy_ytd': 1551, 'dtm_adp_and_stay_length_by_agency_monthly': 1164, 'dtm_atd_by_aor': 14657, 'dtm_atd_court_appearances': 462, 'dtm_atd_population': 1099, 'dtm_bond_stats': 330, 'dtm_book_ins_by_arresting_agency_fy_ytd': 387, 'dtm_book_ins_by_arresting_agency_monthly': 282, 'dtm_book_outs_by_reason_fy_ytd': 4521, 'dtm_book_outs_by_reason_monthly': 2606, 'dtm_currently_detained_by_criminality': 1536, 'dtm_currently_detained_by_disposition': 1738, 'dtm_facilities': 20430, 'dtm_facility_alos': 2045, 'dtm_fear_decision_time': 21, 'dtm_fear_decisions_by_facility_type': 348, 'dtm_iclos_and_detainees': 1665, 'dtm_movements_by_facility_type': 1875, 'dtm_removals': 128, 'dtm_segregation': 1383, 'dtm_special_population_actions': 468, 'dtm_vulnerable_population': 114}.items():
        require(con.execute('SELECT count(*) FROM "'+table+'"').fetchone()[0]==expected, "Smoke check failed")
    require(con.execute('SELECT count(*) FROM _metadata').fetchone()[0]==22, "Smoke check failed")
    for sql,expected in [('SELECT count(*) FROM dtm_atd_by_aor WHERE avg_length_in_program<0', 7)]:require(con.execute(sql).fetchone()[0]==expected, "Smoke check failed")
    example=con.execute("SELECT fiscal_year, pull_date, n_book_ins_ytd FROM dtm_book_ins_by_arresting_agency_fy_ytd WHERE arresting_agency='Total' QUALIFY row_number() OVER (PARTITION BY fiscal_year ORDER BY pull_date DESC, file_date DESC)=1 ORDER BY fiscal_year DESC LIMIT 3").fetchall()
    print(json.dumps({'passed':True,'client':'Python datapond','version':importlib.metadata.version('datapond'),'duckdb':duckdb.__version__,'example':example},default=str))
finally:con.close()
