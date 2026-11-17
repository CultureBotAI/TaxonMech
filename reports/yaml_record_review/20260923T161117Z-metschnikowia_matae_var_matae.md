# YAML Record Review: Metschnikowia matae var. matae

- Record: `data/taxa/eukaryota/metschnikowia_matae_var_matae.yaml`
- Reviewed: `2026-09-23T16:11:17Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1697386`
- Label: `Metschnikowia matae var. matae`
- Rank/domain: `VARIETAS` / `EUKARYOTA`
- Parent: `NCBITaxon:1697385` (`Metschnikowia matae`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_matae_var_matae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_matae.yaml data/taxa/eukaryota/metschnikowia_matae_var_maris.yaml data/taxa/eukaryota/metschnikowia_matae_var_matae.yaml data/taxa/eukaryota/metschnikowia_mauinuiana.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:441934` has the same identifier, label, varietas rank, `NCBITaxon:1697385` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The `Metschnikowia matae var. matae` authority and the three provisional UFMG-CM related synonyms match the NCBI row.
- The YAML lineage contains the expected 14 entries from `root` through `Metschnikowia matae`.

## Evidence

- `data/seed_scope.tsv:61034` includes `NCBITaxon:1697386` with reason `attested rule: Metschnikowia matae var. matae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:14643` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project/analysis chains for `Go0455135` / `UFMG-CM-Y391A` and `Go0455136` / `UFMG-CM-Y395`, with projects `Gp0323461` and `Gp0323462`.
- A complete `rg --no-ignore --hidden` scan found seven NCBI type-material rows at `data/raw/ncbi_type_material.tsv:53066-53072`, covering `UFMG-CM-Y395T`, `CBS 13986`, and `NRRL Y-63736` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:22877-22879` maps side-inventory old IDs `NCBITaxon:1644095`, `NCBITaxon:1644096`, and `NCBITaxon:1644097` into `NCBITaxon:1697386`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the seven type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the three omitted old IDs.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1697386`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
