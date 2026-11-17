# YAML Record Review: Archaeoglobus sulfaticallidus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_sulfaticallidus.yaml
- Started UTC: 2026-09-27T11:12:15Z
- Finished UTC: 2026-09-27T11:12:15Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_sulfaticallidus.yaml` |
| Identifier | `NCBITaxon:1316941` |
| Label | `Archaeoglobus sulfaticallidus` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2233` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated multisource species record for the PM70-1 type-strain
species, with path pinned by `data/taxa/PATHS.tsv:111983`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_sulfaticallidus.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_sp_uba234.yaml data/taxa/archaea/archaeoglobus_sp_uba236.yaml data/taxa/archaea/archaeoglobus_sulfaticallidus.yaml data/taxa/archaea/archaeoglobus_sulfaticallidus_pm70_1.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 285 YAML lines, 9 lineage entries, 6 source attestations across NCBITAXON, LPSN, BACDIVE, MEDIADIVE, GOLD, and MADIN, 1 LPSN nomenclature entry, 1 related NCBI synonym, 1 xref, 1 BacDive strain, 2 genome assemblies, 3 genome records, 9 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1316941` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated YAML rows; also found `NCBITaxon:387631` only in expected PM70-1 child and strain-linked generated rows. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:313610`, 9 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 6 NCBI type-material rows, 1 LPSN row, 1 exact BacDive row, 1 retained GOLD aggregate row, 1 native GOLD organism row, 0 native GOLD project rows, 0 native GOLD analysis rows, 1 MediaDive row, 1 MADIN row, no exact GTDB or BactoTraits row, 2 raw culture-collection rows, 2 normalized GOLD related rows, 1 StrainInfo direct row, 1 StrainInfo deposit, and 2 normalized StrainInfo related rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1316941` resolves to label `Archaeoglobus sulfaticallidus`, rank
`SPECIES`, parent `NCBITaxon:2233`, genetic code `11`, source set
`ncbitaxon|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches all 9 committed NCBI rows, ending at the
`NCBITaxon:2233` Archaeoglobus genus. The bounded scan found no NCBI merge row
and no retained old-id row.

## Evidence

The NCBI row supports the species identity, parent, genetic code, one related
synonym, the six-source attestation set, and the 2026-09-13 snapshot date. The
seed event is supported by `curation/seed_scope.tsv:12105`.

The LPSN row at `data/raw/lpsn_names.tsv:25993` supports `lpsn:788917`,
ICNP-valid status, type strain IDs DSM-19444 and JCM-14716, publications,
sequence accession FJ810190, and the generated LPSN xref.

BacDive exact row `data/raw/bacdive_strains.tsv:17909` supports the PM70-1
strain `kgmicrobe.strain:bacdive_18100`, its DSM-19444 and JCM-14716 culture
collection IDs, and type-strain status. The PM70-1 child evidence contributes 2
genome assemblies, 3 genome records, 5 GOLD related records, and 2 StrainInfo
related records through the same BacDive strain.

The retained aggregate at `data/raw/gold_organism_counts.tsv:7784` supports a
GOLD organism attestation; `Go0608852` is retained as related JCM 14716 strain
evidence under the BacDive type strain. MediaDive row 2957 contributes two
media IDs, and MADIN row 12051 contributes six trait assertions.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, seed, path, LPSN, BacDive, MediaDive,
MADIN, retained GOLD, generated child-strain GOLD, and StrainInfo inputs, and
found no omitted exact GTDB or BactoTraits row.

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
The ignored report probe included gitignored files.
