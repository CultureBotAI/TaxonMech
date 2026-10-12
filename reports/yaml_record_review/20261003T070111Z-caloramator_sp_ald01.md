# YAML Record Review: Caloramator sp. ALD01

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/caloramator_sp_ald01.yaml
- Started UTC: 2026-10-03T07:01:11Z
- Finished UTC: 2026-10-03T07:01:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/caloramator_sp_ald01.yaml` |
| Identifier | `NCBITaxon:1031288` |
| Label | `Caloramator sp. ALD01` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2629145` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon+GTDB `Caloramator` placeholder record, with
path pinned by `data/taxa/PATHS.tsv:12939`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/caloramator_sp_ald01.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12938-12947` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 73 YAML lines, 10 lineage entries, 2 source attestations, 1 taxonomy mapping, 1 GTDB synonym, 1 xref, 0 nomenclature entries, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1031288` in the expected seed, NCBI, and GTDB rows; found no exact GOLD, MADIN, StrainInfo, ATB, or legacy-path row for this identifier. |
| Exact prior-report probe | Found no `*-caloramator_sp_ald01.md` report under `reports/yaml_record_review`, with ignored files included. |
| First-column lineage scan | Found all expected committed NCBI lineage rows, ending at `NCBITaxon:2629145`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1031288` resolves to label `Caloramator sp. ALD01`, rank `SPECIES`,
direct parent `NCBITaxon:2629145`, genetic code `11`, source set
`ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`unclassified Caloramator`. GTDB contributes one closeMatch mapping with three
supporting genomes, a `Thermobrachium proteoclasticum` exact synonym, and the
matching GTDB xref.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220637` supports the species
identity, direct `unclassified Caloramator` parent, genetic code, source set,
and 2026-09-13 snapshot date. The GTDB mapping is supported by
`data/raw/gtdb_mappings.tsv:1300`, and the seed event by
`curation/seed_scope.tsv:66001`.

Exact source scans found no exact GOLD organism row, MADIN row, legacy page
path, StrainInfo row, or ATB row for `NCBITaxon:1031288`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, GTDB, seed, and target YAML inputs
and found no extra retained source rows or strain evidence for this identifier.

The 73-line YAML shape is expected for this NCBITaxon+GTDB placeholder lineage;
no nomenclature, strain, genome, or causal graph section is expected.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.
