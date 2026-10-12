# YAML Record Review: Meyerozyma carpophila

- Record: `data/taxa/eukaryota/meyerozyma_carpophila.yaml`
- Reviewed: `2026-09-23T16:26:51Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:374178`
- Label: `Meyerozyma carpophila`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:766728` (`Meyerozyma`)

## Validation

- `just validate data/taxa/eukaryota/meyerozyma_carpophila.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/meyerozyma_amylolytica.yaml data/taxa/eukaryota/meyerozyma_athensensis.yaml data/taxa/eukaryota/meyerozyma_caribbica.yaml data/taxa/eukaryota/meyerozyma_carpophila.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:78443` has the same identifier, label, species rank, `NCBITaxon:766728` parent, genetic code `12`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The Candida exact synonyms, `Candida guilliermondii var. carpophila` authority string, and Meyerozyma recombination authority string match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Meyerozyma`.

## Evidence

- `data/seed_scope.tsv:55398` includes `NCBITaxon:374178` with reason `attested rule: Meyerozyma carpophila, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:33670` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0138984` / `JCM 9396` / `Gp0144041` and `Go0705361` / `NRRL Y-17905` / `Gp0831398`, with one native analysis row for the JCM project.
- A complete `rg --no-ignore --hidden` scan found eight NCBI type-material rows at `data/raw/ncbi_type_material.tsv:197928-197935`, covering `CBS 5256` and `NRRL Y-17905` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:374178`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1608281`, `NCBITaxon:45605`, and `NCBITaxon:49326` into `NCBITaxon:374178`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the eight type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the large exact StrainInfo hit set for this taxon.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the three omitted old IDs.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:374178`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
