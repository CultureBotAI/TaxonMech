# YAML Record Review: Acidiplasma aeolicum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidiplasma_aeolicum.yaml
- Started UTC: 2026-09-27T09:19:52Z
- Finished UTC: 2026-09-27T09:19:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidiplasma_aeolicum.yaml` |
| Identifier | `NCBITaxon:507754` |
| Label | `Acidiplasma aeolicum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:507753` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI species record with LPSN, GTDB, BacDive, MediaDive,
GOLD, MADIN, and StrainInfo strain-side evidence, with path pinned by
`data/taxa/PATHS.tsv:523646`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidiplasma_aeolicum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidiplasma_aeolicum.yaml data/taxa/archaea/acidiplasma_cupricumulans.yaml data/taxa/archaea/acidiplasma_cupricumulans_jcm_13668_dsm_16651.yaml data/taxa/archaea/acidiplasma_sp.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 354 YAML lines, 9 lineage entries, 1 LPSN nomenclature entry, 1 GTDB mapping, 1 related NCBI synonym, 2 xrefs, 1 BacDive strain, 3 genome assemblies, 4 genome records, 12 related records, 7 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:507754` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, GTDB, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:115397`, 9 checked lineage rows with no mismatches, 1 LPSN row, 1 GTDB mapping, 1 exact BacDive row, 1 GOLD aggregate row with 4 organisms, 1 MediaDive row with 2 media, 1 MADIN row with 3 assertions, 3 native GOLD organisms, 1 StrainInfo direct row, 3 StrainInfo related rows, 6 NCBI type-material rows, and no NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:507754` resolves to label `Acidiplasma aeolicum`, rank `SPECIES`,
parent `NCBITaxon:507753`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through genus `NCBITaxon:507753` Acidiplasma. The
bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The LPSN row `lpsn:772583` supports legitimate, validly published, correct-name
nomenclature; DSM 18409 and JCM 14615 type-strain designations; the AM943980
sequence accession; and its direct link to `GTDB:s__Acidiplasma_aeolicum`.

BacDive exact row `bacdive:5459` supplies strain V with deposits DSM 18409 and
JCM 14615. The generated strain is a type strain and carries BacDive, GOLD,
BV-BRC, and StrainInfo links: 3 genome assemblies, 4 genome records, and 12
related records anchored to the retained raw strain rows.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, GTDB, BacDive, MediaDive,
GOLD, MADIN, StrainInfo, type-material, native GOLD, seed, path, and YAML
inputs, and found no omitted NCBI merge or BactoTraits row.

The retained GOLD aggregate supplies 4 organism assertions. The current native
GOLD catalogs expose 3 exact organisms, 2 projects, and 2 analyses as side
evidence; the generated strain links only the supported DSM 18409 chain.

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
`strain_count: 1` matches the single BacDive-derived V strain.
The generated xrefs are the expected LPSN and GTDB identifiers.
The GOLD workbook has an extra JCM 14615 organism side row without a genome link.
The StrainInfo rows add DSM 18409 strain, deposit, and AM943980 sequence refs.
NCBI also retains type-material spelling variants for V, DSM 18409, and JCM 14615.
The `MEDIADIVE` row contributes 2 media to the exact species taxon.
The GOLD source attestation intentionally follows `data/raw/gold_organisms.tsv`.
No upstream side row needs staging in kg-microbe or the seeder.
The ignored report probe included gitignored files.
