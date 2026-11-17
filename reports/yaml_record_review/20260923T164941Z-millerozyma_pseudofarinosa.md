# YAML Record Review: Millerozyma pseudofarinosa

- Record: `data/taxa/eukaryota/millerozyma_pseudofarinosa.yaml`
- Reviewed: `2026-09-23T16:49:41Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:676211`
- Label: `Millerozyma pseudofarinosa`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:766502` (`Millerozyma`)

## Validation

- `just validate data/taxa/eukaryota/millerozyma_pseudofarinosa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/millerozyma_pseudofarinosa.yaml data/taxa/eukaryota/minidiscus_trioculatus.yaml data/taxa/eukaryota/minutisphaera_aspera.yaml data/taxa/eukaryota/minutisphaera_parafimbriatispora.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:157659` has the same identifier, label, species rank, `NCBITaxon:766502` parent, yeast genetic code `12`, exact synonym, three related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Candida pseudofarinosa` as an exact synonym and preserves the 2012 `Candida`, `Candida sp. NCYC 386`, and 2026 `Millerozyma` names as related synonyms from NCBI.
- The YAML lineage contains the expected 13 entries from `root` through `Millerozyma`.

## Evidence

- `curation/seed_scope.tsv:56371` includes `NCBITaxon:676211` with reason `attested rule: Millerozyma pseudofarinosa, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:41083` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0705196` / `NCYC 386` / `Gp0831219`; no native GOLD analysis rows are linked to that project ID.
- A complete `rg --no-ignore --hidden` scan found four NCBI type-material rows at `data/raw/ncbi_type_material.tsv:253636-253639`, covering `CLIB 1231` and `NCYC 386` aliases under the `Candida pseudofarinosa` type-material name.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has one exact deposit row for `NCBITaxon:676211`, but no exact direct row and no corresponding local strain inventory row.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:676211`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the two `CLIB 1231` and two `NCYC 386` spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:676211`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
