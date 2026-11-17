# YAML Record Review: Metschnikowia viticola

- Record: `data/taxa/eukaryota/metschnikowia_viticola.yaml`
- Reviewed: `2026-09-23T16:25:03Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:280790`
- Label: `Metschnikowia viticola`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_viticola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_torresii.yaml data/taxa/eukaryota/metschnikowia_vanudenii.yaml data/taxa/eukaryota/metschnikowia_viticola.yaml data/taxa/eukaryota/metschnikowia_zobellii.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:57122` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, related synonym, and `gold` attestation copied into the YAML.
- The `Metschnikowia viticola` authority string matches the NCBI row.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54961` includes `NCBITaxon:280790` with reason `attested rule: Metschnikowia viticola, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:26923` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains two exact organism rows, for `Go0527708` / `Y813` and `Go0705548` / `NRRL Y-48693`, with three projects: `Gp0456070`, `Gp0456168`, and `Gp0831591`.
- No native analysis rows join through those three GOLD projects.
- A complete `rg --no-ignore --hidden` scan found seven NCBI type-material rows at `data/raw/ncbi_type_material.tsv:124897-124903`, covering `CBS 9950` and `NRRL Y-48693` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:280790`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- A complete `rg --no-ignore --hidden` scan found no `data/raw/ncbi_merged_ids.tsv` rows targeting `NCBITaxon:280790`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the seven type-material spellings remain grouped as source aliases.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the two exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:280790`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
