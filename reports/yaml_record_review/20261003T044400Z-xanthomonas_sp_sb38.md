# YAML Record Review: Xanthomonas sp. SB38

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/xanthomonas_sp_sb38.yaml
- Started UTC: 2026-10-03T04:44:00Z
- Finished UTC: 2026-10-03T04:44:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/xanthomonas_sp_sb38.yaml` |
| Identifier | `NCBITaxon:1030269` |
| Label | `Xanthomonas sp. SB38` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2643310` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only unclassified-Xanthomonas species record,
with path pinned by `data/taxa/PATHS.tsv:12586`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/xanthomonas_sp_sb38.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12578-12587` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 53 YAML lines, 10 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030269` in the expected seed and NCBI rows; found no exact GTDB, GOLD, MADIN, StrainInfo, ATB, legacy-path, or ignored prior report for this stem. |
| First-column lineage scan | Found the 10 expected committed NCBI lineage rows, ending at `NCBITaxon:2643310`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030269` resolves to label `Xanthomonas sp. SB38`, rank `SPECIES`,
direct parent `NCBITaxon:2643310`, genetic code `11`, source set `ncbitaxon`,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`unclassified Xanthomonas`. No retained synonym text is present in the NCBI
row, and the generated YAML correctly omits a `synonyms` section.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220352` supports the species
identity, direct unclassified-Xanthomonas parent, genetic code, empty synonym
columns, single NCBITAXON source attestation, and 2026-09-13 snapshot date.
The seed event is supported by `curation/seed_scope.tsv:320778`.

Exact source scans found no exact GTDB mapping, GOLD organism row, MADIN row,
legacy page path, StrainInfo row, or ATB row for `NCBITaxon:1030269`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, seed, and target YAML inputs, and
found no extra retained source rows or strain evidence for this identifier.

The 53-line YAML shape is expected for this genus-level placeholder lineage; no
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
The direct parent is `NCBITaxon:2643310`, unclassified Xanthomonas.
