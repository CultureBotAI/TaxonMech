# YAML Record Review: Bacteroides sp. dnLKV3

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/bacteroides_sp_dnlkv3.yaml
- Started UTC: 2026-10-03T04:09:00Z
- Finished UTC: 2026-10-03T04:09:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/bacteroides_sp_dnlkv3.yaml` |
| Identifier | `NCBITaxon:1030128` |
| Label | `Bacteroides sp. dnLKV3` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2646097` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only unclassified-Bacteroides species record,
with path pinned by `data/taxa/PATHS.tsv:12514`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/bacteroides_sp_dnlkv3.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12508-12517` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 60 YAML lines, 12 lineage entries, 1 source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030128` in the expected seed and NCBI rows; found no exact GTDB, GOLD, MADIN, StrainInfo, ATB, legacy-path, or ignored prior report for this stem. |
| First-column lineage scan | Found the 12 expected committed NCBI lineage rows, ending at `NCBITaxon:2646097`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030128` resolves to label `Bacteroides sp. dnLKV3`, rank
`SPECIES`, direct parent `NCBITaxon:2646097`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`unclassified Bacteroides`. No retained synonym text is present in the NCBI row,
and the generated YAML correctly omits a `synonyms` section.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220280` supports the species
identity, direct unclassified-Bacteroides parent, genetic code, empty synonym
columns, single NCBITAXON source attestation, and 2026-09-13 snapshot date.
The seed event is supported by `curation/seed_scope.tsv:320708`.

Exact source scans found no exact GTDB mapping, GOLD organism row, MADIN row,
legacy page path, StrainInfo row, or ATB row for `NCBITaxon:1030128`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, seed, and target YAML inputs, and
found no extra retained source rows or strain evidence for this identifier.

The 60-line YAML shape is expected for this Bacteroides placeholder lineage; no
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
The direct parent is `NCBITaxon:2646097`, unclassified Bacteroides.
No GTDB, GOLD, or MADIN attestation is expected.
No local strain inventory row is filed on this target.
No genome assembly or genome record section is expected.
No causal graph is expected.
The ignored report probe included gitignored files.
