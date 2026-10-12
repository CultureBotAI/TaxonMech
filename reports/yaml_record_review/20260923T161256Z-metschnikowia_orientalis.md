# YAML Record Review: Metschnikowia orientalis

- Record: `data/taxa/eukaryota/metschnikowia_orientalis.yaml`
- Reviewed: `2026-09-23T16:12:56Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:150224`
- Label: `Metschnikowia orientalis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_orientalis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_noctiluminum.yaml data/taxa/eukaryota/metschnikowia_orientalis.yaml data/taxa/eukaryota/metschnikowia_peoriensis.yaml data/taxa/eukaryota/metschnikowia_picachoensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:30980` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The related synonyms `Metschnikowia orientalis Lachance & J.M. Bowles, 2006` and `Metschnikowiaceae sp. UWO(PS)99-733.2` match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54065` includes `NCBITaxon:150224` with reason `attested rule: Metschnikowia orientalis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:11769` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project chain for `Go0705517` / `NRRL Y-27991` and project `Gp0831560`.
- A complete `rg --no-ignore --hidden` scan found 13 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:37275-37287`, covering `CBS 10331`, `NRRL Y-27991`, and `UWOPS 99-745.6` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:150224`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the 13 type-material spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:150224`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
