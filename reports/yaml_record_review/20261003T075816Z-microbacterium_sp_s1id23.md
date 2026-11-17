# YAML Record Review: Microbacterium sp. S1ID23

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/microbacterium_sp_s1id23.yaml
- Started UTC: 2026-10-03T07:58:16Z
- Finished UTC: 2026-10-03T07:58:16Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/microbacterium_sp_s1id23.yaml` |
| Identifier | `NCBITaxon:1031577` |
| Label | `Microbacterium sp. S1ID23` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2609290` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only `Microbacterium` species placeholder,
with path pinned by `data/taxa/PATHS.tsv:13085`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/microbacterium_sp_s1id23.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 9-file covered `data/taxa/PATHS.tsv:13079-13087` subset | Passed strict validation with 9 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 54 YAML lines, 10 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1031577` in the expected seed and NCBI rows; found no exact GTDB, GOLD, MADIN, StrainInfo, ATB, or auxiliary raw row for this identifier. |
| Exact prior-report probe | Found no `*-microbacterium_sp_s1id23.md` report under `reports/yaml_record_review`, with ignored files included. |
| First-column lineage scan | Found all expected committed NCBI lineage rows, ending at `NCBITaxon:2609290`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1031577` resolves to label `Microbacterium sp. S1ID23`, rank
`SPECIES`, direct parent `NCBITaxon:2609290`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`unclassified Microbacterium`. No retained synonym text is present in the NCBI
row, and the generated YAML correctly omits a `synonyms` section.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220755` supports the species
placeholder identity, direct `unclassified Microbacterium` parent, genetic code,
empty synonym columns, single NCBITAXON source attestation, and 2026-09-13
snapshot date. The seed event is supported by `curation/seed_scope.tsv:321160`.

Exact source scans found no exact GTDB mapping, GOLD organism row, MADIN row,
StrainInfo row, or ATB row for `NCBITaxon:1031577`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, seed, and target YAML inputs, and
found no extra retained source rows or strain evidence for this identifier.

The 54-line YAML shape is expected for this NCBITaxon-only species placeholder
lineage; no `taxonomy_mappings`, `synonyms`, xref, strain, genome, or causal
graph section is expected.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.
