# YAML Record Review: Aigarchaeota archaeon JGI 0000001-B8

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/aigarchaeota_archaeon_jgi_0000001_b8.yaml
- Started UTC: 2026-09-27T09:35:40Z
- Finished UTC: 2026-09-27T09:35:40Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/aigarchaeota_archaeon_jgi_0000001_b8.yaml` |
| Identifier | `NCBITaxon:1052839` |
| Label | `Aigarchaeota archaeon JGI 0000001-B8` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:1104572` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only archaeal species record, with path
pinned by `data/taxa/PATHS.tsv:19921` and one NCBI exact synonym.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/aigarchaeota_archaeon_jgi_0000001_b8.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/aigarchaeota_archaeon_jgi_0000001_a7.yaml data/taxa/archaea/aigarchaeota_archaeon_jgi_0000001_b8.yaml data/taxa/archaea/aigarchaeota_archaeon_jgi_0000001_h6.yaml data/taxa/archaea/aigarchaeota_archaeon_scgc_aaa471_a16.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 46 YAML lines, 6 lineage entries, 1 exact NCBI synonym, 1 NCBITAXON source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1052839` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:227168`, 6 checked lineage entries with no missing rows or mismatches, 1 exact native GOLD organism at line 9976, 1 native GOLD project at line 9837, 1 native GOLD analysis at line 16719, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1052839` resolves to label `Aigarchaeota archaeon JGI 0000001-B8`,
rank `SPECIES`, parent `NCBITaxon:1104572`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`. The generated record carries
those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 6 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:1104572` unclassified
Nitrososphaerota. The bounded scan found no NCBI merge row and no retained
old-id row.

## Evidence

The NCBI row supports exact synonym `candidate division pSL4 archaeon JGI
0000001-B8`, the single NCBITAXON source attestation, and the 2026-09-13
snapshot date. The seed event is supported by `curation/seed_scope.tsv:326772`.

Native GOLD has exact side evidence for `Go0011359`, project `Gp0011359`, and
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
