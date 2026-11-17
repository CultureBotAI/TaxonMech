# YAML Record Review: Halopenitus persicus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/halopenitus_persicus.yaml
- Started UTC: 2026-09-27T14:54:26Z
- Finished UTC: 2026-09-27T14:54:26Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/halopenitus_persicus.yaml` |
| Identifier | `NCBITaxon:1048396` |
| Label | `Halopenitus persicus` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:1209988` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated BacDive, GOLD, GTDB, LPSN, MADIN, StrainInfo, and
NCBI-backed archaeal species record, with path pinned by `data/taxa/PATHS.tsv:18178`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/halopenitus_persicus.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/thaumarchaeota_archaeon_scgc_aaa471_d07.yaml data/taxa/archaea/halopenitus_persicus.yaml data/taxa/archaea/methanohalophilus_sp_t3_30_5.yaml data/taxa/archaea/methanohalophilus_sp_t2_21_5.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 472 YAML lines, 10 lineage entries, 1 LPSN nomenclature entry, 2 broad GTDB mappings, 2 related NCBI synonyms, 2 xrefs, 1 BacDive strain, 7 assembly rows, 6 genome records, 16 related records, 6 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1048396` in the expected seed, NCBI, GTDB, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:225529`, 10 checked lineage entries with no missing rows or mismatches, 1 LPSN row, 2 GTDB rows, 1 BacDive row, 1 MADIN row, 1 retained GOLD aggregate row, 2 native GOLD organism rows, 2 native GOLD projects, 2 native GOLD analyses, 2 culture rows, 6 raw assemblies plus 1 StrainInfo assembly, 6 genome rows, 14 raw related rows plus 2 StrainInfo related rows, 6 type-material rows, and 0 NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1048396` resolves to `Halopenitus persicus`, rank `SPECIES`, parent
`NCBITaxon:1209988`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
genus `NCBITaxon:1209988` Halopenitus. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

LPSN row `lpsn:790044` supports the nomenclature block, Amoozegar et al. 2012
authority, correct-name status, type strain ID KCTC-4046, two DOIs,
PMID:22003044, and sequence accession `INSDC:JF979130`.

GTDB rows support the `GTDB:s__Halopenitus_persicus` and
`GTDB:s__Halopenitus_persicus_A` broadMatch mappings. BacDive row 133781
supports local strain `bacdive_133781`, designation DC30, and two culture IDs.

Retained GOLD, native GOLD, GTDB, BV-BRC, BacDive genome, MADIN, and
StrainInfo rows account for the 7 assembly rows, 6 genome rows, and 16 related
records. All generated related records carry exact target taxon IDs.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, GTDB, BacDive, GOLD, MADIN,
StrainInfo, type-material, seed, path, strain, assembly, genome, and generated
YAML inputs.

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
One exact StrainInfo assembly row was materialized.
Two exact StrainInfo related rows were materialized.
The generated record materializes 16 related records.
Six NCBI type-material rows were checked.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The 472-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
