# YAML Record Review: Salmonella enterica subsp. enterica serovar Heidelberg str. 640151-11

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_640151_11.yaml
- Started UTC: 2026-10-03T03:29:00Z
- Finished UTC: 2026-10-03T03:29:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_640151_11.yaml` |
| Identifier | `NCBITaxon:1030003` |
| Label | `Salmonella enterica subsp. enterica serovar Heidelberg str. 640151-11` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:611` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon+GTDB+GOLD Salmonella strain record, with path
pinned by `data/taxa/PATHS.tsv:12428`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_heidelberg_str_640151_11.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `NCBITaxon:1030003` through `NCBITaxon:1030048` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 87 YAML lines, 12 lineage entries, 3 source attestations, 0 nomenclature entries, 1 taxonomy mapping, 2 synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030003` in the expected NCBI, GTDB, GOLD, seed, and legacy-path rows; found no exact MADIN, StrainInfo, ATB, or ignored prior report for this stem. |
| First-column lineage scan | Found the 12 expected committed NCBI lineage rows, ending at `NCBITaxon:611`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030003` resolves to label `Salmonella enterica subsp. enterica
serovar Heidelberg str. 640151-11`, rank `STRAIN`, direct parent
`NCBITaxon:611`, genetic code `11`, source set `ncbitaxon|gtdb|gold`, and
taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`Salmonella enterica subsp. enterica serovar Heidelberg`. The strain-level
NCBI row keeps the expected `Salmonella enterica subsp. enterica serovar
Heidelberg strain 640151-11` exact synonym.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220194` supports the strain
identity, direct Heidelberg parent, genetic code, NCBI synonym, NCBITAXON
attestation, and 2026-09-13 snapshot date. The seed event is supported by
`curation/seed_scope.tsv:36124`, and the legacy path is retained at
`curation/legacy_page_paths.tsv:721`.

The GTDB mapping at `data/raw/gtdb_mappings.tsv:1284` supports the
`GTDB:s__Salmonella_enterica` close match, 21,527-genome GTDB attestation,
GTDB synonym, and xref. The GOLD row at `data/raw/gold_organisms.tsv:390`
supports the third retained source attestation.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, GTDB, GOLD, seed, legacy path,
and target YAML inputs, and found no exact MADIN, BacDive, StrainInfo, ATB, or
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
No MADIN attestation is expected for this target.
No local strain inventory row is filed on this target.
No genome assembly or genome record section is expected.
No causal graph is expected.
The ignored report probe included gitignored files.
