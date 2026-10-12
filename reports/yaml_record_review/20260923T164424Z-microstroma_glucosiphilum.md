# YAML Record Review: Microstroma glucosiphilum

- Record: `data/taxa/eukaryota/microstroma_glucosiphilum.yaml`
- Reviewed: `2026-09-23T16:44:24Z`
- Reviewer: Codex
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1684307`
- Label: `Microstroma glucosiphilum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Parent: `NCBITaxon:5032` (`Microstroma`)

## Validation

- `just validate data/taxa/eukaryota/microstroma_glucosiphilum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/microscypha_sp.yaml data/taxa/eukaryota/microsporum_canis.yaml data/taxa/eukaryota/microstoma_floccosum.yaml data/taxa/eukaryota/microstroma_glucosiphilum.yaml` scanned four files with 0 files containing ERROR rows and 0 total ERROR rows.
- The source record is seeded and was not edited.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:439940` has the same identifier, label, species rank, `NCBITaxon:5032` parent, genetic code `1`, exact synonym, four related synonyms, and `gold` attestation copied into the YAML.
- The YAML keeps `Pseudomicrostroma glucosiphilum` as an exact synonym and preserves the `Microstroma`, `Microstromatales`, `Pseudomicrostroma`, and `Rhodotorula` names as related synonyms from NCBI.
- The YAML lineage contains the expected 12 entries from `root` through `Microstroma`.

## Evidence

- `curation/seed_scope.tsv:61021` includes `NCBITaxon:1684307` with reason `attested rule: Microstroma glucosiphilum, 2 sources incl. NCBI`.
- `data/raw/gold_organisms.tsv:14523` reports GOLD organism count `1`, matching the YAML GOLD `assertion_count`.
- The native GOLD snapshot contains exact organism/project evidence for `Go0106754` / `MCA 4718`, including projects `Gp0106754` and `Gp0114232`; no native GOLD analysis rows are linked to those project IDs.
- A complete `rg --no-ignore --hidden` scan found six NCBI type-material rows at `data/raw/ncbi_type_material.tsv:52088-52093`, covering `CBS 14053`, `MCA 4718`, and `NRRL 66310` aliases under the `Pseudomicrostroma glucosiphilum` type-material name.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows, zero exact generated strain rows under `data/raw/strain_*`, and zero target rows in `data/straininfo/assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.
- The native StrainInfo records dump has one exact direct row and one exact deposit row for `NCBITaxon:1684307`, but no corresponding local strain inventory row is generated.
- No auxiliary rows were found for this fungal taxon in BactoTraits, GTDB, LPSN, MADIN, or MediaDive inventories.
- `data/raw/ncbi_merged_ids.tsv:20205` redirects `NCBITaxon:1566438` into this taxon, but a complete `rg --no-ignore --hidden` scan found no retained old-ID row in `data/raw/ncbitaxon_taxa.tsv`, so no YAML `replaces` entry is expected.

## Findings

- No blocking issues.

## Recommended Edits

- None.

## Follow-up Checks

- If future generation begins materializing NCBI type-material accessions, verify that the six `CBS 14053`, `MCA 4718`, and `NRRL 66310` spellings remain grouped as source aliases.

## Additional Notes

- All absence checks above come from bounded exact-ID scans of the relevant raw inventories for `NCBITaxon:1684307`; type-material and side-inventory old-ID conclusions were additionally checked with complete ignored-file-inclusive `rg --no-ignore --hidden` passes.
