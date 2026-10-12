# YAML Record Review: Chryseobacterium sp. MWE-A31

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/chryseobacterium_sp_mwe_a31.yaml
- Started UTC: 2026-10-03T04:49:00Z
- Finished UTC: 2026-10-03T04:49:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/chryseobacterium_sp_mwe_a31.yaml` |
| Identifier | `NCBITaxon:1030310` |
| Label | `Chryseobacterium sp. MWE-A31` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2593645` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only unclassified-Chryseobacterium species
record, with path pinned by `data/taxa/PATHS.tsv:12596`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/chryseobacterium_sp_mwe_a31.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12588-12597` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 63 YAML lines, 13 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030310` in the expected seed and NCBI rows; found no exact GTDB, GOLD, MADIN, StrainInfo, ATB, legacy-path, or ignored prior report for this stem. |
| First-column lineage scan | Found the 13 expected committed NCBI lineage rows, ending at `NCBITaxon:2593645`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030310` resolves to label `Chryseobacterium sp. MWE-A31`, rank
`SPECIES`, direct parent `NCBITaxon:2593645`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`unclassified Chryseobacterium`. No retained synonym text is present in the
NCBI row, and the generated YAML correctly omits a `synonyms` section.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220363` supports the species
identity, direct unclassified-Chryseobacterium parent, genetic code, empty
synonym columns, single NCBITAXON source attestation, and 2026-09-13 snapshot
date. The seed event is supported by `curation/seed_scope.tsv:320788`.

Exact source scans found no exact GTDB mapping, GOLD organism row, MADIN row,
legacy page path, StrainInfo row, or ATB row for `NCBITaxon:1030310`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, seed, and target YAML inputs, and
found no extra retained source rows or strain evidence for this identifier.

The 63-line YAML shape is expected for this placeholder lineage with FCB group,
Bacteroidota/Chlorobiota group, and Chryseobacterium group ancestors; no
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
The direct parent is `NCBITaxon:2593645`, unclassified Chryseobacterium.
