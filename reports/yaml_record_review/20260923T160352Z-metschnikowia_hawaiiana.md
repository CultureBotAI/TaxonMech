# YAML Record Review: Metschnikowia hawaiiana

- Record: `data/taxa/eukaryota/metschnikowia_hawaiiana.yaml`
- Reviewed: `2026-09-23T16:03:52Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:197672`
- Label: `Metschnikowia hawaiiana`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_hawaiiana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_hawaiiana.yaml data/taxa/eukaryota/metschnikowia_hawaiiensis.yaml data/taxa/eukaryota/metschnikowia_henanensis.yaml data/taxa/eukaryota/metschnikowia_hibisci.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:39277` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonym, related synonyms, and `gold` attestation copied into the YAML.
- The exact synonym `Candida hawaiiana` and the two related Candida/Metschnikowia synonyms match the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54440` includes `NCBITaxon:197672` with reason `attested rule: Metschnikowia hawaiiana, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:18277` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains an exact organism/project/analysis chain for `NRRL Y-27473`: organism `Go0517012`, projects `Gp0441050` and `Gp0780264`, and two analysis rows linked by those project IDs.
- A complete `rg --no-ignore --hidden` scan found eight NCBI type-material rows at `data/raw/ncbi_type_material.tsv:76035-76042`, covering `CBS 9146`, `MUCL 46200`, `NRRL Y-27473`, and `UWO(PS) 91-698.3` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:197672`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:197672`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the eight type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:197672`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
