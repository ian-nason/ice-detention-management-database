"""Enforced source invariants; exceptions remain active under optimized Python."""
from build_safety import require

def quote(name):return '"'+name.replace('"','""')+'"'

def validate_keys_and_dates(con, table, candidate_key, date_columns):
    name=quote(table);result={}
    if candidate_key:
        keys=','.join(quote(k) for k in candidate_key)
        duplicates=con.execute(f'SELECT count(*) FROM (SELECT {keys} FROM {name} GROUP BY {keys} HAVING count(*)>1)').fetchone()[0]
        result['duplicate_key_groups']=duplicates
        require(duplicates==0,f'Candidate-key duplicates in {table}: {duplicates}')
    if {'file_date','pull_date'}<=set(date_columns):
        invalid=con.execute(f'SELECT count(*) FROM {name} WHERE file_date<pull_date').fetchone()[0]
        result['file_before_pull_rows']=invalid
        require(invalid==0,f'File date before pull date in {table}: {invalid}')
    # `date` is the observation-date field in the six applicable source tables.
    # Workbook releases, pull dates and fiscal-year labels are different clocks.
    if {'date','pull_date'}<=set(date_columns):
        invalid=con.execute(f'SELECT count(*) FROM {name} WHERE "date">pull_date').fetchone()[0]
        result['observation_after_pull_rows']=invalid
        require(invalid==0,f'Observation date after pull date in {table}: {invalid}')
    return result

def validate_criminality_totals(con, table='dtm_currently_detained_by_criminality'):
    groups,invalid=con.execute(f'''SELECT count(*),count(*) FILTER(WHERE
        ice_rows<>1 OR cbp_rows<>1 OR total_rows<>1 OR known_rows<>all_rows
        OR present_counts<>all_rows OR ice_count+cbp_count IS DISTINCT FROM total_count)
        FROM (SELECT pull_date,criminality,count(*) AS all_rows,
        count(*) FILTER(WHERE arresting_agency IN ('ICE','CBP','Total')) AS known_rows,
        count(n_detained) AS present_counts,
        count(*) FILTER(WHERE arresting_agency='ICE') AS ice_rows,
        count(*) FILTER(WHERE arresting_agency='CBP') AS cbp_rows,
        count(*) FILTER(WHERE arresting_agency='Total') AS total_rows,
        sum(n_detained) FILTER(WHERE arresting_agency='ICE') AS ice_count,
        sum(n_detained) FILTER(WHERE arresting_agency='CBP') AS cbp_count,
        sum(n_detained) FILTER(WHERE arresting_agency='Total') AS total_count
        FROM {quote(table)} GROUP BY pull_date,criminality)''').fetchone()
    require(groups>0 and invalid==0,f'Criminality Total must equal ICE+CBP with one row per agency: {invalid} invalid groups')
    return {'criminality_total_groups':groups,'criminality_total_mismatches':invalid}
