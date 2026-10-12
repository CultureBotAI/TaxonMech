# YAML Record Review: Listeria monocytogenes M7

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/listeria_monocytogenes_m7.yaml
- Started UTC: 2026-10-03T03:29:00Z
- Finished UTC: 2026-10-03T03:29:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/listeria_monocytogenes_m7.yaml` |
| Identifier | `NCBITaxon:1030009` |
| Label | `Listeria monocytogenes M7` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1639` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon+GTDB+GOLD+MADIN Listeria strain record,
with path pinned by `data/taxa/PATHS.tsv:12433`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/listeria_monocytogenes_m7.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `NCBITaxon:1030003` through `NCBITaxon:1030048` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 89 YAML lines, 10 lineage entries, 4 source attestations, 0 nomenclature entries, 1 taxonomy mapping, 3 synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030009` in the expected NCBI, GTDB, GOLD, MADIN, seed, and legacy-path rows; found no exact StrainInfo, ATB, or ignored prior report for this stem. |
| First-column lineage scan | Found the 10 expected committed NCBI lineage rows, ending at `NCBITaxon:1639`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030009` resolves to label `Listeria monocytogenes M7`, rank
`STRAIN`, direct parent `NCBITaxon:1639`, genetic code `11`, source set
`ncbitaxon|gtdb|gold|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`Listeria monocytogenes`. The strain-level NCBI row keeps the expected
`Listeria monocytogenes str. M7` and `Listeria monocytogenes strain M7` exact
synonyms.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220199` supports the strain
identity, direct species parent, genetic code, NCBI synonyms, NCBITAXON
attestation, and 2026-09-13 snapshot date. The seed event is supported by
`curation/seed_scope.tsv:26072`, and the legacy path is retained at
`curation/legacy_page_paths.tsv:726`.

The GTDB mapping at `data/raw/gtdb_mappings.tsv:1289` supports the
`GTDB:s__Listeria_monocytogenes_D` close match, 220-genome GTDB attestation,
`Listeria monocytogenes D` synonym, and xref. `data/raw/gold_organisms.tsv:395`
supports the GOLD attestation, and `data/raw/madin_taxa.tsv:567` supports the
MADIN attestation with 5 trait assertions.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, GTDB, GOLD, MADIN, seed, legacy
path, and target YAML inputs, and found no exact BacDive, StrainInfo, ATB, or
NCBI type-material row for this identifier.

`strain_count: 0` is expected here because there is no exact normalized strain
or BacDive row; the GTDB mapping is represented by one mapping, one GTDB
synonym, and one xref.

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
The GTDB split-species mapping to `s__Listeria_monocytogenes_D` is retained as
a close match.
The MADIN source contributes 5 trait assertions.
No local strain inventory row is filed on this target.
No genome assembly or genome record section is expected.
No causal graph is expected.
The ignored report probe included gitignored files.
