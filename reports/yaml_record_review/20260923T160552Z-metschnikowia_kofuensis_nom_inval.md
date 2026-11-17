# YAML Record Review: Metschnikowia kofuensis (nom. inval.)

- Record: `data/taxa/eukaryota/metschnikowia_kofuensis_nom_inval.yaml`
- Reviewed: `2026-09-23T16:05:52Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:329642`
- Label: `Metschnikowia kofuensis (nom. inval.)`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:2613759` (`unclassified Metschnikowia (in: budding yeasts & allies)`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_kofuensis_nom_inval.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_kamakouana.yaml data/taxa/eukaryota/metschnikowia_kipukae.yaml data/taxa/eukaryota/metschnikowia_kofuensis_nom_inval.yaml data/taxa/eukaryota/metschnikowia_koreensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:67314` has the same identifier, label, species rank, `NCBITaxon:2613759` parent, genetic code `12`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The exact synonyms `Candida kofuensis` and `Metschnikowia kofuensis` match the NCBI row.
- The two Candida/Metschnikowia authority strings match the NCBI related synonyms.
- The YAML lineage contains the expected 14 entries from `root` through `unclassified Metschnikowia (in: budding yeasts & allies)`.

## Evidence

- `data/seed_scope.tsv:55239` includes `NCBITaxon:329642` with reason `attested rule: Metschnikowia kofuensis (nom. inval.), 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:32226` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project chain for `Go0705404` / `NRRL Y-27226` and project `Gp0831447`.
- A complete `rg --no-ignore --hidden` scan found no NCBI type-material rows for `NCBITaxon:329642`, so no type-material assertions are missing from the YAML.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:329642`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:329642`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If NCBI later adds type-material rows for this invalidly published name, verify that they remain absent from the generated strain layer unless an exact local strain inventory row appears.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:329642`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
