# Validation of the corrected local statistics candidate

## Current audit corrections, November 3, 2026

The newly built candidate is `ice-detention-management.duckdb`:
10,498,048 bytes, SHA-256
`b29a199fe88141973912af8b62a3c4d26dc0bf51f7ccc097a528176e385e9201`.
The previous database and manifest remain preserved. All 58,810 source rows,
source ordinals, provenance, geometry metadata and `_columns` are unchanged.
The new checks affect validation and do not repair or remove source values.

The builder now requires zero duplicate groups for all 21 declared candidate
keys, `file_date >= pull_date` across all 22 tables, and observation `date <=
pull_date` for the six applicable tables. It verifies one ICE, one CBP and one
Total row per criminality/pull group, with Total exactly ICE+CBP: 512 groups,
zero mismatches. All 1,024 nonmissing agency-share comparisons still pass within
0.005 rounding tolerance. Seven negative ATD duration values remain preserved.

Eighteen repository tests passed, including malformed nullable keys, reversed
file/pull dates, future observations, incorrect or incomplete criminality totals,
optimized-Python smoke failures, exclusive reports and disappearing WAL files.
The shared acquisition, safety and safety-test files are byte-identical to the
reference copies, closing Claude's unread-code condition. Parquet row numbers
now establish `_source_row`; ordinal/value equality is enforced. Automatic
extension installation is disabled and validation reports refuse existing paths.

The fresh build used existing WSL tmpfs with the unchanged 32 MiB working cap,
128 MiB DuckDB memory limit and 512 MiB physical reserve. Copy-back preserved at
least 128 MiB on Windows. Source archive/member hashes and immutable pins are
unchanged. No download, installation or source mutation occurred.

Python Datapond 0.1.5 / DuckDB 1.5.6 and R Datapond 0.1.0 / DuckDB 1.5.5 passed
on the new artifact through localhost with `PYTHONOPTIMIZE=2`. New build, client
and equality receipts are `evidence/audit-fix-*.json`. The owner independently reviewed the implementation diff and exact test/build/client scope. Original candidates remain archived separately.


The initial independent Claude source review completed under included Max usage and identified these corrections. Final corrected-source review is required before publication. These validation claims distinguish executed local checks from that separate source review. Public URL verification is recorded after upload; registry approval or merge is separate.
