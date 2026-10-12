# YAML Record Review: Candidatus Methanophagaceae archaeon SCGC AAA252-L18

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/candidatus_methanophagaceae_archaeon_scgc_aaa252_l18.yaml
- Started UTC: 2026-09-27T14:44:51Z
- Finished UTC: 2026-09-27T14:44:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/candidatus_methanophagaceae_archaeon_scgc_aaa252_l18.yaml` |
| Identifier | `NCBITaxon:1046934` |
| Label | `Candidatus Methanophagaceae archaeon SCGC AAA252-L18` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:3386246` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated GOLD- and NCBI-backed Candidatus Methanophagaceae
species record, with path pinned by `data/taxa/PATHS.tsv:17366`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/candidatus_methanophagaceae_archaeon_scgc_aaa252_l18.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/natronomonas_sp_sa2.yaml data/taxa/archaea/natronomonas_sp_sa21.yaml data/taxa/archaea/natronomonas_gomsonensis.yaml data/taxa/archaea/candidatus_methanophagaceae_archaeon_scgc_aaa252_l18.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 63 YAML lines, 10 lineage entries, 1 exact NCBI synonym, 2 source attestations, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1046934` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:224702`, 10 checked lineage entries with no missing rows or mismatches, 1 retained GOLD aggregate row, 0 native GOLD organism rows, 0 native GOLD projects, 0 native GOLD analyses, 0 NCBI merge rows, 0 NCBI type-material rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1046934` resolves to `Candidatus Methanophagaceae archaeon SCGC
AAA252-L18`, rank `SPECIES`, parent `NCBITaxon:3386246`, genetic code `11`,
source set `ncbitaxon|gold`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:3386246` unclassified Candidatus Methanophagaceae. The bounded scan
found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species-rank single-cell identity, direct
unclassified-Candidatus-Methanophagaceae parent, genetic code, exact synonym
`ANME-1 cluster archaeon SCGC AAA252-L18`, and 2026-09-13 snapshot date. The
seed event is supported by `curation/seed_scope.tsv:57295`.

The retained GOLD aggregate row recorded 1 organism for the exact target but
no native GOLD organism, project, or analysis rows and no normalized GOLD
strain rows are filed under this taxon in committed source tables.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, retained GOLD, seed, path, and
generated YAML inputs, and found no omitted GTDB, LPSN, BacDive, strain,
native GOLD, type-material, StrainInfo, or culture-collection row.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

This was a read-only generated-record review; it did not append history, promote `mapping_status`, or touch YAML.
`strain_count: 0` is expected without an exact BacDive or normalized strain row.
The exact NCBI synonym was materialized.
The retained GOLD row remained aggregate-only.
No `taxonomy_mappings` section is expected.
No xref section is expected.
No native GOLD rows were present for this target.
One retained GOLD aggregate row is filed on this target.
No normalized genome assembly rows were present.
No normalized genome records were present.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The GOLD source attestation is expected without a strain block.
The 63-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
