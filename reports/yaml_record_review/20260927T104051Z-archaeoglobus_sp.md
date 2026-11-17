# YAML Record Review: Archaeoglobus sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_sp.yaml
- Started UTC: 2026-09-27T10:40:51Z
- Finished UTC: 2026-09-27T10:40:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_sp.yaml` |
| Identifier | `NCBITaxon:1872626` |
| Label | `Archaeoglobus sp.` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2643606` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon and GTDB-backed unclassified-Archaeoglobus
species record, with six generated broadMatch rows and path pinned by
`data/taxa/PATHS.tsv:296818`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_sp.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_profundus_dsm_5631.yaml data/taxa/archaea/archaeoglobus_sp.yaml data/taxa/archaea/archaeoglobus_sp_arc22.yaml data/taxa/archaea/archaeoglobus_sp_enrichment_culture.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 104 YAML lines, 10 lineage entries, 2 source attestations across NCBITAXON and GTDB, 6 GTDB taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1872626` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:489383`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 6 GTDB mapping rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1872626` resolves to label `Archaeoglobus sp.`, rank `SPECIES`,
parent `NCBITaxon:2643606`, source set `ncbitaxon|gtdb`, and taxonomy snapshot
`2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, ending at `NCBITaxon:2643606` unclassified Archaeoglobus.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the generic species identity, direct unclassified
Archaeoglobus parent, genetic code, empty synonym columns, multi-source
attestation set, and 2026-09-13 snapshot date.

Six GTDB rows at `data/raw/gtdb_mappings.tsv:72201` through 72206 account for
all generated broadMatch mappings and pooled genome counts.
They range from 1 to 6 genomes per GTDB species.

No LPSN, GOLD aggregate, BacDive, MediaDive, MADIN, BactoTraits, NCBI
type-material, StrainInfo, culture-collection, normalized assembly, normalized
genome, normalized related-record, or native GOLD row is filed under this exact
taxon in the committed source tables.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, seed, path, generated YAML, and
retained GTDB inputs, and found no omitted LPSN, retained GOLD, native GOLD,
BacDive, MediaDive, MADIN, BactoTraits, type-material, or strain inventory row.

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
The six GTDB mappings are broadMatch evidence.
No retained GOLD aggregate row is filed on this target.
No native GOLD rows were present for this target.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The ignored report probe included gitignored files.
