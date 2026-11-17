# YAML Record Review: Metarhizium humberi

- Record: `data/taxa/eukaryota/metarhizium_humberi.yaml`
- Reviewed: `2026-09-23T15:37:10Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:2596975`
- Label: `Metarhizium humberi`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:5529` (`Metarhizium`)

## Validation

- `just validate data/taxa/eukaryota/metarhizium_humberi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metarhizium_guizhouense.yaml data/taxa/eukaryota/metarhizium_humberi.yaml data/taxa/eukaryota/metarhizium_hybridum.yaml data/taxa/eukaryota/metarhizium_majus.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:535113` has the same identifier, label, species rank, `NCBITaxon:5529` parent, genetic code `1`, and `gold` attestation copied into the YAML.
- The single related synonym, `Metarhizium humberi Luz, Rocha & Delalibera, 2019`, matches the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 16 entries from `root` through `Metarhizium`.

## Evidence

- `data/seed_scope.tsv:62885` includes `NCBITaxon:2596975` with reason `attested rule: Metarhizium humberi, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:23838` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains one exact organism/project/analysis chain for `Metarhizium humberi ESALQ1638`: `Go0631555`, `Gp0645065`, and AP name `Metarhizium humberi ESALQ1638`.
- `data/raw/ncbi_type_material.tsv:104510-104513` has four type-material spellings for the `UFG 50751` holotype and `IP 46` type material.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:2596975`.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether `Go0631555` should become a concrete strain or remain aggregate evidence only.
- If future generation begins materializing NCBI type-material accessions, verify that the `UFG 50751` and `IP 46` aliases remain grouped by biological strain rather than counted as independent strains.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:2596975`.
