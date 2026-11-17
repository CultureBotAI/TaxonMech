# YAML Record Review: Metschnikowia kipukae

- Record: `data/taxa/eukaryota/metschnikowia_kipukae.yaml`
- Reviewed: `2026-09-23T16:05:52Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:197673`
- Label: `Metschnikowia kipukae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_kipukae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_kamakouana.yaml data/taxa/eukaryota/metschnikowia_kipukae.yaml data/taxa/eukaryota/metschnikowia_kofuensis_nom_inval.yaml data/taxa/eukaryota/metschnikowia_koreensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:39278` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The exact synonym `Candida kipukae` and the two related Candida/Metschnikowia synonyms match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54441` includes `NCBITaxon:197673` with reason `attested rule: Metschnikowia kipukae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:18278` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0455139` / `UWOPS 00-669.2` and `Go0705432` / `NRRL Y-27474`, with projects `Gp0323465` and `Gp0831475`.
- Native GOLD also contains an analysis row for the `UWOPS 00-669.2` project.
- A complete `rg --no-ignore --hidden` scan found 12 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:76043-76054`, covering `CBS 9147`, `MUCL 46201`, `NRRL Y-27474`, and `UWO(PS) 00-669.2` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:197673`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:28690` maps side-inventory old ID `NCBITaxon:1807682` into `NCBITaxon:197673`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 12 type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted old ID.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:197673`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
