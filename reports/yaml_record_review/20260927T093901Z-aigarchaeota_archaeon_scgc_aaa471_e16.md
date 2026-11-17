# YAML Record Review: Aigarchaeota archaeon SCGC AAA471-E16

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/aigarchaeota_archaeon_scgc_aaa471_e16.yaml
- Started UTC: 2026-09-27T09:39:01Z
- Finished UTC: 2026-09-27T09:39:01Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/aigarchaeota_archaeon_scgc_aaa471_e16.yaml` |
| Identifier | `NCBITaxon:1052828` |
| Label | `Aigarchaeota archaeon SCGC AAA471-E16` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:1104572` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only archaeal species record, with path
pinned by `data/taxa/PATHS.tsv:19909` and one NCBI exact synonym.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/aigarchaeota_archaeon_scgc_aaa471_e16.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/aigarchaeota_archaeon_scgc_aaa471_b22.yaml data/taxa/archaea/aigarchaeota_archaeon_scgc_aaa471_d15.yaml data/taxa/archaea/aigarchaeota_archaeon_scgc_aaa471_e16.yaml data/taxa/archaea/aigarchaeota_archaeon_scgc_aaa471_g05.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 46 YAML lines, 6 lineage entries, 1 exact NCBI synonym, 1 NCBITAXON source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1052828` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:227157`, 6 checked lineage entries with no missing rows or mismatches, 1 exact native GOLD organism at line 10580, 1 native GOLD project at line 10438, 1 native GOLD analysis at line 16721, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1052828` resolves to label `Aigarchaeota archaeon SCGC AAA471-E16`,
rank `SPECIES`, parent `NCBITaxon:1104572`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`. The generated record carries
those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 6 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:1104572` unclassified
Nitrososphaerota. The bounded scan found no NCBI merge row and no retained
old-id row.

## Evidence

The NCBI row supports exact synonym `candidate division pSL4 archaeon SCGC
AAA471-E16`, the single NCBITAXON source attestation, and the 2026-09-13
snapshot date. The seed event is supported by `curation/seed_scope.tsv:326762`.

Native GOLD has exact side evidence for `Go0012013`, project `Gp0012013`, and
one contamination-screened analysis. There is no retained aggregate GOLD row,
so the generated YAML correctly remains NCBITaxon-only.

No LPSN, GTDB, GOLD aggregate, BacDive, MediaDive, MADIN, BactoTraits, NCBI
type-material, StrainInfo, culture-collection, normalized assembly, normalized
genome, or normalized related-record row is filed under this exact taxon.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, seed, path, native GOLD side rows,
and generated YAML inputs, and found no omitted GTDB, LPSN, retained GOLD,
BacDive, MediaDive, MADIN, BactoTraits, type-material, or strain inventory row.

An ignored-file-inclusive `find` under `reports/yaml_record_review` returned no
existing Markdown report for this stem before this report was written.

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
No `taxonomy_mappings` section is expected.
No xref section is expected.
No retained GOLD aggregate row is filed on this target.
Native GOLD rows do not create generated child strains by themselves.
No NCBI merge row complicates identity.
The ignored report probe included gitignored files.
