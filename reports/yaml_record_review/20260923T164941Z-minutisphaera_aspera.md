# YAML Record Review: Minutisphaera aspera

- Record: `data/taxa/eukaryota/minutisphaera_aspera.yaml`
- Reviewed: `2026-09-23T16:49:41Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1660031`
- Label: `Minutisphaera aspera`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:980421` (`Minutisphaera`)

## Validation

- `just validate data/taxa/eukaryota/minutisphaera_aspera.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/millerozyma_pseudofarinosa.yaml data/taxa/eukaryota/minidiscus_trioculatus.yaml data/taxa/eukaryota/minutisphaera_aspera.yaml data/taxa/eukaryota/minutisphaera_parafimbriatispora.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:433499` has the same identifier, label, species rank, `NCBITaxon:980421` parent, genetic code `1`, two related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps the `Minutisphaera aspera` authority string and `Minutisphaera sp. HR-2015a` as related synonyms from NCBI.
- The YAML lineage contains the expected 16 entries from `root` through `Minutisphaera`.

## Evidence

- `curation/seed_scope.tsv:60996` includes `NCBITaxon:1660031` with reason `attested rule: Minutisphaera aspera, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:14293` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism rows for `G427-1`, `DSM 29478`, and `CBS 140767`; no native GOLD project or analysis rows are linked to those organism IDs.
- A complete `rg --no-ignore --hidden` scan found eight NCBI type-material rows at `data/raw/ncbi_type_material.tsv:50482-50489`, covering `DSM 29478`, `CBS 140767`, `ILLS 72340`, and `G427-1a` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has one exact direct row and one exact deposit row for `NCBITaxon:1660031`, but no corresponding local strain inventory row is generated.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:1660031`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the eight `DSM 29478`, `CBS 140767`, `ILLS 72340`, and `G427-1a` spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1660031`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
