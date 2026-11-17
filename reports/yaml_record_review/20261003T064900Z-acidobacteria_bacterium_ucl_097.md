# YAML Record Review: Acidobacteria bacterium UCL-097

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acidobacteria_bacterium_ucl_097.yaml
- Started UTC: 2026-10-03T06:49:00Z
- Finished UTC: 2026-10-03T06:49:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acidobacteria_bacterium_ucl_097.yaml` |
| Identifier | `NCBITaxon:1030811` |
| Label | `Acidobacteria bacterium UCL-097` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:305072` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only phylum-level placeholder record, with
path pinned by `data/taxa/PATHS.tsv:12835`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acidobacteria_bacterium_ucl_097.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12828-12837` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 42 YAML lines, 6 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030811` in the expected seed and NCBI rows; found no exact GTDB, GOLD, MADIN, StrainInfo, ATB, or legacy-path row for this identifier. |
| Exact prior-report probe | Found no `*-acidobacteria_bacterium_ucl_097.md` report under `reports/yaml_record_review`, with ignored files included. |
| First-column lineage scan | Found all expected committed NCBI lineage rows, ending at `NCBITaxon:305072`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030811` resolves to label `Acidobacteria bacterium UCL-097`, rank
`SPECIES`, direct parent `NCBITaxon:305072`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`unclassified Acidobacteriota`. No retained synonym text is present in the NCBI
row, and the generated YAML correctly omits a `synonyms` section.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220579` supports the species
identity, direct unclassified-Acidobacteriota parent, genetic code, empty
synonym columns, single NCBITAXON source attestation, and 2026-09-13 snapshot
date. The seed event is supported by `curation/seed_scope.tsv:321002`.

Exact source scans found no exact GTDB mapping, GOLD organism row, MADIN row,
legacy page path, StrainInfo row, or ATB row for `NCBITaxon:1030811`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, seed, and target YAML inputs, and
found no extra retained source rows or strain evidence for this identifier.

The 42-line YAML shape is expected for this phylum-level placeholder lineage; no
class, order, family, genus, `taxonomy_mappings`, `synonyms`, xref, strain,
genome, or causal graph section is expected.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.
