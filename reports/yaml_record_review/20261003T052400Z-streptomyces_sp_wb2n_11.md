# YAML Record Review: Streptomyces sp. Wb2n-11

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/streptomyces_sp_wb2n_11.yaml
- Started UTC: 2026-10-03T05:24:00Z
- Finished UTC: 2026-10-03T05:24:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/streptomyces_sp_wb2n_11.yaml` |
| Identifier | `NCBITaxon:1030533` |
| Label | `Streptomyces sp. Wb2n-11` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2593676` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon species record with a retained GTDB mapping,
with path pinned by `data/taxa/PATHS.tsv:12662`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/streptomyces_sp_wb2n_11.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12658-12667` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 73 YAML lines, 10 lineage entries, 2 source attestations, 1 taxonomy mapping, 1 GTDB synonym, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030533` in the expected seed, NCBI, and GTDB rows; found no exact GOLD, MADIN, StrainInfo, ATB, or legacy-path row for this identifier. |
| Exact prior-report probe | Found no `*-streptomyces_sp_wb2n_11.md` report under `reports/yaml_record_review`, with ignored files included. |
| First-column lineage scan | Found all expected committed NCBI lineage rows, ending at `NCBITaxon:2593676`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030533` resolves to label `Streptomyces sp. Wb2n-11`, rank
`SPECIES`, direct parent `NCBITaxon:2593676`, genetic code `11`, source set
`ncbitaxon|gtdb`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`unclassified Streptomyces`. No retained synonym text is present in the NCBI
row, and the generated non-NCBI synonym is attributable to GTDB.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220428` supports the species
identity, direct unclassified-Streptomyces parent, genetic code, source set,
NCBITAXON source attestation, and 2026-09-13 snapshot date. The seed event is
supported by `curation/seed_scope.tsv:66000`.

The GTDB mapping at `data/raw/gtdb_mappings.tsv:1294` supports the retained
`GTDB:s__Streptomyces_altiplanensis` `skos:closeMatch`, 2-genome count, xref,
GTDB source attestation, and `Streptomyces altiplanensis` exact synonym.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, GTDB, seed, and target YAML
inputs, and found no extra GOLD, MADIN, StrainInfo, or ATB row for this
identifier.

The 73-line YAML shape is expected for a generated unclassified-Streptomyces
record with one retained GTDB mapping; no strain, genome assembly, genome
record, or causal graph section is expected.

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

This was a read-only generated-record review.

