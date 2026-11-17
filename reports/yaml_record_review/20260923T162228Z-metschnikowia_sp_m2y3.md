# YAML Record Review: Metschnikowia sp. M2Y3

- Record: `data/taxa/eukaryota/metschnikowia_sp_m2y3.yaml`
- Reviewed: `2026-09-23T16:22:28Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1807689`
- Label: `Metschnikowia sp. M2Y3`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:2613759` (`unclassified Metschnikowia (in: budding yeasts & allies)`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_sp_m2y3.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_sp_04_218_3.yaml data/taxa/eukaryota/metschnikowia_sp_04_226_1.yaml data/taxa/eukaryota/metschnikowia_sp_13_106_1.yaml data/taxa/eukaryota/metschnikowia_sp_m2y3.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:472457` has the same identifier, label, species rank, `NCBITaxon:2613759` parent, genetic code `12`, and `gold` attestation copied into the YAML.
- The absence of YAML synonyms matches the empty synonym fields in the NCBI row.
- The YAML lineage contains the expected 14 entries from `root` through `unclassified Metschnikowia (in: budding yeasts & allies)`.

## Evidence

- `data/seed_scope.tsv:61298` includes `NCBITaxon:1807689` with reason `attested rule: Metschnikowia sp. M2Y3, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:15923` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0455125` / `EBD-CdV M2Y3` and `Gp0323451`, plus one analysis row for the same project.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:1807689`.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact StrainInfo rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:1807689`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future GOLD refreshes remap the provisional `EBD-CdV M2Y3` organism to a named Metschnikowia species, revisit this record's seed scope and possible merge status.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1807689`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
