# YAML Record Review: Archaeoglobus sp. UBA231

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_sp_uba231.yaml
- Started UTC: 2026-09-27T11:09:22Z
- Finished UTC: 2026-09-27T11:09:22Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_sp_uba231.yaml` |
| Identifier | `NCBITaxon:1915566` |
| Label | `Archaeoglobus sp. UBA231` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2643606` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon and GTDB-backed Archaeoglobus species
record, with one generated GTDB closeMatch row and path pinned by
`data/taxa/PATHS.tsv:302169`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_sp_uba231.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_sp_ns_tsrb_2.yaml data/taxa/archaea/archaeoglobus_sp_scgc_ac_335_l13.yaml data/taxa/archaea/archaeoglobus_sp_uba230.yaml data/taxa/archaea/archaeoglobus_sp_uba231.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 73 YAML lines, 10 lineage entries, 2 source attestations across NCBITAXON and GTDB, 1 GTDB taxonomy mapping, 1 exact GTDB synonym, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1915566` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:494225`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 1 GTDB mapping row, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1915566` resolves to label `Archaeoglobus sp. UBA231`, rank
`SPECIES`, parent `NCBITaxon:2643606`, source set `ncbitaxon|gtdb`, and
taxonomy snapshot `2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, ending at `NCBITaxon:2643606` unclassified Archaeoglobus.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species identity, parent, genetic code, empty synonym
columns, multi-source attestation set, and 2026-09-13 snapshot date. The seed
event is supported by `curation/seed_scope.tsv:81156`.

The GTDB row at `data/raw/gtdb_mappings.tsv:95543` supports the closeMatch
mapping to `GTDB:s__Archaeoglobus_sp002507545`, the generated exact synonym,
the GTDB xref, the GTDB source attestation, and its five-genome assertion count.

No GOLD aggregate, native GOLD, LPSN, BacDive, MediaDive, MADIN, BactoTraits,
NCBI type-material, StrainInfo, culture-collection, normalized assembly,
normalized genome, or normalized related-record row is filed for this taxon.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, seed, path, generated YAML, retained
GTDB, and found no omitted LPSN, retained GOLD, native GOLD, BacDive, MediaDive,
MADIN, BactoTraits, type-material, or strain inventory row.

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
The GTDB closeMatch mints both the exact synonym and xref.
No native GOLD rows were present for this target.
No retained GOLD aggregate row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The ignored report probe included gitignored files.
