# Schema Mapping – NYC Taxi & Uber (2014)

## 1. Scope

Dataset: Yellow Taxi, Green Taxi GPS, Uber.
Period: 2014-04-01 to 2014-09-30.
Expected records before cleaning: 94,958,638.

The profiling step does not modify raw data.

## 2. Source-to-Canonical Mapping

| Canonical field | Yellow Taxi | Green Taxi | Uber | Data type |
|---|---|---|---|---|
| service_type | constant: yellow | constant: green | constant: uber | string |
| pickup_datetime | pickup_datetime | lpep_pickup_datetime | Date/Time | timestamp |
| pickup_latitude | pickup_latitude | pickup_latitude | Lat | double |
| pickup_longitude | pickup_longitude | pickup_longitude | Lon | double |
| dropoff_datetime | dropoff_datetime | lpep_dropoff_datetime | unavailable | timestamp, nullable |
| trip_distance | trip_distance | trip_distance | unavailable | double, nullable |
| passenger_count | passenger_count | passenger_count | unavailable | integer, nullable |
| fare_amount | fare_amount | fare_amount | unavailable | double, nullable |
| source_file | CSV path | CSV path | CSV path | string |

## 3. Required Fields for the Main Classification Task

The minimum common schema is:

- service_type: yellow, green or uber
- pickup_datetime: pickup timestamp
- pickup_latitude: pickup latitude
- pickup_longitude: pickup longitude
- source_file: provenance of the record

The service_type field is the source label, not a prediction.

## 4. Timestamp Normalization

Yellow:
- Parse pickup_datetime.

Green:
- Parse lpep_pickup_datetime.

Uber:
- Parse Date/Time using MM/DD/YYYY HH:MM:SS.

All three sources use timestamps without explicit UTC offsets.
Treat them provisionally as New York local wall-clock time.

Do not assume naive timestamps are UTC.
When converting to timezone-aware timestamps, use
America/New_York and handle DST transitions explicitly.

Do not use the current system timezone as an implicit conversion.

## 5. GPS Normalization

Convert latitude and longitude to floating-point values.

Basic geographic validity:
- latitude must be within [-90, 90]
- longitude must be within [-180, 180]

Flag missing/non-numeric values and coordinates containing zero.

Profiling uses an approximate NYC bounding box:
- latitude: 40.4 to 41.1
- longitude: -74.3 to -73.5

This bounding box is only a quality-screening heuristic.
It is not an official NYC geographic boundary.

No records are removed during profiling.

## 6. Duplicate Handling

The profiling report contains duplicate indicators based on
a deterministic approximately 1% hash sample within each file.

This is not a complete global duplicate count.
Identical source rows may not necessarily establish
that two real-world trips are the same.

A later processing task must define the deduplication key
and evaluate duplicates across files and services if necessary.

## 7. Spatio-Temporal Feature Preparation

Potential derived features for subsequent tasks:
- pickup_date
- hour_of_day
- day_of_week
- latitude grid
- longitude grid
- time interval
- spatial-temporal cell identifier

The baseline spatial grid may be defined using
latitude/longitude rounded to three decimal places.

Grid rounding and feature derivation are NOT performed
during Task 4 profiling.

## 8. Provenance and Source Selection

Yellow:
- Read yellow_approved_manifest.csv.
- Select only approved_path.

Green:
- Read green_approved_manifest.csv.
- Select only approved_path.

Uber:
- Read the six verified original Uber CSV files.

Do not combine an obsolete raw file with its repaired replacement.

## 9. Output Contract

This document specifies the target schema for later processing.
It does not mean the Parquet transformation has been performed.

Task 4 deliverables:
- reports/data_profile.csv
- docs/schema_mapping.md

Supporting reports:
- reports/task4_file_profile.csv
- reports/task4_validation.csv
