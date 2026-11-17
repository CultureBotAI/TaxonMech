# YAML Record Review: Meyerozyma caribbica

- Record: `data/taxa/eukaryota/meyerozyma_caribbica.yaml`
- Reviewed: `2026-09-23T16:26:51Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:66948`
- Label: `Meyerozyma caribbica`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:766728` (`Meyerozyma`)

## Validation

- `just validate data/taxa/eukaryota/meyerozyma_caribbica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/meyerozyma_amylolytica.yaml data/taxa/eukaryota/meyerozyma_athensensis.yaml data/taxa/eukaryota/meyerozyma_caribbica.yaml data/taxa/eukaryota/meyerozyma_carpophila.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:8767` has the same identifier, label, species rank, `NCBITaxon:766728` parent, genetic code `12`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The `Candida fermentati` and `Torula fermentati` exact synonyms, four provisional Candida strain-name synonyms, and Meyerozyma recombination authority string match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Meyerozyma`.

## Evidence

- `data/seed_scope.tsv:53141` includes `NCBITaxon:66948` with reason `attested rule: Meyerozyma caribbica, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:40878` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis evidence for `Go0517054` / `NRRL Y-27274` / `Gp0441092`, `Go0657880` / `PYS2905` / `Gp0702148`, and `Go0657881` / `B8028` / `Gp0702149`.
- A complete `rg --no-ignore --hidden` scan found seven NCBI type-material rows at `data/raw/ncbi_type_material.tsv:249299-249305`, covering `CBS 9966`, `DBVPG 4519`, and `NRRL Y-27274` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:66948`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:234555`, `NCBITaxon:234561`, `NCBITaxon:261692`, `NCBITaxon:261693`, and `NCBITaxon:935749` into `NCBITaxon:66948`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the seven type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the large exact StrainInfo hit set for this taxon.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the five omitted old IDs.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:66948`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
