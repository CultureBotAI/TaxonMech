# YAML Record Review: Nanoarchaeota archaeon SCGC AAA011-L22

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/nanoarchaeota_archaeon_scgc_aaa011_l22.yaml
- Started UTC: 2026-09-27T14:49:36Z
- Finished UTC: 2026-09-27T14:49:36Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/nanoarchaeota_archaeon_scgc_aaa011_l22.yaml` |
| Identifier | `NCBITaxon:1046946` |
| Label | `Nanoarchaeota archaeon SCGC AAA011-L22` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2303497` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated GTDB- and NCBI-backed Nanoarchaeota single-cell record,
with path pinned by `data/taxa/PATHS.tsv:17374`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/nanoarchaeota_archaeon_scgc_aaa011_l22.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/candidatus_aenigmarchaeota_archaeon_scgc_aaa011_f07.yaml data/taxa/archaea/candidate_division_dusel4_archaeon_scgc_aaa011_l21.yaml data/taxa/archaea/nanoarchaeota_archaeon_scgc_aaa011_l22.yaml data/taxa/archaea/thaumarchaeota_archaeon_scgc_aaa010_g21.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 64 YAML lines, 6 lineage entries, 1 GTDB closeMatch, 2 exact synonyms, 1 xref, 0 nomenclature entries, 0 strains, 0 genome assemblies, 0 genome records, 2 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1046946` in the expected seed, NCBI, GTDB, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:224713`, 6 checked lineage entries with no missing rows or mismatches, 1 GTDB row at line 1813, 1 native GOLD organism row, 1 native GOLD project, 2 native GOLD analyses, 0 GOLD aggregate rows, 0 NCBI merge rows, 0 NCBI type-material rows, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1046946` resolves to `Nanoarchaeota archaeon SCGC AAA011-L22`, rank
`SPECIES`, parent `NCBITaxon:2303497`, genetic code `11`, source set
`ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 6 committed NCBI rows, ending at
`NCBITaxon:2303497` unclassified Nanobdellota. The bounded scan found no NCBI
merge row and no retained old-id row.

## Evidence

The NCBI row supports the species-rank identity, direct
unclassified-Nanobdellota parent, genetic code, exact synonym `candidate
division DUSEL4 archaeon SCGC AAA011-L22`, and 2026-09-13 snapshot date.

The GTDB row supports the `GTDB:s__SCGC-AAA011-G17_sp000402515` closeMatch
mapping and GTDB exact synonym with 3 genomes. Native GOLD supplied one
organism, one project, and two analyses as side evidence only; no retained
GOLD aggregate or normalized GOLD strain row is filed under this taxon.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, seed, path, and generated
YAML inputs, and found no omitted LPSN, retained GOLD, BacDive, type-material,
StrainInfo, or culture-collection row.

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
The GTDB closeMatch has 3 genomes.
The GTDB exact synonym was materialized.
The NCBI exact synonym was materialized.
No native GOLD row was normalized for this target.
No retained GOLD aggregate row is filed on this target.
One native GOLD organism row was side evidence only.
One native GOLD project row was side evidence only.
Two native GOLD analyses were side evidence only.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Six NCBI lineage rows are expected.
No normalized genome assembly rows were present.
The 64-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
