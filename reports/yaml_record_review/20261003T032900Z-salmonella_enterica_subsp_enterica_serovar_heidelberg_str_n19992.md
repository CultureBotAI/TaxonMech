# YAML Record Review: Salmonella enterica subsp. enterica serovar Heidelberg str. N19992

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_n19992.yaml
- Started UTC: 2026-10-03T03:29:00Z
- Finished UTC: 2026-10-03T03:29:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_n19992.yaml` |
| Identifier | `NCBITaxon:1030006` |
| Label | `Salmonella enterica subsp. enterica serovar Heidelberg str. N19992` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:611` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon+GTDB+GOLD+MADIN Salmonella strain record,
with path pinned by `data/taxa/PATHS.tsv:12431`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_n19992.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `NCBITaxon:1030003` through `NCBITaxon:1030048` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 92 YAML lines, 12 lineage entries, 4 source attestations, 0 nomenclature entries, 1 taxonomy mapping, 2 synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030006` in the expected NCBI, GTDB, GOLD, MADIN, seed, and legacy-path rows; found no exact StrainInfo, ATB, or ignored prior report for this stem. |
| First-column lineage scan | Found the 12 expected committed NCBI lineage rows, ending at `NCBITaxon:611`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030006` resolves to label `Salmonella enterica subsp. enterica
serovar Heidelberg str. N19992`, rank `STRAIN`, direct parent `NCBITaxon:611`,
genetic code `11`, source set `ncbitaxon|gtdb|gold|madin_etal`, and taxonomy
snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`Salmonella enterica subsp. enterica serovar Heidelberg`. The strain-level
NCBI row keeps the expected `Salmonella enterica subsp. enterica serovar
Heidelberg strain N19992` exact synonym.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220197` supports the strain
identity, direct Heidelberg parent, genetic code, NCBI synonym, NCBITAXON
attestation, and 2026-09-13 snapshot date. The seed event is supported by
`curation/seed_scope.tsv:26070`, and the legacy path is retained at
`curation/legacy_page_paths.tsv:724`.

The GTDB mapping at `data/raw/gtdb_mappings.tsv:1287` supports the
`GTDB:s__Salmonella_enterica` close match, 21,527-genome GTDB attestation,
GTDB synonym, and xref. `data/raw/gold_organisms.tsv:393` supports the GOLD
attestation, and `data/raw/madin_taxa.tsv:565` supports the MADIN attestation
with 1 trait assertion.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, GTDB, GOLD, MADIN, seed, legacy
path, and target YAML inputs, and found no exact BacDive, StrainInfo, ATB, or
NCBI type-material row for this identifier.

`strain_count: 0` is expected here because there is no exact normalized strain
or BacDive row; the GTDB species-level mapping is represented by one mapping,
one GTDB synonym, and one xref.

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
The GTDB mapping intentionally lands at species level, not at the Heidelberg
serovar node.
The single MADIN row is represented as 1 trait assertion.
No local strain inventory row is filed on this target.
No genome assembly or genome record section is expected.
No causal graph is expected.
The ignored report probe included gitignored files.
