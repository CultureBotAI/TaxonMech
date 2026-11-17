# YAML Record Review: Archaeoglobus sp. NS70-A

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_sp_ns70_a.yaml
- Started UTC: 2026-09-27T11:06:08Z
- Finished UTC: 2026-09-27T11:06:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_sp_ns70_a.yaml` |
| Identifier | `NCBITaxon:269230` |
| Label | `Archaeoglobus sp. NS70-A` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2643606` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only Archaeoglobus species placeholder,
with path pinned by `data/taxa/PATHS.tsv:363953`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_sp_ns70_a.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_sp_jdfr_40.yaml data/taxa/archaea/archaeoglobus_sp_jdfr_41.yaml data/taxa/archaea/archaeoglobus_sp_ni85_a.yaml data/taxa/archaea/archaeoglobus_sp_ns70_a.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 54 YAML lines, 10 lineage entries, 1 NCBITAXON source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:269230` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:55621`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:269230` resolves to label `Archaeoglobus sp. NS70-A`, rank
`SPECIES`, parent `NCBITaxon:2643606`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`. The generated record carries
those fields.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, ending at `NCBITaxon:2643606` unclassified Archaeoglobus.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species-rank placeholder identity, direct
unclassified-Archaeoglobus parent, genetic code, empty synonym columns, single
NCBITAXON source attestation, and 2026-09-13 snapshot date. The seed event is
supported by `curation/seed_scope.tsv:174800`.

No LPSN, GTDB, GOLD aggregate, BacDive, MediaDive, MADIN, BactoTraits, NCBI
type-material, StrainInfo, culture-collection, normalized assembly, normalized
genome, normalized related-record, or native GOLD row is filed under this exact
taxon in the committed source tables.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, seed, path, and generated YAML
inputs, and found no omitted GTDB, LPSN, retained GOLD, native GOLD, BacDive,
MediaDive, MADIN, BactoTraits, type-material, or strain inventory row.

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
`strain_count: 0` is expected without an exact BacDive or normalized strain row.
No `synonyms` section is expected.
No `taxonomy_mappings` section is expected.
No xref section is expected.
No native GOLD rows were present for this target.
No retained GOLD aggregate row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The ignored report probe included gitignored files.
