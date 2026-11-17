# YAML Record Review: Metschnikowia rancensis

- Record: `data/taxa/eukaryota/metschnikowia_rancensis.yaml`
- Reviewed: `2026-09-23T16:15:14Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:208486`
- Label: `Metschnikowia rancensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:27320` (`Metschnikowia`)

## Validation

- `just validate data/taxa/eukaryota/metschnikowia_rancensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metschnikowia_pimensis.yaml data/taxa/eukaryota/metschnikowia_proteae.yaml data/taxa/eukaryota/metschnikowia_pulcherrima.yaml data/taxa/eukaryota/metschnikowia_rancensis.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:41129` has the same identifier, label, species rank, `NCBITaxon:27320` parent, genetic code `12`, exact synonyms, related synonyms, and `gold` attestation copied into the YAML.
- The exact synonyms `Candida rancensis` and `Candida rancensis C. Ramirez & A.E. Gonzalez, 1984` match the NCBI row; the authority string also appears as a related synonym, matching the YAML.
- The YAML lineage contains the expected 13 entries from `root` through `Metschnikowia`.

## Evidence

- `data/seed_scope.tsv:54506` includes `NCBITaxon:208486` with reason `attested rule: Metschnikowia rancensis, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:19960` reports GOLD organism count `2`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0527858` / `Candida rancensis CR1` and `Go0529137` / `Metschnikowia rancensis CR1`, with projects `Gp0456392` and `Gp0458001`.
- A complete `rg --no-ignore --hidden` scan found four NCBI type-material rows at `data/raw/ncbi_type_material.tsv:83611-83614`, covering `CBS 8174` aliases.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- Exact StrainInfo direct/deposit rows exist for `NCBITaxon:208486`, but no BacDive-derived local strain inventory row was available for this taxon, so no StrainInfo overlay rows are expected.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:21886` maps side-inventory old ID `NCBITaxon:1615653` into `NCBITaxon:208486`; no retained old-ID rows were present in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entries are expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the four type-material spellings remain grouped as source aliases.
- If `replaces` policy changes to emit all `data/raw/ncbi_merged_ids.tsv` rows, revisit the omitted old ID.
- If StrainInfo-only exact rows become eligible for strain generation, revisit the exact StrainInfo hits for this taxon.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:208486`; type-material and merged-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
