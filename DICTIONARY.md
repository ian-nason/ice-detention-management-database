# ICE detention-management statistics — dictionary

All original source fields retain their source meanings. The table unit and time semantics below are required context; names alone do not define a universal measure. Exact NULL counts are distinct from empty strings, empty geometry and source-coded missingness. See README for known anomalies and the immutable source lock.

## dtm_adp_and_stay_length_by_agency_fy_ytd

FY-to-date average daily population (people) and mean stay length (days). Time semantics: snapshot.

Candidate key: agency, criminality, fiscal_year, pull_date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `agency` | VARCHAR | 0 | Source agency category for the population/duration measure; total rows may coexist with components. |
| `criminality` | VARCHAR | 0 | Source criminality category, including totals where present; not an independently adjudicated status. |
| `adp_fy_ytd` | DOUBLE | 6 | Fiscal-year-to-date average daily detained population, in people; do not sum across snapshots. |
| `avg_stay_length_days_fy_ytd` | DOUBLE | 3 | Source fiscal-year-to-date mean detention duration in days. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_adp_and_stay_length_by_agency_monthly

Monthly average daily population (people) and mean stay length (days). Time semantics: latest_cell.

Candidate key: agency, criminality, date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `agency` | VARCHAR | 0 | Source agency category for the population/duration measure; total rows may coexist with components. |
| `criminality` | VARCHAR | 0 | Source criminality category, including totals where present; not an independently adjudicated status. |
| `month` | VARCHAR | 0 | Original source month label; use date when a normalized observation month is provided. |
| `date` | DATE | 0 | Observation date/month anchor; ICLOS mid/end-month timing is additionally distinguished by period. |
| `adp` | DOUBLE | 72 | Average daily detained population for the indicated month, in people. |
| `avg_stay_length_days` | DOUBLE | 36 | Source monthly mean detention duration in days. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_atd_by_aor

Active alternative-to-detention participants and average days in program by AOR/technology; nullable technology is a subtotal. Time semantics: snapshot.

Candidate key: aor, technology, pull_date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `aor` | VARCHAR | 0 | Source area-of-responsibility label; no automatic crosswalk to the reference AOR table. |
| `technology` | VARCHAR | 3,166 | ATD technology category; NULL rows are source subtotals and must not be summed with components. |
| `n_active` | DOUBLE | 5 | Active ATD participant count for the stated category/snapshot; repeated snapshots overlap. |
| `avg_length_in_program` | DOUBLE | 5 | Mean program duration in days; seven negative source anomalies are retained. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_atd_court_appearances

Appearance count and percentage by hearing type and outcome; includes totals. Time semantics: snapshot.

Candidate key: hearing_type, metric, pull_date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `hearing_type` | VARCHAR | 0 | Source type of court hearing, retained as a categorical dimension. |
| `metric` | VARCHAR | 0 | Source measure/outcome category; interpret jointly with unit and other dimensions. |
| `count` | DOUBLE | 0 | Court-appearance count for the hearing type/outcome; total rows coexist with components. |
| `pct` | DOUBLE | 0 | Court-appearance share stored as a fraction from 0 to 1, despite the percent-like name. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_atd_population

Active participants; technology rows report daily cost USD, status rows report ALIP days. Time semantics: snapshot.

Candidate key: table, category, pull_date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `table` | VARCHAR | 0 | Source ATD subtable discriminator, separating technology and participant-status sections. |
| `category` | VARCHAR | 0 | Category within the source ATD subtable; categories from different subtables are not disjoint. |
| `n_active` | DOUBLE | 0 | Active ATD participant count for the stated category/snapshot; repeated snapshots overlap. |
| `daily_tech_cost` | DOUBLE | 596 | Source daily technology cost in USD; a per-participant denominator is not inferred. |
| `alip` | DOUBLE | 503 | Average length in the ATD program, in days, for the source participant-status category. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_bond_stats

Counts, percent, USD average bond, or ALOS days, distinguished by unit. Time semantics: latest_cell.

Candidate key: date, metric.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `month` | VARCHAR | 0 | Original source month label; use date when a normalized observation month is provided. |
| `date` | DATE | 0 | Observation date/month anchor; ICLOS mid/end-month timing is additionally distinguished by period. |
| `metric` | VARCHAR | 0 | Source measure/outcome category; interpret jointly with unit and other dimensions. |
| `unit` | VARCHAR | 0 | Source unit label; percent-labelled bond values are stored as fractions. |
| `value` | DOUBLE | 0 | Source measure, interpreted jointly with metric/unit and table dimensions. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_book_ins_by_arresting_agency_fy_ytd

FY-to-date count of book-ins by ICE/CBP/Total. Time semantics: snapshot.

Candidate key: arresting_agency, fiscal_year, pull_date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `arresting_agency` | VARCHAR | 0 | Source arresting agency category, including ICE, CBP and Total; separate total from components. |
| `n_book_ins_ytd` | DOUBLE | 0 | Fiscal-year-to-date book-in count; count of admissions, not unique people. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_book_ins_by_arresting_agency_monthly

Monthly book-in count by ICE/CBP/Total. Time semantics: latest_cell.

Candidate key: arresting_agency, date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `arresting_agency` | VARCHAR | 0 | Source arresting agency category, including ICE, CBP and Total; separate total from components. |
| `month` | VARCHAR | 0 | Original source month label; use date when a normalized observation month is provided. |
| `date` | DATE | 0 | Observation date/month anchor; ICLOS mid/end-month timing is additionally distinguished by period. |
| `n_book_ins` | DOUBLE | 0 | Monthly book-in count; count of admissions, not unique people. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_book_outs_by_reason_fy_ytd

FY-to-date final release/book-out count by reason and criminality. Time semantics: snapshot.

Candidate key: release_reason, criminality, fiscal_year, pull_date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `release_reason` | VARCHAR | 0 | Source final release/book-out reason category. |
| `criminality` | VARCHAR | 0 | Source criminality category, including totals where present; not an independently adjudicated status. |
| `n_book_outs_ytd` | DOUBLE | 0 | Fiscal-year-to-date final release/book-out count, not unique people. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_book_outs_by_reason_monthly

Monthly final release/book-out count by reason and criminality. Time semantics: latest_cell.

Candidate key: release_reason, criminality, date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `release_reason` | VARCHAR | 0 | Source final release/book-out reason category. |
| `criminality` | VARCHAR | 0 | Source criminality category, including totals where present; not an independently adjudicated status. |
| `month` | VARCHAR | 0 | Original source month label; use date when a normalized observation month is provided. |
| `date` | DATE | 0 | Observation date/month anchor; ICLOS mid/end-month timing is additionally distinguished by period. |
| `n_book_outs` | DOUBLE | 1 | Monthly final release/book-out count, not unique people. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_currently_detained_by_criminality

Detained population count and arresting-agency share within each criminality category (fraction; source rounding retained). Time semantics: snapshot.

Candidate key: criminality, arresting_agency, pull_date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `criminality` | VARCHAR | 0 | Source criminality category, including totals where present; not an independently adjudicated status. |
| `arresting_agency` | VARCHAR | 0 | Source arresting agency category, including ICE, CBP and Total; separate total from components. |
| `n_detained` | DOUBLE | 0 | Detained population stock at the source snapshot; do not sum across dates. |
| `share_of_total` | DOUBLE | 512 | Fraction of the combined ICE+CBP population within the same criminality category and pull_date; source rounding is retained. Not a within-agency criminality share. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_currently_detained_by_disposition

Current detention population count by processing disposition and facility type. Time semantics: snapshot.

Candidate key: disposition, facility_type, pull_date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `disposition` | VARCHAR | 0 | Source processing-disposition category, including totals where present. |
| `facility_type` | VARCHAR | 0 | Source facility-type grouping; not an individual facility identifier. |
| `n_detained` | DOUBLE | 0 | Detained population stock at the source snapshot; do not sum across dates. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_facilities

Facility-by-release characteristics: beds, threat composition, inspection information; not the geocoded facility directory. Time semantics: snapshot.

Candidate key: No asserted natural key; preserve _source_row.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `name` | VARCHAR | 0 | Facility name reported by the source; names are not stable facility identifiers. |
| `address` | VARCHAR | 236 | Institutional street address as recorded by the source. |
| `city` | VARCHAR | 235 | City label associated with the reported address. |
| `state` | VARCHAR | 240 | State or territory label associated with the source location. |
| `zip` | VARCHAR | 236 | Postal ZIP code retained as text, preserving leading zeros. |
| `aor` | VARCHAR | 235 | Source area-of-responsibility label; no automatic crosswalk to the reference AOR table. |
| `type_detailed` | VARCHAR | 235 | Detailed source facility classification, retained without recoding. |
| `male_female` | VARCHAR | 561 | Source facility sex-accommodation label, retained without recoding. |
| `level_a` | VARCHAR | 345 | Source facility composition/risk field (level_a), retained verbatim; text percentages, counts and missing markers are not automatically numeric. |
| `level_b` | VARCHAR | 263 | Source facility composition/risk field (level_b), retained verbatim; text percentages, counts and missing markers are not automatically numeric. |
| `level_c` | VARCHAR | 263 | Source facility composition/risk field (level_c), retained verbatim; text percentages, counts and missing markers are not automatically numeric. |
| `level_d` | VARCHAR | 263 | Source facility composition/risk field (level_d), retained verbatim; text percentages, counts and missing markers are not automatically numeric. |
| `male_crim` | VARCHAR | 263 | Source facility composition/risk field (male_crim), retained verbatim; text percentages, counts and missing markers are not automatically numeric. |
| `male_non_crim` | VARCHAR | 263 | Source facility composition/risk field (male_non_crim), retained verbatim; text percentages, counts and missing markers are not automatically numeric. |
| `female_crim` | VARCHAR | 263 | Source facility composition/risk field (female_crim), retained verbatim; text percentages, counts and missing markers are not automatically numeric. |
| `female_non_crim` | VARCHAR | 263 | Source facility composition/risk field (female_non_crim), retained verbatim; text percentages, counts and missing markers are not automatically numeric. |
| `ice_threat_level_1` | VARCHAR | 264 | Source facility composition/risk field (ice_threat_level_1), retained verbatim; text percentages, counts and missing markers are not automatically numeric. |
| `ice_threat_level_2` | VARCHAR | 263 | Source facility composition/risk field (ice_threat_level_2), retained verbatim; text percentages, counts and missing markers are not automatically numeric. |
| `ice_threat_level_3` | VARCHAR | 263 | Source facility composition/risk field (ice_threat_level_3), retained verbatim; text percentages, counts and missing markers are not automatically numeric. |
| `no_ice_threat_level` | VARCHAR | 263 | Source facility composition/risk field (no_ice_threat_level), retained verbatim; text percentages, counts and missing markers are not automatically numeric. |
| `mandatory` | VARCHAR | 371 | Source mandatory field preserved verbatim; no boolean or numeric meaning is imposed. |
| `guaranteed_minimum` | VARCHAR | 10,186 | Source guaranteed-minimum field retained verbatim; do not interpret as occupied population. |
| `last_inspection_type` | VARCHAR | 1,043 | Source inspection field: last inspection type. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `last_inspection_standard` | VARCHAR | 5,853 | Source inspection field: last inspection standard. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `last_inspection_rating_final` | VARCHAR | 12,788 | Source inspection field: last inspection rating final. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `last_inspection_date` | VARCHAR | 11,550 | Source inspection field: last inspection date. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `second_to_last_inspection_type` | VARCHAR | 10,763 | Source inspection field: second to last inspection type. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `s2l_inspection_standard` | VARCHAR | 12,120 | Source inspection field: s2l inspection standard. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `second_to_last_inspection_rating` | VARCHAR | 15,167 | Source inspection field: second to last inspection rating. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `second_to_last_inspection_date` | VARCHAR | 12,161 | Source inspection field: second to last inspection date. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `odo_inspection_end_date` | VARCHAR | 17,155 | Source inspection field: odo inspection end date. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `odo_last_inspection_standard` | VARCHAR | 16,928 | Source inspection field: odo last inspection standard. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `odo_final_rating` | VARCHAR | 16,928 | Source inspection field: odo final rating. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `last_nak_inspection_standard` | VARCHAR | 17,918 | Source inspection field: last nak inspection standard. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `last_nak_inspection_rating` | VARCHAR | 17,922 | Source inspection field: last nak inspection rating. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `last_nakamoto_inspection_date` | VARCHAR | 17,918 | Source inspection field: last nakamoto inspection date. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `s2l_nak_inspection_type` | VARCHAR | 17,918 | Source inspection field: s2l nak inspection type. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `last_inspection_end_date` | VARCHAR | 14,591 | Source inspection field: last inspection end date. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `pending_fy25_inspection` | VARCHAR | 19,287 | Source inspection field: pending fy25 inspection. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `last_final_rating` | VARCHAR | 14,639 | Source inspection field: last final rating. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `odo_final_report_date` | VARCHAR | 20,192 | Source inspection field: odo final report date. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `pending_fy24_inspection` | VARCHAR | 20,333 | Source inspection field: pending fy24 inspection. Names and values are retained across changing workbook layouts; date-like text is not silently parsed. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_facility_alos

Annual mean stay length (days) for named facility. Time semantics: latest_cell.

Candidate key: name, alos_fiscal_year.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `name` | VARCHAR | 0 | Facility name reported by the source; names are not stable facility identifiers. |
| `alos_fiscal_year` | INTEGER | 0 | Fiscal year of the reported facility mean length of stay, distinct from workbook fiscal_year. |
| `alos` | DOUBLE | 2 | Reported facility average length of detention stay, in days. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_fear_decision_time

Time from USCIS fear decision to ICE release (days), fiscal-year/facility-type series. Time semantics: latest_cell.

Candidate key: data_fiscal_year, facility_type.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `data_fiscal_year` | INTEGER | 0 | Fiscal year of the measured series, distinct from the workbook fiscal_year. |
| `facility_type` | VARCHAR | 0 | Source facility-type grouping; not an individual facility identifier. |
| `decision_days` | DOUBLE | 0 | Reported time in days from USCIS fear decision to ICE release. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_fear_decisions_by_facility_type

Current detained count in fear-decision source table by facility type. Time semantics: snapshot.

Candidate key: facility_type, pull_date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `facility_type` | VARCHAR | 0 | Source facility-type grouping; not an individual facility identifier. |
| `total_detained` | DOUBLE | 0 | Current detained stock in the fear-decision source table for the specified facility type. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_iclos_and_detainees

Mid/end-month population count by ICLOS/detainees section and duration bucket. Time semantics: latest_cell.

Candidate key: section, population_type, duration_bucket, date, period.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `section` | VARCHAR | 0 | Source ICLOS/detainees section; keep this dimension when interpreting values. |
| `population_type` | VARCHAR | 0 | Source population classification within the ICLOS/detainees section. |
| `duration_bucket` | VARCHAR | 290 | Source elapsed-duration category; buckets and totals must not be assumed disjoint. |
| `month` | VARCHAR | 0 | Original source month label; use date when a normalized observation month is provided. |
| `date` | DATE | 0 | Observation date/month anchor; ICLOS mid/end-month timing is additionally distinguished by period. |
| `period` | VARCHAR | 0 | Source mid-month/end-month observation marker. |
| `value` | DOUBLE | 0 | Source population count for the section, population type, duration bucket and observation period; zero placeholders were omitted upstream. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_movements_by_facility_type

FY-to-date book-in/book-out counts by facility type; book-outs only have Total criminality. Time semantics: snapshot.

Candidate key: facility_type, movement, criminality, pull_date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `facility_type` | VARCHAR | 0 | Source facility-type grouping; not an individual facility identifier. |
| `movement` | VARCHAR | 0 | Source book-in or book-out category; do not interpret a movement as a unique person. |
| `criminality` | VARCHAR | 0 | Source criminality category, including totals where present; not an independently adjudicated status. |
| `n_movements` | DOUBLE | 130 | Fiscal-year-to-date book-in/book-out count for the source facility type and criminality. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_removals

FY-to-date removal counts including family-unit removals; not individual-removal events. Time semantics: snapshot.

Candidate key: fiscal_year, pull_date.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `n_removals_fy_ytd` | DOUBLE | 0 | Fiscal-year-to-date reported removals; repeated snapshots are overlapping totals. |
| `famu_removals` | DOUBLE | 0 | Reported family-unit removals; do not add to total removals as an independent category. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_segregation

Monthly segregation-placement count per facility; placements are not unique people. Time semantics: latest_cell.

Candidate key: date, facility.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `month` | VARCHAR | 0 | Original source month label; use date when a normalized observation month is provided. |
| `date` | DATE | 0 | Observation date/month anchor; ICLOS mid/end-month timing is additionally distinguished by period. |
| `facility` | VARCHAR | 0 | Facility name in the segregation table, not a verified key to the reference directory. |
| `placement_count` | DOUBLE | 0 | Monthly count of segregation placements; individuals may have multiple placements. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_special_population_actions

Annual action counts for special populations; nullable country applies only to country tables. Time semantics: latest_cell.

Candidate key: population_group, action, data_fiscal_year, country.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `population_group` | VARCHAR | 0 | Source special-population classification; groups need not be disjoint. |
| `action` | VARCHAR | 0 | Source action category for a special population. |
| `data_fiscal_year` | INTEGER | 0 | Fiscal year of the measured series, distinct from the workbook fiscal_year. |
| `country` | VARCHAR | 81 | Country category for applicable source subtables; NULL is structural for other subtables. |
| `value` | DOUBLE | 0 | Annual count of the specified action for the population group and applicable country. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |

## dtm_vulnerable_population

Quarterly segregation placement counts and average consecutive/cumulative days for vulnerable populations. Time semantics: latest_cell.

Candidate key: placement_reason, data_fiscal_year, data_quarter.

| Field | SQL type | NULL rows | Meaning |
|---|---|---:|---|
| `_source_row` | BIGINT | 0 | Ordinal in the pinned source member; not a cross-release entity key. |
| `placement_reason` | VARCHAR | 0 | Source category/reason associated with vulnerable-population segregation placement. |
| `data_fiscal_year` | INTEGER | 0 | Fiscal year of the measured series, distinct from the workbook fiscal_year. |
| `data_quarter` | INTEGER | 0 | Fiscal quarter of the measured vulnerable-population series. |
| `n_placements` | DOUBLE | 0 | Quarterly count of segregation placements, not unique individuals. |
| `avg_consecutive_days` | DOUBLE | 0 | Source mean consecutive segregation duration, in days. |
| `avg_cumulative_days` | DOUBLE | 0 | Source mean cumulative segregation duration, in days. |
| `fiscal_year` | INTEGER | 0 | Source workbook fiscal year; measured period may use another date/year field. |
| `file_date` | DATE | 0 | Source-derived workbook release date, inferred from filenames and adjusted upstream to the latest known extract; not the observation period. |
| `pull_date` | DATE | 0 | Source extract date; repeated snapshots overlap. |
