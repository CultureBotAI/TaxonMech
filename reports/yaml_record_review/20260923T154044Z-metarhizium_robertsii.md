# YAML Record Review: Metarhizium robertsii

- Record: `data/taxa/eukaryota/metarhizium_robertsii.yaml`
- Reviewed: `2026-09-23T15:40:44Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:568076`
- Label: `Metarhizium robertsii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:5529` (`Metarhizium`)

## Validation

- `just validate data/taxa/eukaryota/metarhizium_robertsii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metarhizium_pingshaense.yaml data/taxa/eukaryota/metarhizium_rileyi.yaml data/taxa/eukaryota/metarhizium_robertsii.yaml data/taxa/eukaryota/metarhizium_robertsii_arsef_23.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:133746` has the same identifier, label, species rank, `NCBITaxon:5529` parent, genetic code `1`, and `gold` attestation copied into the YAML.
- The three related synonyms, `Metarhizium robertsii J.F. Bisch., Rehner & Humber, 2009`, `Metarhizium sp. ARSEF 8680`, and `Metarhizium sp. SAR-2008b`, match the NCBI row; the row has no exact synonyms.
- The YAML lineage contains the expected 16 entries from `root` through `Metarhizium`.

## Evidence

- `data/seed_scope.tsv:56062` includes `NCBITaxon:568076` with reason `attested rule: Metarhizium robertsii, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:39037` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count` and the YAML note that descendant taxa are not gathered.
- The native GOLD snapshot contains one exact organism/project/analysis chain for direct species record `Metarhizium robertsii`: `Go0076192`, `Gp0076192`, and AP name `Metarhizium robertsii`.
- `data/raw/ncbi_type_material.tsv:236525-236526` has the two exact NCBI culture-from-holotype designations for `ARSEF 2575` / `ARSEF:2575`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No NCBI merge row, retained old ID, or auxiliary BactoTraits, GTDB, LPSN, MADIN, or MediaDive row was found for `NCBITaxon:568076`.
- The adjacent strain taxon `NCBITaxon:655844` is represented separately by `data/taxa/eukaryota/metarhizium_robertsii_arsef_23.yaml`, matching the direct-descendant exclusion note on this species record.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the two `ARSEF 2575` forms are treated as source aliases rather than independent strains.
- If descendant aggregation ever becomes desired, keep `NCBITaxon:655844` separate from this direct-species GOLD count to avoid double counting.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:568076`.
