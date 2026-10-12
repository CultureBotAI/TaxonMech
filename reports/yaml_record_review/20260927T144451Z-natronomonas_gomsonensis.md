# YAML Record Review: Natronomonas gomsonensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/natronomonas_gomsonensis.yaml
- Started UTC: 2026-09-27T14:44:51Z
- Finished UTC: 2026-09-27T14:44:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/natronomonas_gomsonensis.yaml` |
| Identifier | `NCBITaxon:1046043` |
| Label | `Natronomonas gomsonensis` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:63743` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated BacDive, GOLD, GTDB, LPSN, and NCBI-backed archaeal
species record, with path pinned by `data/taxa/PATHS.tsv:17157`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/natronomonas_gomsonensis.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/natronomonas_sp_sa2.yaml data/taxa/archaea/natronomonas_sp_sa21.yaml data/taxa/archaea/natronomonas_gomsonensis.yaml data/taxa/archaea/candidatus_methanophagaceae_archaeon_scgc_aaa252_l18.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 627 YAML lines, 10 lineage entries, 1 LPSN nomenclature entry, 2 broad GTDB mappings, 3 related NCBI synonyms, 2 xrefs, 1 BacDive strain, 14 genome assembly rows, 8 genome records, 26 related records, 5 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1046043` in the expected seed, NCBI, GTDB, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:224524`, 10 checked lineage entries with no missing rows or mismatches, 1 LPSN row, 2 GTDB rows, 1 BacDive row, 1 retained GOLD aggregate row, 2 native GOLD organism rows, 2 native GOLD projects, 2 native GOLD analyses, 2 culture rows, 14 normalized assemblies, 8 genome rows, 26 related rows, 6 type-material rows, 0 exact StrainInfo rows, and 0 NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1046043` resolves to `Natronomonas gomsonensis`, rank `SPECIES`,
parent `NCBITaxon:63743`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|gold`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
genus `NCBITaxon:63743` Natronomonas. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

LPSN row `lpsn:791806` supports the nomenclature block, Kim et al. 2014
authority, correct-name status, type strain IDs JCM-17867/KCTC-4088, two DOIs,
PMID:23851717, and sequence accession `INSDC:JF950943`.

GTDB rows support the `GTDB:s__Natronomonas_gomsonensis` and
`GTDB:s__Natronomonas_gomsonensis_A` broadMatch mappings. BacDive row 162125
supports local strain `bacdive_162125`, two culture IDs, and `medium_count: 1`.

Retained GOLD, native GOLD, GTDB, BV-BRC, BacDive genome, and NCBI Assembly
rows account for the 14 assembly rows, 8 genome rows, and 26 related records.
All generated related records carry exact target taxon IDs.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, GTDB, BacDive, GOLD,
type-material, seed, path, strain, assembly, genome, and generated YAML inputs.

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
`strain_count: 1` matches the exact BacDive strain row.
Both GTDB mappings are intentionally `skos:broadMatch`.
The retained GOLD aggregate row counted 2 organisms.
Native GOLD supplied two organism/project/analysis chains.
Fourteen normalized assembly rows were materialized.
Eight genome rows were materialized.
No exact-target StrainInfo row was present.
The generated record materializes 26 related records.
Six NCBI type-material rows were checked.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The 627-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
