# YAML Record Review: Methanothermobacter crinale

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/methanothermobacter_crinale.yaml
- Started UTC: 2026-09-27T14:41:30Z
- Finished UTC: 2026-09-27T14:41:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/methanothermobacter_crinale.yaml` |
| Identifier | `NCBITaxon:1045764` |
| Label | `Methanothermobacter crinale` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:145260` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated BacDive, GOLD, LPSN, MediaDive, MADIN, StrainInfo, and
NCBI-backed archaeal species record, with path pinned by `data/taxa/PATHS.tsv:17092`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/methanothermobacter_crinale.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/methanothermobacter_crinale.yaml data/taxa/archaea/halorubrum_sp_btsh03.yaml data/taxa/archaea/natronomonas_sp_sa1.yaml data/taxa/archaea/natronomonas_sp_sa11.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 326 YAML lines, 10 lineage entries, 1 LPSN nomenclature entry, 0 GTDB mappings, 3 related NCBI synonyms, 1 xref, 1 BacDive strain, 2 NCBI Assembly rows, 2 BV-BRC genome rows, 14 related records, 6 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1045764` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:224469`, 10 checked lineage entries with no missing rows or mismatches, 1 LPSN row, 1 BacDive row, 1 MADIN row, 1 MediaDive row, 1 retained GOLD aggregate row, 4 native GOLD organism rows, no native GOLD projects or analyses, 3 culture rows, 2 normalized assemblies, 2 BV-BRC genome rows, 12 raw strain related rows, 2 exact StrainInfo rows, 8 type-material rows, and 1 NCBI merge row. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1045764` resolves to `Methanothermobacter crinale`, rank `SPECIES`,
parent `NCBITaxon:145260`, genetic code `11`, source set
`ncbitaxon|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
genus `NCBITaxon:145260` Methanothermobacter. Old `NCBITaxon:1054977` is
merged into this current target and no retained old-id row exists.

## Evidence

LPSN row `lpsn:789743` supports the nomenclature block, Cheng et al. 2012
authority, correct-name status, type strain IDs DSM-24598/JCM-17393, two DOIs,
PMID:21705537, and sequence accession `INSDC:HQ283273`.

BacDive row 6899 supports local strain `bacdive_6899`, designation Tm2,
type-material culture IDs ACCC 00699, DSM-24598, and JCM-17393, 2 NCBI
Assembly rows, and 2 BV-BRC genome records.

MediaDive, MADIN, retained GOLD, four native GOLD organism rows, and two
exact-target StrainInfo rows account for the remaining generated source
blocks. The bounded scan found no GTDB, native GOLD project, or analysis row.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, BacDive, MediaDive, MADIN,
GOLD, StrainInfo, type-material, seed, path, and generated YAML inputs.

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
No `taxonomy_mappings` section is expected without a GTDB row.
The retained GOLD aggregate row counted 4 organisms.
Native GOLD supplied four organism rows as side evidence.
Three culture-collection rows were checked.
Two NCBI Assembly rows were materialized.
Two BV-BRC genome records were materialized.
The generated record materializes 14 related records.
Eight NCBI type-material rows were checked.
One NCBI merge row was checked.
Ten NCBI lineage rows are expected.
The 326-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
