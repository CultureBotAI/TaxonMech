# YAML Record Review: Millerozyma farinosa

- Record: `data/taxa/eukaryota/millerozyma_farinosa.yaml`
- Reviewed: `2026-09-23T16:47:56Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:4920`
- Label: `Millerozyma farinosa`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:766502` (`Millerozyma`)

## Validation

- `just validate data/taxa/eukaryota/millerozyma_farinosa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/millerago_galiae.yaml data/taxa/eukaryota/millerozyma_acaciae.yaml data/taxa/eukaryota/millerozyma_farinosa.yaml data/taxa/eukaryota/millerozyma_farinosa_cbs_7064.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2141` has the same identifier, label, species rank, `NCBITaxon:766502` parent, yeast genetic code `12`, seven exact synonyms, four related synonyms, and `gold` attestation copied into the YAML.
- The YAML synonym block preserves the `Candida`, `Millerozyma`, `Pichia`, `Saccharomyces`, and `Yamadazyma` names from the NCBI exact and related synonym fields.
- The YAML lineage contains the expected 13 entries from `root` through `Millerozyma`.

## Evidence

- `curation/seed_scope.tsv:51876` includes `NCBITaxon:4920` with reason `attested rule: Millerozyma farinosa, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:37133` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`; the native GOLD JSONL snapshot currently has one exact organism/project/analysis triplet for `Go0384679` / `KCTC 27753` / `Gp0235795`.
- The YAML GOLD attestation note correctly states that records filed under descendant taxa, such as `NCBITaxon:559304`, are not gathered into this species count.
- A complete `rg --no-ignore --hidden` scan found 22 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:223058-223079`, covering type aliases under `Candida cacaoi`, `Millerozyma miso`, and `Saccharomyces farinosus`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has exact rows for `NCBITaxon:4920` directly and in deposits, but none are represented in the local BacDive-derived strain inventory for this taxon.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:79010`, `:86541`, `:96847`, and `:97394` redirect four old IDs into this taxon, but a complete `rg --no-ignore --hidden` scan found no retained old-ID rows in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- Reconcile the transformed GOLD aggregate count of 2 with the single exact native GOLD organism row on the next GOLD refresh.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:4920`; type-material and side-inventory old-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
