# YAML Record Review: Methanosarcina spelaei

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/methanosarcina_spelaei.yaml
- Started UTC: 2026-09-27T14:27:47Z
- Finished UTC: 2026-09-27T14:27:47Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/methanosarcina_spelaei.yaml` |
| Identifier | `NCBITaxon:1036679` |
| Label | `Methanosarcina spelaei` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2207` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated BacDive, GOLD, GTDB, LPSN, MediaDive, MADIN, and
NCBI-backed archaeal species record, with path pinned by `data/taxa/PATHS.tsv:15098`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/methanosarcina_spelaei.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/methanosarcina_spelaei.yaml data/taxa/archaea/thermococcus_sp_9on_7.yaml data/taxa/archaea/methanocella_conradii_hz254.yaml data/taxa/archaea/thermococcus_sp_4557.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 266 YAML lines, 10 lineage entries, 1 LPSN nomenclature entry, 1 GTDB mapping, 2 related NCBI synonyms, 2 xrefs, 1 BacDive strain, 1 genome assembly, 2 genome records, 7 related records, 7 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1036679` in the expected seed, NCBI, GTDB, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:222580`, 10 checked lineage entries with no missing rows or mismatches, 1 LPSN row, 1 GTDB row at line 1462, 1 BacDive row, 1 MADIN row, 1 MediaDive row, 1 retained GOLD aggregate row, 3 native GOLD organism rows, 1 project, 1 analysis, 2 culture-collection rows, 1 normalized assembly, 2 genome rows, 4 exact GOLD related rows, 3 StrainInfo rows, 6 type-material rows, and 0 NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1036679` resolves to `Methanosarcina spelaei`, rank `SPECIES`,
parent `NCBITaxon:2207`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy
snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
genus `NCBITaxon:2207` Methanosarcina. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

LPSN row `lpsn:792237` supports the nomenclature block, Ganzert et al. 2014
authority, correct-name status, type strain IDs DSM-26047/JCM-18469, two DOIs,
PMID:25052394, and sequence accession `INSDC:JF812257`.

The GTDB row supports the `GTDB:s__Methanosarcina_spelaei` closeMatch with 4
genomes. BacDive row 24168 supports local strain `bacdive_24168`, designation
MC-15, a BacDive contig assembly, and two BacDive genome records.

MediaDive, MADIN, retained GOLD, native GOLD, exact GOLD related rows, and
three exact-target StrainInfo rows account for the remaining generated source
blocks. All 7 related records carry exact target taxon IDs.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, GTDB, BacDive, MediaDive,
MADIN, GOLD, StrainInfo, type-material, seed, path, and generated YAML inputs.

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
The LPSN row links to the same GTDB species.
Native GOLD supplied three organism rows.
One native GOLD project was present for this target.
One native GOLD analysis was present for this target.
Three exact-target StrainInfo rows were materialized.
The generated record materializes 7 related records.
Six NCBI type-material rows were checked.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The 266-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
