# YAML Record Review: Aeropyrum pernix

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/aeropyrum_pernix.yaml
- Started UTC: 2026-09-27T09:27:45Z
- Finished UTC: 2026-09-27T09:27:45Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/aeropyrum_pernix.yaml` |
| Identifier | `NCBITaxon:56636` |
| Label | `Aeropyrum pernix` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:56635` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI species record with LPSN, GTDB, BacDive, MediaDive,
GOLD, MADIN, and StrainInfo strain-side evidence, with path pinned by
`data/taxa/PATHS.tsv:542412`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/aeropyrum_pernix.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/aeropyrum_camini.yaml data/taxa/archaea/aeropyrum_camini_sy1_jcm_12091.yaml data/taxa/archaea/aeropyrum_pernix.yaml data/taxa/archaea/aeropyrum_pernix_k1.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 569 YAML lines, 9 lineage entries, 1 LPSN nomenclature entry, 1 GTDB mapping, 1 related NCBI synonym, 2 xrefs, 1 BacDive strain, 2 genome assemblies, 4 genome records, 28 related records, 7 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:56636` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, GTDB, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:7139`, 9 checked lineage rows with no mismatches, 1 LPSN row, 1 GTDB mapping, 1 exact BacDive row, 1 MediaDive row with 2 media, 1 GOLD aggregate row with 3 organisms, 1 MADIN row with 6 assertions, 3 native GOLD organisms, 8 StrainInfo related rows, 10 NCBI type-material rows, and no NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:56636` resolves to label `Aeropyrum pernix`, rank `SPECIES`, parent
`NCBITaxon:56635`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through genus `NCBITaxon:56635` Aeropyrum. The
bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The LPSN row `lpsn:772925` supports legitimate, validly published, correct-name
nomenclature; ATCC 700893, DSM 11879, JCM 9820, and NBRC 100138 type-strain
designations; AB008745; and the direct link to `GTDB:s__Aeropyrum_pernix`.

BacDive row `bacdive:4195` supplies K1 with four culture identifiers. The
strain block keeps BacDive and GOLD genome rows plus GOLD and StrainInfo
related rows, while GTDB, MediaDive, GOLD, and MADIN source attestations count
the exact species rows.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, GTDB, BacDive, MediaDive,
GOLD, MADIN, StrainInfo, type-material, native GOLD, seed, path, and YAML
inputs, and found no omitted NCBI merge or BactoTraits row.

The exact native GOLD organisms for JCM 9820 and DSM 11879 supply retained
GOLD_ORGANISM rows. Native GOLD also has a YK1-12-2013 organism/project/analysis
chain as side evidence without a local BacDive strain match.

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
`strain_count: 1` matches the single exact BacDive K1 strain.
The generated xrefs are the expected LPSN and GTDB identifiers.
The child `Aeropyrum pernix K1` record has no exact BacDive strain row.
No BactoTraits row maps directly to this species in the retained inventory.
The NCBI type-material rows mirror the four LPSN type-strain deposits.
The exact StrainInfo rows are joined through the K1 BacDive strain.
The exact native GOLD YK1-12-2013 row remains side evidence only.
No upstream side row needs staging in kg-microbe or the seeder.
The ignored report probe included gitignored files.
