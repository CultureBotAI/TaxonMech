# YAML Record Review: Metschnikowia lopburiensis (nom. inval.)

- Record: `data/taxa/eukaryota/metschnikowia_lopburiensis_nom_inval.yaml`
- Reviewed: `2026-09-23T16:09:33Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1217584`
- Label: `Metschnikowia lopburiensis (nom. inval.)`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:2613759` (`unclassified Metschnikowia (in: budding yeasts & allies)`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_lopburiensis_nom_inval.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_laotica.yaml data/taxa/eukaryota/metschnikowia_lochheadii.yaml data/taxa/eukaryota/metschnikowia_lopburiensis_nom_inval.yaml data/taxa/eukaryota/metschnikowia_lunata.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:275533` has the same identifier, label, species rank, `NCBITaxon:2613759` parent, genetic code `12`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The exact synonym `Metschnikowia lopburiensis` and the two `Candida`/`Metschnikowia` related synonyms match the NCBI row.
- The YAML lineage contains the expected 14 entries from `root` through `unclassified Metschnikowia (in: budding yeasts & allies)`.

## Evidence

- `data/seed_scope.tsv:58442` includes `NCBITaxon:1217584` with reason `attested rule: Metschnikowia lopburiensis (nom. inval.), 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:5176` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project chain for `Go0705050` / `CBS 12574` and project `Gp0831070`.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:1217584`, so no type-material assertions are missing from the YAML.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:5273` maps side-inventory old ID `NCBITaxon:1146898` into `NCBITaxon:1217584`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If NCBI later adds type-material rows for this invalidly published name, verify that they remain absent from the generated strain layer unless an exact local strain inventory row appears.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted old ID.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1217584`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
