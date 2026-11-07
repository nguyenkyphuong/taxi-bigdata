# Task 7 – Gate W1 Data Quality Report

## 1. Overview

- Dataset: NYC Yellow Taxi, Green Taxi, Uber
- Period: April–September 2014
- Source files: 129
- Processing version: Task 6 v3
- Spark: 3.5.5, local[2]
- Generated UTC: 2026-11-04T08:37:04.545039+00:00

## 2. Data quality summary

- Raw records: 94,958,638
- Valid Parquet records: 92,982,150
- Rejected records: 1,976,488
- Retention: 97.9186%

### Counts by service

| service | raw_rows | rejected_rows | valid_rows |
|---|---|---|---|
| green | 8,049,224 | 14,508 | 8,034,716 |
| uber | 4,534,327 | 0 | 4,534,327 |
| yellow | 82,375,087 | 1,961,980 | 80,413,107 |

### Counts by month and service

| month | service | source_files | raw_rows | rejected_rows | valid_rows | retention_pct |
|---|---|---|---|---|---|---|
| 2014-04 | green | 6 | 1,309,155 | 2,320 | 1,306,835 | 99.8228 |
| 2014-04 | uber | 1 | 564,516 | 0 | 564,516 | 100.0 |
| 2014-04 | yellow | 19 | 14,618,759 | 297,077 | 14,321,682 | 97.9678 |
| 2014-05 | green | 4 | 1,421,503 | 2,839 | 1,418,664 | 99.8003 |
| 2014-05 | uber | 1 | 652,435 | 0 | 652,435 | 100.0 |
| 2014-05 | yellow | 16 | 14,774,041 | 352,391 | 14,421,650 | 97.6148 |
| 2014-06 | green | 4 | 1,337,759 | 2,739 | 1,335,020 | 99.7953 |
| 2014-06 | uber | 1 | 663,844 | 0 | 663,844 | 100.0 |
| 2014-06 | yellow | 15 | 13,813,029 | 363,562 | 13,449,467 | 97.368 |
| 2014-07 | green | 4 | 1,273,973 | 2,685 | 1,271,288 | 99.7892 |
| 2014-07 | uber | 1 | 796,121 | 0 | 796,121 | 100.0 |
| 2014-07 | yellow | 16 | 13,106,365 | 350,432 | 12,755,933 | 97.3262 |
| 2014-08 | green | 5 | 1,344,941 | 2,058 | 1,342,883 | 99.847 |
| 2014-08 | uber | 1 | 829,275 | 0 | 829,275 | 100.0 |
| 2014-08 | yellow | 16 | 12,688,877 | 336,193 | 12,352,684 | 97.3505 |
| 2014-09 | green | 3 | 1,361,893 | 1,867 | 1,360,026 | 99.8629 |
| 2014-09 | uber | 1 | 1,028,136 | 0 | 1,028,136 | 100.0 |
| 2014-09 | yellow | 15 | 13,374,016 | 262,325 | 13,111,691 | 98.0385 |

## 3. Gate W1 validation

| check | status |
|---|---|
| 01_approved_source_count | PASS |
| 02_spark_source_count | PASS |
| 03_source_keys_match | PASS |
| 04_each_source_row_count_matches | PASS |
| 05_all_six_months | PASS |
| 06_all_three_services | PASS |
| 07_all_18_month_service_groups | PASS |
| 08_raw_total | PASS |
| 09_valid_total | PASS |
| 10_rejected_total | PASS |
| 11_raw_equals_valid_plus_rejected | PASS |
| 12_monthly_counts_match | PASS |
| 13_service_totals_match | PASS |

## 4. Processing methodology

The source dataset was processed in Task 6 v3.

- Invalid pickup timestamps and GPS values were excluded.
- No NYC bounding-box or administrative-boundary filter was used.
- No deduplication was performed.
- Original accepted GPS precision was retained.
- Spatial grid mapping has not yet been performed.

These preprocessing rules are project assumptions where
not explicitly specified in Sun et al. (2018).

## 5. Spark read verification

- Read method: 129 approved source directories.
- Partition base path: /content/drive/MyDrive/taxi-bigdata/data/processed/task6_v3
- Partition columns: month, service, source_id.
- Spark successfully grouped and counted all accepted records.
- Source-level counts reconcile with Task 6 audit outputs.

The initial root-directory read encountered inconsistent
partition-depth discovery. Reading the approved leaf
directories with the explicit basePath resolved this issue.

Non-Parquet files observed at the service directory level:
{'c626523442f4a998.checkpoint.json': 1, '4a6cb9f865222eee.checkpoint.json': 1, 'fdfd678892f37ec2.checkpoint.json': 1, 'f57940e64632bf3b.checkpoint.json': 1, '81b4844469d5c950.checkpoint.json': 1, 'f618fb0a21163b83.checkpoint.json': 1, '689fe4d836356023.checkpoint.json': 1, 'b01099d7321eb9c2.checkpoint.json': 1, '842e03c78ca18d12.checkpoint.json': 1, '9b41a468c857a485.checkpoint.json': 1, 'ec6c9e7e09099eaa.checkpoint.json': 1, '100416d672e3ebf8.checkpoint.json': 1, 'b5a0726be032ae82.checkpoint.json': 1, 'cf151874f9329c39.checkpoint.json': 1, 'afefb4d9dc8742e2.checkpoint.json': 1, '6f3dadc05d126437.checkpoint.json': 1, '2a75c29d92450bd7.checkpoint.json': 1, 'ed0a3d3c75461a18.checkpoint.json': 1, '5f621c1c85ed8594.checkpoint.json': 1, '1bd6c00be2819e39.checkpoint.json': 1, '603850f0d63683b3.checkpoint.json': 1, 'c6b7a6ba6b4b131b.checkpoint.json': 1, 'e6bc72c1ac0e764f.checkpoint.json': 1, '7c373e13ca6cbf33.checkpoint.json': 1, '7acea9e60419250d.checkpoint.json': 1, '819814c8a1055150.checkpoint.json': 1, '92c55b7d4beb670c.checkpoint.json': 1, '64bfb4b6925f6b3e.checkpoint.json': 1, '139c6832046c08ab.checkpoint.json': 1, '255509ca4bcd3499.checkpoint.json': 1, 'ab6c5cf1a577f7f0.checkpoint.json': 1, 'e20f0a9c7b95e7a7.checkpoint.json': 1, 'f08714bc269603eb.checkpoint.json': 1, 'aa02f7a5a581b894.checkpoint.json': 1, 'da3339d49cfe749b.checkpoint.json': 1, '34355c675ef30b99.checkpoint.json': 1, 'bfc071f5c6f04939.checkpoint.json': 1, '033594b55f5e0912.checkpoint.json': 1, 'eb56b6461d8b5095.checkpoint.json': 1, 'ae6fa369b5353cf3.checkpoint.json': 1, '77c86e0802b0bd6e.checkpoint.json': 1, 'b6877f3f4a2ffbed.checkpoint.json': 1, '6683b6b3db410325.checkpoint.json': 1, 'f6b0ce10a19dba8e.checkpoint.json': 1, 'fe5eda9e1444adb3.checkpoint.json': 1, '6a589dcf3be7a4d0.checkpoint.json': 1, '133c1965c9a91253.checkpoint.json': 1, '4b844272bc100517.checkpoint.json': 1, '4116907783037292.checkpoint.json': 1, 'bc4cd0601301fd1b.checkpoint.json': 1, '30dc329a13511207.checkpoint.json': 1, 'ae44cebc4872d8a8.checkpoint.json': 1, 'f660c0258c3cf51c.checkpoint.json': 1, '31719a0dcd360e64.checkpoint.json': 1, 'b9c04ed8c94454b4.checkpoint.json': 1, '90e961067e7b95cd.checkpoint.json': 1, '1bde1a2e159ee7ad.checkpoint.json': 1, 'f391688ef7616865.checkpoint.json': 1, '0d60758ec7c08d40.checkpoint.json': 1, 'd66b41902bf3f70e.checkpoint.json': 1, 'bf41b6ce40285ffe.checkpoint.json': 1, '126cebc445885377.checkpoint.json': 1, 'd751ef8051bf5f69.checkpoint.json': 1, '57286c07b3e64a11.checkpoint.json': 1, '4297f51a1232a10e.checkpoint.json': 1, '54bf29e6a46dbdfe.checkpoint.json': 1, '836f61272ffcf717.checkpoint.json': 1, '7cdee6a4a9804e18.checkpoint.json': 1, '51cf6cfaad985da4.checkpoint.json': 1, '96b7976525d622cd.checkpoint.json': 1, 'e2c3bc8d4e8fe950.checkpoint.json': 1, '20d300824946b21c.checkpoint.json': 1, 'fccb3a5f8ed77075.checkpoint.json': 1, 'bcef86029b9b4755.checkpoint.json': 1, 'ef3dba6b915b9c74.checkpoint.json': 1, 'b1bcc91ad2e24dc6.checkpoint.json': 1, 'b2d48cd5b4c00098.checkpoint.json': 1, '3e39dd315e058c40.checkpoint.json': 1, '445614ff048182f5.checkpoint.json': 1, 'd6d77a6c3b2ed955.checkpoint.json': 1, '3c63cb306ac9a6cd.checkpoint.json': 1, '8486b23300361f9b.checkpoint.json': 1, '90f531e7cbba91a2.checkpoint.json': 1, '8d121410dab15cd6.checkpoint.json': 1, 'b77a762e41e07ab6.checkpoint.json': 1, '4b625ea235e9e622.checkpoint.json': 1, '042155c04941b6a5.checkpoint.json': 1, '94d0088b279e2369.checkpoint.json': 1, 'b56f8d8cc35ef3b0.checkpoint.json': 1, '101caa121809718b.checkpoint.json': 1, 'cb16715271a1df2a.checkpoint.json': 1, '29315181a50fc60f.checkpoint.json': 1, '8f1c373c078e537e.checkpoint.json': 1, '0d5497548685a31b.checkpoint.json': 1, '705ea6ca2bb4d523.checkpoint.json': 1, '2da5e0f4c0ed2af4.checkpoint.json': 1, 'e85658f5efc24cc3.checkpoint.json': 1, '3b6751b45b646417.checkpoint.json': 1, 'f5c823f20b8e4211.checkpoint.json': 1, 'b2c80d5e08ca7cbb.checkpoint.json': 1, 'cd24d4ffababcb3e.checkpoint.json': 1, 'd72ebe5ecc3375a6.checkpoint.json': 1, 'd680430791b623bd.checkpoint.json': 1, '52dbd0efe1a68759.checkpoint.json': 1, 'f90b15cbe60c72b0.checkpoint.json': 1, 'b6693b81bee39acc.checkpoint.json': 1, 'b2f38325f8f5e843.checkpoint.json': 1, '1f68c5640c7d2cfa.checkpoint.json': 1, '27e59844fb1331ac.checkpoint.json': 1, '6eb22936a91c01fe.checkpoint.json': 1, 'f000b9e579c630e2.checkpoint.json': 1, 'e45a4f24d869c61a.checkpoint.json': 1, '10a2881fcd8a91b9.checkpoint.json': 1, 'b8831f48f83463e1.checkpoint.json': 1, 'bd7e908e6ded4cdb.checkpoint.json': 1, '369878c527baac53.checkpoint.json': 1, '8a82b441db79a89b.checkpoint.json': 1, '09a7257a49d09633.checkpoint.json': 1, '4bd8884132d68a40.checkpoint.json': 1, '87d81b2601738724.checkpoint.json': 1, 'b9cc4ac83ae9b678.checkpoint.json': 1, '74196f252ebbf4fb.checkpoint.json': 1, '5e04b2a0310bb4c7.checkpoint.json': 1, 'a48263aeab67f54b.checkpoint.json': 1, '412b98e54417f59d.checkpoint.json': 1, '98e75a56d24cd641.checkpoint.json': 1, 'e796955ab1210825.checkpoint.json': 1, '8a5377602c3b759c.checkpoint.json': 1, 'b5ddfecf87d3d727.checkpoint.json': 1}

No source files or Parquet records were modified.

## 6. Reproducibility and limitations

- Approved manifest: /content/drive/MyDrive/taxi-bigdata/data/processed/manifest.csv
- Monthly statistics: /content/drive/MyDrive/taxi-bigdata/reports/task7_monthly_counts.csv
- Validation results: /content/drive/MyDrive/taxi-bigdata/reports/task7_validation.csv
- Original Task 6 evidence remains unchanged.
- Checksums of all Parquet files were not recomputed.
- This gate validates source-level counts and readability;
  it does not establish model accuracy or system scalability.

## 7. Decision

**Gate W1: PASS (13/13 checks).**

Dataset approved as input to the baseline pipeline.
The validated Parquet files must remain unchanged.
