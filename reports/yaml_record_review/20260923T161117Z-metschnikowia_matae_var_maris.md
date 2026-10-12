# YAML Record Review: Metschnikowia matae var. maris

- Record: `data/taxa/eukaryota/metschnikowia_matae_var_maris.yaml`
- Reviewed: `2026-09-23T16:11:17Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1697387`
- Label: `Metschnikowia matae var. maris`
- Rank/domain: `VARIETAS` / `EUKARYOTA`
- Parent: `NCBITaxon:1697385` (`Metschnikowia matae`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_matae_var_maris.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_matae.yaml data/taxa/eukaryota/metschnikowia_matae_var_maris.yaml data/taxa/eukaryota/metschnikowia_matae_var_matae.yaml data/taxa/eukaryota/metschnikowia_mauinuiana.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:441935` has the same identifier, label, varietas rank, `NCBITaxon:1697385` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The related synonyms `Metschnikowia matae var. maris A.R.O. Santos, C.A. Rosa & Lachance, 2015` and `Metschnikowia sp. UFMG-CM-Y397` match the NCBI row.
- The YAML lineage contains the expected 14 entries from `root` through `Metschnikowia matae`.

## Evidence

- `data/seed_scope.tsv:61035` includes `NCBITaxon:1697387` with reason `attested rule: Metschnikowia matae var. maris, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:14644` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project/analysis chain for `Go0455137` / `UFMG-CM-Y397` and project `Gp0323463`.
- A complete `rg --no-ignore --hidden` scan found 17 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:53073-53089`, covering `NRRL Y-63737`, `UFMG-CM-Y397`, and `CBS 13985` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:22880` maps side-inventory old ID `NCBITaxon:1644098` into `NCBITaxon:1697387`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 17 type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1697387`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
