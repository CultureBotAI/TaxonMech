# YAML Record Review: Archaeoglobus infectus DSM 18877

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_infectus_dsm_18877.yaml
- Started UTC: 2026-09-27T10:37:30Z
- Finished UTC: 2026-09-27T10:37:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_infectus_dsm_18877.yaml` |
| Identifier | `NCBITaxon:1121009` |
| Label | `Archaeoglobus infectus DSM 18877` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:403219` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon, BacDive, MediaDive, and MADIN-backed strain
record, with path pinned by `data/taxa/PATHS.tsv:36067`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_infectus_dsm_18877.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_infectus_dsm_18877.yaml data/taxa/archaea/archaeoglobus_lithotrophicus.yaml data/taxa/archaea/archaeoglobus_neptunius.yaml data/taxa/archaea/archaeoglobus_profundus.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 168 YAML lines, 10 lineage entries, 4 source attestations, 2 exact NCBI synonyms, 0 taxonomy mappings, 0 xrefs, 1 BacDive strain, 0 assemblies, 0 genome records, and 6 related records. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1121009` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:241983`, 10 checked lineage entries with no mismatches, 1 exact BacDive row, 1 MediaDive row, 1 MADIN row, 0 retained GOLD aggregate rows, 1 native GOLD organism row, no LPSN or GTDB rows, and no target-taxid StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1121009` resolves to label `Archaeoglobus infectus DSM 18877`, rank
`STRAIN`, parent `NCBITaxon:403219`, source set
`ncbitaxon|bacdive|mediadive|madin_etal`, and taxonomy snapshot `2026-09-13`.
The generated record carries those fields.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, ending at species `NCBITaxon:403219` Archaeoglobus infectus.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The raw NCBI row supports the strain identity, direct `A. infectus` parent,
genetic code, and exact synonyms `Archaeoglobus infectus Arc51` and
`Archaeoglobus sp. Arc51`.

BacDive row 18099 supports the single generated strain with Arc 51, DSM 18877,
and NBRC 100649 culture identifiers. Native GOLD row `Go0013397` is side
evidence only because no retained GOLD aggregate row is filed for this target.

MediaDive row 646 supports one medium, MADIN row 3114 supports three trait
assertions, and two normalized GOLD_ORGANISM related rows account for the
generated related-record section. No assembly or genome row is filed here.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, BacDive, native GOLD, MediaDive,
MADIN, path, and YAML inputs, and found no omitted GTDB, LPSN, retained GOLD,
BactoTraits, assembly, genome, or target-taxid StrainInfo row.

An ignored-file-inclusive `find` under `reports/yaml_record_review` returned no
existing Markdown report for this stem before this report was written.

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

This was a read-only generated-record review; it did not append history, promote `mapping_status`, or touch YAML.
`strain_count: 1` matches the BacDive-backed strain block.
No `taxonomy_mappings` section is expected.
No retained GOLD aggregate row is filed on this target.
Native GOLD is retained only as side related-record evidence.
No NCBI type-material row is filed on this strain taxon.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The ignored report probe included gitignored files.
