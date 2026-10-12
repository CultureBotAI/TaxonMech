# YAML Record Review: Archaeoglobi archaeon

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobi_archaeon.yaml
- Started UTC: 2026-09-27T10:30:09Z
- Finished UTC: 2026-09-27T10:30:09Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobi_archaeon.yaml` |
| Identifier | `NCBITaxon:2250530` |
| Label | `Archaeoglobi archaeon` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:1935015` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon and GTDB-backed archaeal species record, with
nine generated GTDB broadMatch rows and path pinned by
`data/taxa/PATHS.tsv:334819`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobi_archaeon.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobales_archaeon_enrichment_culture_clone_b11_a_43.yaml data/taxa/archaea/archaeoglobales_archaeon_ex4484_92.yaml data/taxa/archaea/archaeoglobi_archaeon.yaml data/taxa/archaea/archaeoglobi_archaeon_jdfr_42.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 116 YAML lines, 7 lineage entries, 2 source attestations across NCBITAXON and GTDB, 9 GTDB taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:2250530` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:522268`, 7 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 9 GTDB mapping rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:2250530` resolves to label `Archaeoglobi archaeon`, rank `SPECIES`,
parent `NCBITaxon:1935015`, source set `ncbitaxon|gtdb`, and taxonomy snapshot
`2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches the committed NCBI rows for all 7 stored
taxa, ending at `NCBITaxon:1935015` unclassified Archaeoglobi.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species identity, parent, genetic code, empty synonym
columns, multi-source attestation set, and 2026-09-13 snapshot date. The seed
event is supported by `curation/seed_scope.tsv:93317`.

Nine GTDB rows at `data/raw/gtdb_mappings.tsv:178627` through 178635 account
for all generated broadMatch mappings and pooled genome counts.
They range from 1 to 4 genomes per GTDB species.

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
The nine GTDB mappings are broadMatch evidence.
No retained GOLD aggregate row is filed on this target.
No native GOLD rows were present for this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
The ignored report probe included gitignored files.
