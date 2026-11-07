# Task 6 v3 – Paper-aligned cleanup of 2014 taxi pickup locations
**Status:** PASS (11/11 checks)
**Source files:** 129/129; **Missing:** 0
**Task 4 raw records:** 94,958,638
**Read:** 94,958,638; **Accepted:** 92,982,150; **Rejected:** 1,976,488
**Bad timestamp/month:** 0
**Bad GPS (reason union):** 1,976,488
**GPS missing/unparsable:** 0
**GPS NaN/infinite:** 0
**GPS outside Earth latitude/longitude range:** 42
**GPS zero latitude or longitude:** 1,976,446
**Overlapping bad time & bad GPS:** 0
**Retained despite outside v2 NYC box:** 17,392

## Paper method versus our minimal cleaning assumptions
- Sun et al. (2018), Sections 5.1 & 5.3: original pickup coordinates grouped into regions by rounding latitude and longitude to 3 decimal places, six monthly datasets Apr–Sep 2014.
- The paper does NOT specify a geographic bounding box or a historical borough polygon for data cleaning. v3 does NOT apply either.
- We retain 2014 pickup latitude/longitude as measured, with no substitution of 2026 geography.
- To avoid modifying original coordinates prematurely, rounding into 0.001-degree cells is deferred to the spatial mapping/feature task. The 3-decimal grid will use original accepted numeric coordinates.
- Our assumptions (not explicitly documented by paper): reject missing/non-numeric/nonfinite, absolute latitude > 90, absolute longitude > 180, and zero latitude or longitude. Reject invalid pickup timestamps or dates outside the source month.
- Historical 2014 NYC borough boundaries are not used as an exclusion criterion: they are neither specified nor required by paper.
- No deduplication due to absence of a trustworthy common trip ID.
- Time zone America/New_York; local wall time for historical Apr–Sep 2014.
- The old Task6 v2 bounding box (lat 40.4..41.1, lon -74.3..-73.5) is only used for a retention diagnostic; no filtering.

## Reproducibility and persistence
- Source selection: approved_path from Yellow/Green manifests; 6 SHA-256 verified Uber names.
- Source files are opened read-only. Size and mtime are checked before/after individual ETL. This is not a full pre/post SHA-256 audit for Yellow/Green.
- Output: data/processed/task6_v3/month=YYYY-MM/service=SERVICE/source_id=HASH/
- Checkpoints: one JSON per file. Spark mode: local[2], not physically multi-node.
- v1 and v2 are superseded. Do not delete until v3 has been independently verified and backed up as needed.

## Counts by service
- yellow: 80,413,107 accepted; 1,961,980 rejected
- green: 8,034,716 accepted; 14,508 rejected
- uber: 4,534,327 accepted; 0 rejected
