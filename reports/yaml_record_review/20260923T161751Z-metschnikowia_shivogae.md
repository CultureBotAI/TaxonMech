# YAML Record Review: Metschnikowia shivogae

- Record: `data/taxa/eukaryota/metschnikowia_shivogae.yaml`
- Reviewed: `2026-09-23T16:17:51Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:353899`
- Label: `Metschnikowia shivogae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_shivogae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_reukaufii.yaml data/taxa/eukaryota/metschnikowia_rubicola.yaml data/taxa/eukaryota/metschnikowia_santaceciliae.yaml data/taxa/eukaryota/metschnikowia_shivogae.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:73104` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonyms, and `gold` attestation copied into the YAML.
- The `Metschnikowia shivogae` authority string and three provisional Metschnikowia related synonyms match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:55328` includes `NCBITaxon:353899` with reason `attested rule: Metschnikowia shivogae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:33050` reports GOLD organism count `3`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0455161` / `UWOPS 04-310.1`, `Go0455163` / `UWOPS 07-203.2`, and `Go0705506` / `NRRL Y-27924`, with projects `Gp0323487`, `Gp0323489`, and `Gp0831549`.
- Native GOLD also contains analysis rows for the two UWOPS projects.
- A complete `rg --no-ignore --hidden` scan found nine NCBI type-material rows at `data/raw/ncbi_type_material.tsv:191799-191807`, covering `CBS 10292`, `NRRL Y-27924`, and `UWO PS 04-310.1` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:81050-81051` maps side-inventory old IDs `NCBITaxon:481815` and `NCBITaxon:481816` into `NCBITaxon:353899`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the nine type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the two omitted old IDs.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:353899`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
