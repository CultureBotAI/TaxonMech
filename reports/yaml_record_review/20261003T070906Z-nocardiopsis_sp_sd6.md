# YAML Record Review: [Nocardiopsis] sp. SD6

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/nocardiopsis_sp_sd6.yaml
- Started UTC: 2026-10-03T07:09:06Z
- Finished UTC: 2026-10-03T07:09:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/nocardiopsis_sp_sd6.yaml` |
| Identifier | `NCBITaxon:1031330` |
| Label | `[Nocardiopsis] sp. SD6` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2649073` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only `Nocardiopsis` placeholder record, with
path pinned by `data/taxa/PATHS.tsv:12967`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/nocardiopsis_sp_sd6.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12958-12967` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 58 YAML lines, 10 lineage entries, 1 source attestation, 1 synonym, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1031330` in the expected seed and NCBI rows; found no exact GTDB, GOLD, MADIN, StrainInfo, ATB, or legacy-path row for this identifier. |
| Exact prior-report probe | Found no `*-nocardiopsis_sp_sd6.md` report under `reports/yaml_record_review`, with ignored files included. |
| First-column lineage scan | Found all expected committed NCBI lineage rows, ending at `NCBITaxon:2649073`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1031330` resolves to label `[Nocardiopsis] sp. SD6`, rank
`SPECIES`, direct parent `NCBITaxon:2649073`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`unclassified Nocardiopsis`. The single retained NCBI synonym is present as an
`EXACT_SYNONYM`, as expected for the unbracketed `Nocardiopsis sp. SD6` name.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220660` supports the species
identity, direct `unclassified Nocardiopsis` parent, genetic code, retained
synonym, single NCBITAXON source attestation, and 2026-09-13 snapshot date. The
seed event is supported by `curation/seed_scope.tsv:321075`.

Exact source scans found no exact GTDB mapping, GOLD organism row, MADIN row,
legacy page path, StrainInfo row, or ATB row for `NCBITaxon:1031330`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, seed, and target YAML inputs, and
found no extra retained source rows or strain evidence for this identifier.

The 58-line YAML shape is expected for this NCBITaxon-only species placeholder
lineage with one retained NCBI synonym; no `taxonomy_mappings`, xref, strain,
genome, or causal graph section is expected.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.
