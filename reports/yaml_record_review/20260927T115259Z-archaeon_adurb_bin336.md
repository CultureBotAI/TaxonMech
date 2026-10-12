# YAML Record Review: archaeon ADurb.Bin336

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeon_adurb_bin336.yaml
- Started UTC: 2026-09-27T11:52:59Z
- Finished UTC: 2026-09-27T11:52:59Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeon_adurb_bin336.yaml` |
| Identifier | `NCBITaxon:1866922` |
| Label | `archaeon ADurb.Bin336` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:93506` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon plus GTDB unclassified Archaea
species placeholder, with path pinned by `data/taxa/PATHS.tsv:295113`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeon_adurb_bin336.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeon_a_20.yaml data/taxa/archaea/archaeon_adurb_bin336.yaml data/taxa/archaea/archaeon_ah_315_m20.yaml data/taxa/archaea/archaeon_alkanoarchaeia_wyz_lmo23.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 55 YAML lines, 4 lineage entries, 2 source attestations, 0 nomenclature entries, 1 taxonomy mapping, 1 synonym, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1866922` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, the exact GTDB mapping row, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:487794`, the GTDB mapping row at `data/raw/gtdb_mappings.tsv:64425`, 4 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1866922` resolves to label `archaeon ADurb.Bin336`, rank `SPECIES`,
parent `NCBITaxon:93506`, genetic code `11`, source set `ncbitaxon|gtdb`, and
taxonomy snapshot `2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches all 4 committed NCBI rows, ending at
`NCBITaxon:93506` unclassified Archaea. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

The NCBI row supports the species-rank placeholder identity, direct
unclassified-Archaea parent, genetic code, empty synonym columns, NCBITAXON
source attestation, and 2026-09-13 snapshot date. The seed event is supported
by `curation/seed_scope.tsv:79999`.

The GTDB row supports `GTDB:s__JAAZKV01_sp002068885`, label
`s__JAAZKV01_sp002068885`, parent `GTDB:g__JAAZKV01`, `skos:closeMatch`,
three genomes, the exact GTDB synonym, xref, and GTDB source attestation.

No LPSN, GOLD aggregate, BacDive, MediaDive, MADIN, BactoTraits, NCBI
type-material, StrainInfo, culture-collection, normalized assembly, normalized
genome, normalized related-record, or native GOLD row is filed under this exact
taxon in the committed source tables.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, seed, path, and generated YAML
inputs, and found no omitted LPSN, retained GOLD, native GOLD, BacDive,
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
The GTDB `skos:closeMatch` mapping is seeded as side evidence only.
No `nomenclature` section is expected.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Four NCBI lineage rows are expected.
The ignored report probe included gitignored files.
