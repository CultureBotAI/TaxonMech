# YAML Record Review: Metschnikowia drosophilae

- Record: `data/taxa/eukaryota/metschnikowia_drosophilae.yaml`
- Reviewed: `2026-09-23T16:01:17Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:135833`
- Label: `Metschnikowia drosophilae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_drosophilae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_drosophilae.yaml data/taxa/eukaryota/metschnikowia_gelsemii.yaml data/taxa/eukaryota/metschnikowia_gruessii.yaml data/taxa/eukaryota/metschnikowia_hamakuensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:27151` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The related synonyms `Metschnikowia drosophilae Lachance, 2001` and `Metschnikowia sp. CBS 8809` match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:53969` includes `NCBITaxon:135833` with reason `attested rule: Metschnikowia drosophilae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:8710` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project chain for `Go0705431` / `Gp0831474`.
- A complete `rg --no-ignore --hidden` scan found ten NCBI type-material rows at `data/raw/ncbi_type_material.tsv:25766-25775`, covering `CBS 8809`, `NRRL Y-27458`, `WM 07.3`, and `UWO(PS) 83-1135.3` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:135833`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the ten type-material spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:135833`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
