# YAML Record Review: Paenibacillus sp. Mc5Re-14

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/paenibacillus_sp_mc5re_14.yaml
- Started UTC: 2026-10-03T05:24:00Z
- Finished UTC: 2026-10-03T05:24:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/paenibacillus_sp_mc5re_14.yaml` |
| Identifier | `NCBITaxon:1030529` |
| Label | `Paenibacillus sp. Mc5Re-14` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:185978` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon species record with retained GTDB and GOLD
attestations, with path pinned by `data/taxa/PATHS.tsv:12658`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/paenibacillus_sp_mc5re_14.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12658-12667` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 78 YAML lines, 10 lineage entries, 3 source attestations, 1 taxonomy mapping, 1 GTDB synonym, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030529` in the expected seed, NCBI, GTDB, GOLD, and legacy-path rows; found no exact MADIN, StrainInfo, or ATB row for this identifier. |
| Exact prior-report probe | Found no `*-paenibacillus_sp_mc5re_14.md` report under `reports/yaml_record_review`, with ignored files included. |
| First-column lineage scan | Found all expected committed NCBI lineage rows, ending at `NCBITaxon:185978`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030529` resolves to label `Paenibacillus sp. Mc5Re-14`, rank
`SPECIES`, direct parent `NCBITaxon:185978`, genetic code `11`, source set
`ncbitaxon|gtdb|gold`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`unclassified Paenibacillus`. No retained synonym text is present in the NCBI
row, and the generated non-NCBI synonym is attributable to GTDB.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220424` supports the species
identity, direct unclassified-Paenibacillus parent, genetic code, source set,
NCBITAXON source attestation, and 2026-09-13 snapshot date. The seed event is
supported by `curation/seed_scope.tsv:36129`, and the legacy page path is
present at `curation/legacy_page_paths.tsv:729`.

The GTDB mapping at `data/raw/gtdb_mappings.tsv:1293` supports the retained
`GTDB:s__Paenibacillus_polymyxa_C` `skos:closeMatch`, 23-genome count, xref,
GTDB source attestation, and `Paenibacillus polymyxa C` exact synonym. The GOLD
organism row at `data/raw/gold_organisms.tsv:396` supports the GOLD organism
attestation.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, GTDB, GOLD, seed, and target YAML
inputs, and found no extra MADIN, StrainInfo, or ATB row for this identifier.

The 78-line YAML shape is expected for a generated unclassified-Paenibacillus
record with one retained GTDB mapping plus one GOLD organism attestation; no
strain, genome assembly, genome record, or causal graph section is expected.

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

