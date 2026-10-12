# YAML Record Review: Archaeoglobales archaeon

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobales_archaeon.yaml
- Started UTC: 2026-09-27T10:26:15Z
- Finished UTC: 2026-09-27T10:26:15Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobales_archaeon.yaml` |
| Identifier | `NCBITaxon:2250258` |
| Label | `Archaeoglobales archaeon` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:113652` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon, GTDB, and GOLD-backed archaeal species
record, with nine generated GTDB broadMatch rows and path pinned by
`data/taxa/PATHS.tsv:334735`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobales_archaeon.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobaceae_archaeon_ef444597.yaml data/taxa/archaea/archaeoglobaceae_archaeon_enrichment_culture.yaml data/taxa/archaea/archaeoglobaceae_archaeon_sr50.yaml data/taxa/archaea/archaeoglobales_archaeon.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 124 YAML lines, 8 lineage entries, 3 source attestations across NCBITAXON, GTDB, and GOLD, 9 GTDB taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:2250258` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:522189`, 8 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 9 GTDB mapping rows, 1 GOLD aggregate row, 6 native GOLD organism rows, 0 native GOLD project rows, 6 native GOLD analysis rows, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:2250258` resolves to label `Archaeoglobales archaeon`, rank
`SPECIES`, parent `NCBITaxon:113652`, source set `ncbitaxon|gtdb|gold`, and
taxonomy snapshot `2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches the committed NCBI rows for all 8 stored
taxa, ending at `NCBITaxon:113652` unclassified Archaeoglobales.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species identity, parent, genetic code, empty synonym
columns, multi-source attestation set, and 2026-09-13 snapshot date. The seed
event is supported by `curation/seed_scope.tsv:62504`.

Nine GTDB rows at `data/raw/gtdb_mappings.tsv:178153` through 178161 account
for all generated broadMatch mappings and pooled genome counts.
They range from 1 to 4 genomes per GTDB species.

The retained GOLD aggregate row at `data/raw/gold_organism_counts.tsv:21210`
supports the GOLD source attestation with six organisms. Six native GOLD
organism rows and six native GOLD analysis rows are side evidence only because
no normalized native GOLD section is generated for this record.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, seed, path, generated YAML, retained
GTDB, retained GOLD, and native GOLD inputs, and found no omitted LPSN,
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
No `synonyms` section is expected.
The nine GTDB mappings are broadMatch evidence.
The retained GOLD aggregate has organism_count 6.
Six native GOLD organism rows were present for this target.
No NCBI type-material row is available to mint side-only strain evidence.
The ignored report probe included gitignored files.
