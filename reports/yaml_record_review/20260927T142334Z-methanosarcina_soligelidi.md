# YAML Record Review: Methanosarcina soligelidi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/methanosarcina_soligelidi.yaml
- Started UTC: 2026-09-27T14:23:34Z
- Finished UTC: 2026-09-27T14:23:34Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/methanosarcina_soligelidi.yaml` |
| Identifier | `NCBITaxon:1036677` |
| Label | `Methanosarcina soligelidi` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2207` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated BacDive, GOLD, GTDB, LPSN, MediaDive, MADIN, and
NCBI-backed archaeal species record, with path pinned by `data/taxa/PATHS.tsv:15096`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/methanosarcina_soligelidi.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/uncultured_methanogen_r9.yaml data/taxa/archaea/uncultured_thermogymnomonas_sp.yaml data/taxa/archaea/methanosarcina_soligelidi.yaml data/taxa/archaea/methanobacterium_movilense.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 312 YAML lines, 10 lineage entries, 1 LPSN nomenclature entry, 1 GTDB mapping, 3 synonyms, 2 xrefs, 1 BacDive strain, 1 genome assembly, 2 genome records, 9 related records, 7 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1036677` in the expected seed, NCBI, GTDB, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:222578`, 10 checked lineage entries with no missing rows or mismatches, 1 LPSN row, 1 GTDB row at line 1461, 1 BacDive row, 1 MADIN row, 1 MediaDive row, 1 retained GOLD aggregate row, 1 native GOLD organism, 1 project, 1 analysis, 2 culture-collection rows, 1 normalized assembly, 2 genome rows, 3 exact-target StrainInfo related rows, 6 type-material rows, and 0 NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1036677` resolves to `Methanosarcina soligelidi`, rank `SPECIES`,
parent `NCBITaxon:2207`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy
snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
genus `NCBITaxon:2207` Methanosarcina. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

LPSN row `lpsn:791021` supports the nomenclature block, Wagner et al. 2013
authority, correct-name status, type strain IDs DSM-26065/JCM-18468, two DOIs,
PMID:23378113, and sequence accession `INSDC:AB973359`.

The GTDB row supports the `GTDB:s__Methanosarcina_mazei` closeMatch with 89
genomes. BacDive row 24170 supports local strain `bacdive_24170`, designation
SMA-21, a BacDive contig assembly, and two BacDive genome records.

MediaDive, MADIN, retained GOLD, native GOLD, and three exact-target
StrainInfo related rows account for the remaining generated source blocks.
Four GOLD and two StrainInfo related records preserve culture-ID side evidence
whose source rows carry off-target taxon IDs.

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
The GTDB closeMatch has 89 genomes.
Native GOLD supplied one organism/project/analysis chain.
Three exact-target StrainInfo side rows were materialized.
Cross-taxon side rows preserve source taxon IDs.
The generated record materializes 9 related records.
Six NCBI type-material rows were checked.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The 312-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
