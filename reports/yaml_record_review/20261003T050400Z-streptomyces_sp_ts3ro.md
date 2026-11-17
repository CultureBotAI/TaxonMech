# YAML Record Review: Streptomyces sp. TS3RO

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/streptomyces_sp_ts3ro.yaml
- Started UTC: 2026-10-03T05:04:00Z
- Finished UTC: 2026-10-03T05:04:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/streptomyces_sp_ts3ro.yaml` |
| Identifier | `NCBITaxon:1030490` |
| Label | `Streptomyces sp. TS3RO` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2593676` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only unclassified-Streptomyces species
record, with path pinned by `data/taxa/PATHS.tsv:12619`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/streptomyces_sp_ts3ro.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12618-12627` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 54 YAML lines, 10 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030490` in the expected seed and NCBI rows; found no exact GTDB, GOLD, MADIN, StrainInfo, ATB, legacy-path, or ignored prior report for this stem. |
| First-column lineage scan | Found the 10 expected committed NCBI lineage rows, ending at `NCBITaxon:2593676`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030490` resolves to label `Streptomyces sp. TS3RO`, rank
`SPECIES`, direct parent `NCBITaxon:2593676`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`unclassified Streptomyces`. No retained synonym text is present in the NCBI
row, and the generated YAML correctly omits a `synonyms` section.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220385` supports the species
identity, direct unclassified-Streptomyces parent, genetic code, empty synonym
columns, single NCBITAXON source attestation, and 2026-09-13 snapshot date.
The seed event is supported by `curation/seed_scope.tsv:320810`.

Exact source scans found no exact GTDB mapping, GOLD organism row, MADIN row,
legacy page path, StrainInfo row, or ATB row for `NCBITaxon:1030490`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, seed, and target YAML inputs, and
found no extra retained source rows or strain evidence for this identifier.

The 54-line YAML shape is expected for this genus-level placeholder lineage; no
`taxonomy_mappings`, `synonyms`, xref, strain, genome, or causal graph section
is expected.

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
The direct parent is `NCBITaxon:2593676`, unclassified Streptomyces.
