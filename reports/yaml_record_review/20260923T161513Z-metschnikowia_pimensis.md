# YAML Record Review: Metschnikowia pimensis

- Record: `data/taxa/eukaryota/metschnikowia_pimensis.yaml`
- Reviewed: `2026-09-23T16:15:14Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:261282`
- Label: `Metschnikowia pimensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_pimensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_pimensis.yaml data/taxa/eukaryota/metschnikowia_proteae.yaml data/taxa/eukaryota/metschnikowia_pulcherrima.yaml data/taxa/eukaryota/metschnikowia_rancensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:53382` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The exact synonym `Candida pimensis` and the four related Candida/Metschnikowia synonyms match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54841` includes `NCBITaxon:261282` with reason `attested rule: Metschnikowia pimensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:24102` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project chain for `Go0705462` / `NRRL Y-27619` and project `Gp0831505`.
- A complete `rg --no-ignore --hidden` scan found nine NCBI type-material rows at `data/raw/ncbi_type_material.tsv:106116-106124`, covering `ATCC MYA-4306`, `CBS 9805`, `Gibson-1.1`, and `NRRL Y-27619` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:261282`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:46401` maps side-inventory old ID `NCBITaxon:261283` into `NCBITaxon:261282`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the nine type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted old ID.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:261282`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
