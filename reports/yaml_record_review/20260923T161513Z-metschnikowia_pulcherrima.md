# YAML Record Review: Metschnikowia pulcherrima

- Record: `data/taxa/eukaryota/metschnikowia_pulcherrima.yaml`
- Reviewed: `2026-09-23T16:15:14Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:27326`
- Label: `Metschnikowia pulcherrima`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_pulcherrima.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_pimensis.yaml data/taxa/eukaryota/metschnikowia_proteae.yaml data/taxa/eukaryota/metschnikowia_pulcherrima.yaml data/taxa/eukaryota/metschnikowia_rancensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2737` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The 12 exact synonyms and 17 related synonyms for Candida/Torula/Metschnikowia names match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:52154` includes `NCBITaxon:27326` with reason `attested rule: Metschnikowia pulcherrima, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:25473` reports GOLD organism count `8`, matching the YAML GOLD `assertion_count`.
- A complete exact scan of the native GOLD snapshot contains five exact organism rows and six project rows for `NRRL Y-7111`, `CBS 10809`, `CBS 15341`, `NRRL Y-27328`, and `NRRL Y-48710`; a complete `AP PROJECT GOLD IDS` scan found no analysis rows for the six project IDs.
- A complete `rg --no-ignore --hidden` scan found 64 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:115182-115245`, covering synonymized `Metschnikowia andauensis`, `M. fructicola`, `M. leonuri`, `M. pulcherrima`, `M. shanxiensis`, `M. sinensis`, and `M. ziziphicola` accessions.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:27326`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- Twelve side-inventory old IDs map into `NCBITaxon:27326` in `data/raw/ncbi_merged_ids.tsv`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 64 type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the 12 omitted old IDs.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the large exact StrainInfo hit set for this synonym-rich taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:27326`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
- GOLD aggregate rows can differ from local native exact rows; for `NCBITaxon:27326`, the generated aggregate count is `8`, while the exact native GOLD files currently contain five matching organism rows.
