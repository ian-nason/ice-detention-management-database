---
license: cc0-1.0
pretty_name: ICE detention-management statistics
---

# ICE detention-management statistics

Frozen Datapond snapshot: 22 data tables, 58,810 stored source rows,
10,498,048 bytes. The catalog identifier requires separate registry integration.
Row totals mix table units and are not unique people, events or places.

| Table | Rows | Unit | Time semantics |
|---|---:|---|---|
| `dtm_adp_and_stay_length_by_agency_fy_ytd` | 1,551 | FY-to-date average daily population (people) and mean stay length (days) | snapshot |
| `dtm_adp_and_stay_length_by_agency_monthly` | 1,164 | Monthly average daily population (people) and mean stay length (days) | latest_cell |
| `dtm_atd_by_aor` | 14,657 | Active alternative-to-detention participants and average days in program by AOR/technology; nullable technology is a subtotal | snapshot |
| `dtm_atd_court_appearances` | 462 | Appearance count and percentage by hearing type and outcome; includes totals | snapshot |
| `dtm_atd_population` | 1,099 | Active participants; technology rows report daily cost USD, status rows report ALIP days | snapshot |
| `dtm_bond_stats` | 330 | Counts, percent, USD average bond, or ALOS days, distinguished by unit | latest_cell |
| `dtm_book_ins_by_arresting_agency_fy_ytd` | 387 | FY-to-date count of book-ins by ICE/CBP/Total | snapshot |
| `dtm_book_ins_by_arresting_agency_monthly` | 282 | Monthly book-in count by ICE/CBP/Total | latest_cell |
| `dtm_book_outs_by_reason_fy_ytd` | 4,521 | FY-to-date final release/book-out count by reason and criminality | snapshot |
| `dtm_book_outs_by_reason_monthly` | 2,606 | Monthly final release/book-out count by reason and criminality | latest_cell |
| `dtm_currently_detained_by_criminality` | 1,536 | Detained population count and arresting-agency share within each criminality category (fraction; source rounding retained) | snapshot |
| `dtm_currently_detained_by_disposition` | 1,738 | Current detention population count by processing disposition and facility type | snapshot |
| `dtm_facilities` | 20,430 | Facility-by-release characteristics: beds, threat composition, inspection information; not the geocoded facility directory | snapshot |
| `dtm_facility_alos` | 2,045 | Annual mean stay length (days) for named facility | latest_cell |
| `dtm_fear_decision_time` | 21 | Time from USCIS fear decision to ICE release (days), fiscal-year/facility-type series | latest_cell |
| `dtm_fear_decisions_by_facility_type` | 348 | Current detained count in fear-decision source table by facility type | snapshot |
| `dtm_iclos_and_detainees` | 1,665 | Mid/end-month population count by ICLOS/detainees section and duration bucket | latest_cell |
| `dtm_movements_by_facility_type` | 1,875 | FY-to-date book-in/book-out counts by facility type; book-outs only have Total criminality | snapshot |
| `dtm_removals` | 128 | FY-to-date removal counts including family-unit removals; not individual-removal events | snapshot |
| `dtm_segregation` | 1,383 | Monthly segregation-placement count per facility; placements are not unique people | latest_cell |
| `dtm_special_population_actions` | 468 | Annual action counts for special populations; nullable country applies only to country tables | latest_cell |
| `dtm_vulnerable_population` | 114 | Quarterly segregation placement counts and average consecutive/cumulative days for vulnerable populations | latest_cell |

## Source, scope and limitations

This frozen source has maximum file_date July 20, 2026 and pull_date July 9 or 11, despite an October 27 repository commit. It is not current November statistics. Observation periods, source extraction dates, workbook publication dates and commit dates are different concepts.

Twelve tables retain release snapshots; ten retain the latest reported cell for their series key. Never sum FY-to-date snapshots, stock populations across dates, averages, or totals together with components. Totals coexist with detailed rows, and missing categories are not zero. Use the declared series dimensions and a single pull-date snapshot for comparisons. fiscal_year can describe the workbook; data_fiscal_year, alos_fiscal_year or date identifies the measured period when present.

Units vary among counts, USD, days and fractions. `share_of_total` divides each arresting agency's count by the combined ICE+CBP population within that criminality category and pull date. It is not the criminality composition within an agency. All 1,024 nonmissing shares match this denominator within 0.005, reflecting source rounding. The bond_pct series is labelled percent upstream but stores fractions (observed 0.0234378 to 0.279019); ATD court pct values are also fractions (observed about 0.00543 to 1). Convert to percentage points explicitly for display. Seven upstream ATD average-length-in-program values are negative (minimum -7); they are preserved as source anomalies, not meaningful negative durations. Flag or exclude them explicitly for duration analysis.

The upstream parser skips some corrupted sheets and omits zero ICLOS/bond cells as presumed placeholders. These omissions are retained; absence is not a measured zero. dtm_facilities is facility-by-release statistics, not the geocoded directory. No name-based join to microdata or the directory is supplied.

All 21 source-defined candidate keys are unique under NULL-aware grouping; dtm_facilities has no verified natural key and retains _source_row. All source rows/columns are preserved, including anomalies. Independent checks find no file_date before pull_date or observation date after pull_date. ICE plus CBP equals Total in the inspected 129 YTD and 94 monthly book-in series.

Every source byte hash, immutable URL and repository commit is in
[source-lock.json](source-lock.json). Every row is retained; `_source_row` is added
as an ordinal within the pinned member. Geometry, when present, is stored as WKB
in `geometry_wkb`, with all original metadata in `_geometry_metadata`. `_provenance`,
`_metadata` and `_columns` document the build. [DICTIONARY.md](DICTIONARY.md) records
types, exact NULL counts, units and time semantics. Original source flags and text
are not coerced into new numeric categories.

Publisher: [Deportation Data Project](https://deportationdata.org/data/processed/ice.html).
Data license: CC0-1.0, as labelled by the publisher; see the retained license notes.
Cite government data collated by the Deportation Data Project and the pinned source
commit. Repository commit dates do not promise current observations or automatic refreshes.

## Local queries

```python
import duckdb
con = duckdb.connect('ice-detention-management.duckdb', read_only=True,
                     config={'memory_limit':'128MiB','threads':'1'})
try:
    print(con.sql("SELECT fiscal_year, pull_date, n_book_ins_ytd FROM dtm_book_ins_by_arresting_agency_fy_ytd WHERE arresting_agency='Total' QUALIFY row_number() OVER (PARTITION BY fiscal_year ORDER BY pull_date DESC, file_date DESC)=1 ORDER BY fiscal_year DESC LIMIT 3").fetchall())
finally:
    con.close()
```

```r
library(DBI)
con <- dbConnect(duckdb::duckdb(), dbdir='ice-detention-management.duckdb', read_only=TRUE)
tryCatch({
  dbExecute(con, "SET memory_limit='128MiB'")
  dbExecute(con, 'SET threads=1')
  print(dbGetQuery(con, "SELECT fiscal_year, pull_date, n_book_ins_ytd FROM dtm_book_ins_by_arresting_agency_fy_ytd WHERE arresting_agency='Total' QUALIFY row_number() OVER (PARTITION BY fiscal_year ORDER BY pull_date DESC, file_date DESC)=1 ORDER BY fiscal_year DESC LIMIT 3"))
}, finally=dbDisconnect(con, shutdown=TRUE))
```

Public datapond identifier `ice-detention-management` requires a future approved catalog release.
The smoke scripts use an isolated localhost registry, never a global registry edit.

## Reproduce and refresh

Use Python 3.11 or newer in a dedicated environment. Install the exact tested dependencies with `python -m pip install -r requirements.txt` (or use the pinned uv source in pyproject.toml), then:

```sh
python acquire_sources.py
python build_database.py --validate-only --report fresh-validation.json
python build_database.py --output fresh-ice-detention-management.duckdb
```

Downloads are pinned, bounded and SHA-verified; existing source files are checked
and reused. The importer preserves all source fields and compares every stored
row with the input using symmetric EXCEPT ALL. It uses one thread, 128 MiB DuckDB
memory, no spill, a 32 MiB working-file cap
and a 512 MiB physical free-space reserve. A watchdog interrupts work when a budget
is crossed. Builds are private until complete; hard-link publication refuses an
existing final database, manifest or orphan WAL path. Synchronous checks enforce the working-file cap and physical reserve after close and before publication; hash checks remain enabled under optimized Python. Failed/private files remain for inspection, with no cleanup
of unrelated work. Peak process memory can exceed DuckDB's buffer limit.

To refresh, review the publisher's changed files and definitions, update pins and
expected schemas/counts, run full source checks and Python/R smoke tests, and audit
both data and documentation. No scheduled or unattended refresh is configured.

Source transformation semantics were checked against the [pinned publisher parser](https://github.com/deportationdata/ice-detention-management/blob/5126c6e8482cb8d28d5a7704e96a9cab0df8b528/code/parse-spreadsheets.R). Facility composition and inspection fields retain changing source text layouts; no unsupported numeric scale or crosswalk is imposed.

Validation commands: `python -m unittest -v test_safety.py` and `python run_smoke.py --python /path/to/python --rscript /path/to/Rscript --r-library /path/to/R/library`. The latter needs the released Python and R datapond packages and an already installed HTTPFS extension. It uses only localhost and this database. See VALIDATION.md for the executed versions and results.

## Snapshot files

[Download the database](https://huggingface.co/datasets/Nason/ice-detention-management-database/resolve/main/ice-detention-management.duckdb), [browse its files](https://huggingface.co/datasets/Nason/ice-detention-management-database/tree/main), or inspect the [reproducible source](https://github.com/ian-nason/ice-detention-management-database). Verify the snapshot SHA-256 `b29a199fe88141973912af8b62a3c4d26dc0bf51f7ccc097a528176e385e9201` (10,498,048 bytes). The registry PR pins immutable Hugging Face revisions; a later `main` may refer to a newer snapshot.

Once the separate catalog entry is merged, use the released clients:

```python
import datapond
con = datapond.connect("ice-detention-management")
try:
    print(con.sql("SELECT fiscal_year, pull_date, n_book_ins_ytd FROM dtm_book_ins_by_arresting_agency_fy_ytd WHERE arresting_agency='Total' QUALIFY row_number() OVER (PARTITION BY fiscal_year ORDER BY pull_date DESC, file_date DESC)=1 ORDER BY fiscal_year DESC LIMIT 3").fetchall())
finally:
    con.close()
```

```r
library(datapond)
con <- dp_connect("ice-detention-management")
tryCatch(print(DBI::dbGetQuery(con, "SELECT fiscal_year, pull_date, n_book_ins_ytd FROM dtm_book_ins_by_arresting_agency_fy_ytd WHERE arresting_agency='Total' QUALIFY row_number() OVER (PARTITION BY fiscal_year ORDER BY pull_date DESC, file_date DESC)=1 ORDER BY fiscal_year DESC LIMIT 3")), finally=DBI::dbDisconnect(con, shutdown=TRUE))
```

Until catalog integration, the local Python/R examples above work with the downloaded snapshot. The smoke scripts exercise both released clients with an isolated registry and this same database.
