# YAML Record Review: anaerobic hyperthermophile Gorda1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/anaerobic_hyperthermophile_gorda1.yaml
- Started UTC: 2026-09-27T09:45:26Z
- Finished UTC: 2026-09-27T09:45:26Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/anaerobic_hyperthermophile_gorda1.yaml` |
| Identifier | `NCBITaxon:81399` |
| Label | `anaerobic hyperthermophile Gorda1` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:114579` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only archaeal species record, with path
pinned by `data/taxa/PATHS.tsv:592918` and one NCBI exact synonym.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/anaerobic_hyperthermophile_gorda1.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/anaerobic_hyperthermophile_gorda1.yaml data/taxa/archaea/anaerobic_methanogenic_archaeon_e15_1.yaml data/taxa/archaea/anaerobic_methanogenic_archaeon_e15_10.yaml data/taxa/archaea/anaerobic_methanogenic_archaeon_e15_2.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 52 YAML lines, 8 lineage entries, 1 exact NCBI synonym, 1 NCBITAXON source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:81399` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:12206`, 8 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:81399` resolves to label `anaerobic hyperthermophile Gorda1`, rank
`SPECIES`, parent `NCBITaxon:114579`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`. The generated record carries
those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 8 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:114579` unclassified
Thermococcales. The bounded scan found no NCBI merge row and no retained
old-id row.

## Evidence

The NCBI row supports exact synonym `anaerobic hyperthermophile GR1`, the
single NCBITAXON source attestation, and the 2026-09-13 snapshot date. The
seed event is supported by `curation/seed_scope.tsv:139269`.

No LPSN, GTDB, GOLD aggregate, BacDive, MediaDive, MADIN, BactoTraits, NCBI
type-material, StrainInfo, culture-collection, normalized assembly, normalized
genome, normalized related-record, or native GOLD row is filed under this exact
taxon in the committed source tables.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, seed, path, synonym, and generated
YAML inputs, and found no omitted GTDB, LPSN, retained GOLD, native GOLD,
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
No `taxonomy_mappings` section is expected.
No xref section is expected.
No LPSN nomenclature section is expected.
No native GOLD rows were present for this target.
No retained GOLD aggregate row is filed on this target.
No generated related-record section is expected.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
The ignored report probe included gitignored files.
