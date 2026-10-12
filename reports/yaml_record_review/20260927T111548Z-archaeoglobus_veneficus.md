# YAML Record Review: Archaeoglobus veneficus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_veneficus.yaml
- Started UTC: 2026-09-27T11:15:48Z
- Finished UTC: 2026-09-27T11:15:48Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_veneficus.yaml` |
| Identifier | `NCBITaxon:58290` |
| Label | `Archaeoglobus veneficus` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2233` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated multisource species record for the DSM 11195 / SNP6
type-strain species, with path pinned by `data/taxa/PATHS.tsv:547192`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_veneficus.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_veneficus.yaml data/taxa/archaea/archaeoglobus_veneficus_snp6.yaml data/taxa/archaea/archaeon.yaml data/taxa/archaea/archaeon_13_1_20cm_2_51_10.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 441 YAML lines, 9 lineage entries, 4 source attestations across NCBITAXON, LPSN, BACDIVE, and MADIN, 1 LPSN nomenclature entry, 1 related NCBI synonym, 1 xref, 1 BacDive strain, 3 genome assemblies, 4 genome records, 17 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:58290` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, generated target YAML, and SNP6 child YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:7401`, 9 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 4 NCBI type-material rows, 1 LPSN row, 1 exact BacDive row, 1 MADIN row, 0 retained GOLD aggregate rows, no native GOLD, GTDB, MediaDive, or BactoTraits rows, 1 StrainInfo direct row, 1 StrainInfo deposit, and 7 normalized StrainInfo related rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:58290` resolves to label `Archaeoglobus veneficus`, rank `SPECIES`,
parent `NCBITaxon:2233`, genetic code `11`, source set
`ncbitaxon|lpsn|madin_etal`, and taxonomy snapshot `2026-09-13`. The generated
record carries those fields and adds BacDive child-strain evidence.

The lineage is root-first and matches all 9 committed NCBI rows, ending at the
`NCBITaxon:2233` Archaeoglobus genus. The bounded scan found no NCBI merge row
and no retained old-id row.

## Evidence

The NCBI row supports the species identity, parent, genetic code, one related
synonym, the three-source NCBI attestation set, and the 2026-09-13 snapshot
date. The seed event is supported by `curation/seed_scope.tsv:31526`.

The LPSN row at `data/raw/lpsn_names.tsv:15383` supports `lpsn:773362`,
ICNP-valid status, type strain ID DSM-11195, two publications, INSDC:Y10011,
and the generated LPSN xref.

BacDive exact row `data/raw/bacdive_strains.tsv:17906` supports bacdive:18098
as species and SNP6 strain evidence. The SNP6 child evidence contributes the
generated BacDive strain, DSM-11195 culture ID, 3 assemblies, 4 genome records,
and 17 related records through the same strain.

MADIN row 27438 contributes five trait assertions. StrainInfo line 36914 and
related rows 186712-186718 support the same DSM 11195 deposit. No exact GTDB,
GOLD aggregate, native GOLD, MediaDive, or BactoTraits row is filed here.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, seed, path, LPSN, BacDive, MADIN,
type-material, child-strain, and StrainInfo inputs, and found no omitted exact
GTDB, retained GOLD, native GOLD, MediaDive, or BactoTraits row.

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
The retained SNP6 strain is side evidence on the species and the next reviewed target.
No exact GTDB row is filed on the species-level NCBI taxon.
The ignored report probe included gitignored files.
