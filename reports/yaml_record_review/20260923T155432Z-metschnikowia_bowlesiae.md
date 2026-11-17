# YAML Record Review: Metschnikowia bowlesiae

- Record: `data/taxa/eukaryota/metschnikowia_bowlesiae.yaml`
- Reviewed: `2026-09-23T15:54:32Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1699426`
- Label: `Metschnikowia bowlesiae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_bowlesiae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_borealis.yaml data/taxa/eukaryota/metschnikowia_bowlesiae.yaml data/taxa/eukaryota/metschnikowia_caudata.yaml data/taxa/eukaryota/metschnikowia_cerradonensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:442254` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, and `gold` attestation copied into the YAML.
- The six related synonyms in the YAML match the NCBI row, including the `UWOPS` provisional names; the row has no exact synonyms.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:61072` includes `NCBITaxon:1699426` with reason `attested rule: Metschnikowia bowlesiae, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:14697` reports GOLD organism count `4`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains four exact organism/project rows for `UWOPS 04-243x5`, `UWOPS 12-611.1`, `UWOPS 12-619.1`, and `NRRL Y-63671`, with analyses for the first three projects.
- A complete `rg --no-ignore --hidden` scan found 13 NCBI type-material rows at `data/raw/ncbi_type_material.tsv:53296-53308`, covering `CBS 12940`, `NRRL Y-63671`, and `UWOPS 04-243x5` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1432398`, `NCBITaxon:1432399`, `NCBITaxon:1432400`, `NCBITaxon:1432401`, and `NCBITaxon:1437198` into `NCBITaxon:1699426`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future GOLD-to-strain joins start emitting non-BacDive organisms, check whether the four exact native GOLD rows should become concrete strain records or remain aggregate evidence only.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the five omitted old IDs.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1699426`; the type-material rows were additionally confirmed with a complete ignored-file-inclusive `rg --no-ignore --hidden` pass.
