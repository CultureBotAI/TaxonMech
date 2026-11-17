# YAML Record Review: Lactobacillus sp. AbxANB4

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/lactobacillus_sp_abxanb4.yaml
- Started UTC: 2026-10-03T04:14:00Z
- Finished UTC: 2026-10-03T04:14:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/lactobacillus_sp_abxanb4.yaml` |
| Identifier | `NCBITaxon:1030134` |
| Label | `Lactobacillus sp. AbxANB4` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2620435` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only unclassified-Lactobacillus species
record, with path pinned by `data/taxa/PATHS.tsv:12520`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/lactobacillus_sp_abxanb4.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12518-12527` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 54 YAML lines, 10 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030134` in the expected seed and NCBI rows; found no exact GTDB, GOLD, MADIN, StrainInfo, ATB, legacy-path, or ignored prior report for this stem. |
| First-column lineage scan | Found the 10 expected committed NCBI lineage rows, ending at `NCBITaxon:2620435`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030134` resolves to label `Lactobacillus sp. AbxANB4`, rank
`SPECIES`, direct parent `NCBITaxon:2620435`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`unclassified Lactobacillus`. No retained synonym text is present in the NCBI
row, and the generated YAML correctly omits a `synonyms` section.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220286` supports the species
identity, direct unclassified-Lactobacillus parent, genetic code, empty synonym
columns, single NCBITAXON source attestation, and 2026-09-13 snapshot date.
The seed event is supported by `curation/seed_scope.tsv:320714`.

Exact source scans found no exact GTDB mapping, GOLD organism row, MADIN row,
legacy page path, StrainInfo row, or ATB row for `NCBITaxon:1030134`.

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
The direct parent is `NCBITaxon:2620435`, unclassified Lactobacillus.
No GTDB, GOLD, or MADIN attestation is expected.
No local strain inventory row is filed on this target.
No genome assembly or genome record section is expected.
No causal graph is expected.
The ignored report probe included gitignored files.
