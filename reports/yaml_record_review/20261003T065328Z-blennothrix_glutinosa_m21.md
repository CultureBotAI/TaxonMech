# YAML Record Review: Blennothrix glutinosa M21

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/blennothrix_glutinosa_m21.yaml
- Started UTC: 2026-10-03T06:53:28Z
- Finished UTC: 2026-10-03T06:53:28Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/blennothrix_glutinosa_m21.yaml` |
| Identifier | `NCBITaxon:1031253` |
| Label | `Blennothrix glutinosa M21` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:933307` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only `Blennothrix glutinosa` strain record,
with path pinned by `data/taxa/PATHS.tsv:12923`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/blennothrix_glutinosa_m21.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12918-12927` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 64 YAML lines, 12 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 1 synonym, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1031253` in the expected seed and NCBI rows; found no exact GTDB, GOLD, MADIN, StrainInfo, ATB, or legacy-path row for this identifier. |
| Exact prior-report probe | Found no `*-blennothrix_glutinosa_m21.md` report under `reports/yaml_record_review`, with ignored files included. |
| First-column lineage scan | Found all expected committed NCBI lineage rows, ending at `NCBITaxon:933307`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1031253` resolves to label `Blennothrix glutinosa M21`, rank
`STRAIN`, direct parent `NCBITaxon:933307`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`Blennothrix glutinosa`. The single retained NCBI synonym is present as an
`EXACT_SYNONYM`, as expected for `Hydrocoleum glutinosum M21`.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220622` supports the strain
identity, direct `Blennothrix glutinosa` parent, genetic code, retained synonym,
single NCBITAXON source attestation, and 2026-09-13 snapshot date. The seed
event is supported by `curation/seed_scope.tsv:321041`.

Exact source scans found no exact GTDB mapping, GOLD organism row, MADIN row,
legacy page path, StrainInfo row, or ATB row for `NCBITaxon:1031253`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, seed, and target YAML inputs, and
found no extra retained source rows or strain evidence for this identifier.

The 64-line YAML shape is expected for this NCBITaxon-only strain lineage with
one retained NCBI synonym; no `taxonomy_mappings`, xref, strain, genome, or
causal graph section is expected.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.
