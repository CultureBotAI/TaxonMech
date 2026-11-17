# YAML Record Review: Metarhizium majus

- Record: `data/taxa/eukaryota/metarhizium_majus.yaml`
- Reviewed: `2026-09-23T15:37:10Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1650735`
- Label: `Metarhizium majus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:5529` (`Metarhizium`)

## Validation

- `just validate data/taxa/eukaryota/metarhizium_majus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metarhizium_guizhouense.yaml data/taxa/eukaryota/metarhizium_humberi.yaml data/taxa/eukaryota/metarhizium_hybridum.yaml data/taxa/eukaryota/metarhizium_majus.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:431760` has the same identifier, label, species rank, `NCBITaxon:5529` parent, genetic code `1`, and `gold` attestation copied into the YAML.
- The exact synonyms `Metarhizium anisopliae f. majus`, `Metarhizium anisopliae var. major`, and `Metarhizium anisopliae var. majus`, plus the two related authority synonyms, match the NCBI row.
- The YAML lineage contains the expected 16 entries from `root` through `Metarhizium`.

## Evidence

- `data/seed_scope.tsv:60960` includes `NCBITaxon:1650735` with reason `attested rule: Metarhizium majus, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:14181` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- `data/raw/ncbi_type_material.tsv:49807-49808` has the two exact NCBI type-material designations for `ARSEF 1914` / `ARSEF:1914`.
- The bounded scan found no exact native GOLD organism/project/analysis rows for this NCBI ID in the local `data/gold/*.jsonl.gz` snapshots.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:1650735`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the two `ARSEF 1914` forms are treated as source aliases rather than independent strains.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1650735`.
