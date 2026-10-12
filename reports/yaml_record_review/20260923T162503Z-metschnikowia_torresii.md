# YAML Record Review: Metschnikowia torresii

- Record: `data/taxa/eukaryota/metschnikowia_torresii.yaml`
- Reviewed: `2026-09-23T16:25:03Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:45599`
- Label: `Metschnikowia torresii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_torresii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_torresii.yaml data/taxa/eukaryota/metschnikowia_vanudenii.yaml data/taxa/eukaryota/metschnikowia_viticola.yaml data/taxa/eukaryota/metschnikowia_zobellii.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:5634` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The `Candida torresii` and `Torulopsis torresii` exact synonyms and three authority-bearing related synonyms match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:52680` includes `NCBITaxon:45599` with reason `attested rule: Metschnikowia torresii, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:36089` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0705611` / `NRRL Y-6699` and `Gp0831656`; no native analysis rows join through that project.
- A complete `rg --no-ignore --hidden` scan found 21 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:215671-215691`, covering `ATCC 22999`, `BCRC 22404`, `CBS 5152`, `CCRC 22404`, `IFO 10421`, `IGC 3022`, `JCM 1845`, `NCYC 786`, `NRRL Y-6699`, and `VKM Y-1464` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:45599`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:45599`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 21 type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hit set for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:45599`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
