# YAML Record Review: Helicobacter pylori BO2362

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/helicobacter_pylori_bo2362.yaml
- Started UTC: 2026-10-03T06:37:21Z
- Finished UTC: 2026-10-03T06:37:21Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/helicobacter_pylori_bo2362.yaml` |
| Identifier | `NCBITaxon:103104` |
| Label | `Helicobacter pylori BO2362` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:210` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only `Helicobacter pylori` strain record,
with path pinned by `data/taxa/PATHS.tsv:12886`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/helicobacter_pylori_bo2362.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 9 reviewed `Helicobacter pylori` files from `data/taxa/PATHS.tsv:12878-12887` | Passed strict validation with 9 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 54 YAML lines, 10 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:103104` in the expected seed and NCBI rows; found no exact GTDB, GOLD, MADIN, StrainInfo, ATB, or legacy-path row for this identifier. |
| Exact prior-report probe | Found no `*-helicobacter_pylori_bo2362.md` report under `reports/yaml_record_review`, with ignored files included. |
| First-column lineage scan | Found all expected committed NCBI lineage rows, ending at `NCBITaxon:210`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:103104` resolves to label `Helicobacter pylori BO2362`, rank
`STRAIN`, direct parent `NCBITaxon:210`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`Helicobacter pylori`. No retained synonym text is present in the NCBI row, and
the generated YAML correctly omits a `synonyms` section.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:18271` supports the strain
identity, direct `Helicobacter pylori` parent, genetic code, empty synonym
columns, single NCBITAXON source attestation, and 2026-09-13 snapshot date. The
seed event is supported by `curation/seed_scope.tsv:143932`.

Exact source scans found no exact GTDB mapping, GOLD organism row, MADIN row,
legacy page path, StrainInfo row, or ATB row for `NCBITaxon:103104`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, seed, and target YAML inputs, and
found no extra retained source rows or strain evidence for this identifier.

The 54-line YAML shape is expected for this NCBITaxon-only strain lineage; no
`taxonomy_mappings`, `synonyms`, xref, strain, genome, or causal graph section
is expected.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.
