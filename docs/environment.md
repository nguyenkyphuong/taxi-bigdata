# Task 5 — Hadoop–Spark Environment

- Timestamp (UTC): 2026-11-03T11:20:43.165593+00:00
- Overall validation: **PASS** (8/8 checks PASS)
- Mode: HDFS pseudo-distributed (NameNode + DataNode on ONE Colab VM); Spark local[2] on same VM. **Not multi-node physically distributed.**
- OS: Linux-6.6.159+-x86_64-with-glibc2.39
- CPU logical cores: 2; RAM GiB: 12.67
- Java: openjdk version "21.0.12.1" 2026-08-18
- Hadoop: 3.4.1
- Spark (PySpark): 3.5.5 (3.5.5)
- HDFS defaultFS: hdfs://localhost:9000; replication: 1
- Spark master: local[2]; Spark driver memory setting: 2g; Spark shuffle partitions: 2
- Data used in Task 5: 1,000 header-preserving CSV sample rows **per service** (Yellow, Green, Uber).
- Source selection: Yellow/Green by `approved_path` only, Uber by verified source basename. Never read obsolete raw + repaired duplicates together.
- Full raw inventory from Tasks 1–4: 97 + 26 + 6 files = 129 files; 94,958,638 raw records (prior approved profiling, NOT recounted by this task).
- Data processing: NONE. No filtering, canonical mapping, Parquet, training or benchmark in Task 5.

## Outputs
- `infra/core-site.xml` and `infra/hdfs-site.xml`
- `infra/task5_config.json`
- `docs/environment.md` (this file)
- `reports/task5_validation.csv`

## Persistence / limitations
- HDFS blocks at `/content/hdfs_task5` are **ephemeral Colab VM files**: lost after runtime reset; repeat notebook installation/config/sample upload on a new session.
- The files under Drive `infra/`, `docs/`, `reports/` persist.
- This check demonstrates correct HDFS upload/read through Spark on one machine; it does **not** demonstrate physical cluster scalability, production availability, or full 95-million-row performance.
- In Task 6 (separate approval), full raw data can be read and transformed; Task 5 leaves raw unchanged.

## Validation criteria
- Hadoop reports **Live datanodes (1)**.
- Spark session starts in `local[2]` mode.
- Yellow/Green manifest approved paths and Uber SHA-256 manifest check pass.
- 1,000 sample rows for EACH service can be uploaded to HDFS and read by Spark.
- All checks in `reports/task5_validation.csv` have status PASS.
