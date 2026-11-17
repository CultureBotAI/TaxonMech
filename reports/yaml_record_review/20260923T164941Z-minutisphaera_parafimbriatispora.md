# YAML Record Review: Minutisphaera parafimbriatispora

- Record: `data/taxa/eukaryota/minutisphaera_parafimbriatispora.yaml`
- Reviewed: `2026-09-23T16:49:41Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1660032`
- Label: `Minutisphaera parafimbriatispora`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:980421` (`Minutisphaera`)

## Validation

- `just validate data/taxa/eukaryota/minutisphaera_parafimbriatispora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/millerozyma_pseudofarinosa.yaml data/taxa/eukaryota/minidiscus_trioculatus.yaml data/taxa/eukaryota/minutisphaera_aspera.yaml data/taxa/eukaryota/minutisphaera_parafimbriatispora.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:433500` has the same identifier, label, species rank, `NCBITaxon:980421` parent, genetic code `1`, three related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps the `Minutisphaera parafimbriatispora` authority string plus `Minutisphaera sp. G156-1` and `Minutisphaera sp. HR-2015b` as related synonyms from NCBI.
- The YAML lineage contains the expected 16 entries from `root` through `Minutisphaera`.

## Evidence

- `curation/seed_scope.tsv:60997` includes `NCBITaxon:1660032` with reason `attested rule: Minutisphaera parafimbriatispora, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:14294` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism rows for `G156-1` and `DSM 29479`; no native GOLD project or analysis rows are linked to those organism IDs.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:50490-50495`, covering `DSM 29479`, `ILLS 72341`, and `G156-1a` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has two exact direct rows and two exact deposit rows for `NCBITaxon:1660032`, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:8403` redirects `NCBITaxon:1221211` into this taxon, but a complete `rg --no-ignore --hidden` scan found no retained old-ID row in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the six `DSM 29479`, `ILLS 72341`, and `G156-1a` spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1660032`; type-material and side-inventory old-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
