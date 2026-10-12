# YAML Record Review: Archaeoglobi archaeon JdFR-42

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobi_archaeon_jdfr_42.yaml
- Started UTC: 2026-09-27T10:30:09Z
- Finished UTC: 2026-09-27T10:30:09Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobi_archaeon_jdfr_42.yaml` |
| Identifier | `NCBITaxon:1935016` |
| Label | `Archaeoglobi archaeon JdFR-42` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:1935015` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon and GTDB-backed archaeal species record, with
one generated GTDB closeMatch row and path pinned by
`data/taxa/PATHS.tsv:304843`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobi_archaeon_jdfr_42.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobales_archaeon_enrichment_culture_clone_b11_a_43.yaml data/taxa/archaea/archaeoglobales_archaeon_ex4484_92.yaml data/taxa/archaea/archaeoglobi_archaeon.yaml data/taxa/archaea/archaeoglobi_archaeon_jdfr_42.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 64 YAML lines, 7 lineage entries, 2 source attestations across NCBITAXON and GTDB, 1 GTDB taxonomy mapping, 1 exact GTDB synonym, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1935016` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:496674`, 7 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 1 GTDB mapping row, 0 GOLD aggregate rows, 1 native GOLD organism row, 0 native GOLD project rows, 1 native GOLD analysis row, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1935016` resolves to label `Archaeoglobi archaeon JdFR-42`, rank
`SPECIES`, parent `NCBITaxon:1935015`, source set `ncbitaxon|gtdb`, and
taxonomy snapshot `2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches the committed NCBI rows for all 7 stored
taxa, ending at `NCBITaxon:1935015` unclassified Archaeoglobi.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species identity, parent, genetic code, empty synonym
columns, multi-source attestation set, and 2026-09-13 snapshot date. The seed
event is supported by `curation/seed_scope.tsv:82091`.

The GTDB row at `data/raw/gtdb_mappings.tsv:98719` supports the closeMatch
mapping to `GTDB:s__JdFR-42_sp002010305`, the generated exact synonym, the
GTDB xref, the GTDB source attestation, and its two-genome assertion count.

Native GOLD has one exact organism row and one exact analysis row for this
NCBI taxon, both under organism GOLD id `Go0367295`. They are side evidence
only: no retained GOLD aggregate row or normalized GOLD section is generated.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, seed, path, generated YAML, retained
GTDB, and native GOLD inputs, and found no omitted LPSN, retained GOLD,
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
The GTDB closeMatch mints both the exact synonym and xref.
The native GOLD rows did not produce a GOLD source attestation.
No retained GOLD aggregate row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Seven NCBI lineage rows are expected.
The ignored report probe included gitignored files.
