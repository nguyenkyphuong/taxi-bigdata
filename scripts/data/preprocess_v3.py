"""Task 6 v3 -- paper-aligned NYC Taxi / Uber 2014 Parquet ETL.

Sun et al. (2018), sec. 5.1: spatial regions are obtained by rounding
pickup lat/lon to 3 decimal places. Paper does NOT specify a NYC bounding-box
cleaning rule. This ETL does NOT apply any NYC/historical administrative
boundary filter. It retains original pickup coordinates for future grid mapping.

Assumptions not stated in the paper (explicitly documented): reject missing,
unparsable, NaN/infinite, Earth-range-invalid and zero GPS coordinates;
reject missing/unparsable or out-of-designated-month pickup timestamps.
Keep duplicate rows because no stable shared trip key is available.

Run with Google Colab Pro: 1 input file at a time, checkpointed on Drive.
Read-only Raw/Repairs; outputs ONLY under task6_v3 and versioned reports.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(os.getenv('TAXI_ROOT', '/content/drive/MyDrive/taxi-bigdata'))
RUNROOT = ROOT / 'data' / 'processed' / 'task6_v3'
REPORTS = ROOT / 'reports'
SCRATCH = Path('/content/task6_v3_scratch')
EXPECTED_FILES = {'yellow': 97, 'green': 26, 'uber': 6}
EXPECTED_ROWS = {'yellow': 82375087, 'green': 8049224, 'uber': 4534327}
MONTHS = {f'2014-{m:02d}' for m in range(4, 10)}
POLICY_ID = 'paper_2014_no_nyc_boundary_v3'
# OLD bounding box is only used to count *retained* coordinates excluded by v2.
# It is NEVER a rejection rule in v3.
OLD_BOX = {'lat_min': 40.4, 'lat_max': 41.1, 'lon_min': -74.3, 'lon_max': -73.5}
ALIASES = {
    'yellow': {'timestamp': ['pickup_datetime', 'tpep_pickup_datetime'],
               'latitude': ['pickup_latitude', 'start_lat', 'Start_Lat'],
               'longitude': ['pickup_longitude', 'start_lon', 'Start_Lon']},
    'green': {'timestamp': ['lpep_pickup_datetime', 'pickup_datetime'],
              'latitude': ['pickup_latitude', 'start_lat', 'Start_Lat'],
              'longitude': ['pickup_longitude', 'start_lon', 'Start_Lon']},
    'uber': {'timestamp': ['Date/Time'], 'latitude': ['Lat'], 'longitude': ['Lon']},
}
METRICS = [
    'input_rows', 'bad_time', 'bad_gps', 'both_bad', 'gps_missing',
    'gps_nan_or_inf', 'gps_out_of_earth_range', 'gps_zero',
    'retained_outside_old_bbox', 'rejected_rows', 'valid_rows', 'parquet_rows',
]


def manifest_location(name):
    found = list(ROOT.rglob(name))
    if len(found) != 1:
        raise RuntimeError(f'Expected exactly one manifest {name}, found: {found}')
    return found[0]


def read_manifest(name):
    with manifest_location(name).open(newline='', encoding='utf-8-sig') as stream:
        return list(csv.DictReader(stream))


def source_inventory():
    yellow = read_manifest('yellow_approved_manifest.csv')
    green = read_manifest('green_approved_manifest.csv')
    uber = read_manifest('uber_source_integrity.csv')
    if (len(yellow), len(green), len(uber)) != (97, 26, 6):
        raise AssertionError('Expected 97 Yellow, 26 Green, 6 Uber files')
    items = []
    for service, records in [('yellow', yellow), ('green', green)]:
        if not all(x['status'].upper() == 'APPROVED' for x in records):
            raise AssertionError(f'{service} manifest contains unapproved entries')
        if sum(int(x['expected_rows']) for x in records) != EXPECTED_ROWS[service]:
            raise AssertionError(f'{service} manifest row counts mismatch Task 4')
        for rec in records:
            path = Path(rec['approved_path'])
            if not path.is_file():
                raise FileNotFoundError(path)
            month = rec['month']
            if month not in MONTHS:
                raise ValueError((path, month))
            items.append(dict(service=service, path=path, month=month,
                              expected=int(rec['expected_rows'])))
    if not all(x['status'] == 'MATCH' and
               x['local_sha256'] == x['source_sha256'] for x in uber):
        raise AssertionError('Uber SHA-256 manifest does not verify')
    raw = ROOT / 'data' / 'raw'
    month_names = dict(apr14='2014-04', may14='2014-05', jun14='2014-06',
                       jul14='2014-07', aug14='2014-08', sep14='2014-09')
    for rec in uber:
        found = list(raw.rglob(rec['file']))  # green_uber folder is valid
        if len(found) != 1:
            raise AssertionError(f'Uber name not unique: {rec["file"]}: {found}')
        month_code = rec['file'].split('-')[-1].split('.')[0].lower()
        month = month_names[month_code]
        items.append(dict(service='uber', path=found[0], month=month, expected=None))
    if len(items) != 129 or len({str(x['path']) for x in items}) != 129:
        raise AssertionError('Source path count or uniqueness failure')
    for rec in items:
        rec['source_id'] = hashlib.sha256(str(rec['path']).encode()).hexdigest()[:16]
        rec['target'] = RUNROOT / f'month={rec["month"]}' / f'service={rec["service"]}' / f'source_id={rec["source_id"]}'
    return sorted(items, key=lambda x: (x['month'], x['service'], str(x['path'])))


def header_map(path, service):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        header = next(csv.reader(stream))
    normalized = {x.strip().lower(): x for x in header}
    selected = {}
    for field, aliases in ALIASES[service].items():
        match = [normalized[a.lower()] for a in aliases if a.lower() in normalized]
        if not match:
            raise ValueError(f'{path} missing {field}. Header: {header}')
        selected[field] = match[0]
    return selected, header


def preflight():
    items = source_inventory()
    rows = []
    for rec in items:
        picks, cols = header_map(rec['path'], rec['service'])
        rows.append(dict(service=rec['service'], month=rec['month'],
                         file=str(rec['path']), expected_rows=rec['expected'],
                         timestamp_col=picks['timestamp'], latitude_col=picks['latitude'],
                         longitude_col=picks['longitude'], n_columns=len(cols), status='PASS'))
    REPORTS.mkdir(parents=True, exist_ok=True)
    with (REPORTS / 'task6_v3_schema_preflight.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print('PREFLIGHT PASS:', len(rows), 'files; counts:', dict(Counter(x['service'] for x in items)))
    print('Expected raw rows:', sum(EXPECTED_ROWS.values()))
    return items


def spark_session():
    from pyspark.sql import SparkSession
    spark = (SparkSession.builder.master('local[2]').appName('NYC-Taxi-Task6-v3-Paper-Grid')
             .config('spark.driver.memory', '3g')
             .config('spark.sql.session.timeZone', 'America/New_York')
             .config('spark.sql.shuffle.partitions', '2')
             .config('spark.sql.files.maxPartitionBytes', str(64 * 1024 * 1024))
             .config('spark.sql.legacy.timeParserPolicy', 'CORRECTED')
             .getOrCreate())
    # A pre-existing SparkSession may ignore builder settings: verify explicitly.
    if spark.conf.get('spark.sql.session.timeZone') != 'America/New_York':
        raise RuntimeError('Spark timezone must be America/New_York')
    return spark


def prepare_df(spark, rec):
    from pyspark.sql import functions as F
    picks, _ = header_map(rec['path'], rec['service'])
    raw = (spark.read.option('header', 'true').option('inferSchema', 'false')
           .option('mode', 'PERMISSIVE').option('multiLine', 'false')
           .option('encoding', 'UTF-8').csv(str(rec['path'])))
    def quoted(name):
        return F.col('`' + name.replace('`', '``') + '`')
    df = raw.select(quoted(picks['timestamp']).alias('timestamp_raw'),
                    quoted(picks['latitude']).alias('latitude_raw'),
                    quoted(picks['longitude']).alias('longitude_raw'))
    fmt = 'M/d/yyyy H:mm:ss' if rec['service'] == 'uber' else "yyyy-MM-dd'T'HH:mm:ss.SSS"
    df = (df.withColumn('pickup_datetime', F.to_timestamp(F.trim('timestamp_raw'), fmt))
          .withColumn('pickup_latitude', F.trim('latitude_raw').cast('double'))
          .withColumn('pickup_longitude', F.trim('longitude_raw').cast('double')))
    lat, lon = F.col('pickup_latitude'), F.col('pickup_longitude')
    df = df.withColumn('time_invalid', F.col('pickup_datetime').isNull() |
                       (F.date_format('pickup_datetime', 'yyyy-MM') != F.lit(rec['month'])))
    df = (df.withColumn('gps_missing', lat.isNull() | lon.isNull())
          .withColumn('gps_nan_or_inf', F.coalesce(F.isnan(lat) | F.isnan(lon) |
                     (F.abs(lat) == F.lit(float('inf'))) |
                     (F.abs(lon) == F.lit(float('inf'))), F.lit(False)))
          .withColumn('gps_out_of_earth_range', F.coalesce((F.abs(lat) > 90) |
                     (F.abs(lon) > 180), F.lit(False)))
          .withColumn('gps_zero', F.coalesce((lat == 0) | (lon == 0), F.lit(False))))
    df = df.withColumn('gps_invalid', F.col('gps_missing') | F.col('gps_nan_or_inf') |
                       F.col('gps_out_of_earth_range') | F.col('gps_zero'))
    df = df.withColumn('valid', ~(F.col('time_invalid') | F.col('gps_invalid')))
    # Diagnostics only: NOT a geographic exclusion.
    df = df.withColumn('outside_old_bbox', F.coalesce(
        (~lat.between(OLD_BOX['lat_min'], OLD_BOX['lat_max'])) |
        (~lon.between(OLD_BOX['lon_min'], OLD_BOX['lon_max'])), F.lit(False)))
    return df


def count_quality(df):
    from pyspark.sql import functions as F
    flags = {
        'bad_time': 'time_invalid',
        'bad_gps': 'gps_invalid',
        'both_bad': None,
        'gps_missing': 'gps_missing',
        'gps_nan_or_inf': 'gps_nan_or_inf',
        'gps_out_of_earth_range': 'gps_out_of_earth_range',
        'gps_zero': 'gps_zero',
        'valid_rows': 'valid',
        'retained_outside_old_bbox': None,
    }
    aggs = [F.count('*').alias('input_rows')]
    for output, source in flags.items():
        condition = (F.col(source) if source else
                     (F.col('time_invalid') & F.col('gps_invalid') if output == 'both_bad'
                      else F.col('valid') & F.col('outside_old_bbox')))
        aggs.append(F.sum(F.when(condition, F.lit(1)).otherwise(F.lit(0))).alias(output))
    row = df.agg(*aggs).first().asDict()
    return {key: int(value or 0) for key, value in row.items()}


def output_columns(df, service, path):
    from pyspark.sql import functions as F
    return df.filter(F.col('valid')).select(
        F.lit(service).alias('service_type'), F.col('pickup_datetime'),
        F.col('pickup_latitude'), F.col('pickup_longitude'),
        F.lit(str(path)).alias('source_file'))


def checkpoint_path(rec):
    return rec['target'].parent / f'{rec["source_id"]}.checkpoint.json'


def already_done(rec):
    cp = checkpoint_path(rec)
    if not cp.is_file():
        return False
    try:
        data = json.loads(cp.read_text(encoding='utf-8'))
        target = rec['target']
        return (data['status'] == 'PASS' and data.get('policy_id') == POLICY_ID and
                int(data['valid_rows']) > 0 and
                data['source_file'] == str(rec['path']) and
                (target / '_SUCCESS').is_file() and bool(list(target.glob('part-*.parquet'))))
    except (ValueError, KeyError, TypeError):
        return False


def persist_one(spark, rec):
    started = time.monotonic()
    path = rec['path']
    # Read-only source: metadata must be identical after processing.
    before = path.stat()
    df = prepare_df(spark, rec)
    stats = count_quality(df)
    if rec['expected'] is not None and stats['input_rows'] != rec['expected']:
        raise ValueError(f'Incorrect input rows for {path}: {stats["input_rows"]}')
    if not stats['valid_rows'] or not stats['input_rows']:
        raise AssertionError(f'No accepted records for {path}: {stats}')
    if stats['bad_time'] == stats['input_rows']:
        raise AssertionError(f'All timestamps invalid for {path}; check parsing')
    if stats['gps_missing'] + stats['gps_zero'] + stats['gps_nan_or_inf'] + stats['gps_out_of_earth_range'] < stats['bad_gps']:
        raise AssertionError(f'GPS reason accounting failed {path}')
    clean = output_columns(df, rec['service'], path)
    SCRATCH.mkdir(parents=True, exist_ok=True)
    temp = SCRATCH / f'out_{rec["source_id"]}'
    if temp.exists():
        shutil.rmtree(temp)
    clean.coalesce(2).write.mode('overwrite').parquet(str(temp))
    local_count = spark.read.parquet(str(temp)).count()
    if local_count != stats['valid_rows']:
        raise AssertionError(f'Local Parquet count mismatch {path}')
    target = rec['target']
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f'Incomplete/stale output exists: {target}. Inspect manually; no silent overwrites.')
    shutil.copytree(temp, target)
    if not (target / '_SUCCESS').is_file() or not list(target.glob('part-*.parquet')):
        raise AssertionError('Drive output missing Parquet files / _SUCCESS')
    parquet_rows = spark.read.parquet(str(target)).count()
    if parquet_rows != local_count:
        raise AssertionError(f'Drive Parquet recount mismatch {path}')
    after = path.stat()
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
        raise AssertionError(f'Source metadata unexpectedly changed: {path}')
    detail = dict(
        status='PASS', policy_id=POLICY_ID, service=rec['service'], month=rec['month'],
        source_file=str(path), source_id=rec['source_id'],
        input_rows=stats['input_rows'], bad_time=stats['bad_time'], bad_gps=stats['bad_gps'],
        both_bad=stats['both_bad'], gps_missing=stats['gps_missing'],
        gps_nan_or_inf=stats['gps_nan_or_inf'], gps_out_of_earth_range=stats['gps_out_of_earth_range'],
        gps_zero=stats['gps_zero'], retained_outside_old_bbox=stats['retained_outside_old_bbox'],
        rejected_rows=stats['input_rows'] - stats['valid_rows'],
        valid_rows=stats['valid_rows'], parquet_rows=int(parquet_rows),
        source_size_bytes=after.st_size, source_mtime_ns=after.st_mtime_ns,
        target=str(target), elapsed_seconds=round(time.monotonic() - started, 2),
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
        time_semantics='America/New_York wall time (Apr-Sep 2014)',
        gps_policy='No NYC boundary/bbox exclusion; only null/nonfinite/earth-range/zero',
        deduplication='Not applied; paper does not specify a reliable common trip ID',
    )
    checkpoint_path(rec).write_text(json.dumps(detail, ensure_ascii=False, indent=2), encoding='utf-8')
    shutil.rmtree(temp)
    return detail


def finalize(items):
    complete, missing = [], []
    for rec in items:
        if already_done(rec):
            complete.append(json.loads(checkpoint_path(rec).read_text(encoding='utf-8')))
        else:
            missing.append(str(rec['path']))
    REPORTS.mkdir(parents=True, exist_ok=True)
    if complete:
        with (REPORTS / 'task6_v3_file_quality.csv').open('w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=list(complete[0])); w.writeheader(); w.writerows(complete)
    total = Counter()
    for entry in complete:
        for metric in METRICS:
            total[metric] += int(entry[metric])
    by_service = Counter()
    for entry in complete:
        by_service[entry['service']] += int(entry['input_rows'])
    checks = {
        'all_129_files_processed': len(complete) == 129,
        'source_inventory_matches_task4': len(complete) == 129 and total['input_rows'] == sum(EXPECTED_ROWS.values()) and all(by_service[s] == EXPECTED_ROWS[s] for s in EXPECTED_ROWS),
        'input_equals_accepted_plus_rejected': total['input_rows'] == total['valid_rows'] + total['rejected_rows'],
        'rejected_union_correct': total['rejected_rows'] == total['bad_time'] + total['bad_gps'] - total['both_bad'],
        'parquet_recount_consistent': total['valid_rows'] == total['parquet_rows'],
        'v3_keeps_at_least_v2_accepted_rows': len(complete) == 129 and total['valid_rows'] >= 92964758,
        'all_18_month_service_pairs_present': len({(x['month'], x['service']) for x in complete}) == 18,
        'positive_accepted_rows_every_file': len(complete) == 129 and all(int(x['valid_rows']) > 0 for x in complete),
        'timestamps_not_all_invalid': total['input_rows'] > total['bad_time'],
        'correct_paper_no_bbox_policy': len(complete) == 129 and all(x['policy_id'] == POLICY_ID for x in complete),
        'original_source_size_and_mtime_recorded': len(complete) == 129 and all(int(x['source_size_bytes']) > 0 for x in complete),
    }
    status = 'PASS' if all(checks.values()) else 'FAIL'
    with (REPORTS / 'task6_v3_validation.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(['check', 'status'])
        w.writerows((name, 'PASS' if passed else 'FAIL') for name, passed in checks.items())
    doc = ROOT / 'docs' / 'task6_v3_data_quality.md'
    doc.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        '# Task 6 v3 – Paper-aligned cleanup of 2014 taxi pickup locations',
        f'**Status:** {status} ({sum(checks.values())}/{len(checks)} checks)',
        f'**Source files:** {len(complete)}/129; **Missing:** {len(missing)}',
        f'**Task 4 raw records:** {sum(EXPECTED_ROWS.values()):,}',
        f'**Read:** {total["input_rows"]:,}; **Accepted:** {total["valid_rows"]:,}; **Rejected:** {total["rejected_rows"]:,}',
        f'**Bad timestamp/month:** {total["bad_time"]:,}',
        f'**Bad GPS (reason union):** {total["bad_gps"]:,}',
        f'**GPS missing/unparsable:** {total["gps_missing"]:,}',
        f'**GPS NaN/infinite:** {total["gps_nan_or_inf"]:,}',
        f'**GPS outside Earth latitude/longitude range:** {total["gps_out_of_earth_range"]:,}',
        f'**GPS zero latitude or longitude:** {total["gps_zero"]:,}',
        f'**Overlapping bad time & bad GPS:** {total["both_bad"]:,}',
        f'**Retained despite outside v2 NYC box:** {total["retained_outside_old_bbox"]:,}',
        '',
        '## Paper method versus our minimal cleaning assumptions',
        '- Sun et al. (2018), Sections 5.1 & 5.3: original pickup coordinates grouped into regions by rounding latitude and longitude to 3 decimal places, six monthly datasets Apr–Sep 2014.',
        '- The paper does NOT specify a geographic bounding box or a historical borough polygon for data cleaning. v3 does NOT apply either.',
        '- We retain 2014 pickup latitude/longitude as measured, with no substitution of 2026 geography.',
        '- To avoid modifying original coordinates prematurely, rounding into 0.001-degree cells is deferred to the spatial mapping/feature task. The 3-decimal grid will use original accepted numeric coordinates.',
        '- Our assumptions (not explicitly documented by paper): reject missing/non-numeric/nonfinite, absolute latitude > 90, absolute longitude > 180, and zero latitude or longitude. Reject invalid pickup timestamps or dates outside the source month.',
        '- Historical 2014 NYC borough boundaries are not used as an exclusion criterion: they are neither specified nor required by paper.',
        '- No deduplication due to absence of a trustworthy common trip ID.',
        '- Time zone America/New_York; local wall time for historical Apr–Sep 2014.',
        '- The old Task6 v2 bounding box (lat 40.4..41.1, lon -74.3..-73.5) is only used for a retention diagnostic; no filtering.',
        '',
        '## Reproducibility and persistence',
        f'- Source selection: approved_path from Yellow/Green manifests; 6 SHA-256 verified Uber names.',
        '- Source files are opened read-only. Size and mtime are checked before/after individual ETL. This is not a full pre/post SHA-256 audit for Yellow/Green.',
        '- Output: data/processed/task6_v3/month=YYYY-MM/service=SERVICE/source_id=HASH/',
        '- Checkpoints: one JSON per file. Spark mode: local[2], not physically multi-node.',
        '- v1 and v2 are superseded. Do not delete until v3 has been independently verified and backed up as needed.',
        '',
        '## Counts by service',
    ]
    for service in ['yellow', 'green', 'uber']:
        selected = [x for x in complete if x['service'] == service]
        lines.append(f'- {service}: {sum(int(x["valid_rows"]) for x in selected):,} accepted; '
                     f'{sum(int(x["rejected_rows"]) for x in selected):,} rejected')
    doc.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'TASK 6 v3: {status} | {len(complete)}/129 | read={total["input_rows"]:,} | accepted={total["valid_rows"]:,} | rejected={total["rejected_rows"]:,}')
    print('Previously excluded by old box but now retained:', f'{total["retained_outside_old_bbox"]:,}')
    print('Validation:', REPORTS / 'task6_v3_validation.csv')
    if missing:
        print('First missing files:', missing[:5])
    return status


def run(limit=None):
    items = preflight()
    spark = spark_session()
    free = shutil.disk_usage('/content').free / 1024**3
    print(f'Colab scratch free: {free:.2f} GiB')
    if free < 3:
        raise RuntimeError('Free Colab scratch space below 3 GiB')
    processed = 0
    for i, rec in enumerate(items, 1):
        if already_done(rec):
            continue
        print(f'[{i}/129] {rec["service"]} {rec["month"]} {rec["path"].name}', flush=True)
        result = persist_one(spark, rec)
        print(f'  PASS: {result["input_rows"]:,} -> {result["valid_rows"]:,}; rejected={result["rejected_rows"]:,}; retained_outside_old_box={result["retained_outside_old_bbox"]:,}', flush=True)
        processed += 1
        if limit is not None and processed >= limit:
            break
    return finalize(items)


def pilot():
    items = preflight()
    spark = spark_session()
    chosen = [next(x for x in items if x['service'] == service and x['month'] == '2014-04')
              for service in ('yellow', 'green', 'uber')]
    for rec in chosen:
        if already_done(rec):
            saved = json.loads(checkpoint_path(rec).read_text(encoding='utf-8'))
            print('PILOT SKIP checkpoint:', rec['path'].name, 'valid=', saved['valid_rows'])
            continue
        print('PILOT:', rec['service'], rec['path'].name, flush=True)
        result = persist_one(spark, rec)
        assert result['valid_rows'] == result['parquet_rows'] and result['valid_rows'] > 0
        print({k: result[k] for k in ['service', 'input_rows', 'bad_time', 'bad_gps', 'gps_zero', 'gps_out_of_earth_range', 'retained_outside_old_bbox', 'rejected_rows', 'valid_rows', 'parquet_rows']})
    print('PILOT done; not full Task 6 PASS. Review the 3 sources before running 129 files.')


if __name__ == '__main__':
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    print(run(limit))
