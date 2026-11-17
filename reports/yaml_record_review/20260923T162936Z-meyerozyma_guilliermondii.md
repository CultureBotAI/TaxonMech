# YAML Record Review: Meyerozyma guilliermondii

- Record: `data/taxa/eukaryota/meyerozyma_guilliermondii.yaml`
- Reviewed: `2026-09-23T16:29:36Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:4929`
- Label: `Meyerozyma guilliermondii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:766728` (`Meyerozyma`)

## Validation

- `just validate data/taxa/eukaryota/meyerozyma_guilliermondii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/meyerozyma_elateridarum.yaml data/taxa/eukaryota/meyerozyma_guilliermondii.yaml data/taxa/eukaryota/meyerozyma_smithsonii.yaml data/taxa/eukaryota/microascus_trigonosporus.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2149` has the same identifier, label, species rank, `NCBITaxon:766728` parent, genetic code `12`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The Candida/Endomyces/Meyerozyma/Pichia/Yamadazyma exact synonyms and the two `HB45` provisional related synonyms match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Meyerozyma`.

## Evidence

- `data/seed_scope.tsv:51884` includes `NCBITaxon:4929` with reason `attested rule: Meyerozyma guilliermondii, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:37161` reports GOLD organism count `12`, matching the YAML GOLD `assertion_count`.
- A complete exact scan of the native GOLD snapshot contains 12 organism rows and 12 project rows, spanning `yHKB36`, `yHKB51`, `yHQL*`, `yHMP*`, `yHRVM115`, `yHSLC51`, `099134_271_A07`, `X1902-2`, and `NRRL Y-2075` strains.
- A complete `AP PROJECT GOLD IDS` scan found one native analysis row for project `Gp0702150` / `Meyerozyma guilliermondii X1902-2`.
- A complete `rg --no-ignore --hidden` scan found 26 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:223301-223326`, covering `ATCC 6260`, `CBS 566`, `NRRL Y-6889`, `CBS 2030`, `NRRL Y-2075`, `ATCC 46036`, `BCRC 21697`, `BCRC 22093`, `CCRC 21697`, `CCRC 22093`, `DBVPG 6571`, `IFO 10106`, and `NCYC 443` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:4929`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1348593`, `NCBITaxon:67434`, and `NCBITaxon:796031` into `NCBITaxon:4929`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 26 type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the large exact StrainInfo hit set for this taxon.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the three omitted old IDs.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:4929`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
