# YAML Record Review: actinomycete MS7

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/actinomycete_ms7.yaml
- Started UTC: 2026-10-03T08:08:27Z
- Finished UTC: 2026-10-03T08:08:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/actinomycete_ms7.yaml` |
| Identifier | `NCBITaxon:1031688` |
| Label | `actinomycete MS7` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:105426` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only unclassified `Actinomycetales` species
placeholder, with path pinned by `data/taxa/PATHS.tsv:13117`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/actinomycete_ms7.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file covered `data/taxa/PATHS.tsv:13108-13117` subset | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 47 YAML lines, 8 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1031688` in the expected seed and NCBI rows; found no exact GTDB, GOLD, MADIN, StrainInfo, ATB, or auxiliary raw row for this identifier. |
| Exact prior-report probe | Found no `*-actinomycete_ms7.md` report under `reports/yaml_record_review`, with ignored files included. |
| First-column lineage scan | Found all expected committed NCBI lineage rows, ending at `NCBITaxon:105426`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1031688` resolves to label `actinomycete MS7`, rank `SPECIES`,
direct parent `NCBITaxon:105426`, genetic code `11`, source set `ncbitaxon`,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`unclassified Actinomycetales`. No retained synonym text is present in the NCBI
row, and the generated YAML correctly omits a `synonyms` section.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220776` supports the species
placeholder identity, direct `unclassified Actinomycetales` parent, genetic
code, empty synonym columns, single NCBITAXON source attestation, and
2026-09-13 snapshot date. The seed event is supported by
`curation/seed_scope.tsv:321180`.

Exact source scans found no exact GTDB mapping, GOLD organism row, MADIN row,
StrainInfo row, or ATB row for `NCBITaxon:1031688`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, seed, and target YAML inputs, and
found no extra retained source rows or strain evidence for this identifier.

The 47-line YAML shape is expected for this NCBITaxon-only species placeholder
lineage; no `taxonomy_mappings`, `synonyms`, xref, strain, genome, or causal
graph section is expected.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.
