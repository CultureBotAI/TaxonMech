# YAML Record Review: Metschnikowia proteae

- Record: `data/taxa/eukaryota/metschnikowia_proteae.yaml`
- Reviewed: `2026-09-23T16:15:14Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1150643`
- Label: `Metschnikowia proteae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_proteae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_pimensis.yaml data/taxa/eukaryota/metschnikowia_proteae.yaml data/taxa/eukaryota/metschnikowia_pulcherrima.yaml data/taxa/eukaryota/metschnikowia_rancensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:251760` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The related synonyms `Metschnikowia proteae de Vega, Guzman, Lachance & Herrera, 2012` and `Metschnikowia sp. CV-2012` match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:58004` includes `NCBITaxon:1150643` with reason `attested rule: Metschnikowia proteae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:3049` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0455124` / `EBD-A10Y1`, `Go0455128` / `EBD-T1Y1T`, and `Go0705562` / `NRRL Y-48784`, with projects `Gp0323450`, `Gp0323454`, and `Gp0831605`.
- Native GOLD also contains analysis rows for the two EBD projects.
- A complete `rg --no-ignore --hidden` scan found eight NCBI type-material rows at `data/raw/ncbi_type_material.tsv:9900-9907`, covering `CBS 12522`, `NRRL Y-48784`, and `EBDT1Y1` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:1150643`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the eight type-material spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1150643`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
