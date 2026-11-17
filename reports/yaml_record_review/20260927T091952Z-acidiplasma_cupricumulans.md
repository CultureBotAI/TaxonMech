# YAML Record Review: Acidiplasma cupricumulans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidiplasma_cupricumulans.yaml
- Started UTC: 2026-09-27T09:19:52Z
- Finished UTC: 2026-09-27T09:19:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidiplasma_cupricumulans.yaml` |
| Identifier | `NCBITaxon:312540` |
| Label | `Acidiplasma cupricumulans` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:507753` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI species record with LPSN, GTDB, BacDive descendant,
GOLD, MADIN, and StrainInfo strain-side evidence, with path pinned by
`data/taxa/PATHS.tsv:426237`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidiplasma_cupricumulans.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidiplasma_aeolicum.yaml data/taxa/archaea/acidiplasma_cupricumulans.yaml data/taxa/archaea/acidiplasma_cupricumulans_jcm_13668_dsm_16651.yaml data/taxa/archaea/acidiplasma_sp.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 673 YAML lines, 9 lineage entries, 1 LPSN nomenclature entry, 1 GTDB mapping, 2 exact and 3 related synonyms, 2 xrefs, 1 gathered BacDive strain, 12 genome assemblies, 8 genome records, 26 related records, 6 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:312540` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, GTDB, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:63924`, 9 checked lineage rows with no mismatches, 1 LPSN row, 1 GTDB mapping, 1 exact BacDive source record that also names descendant strain `NCBITaxon:1295373`, 1 GOLD aggregate row with 3 organisms, 1 MADIN row with 3 assertions, 3 native GOLD organisms, 2 StrainInfo assemblies, 4 StrainInfo related rows, 6 NCBI type-material rows, and no NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:312540` resolves to label `Acidiplasma cupricumulans`, rank
`SPECIES`, parent `NCBITaxon:507753`, genetic code `11`, source set
`ncbitaxon|gtdb|lpsn|gold|madin_etal`, and taxonomy snapshot `2026-09-13`.
The generated record carries those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through genus `NCBITaxon:507753` Acidiplasma. The
bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The LPSN row `lpsn:788161` supports legitimate, validly published, correct-name
nomenclature for the renamed species, preserves old name `Ferroplasma
cupricumulans`, and lists DSM 16651 and JCM 13668 as type-strain designations.

BacDive row `bacdive:5460` is filed under child strain `NCBITaxon:1295373`;
the parent species intentionally gathers it with `classified_as`. Its BH2
strain block carries BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo
links, including the two StrainInfo genome rows matched by DSM 16651 and JCM
13668 deposits.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, GTDB, BacDive, GOLD, MADIN,
StrainInfo, type-material, native GOLD, seed, path, and YAML inputs, and found
no omitted NCBI merge, MediaDive, or BactoTraits row.

The same BacDive strain is emitted on this species and on child strain record
`NCBITaxon:1295373`; the species copy keeps every descendant-taxonomy boundary
visible through `classified_as` and per-genome `taxon_id` values.

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
`strain_count: 1` matches the single gathered BacDive BH2 strain.
The `GOLD` and `MADIN` source attestations count direct species rows only.
`MEDIADIVE` is absent because its 2-medium row is filed to the child strain.
The retained GTDB closeMatch is the committed kg-microbe mapping.
NCBI type material names DSM 16651, JCM 13668, and BH2 spelling variants.
The generated xrefs are the retained GTDB and LPSN identifiers.
No upstream side row needs staging in kg-microbe or the seeder.
The ignored report probe included gitignored files.
