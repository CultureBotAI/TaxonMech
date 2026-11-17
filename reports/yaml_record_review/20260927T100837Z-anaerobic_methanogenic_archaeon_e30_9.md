# YAML Record Review: anaerobic methanogenic archaeon E30-9

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/anaerobic_methanogenic_archaeon_e30_9.yaml
- Started UTC: 2026-09-27T10:08:37Z
- Finished UTC: 2026-09-27T10:08:37Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/anaerobic_methanogenic_archaeon_e30_9.yaml` |
| Identifier | `NCBITaxon:93535` |
| Label | `anaerobic methanogenic archaeon E30-9` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:93506` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated compact NCBITaxon-only archaeal placeholder species
record, with path pinned by `data/taxa/PATHS.tsv:613444`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/anaerobic_methanogenic_archaeon_e30_9.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/anaerobic_methanogenic_archaeon_e30_9.yaml data/taxa/archaea/anaerobic_methanogenic_archaeon_et1_1.yaml data/taxa/archaea/anaerobic_methanogenic_archaeon_et1_10.yaml data/taxa/archaea/anaerobic_methanogenic_archaeon_et1_2.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 36 YAML lines, 4 lineage entries, 1 NCBITAXON source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:93535` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:15358`, 4 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:93535` resolves to label `anaerobic methanogenic archaeon E30-9`,
rank `SPECIES`, parent `NCBITaxon:93506`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`. The generated record carries
those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 4 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:93506` unclassified Archaea.
The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species-rank placeholder identity, direct
unclassified-Archaea parent, genetic code, empty synonym columns, single
NCBITAXON source attestation, and 2026-09-13 snapshot date. The seed event is
supported by `curation/seed_scope.tsv:141502`.

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
No generated synonym section is expected.
No native GOLD rows were present for this target.
No retained GOLD aggregate row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
The ignored report probe included gitignored files.
