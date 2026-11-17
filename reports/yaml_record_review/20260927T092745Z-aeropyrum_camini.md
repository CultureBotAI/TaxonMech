# YAML Record Review: Aeropyrum camini

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/aeropyrum_camini.yaml
- Started UTC: 2026-09-27T09:27:45Z
- Finished UTC: 2026-09-27T09:27:45Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/aeropyrum_camini.yaml` |
| Identifier | `NCBITaxon:229980` |
| Label | `Aeropyrum camini` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:56635` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI species record with LPSN, BacDive descendant, GOLD,
MADIN, and StrainInfo strain-side evidence, with path pinned by
`data/taxa/PATHS.tsv:337430`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/aeropyrum_camini.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/aeropyrum_camini.yaml data/taxa/archaea/aeropyrum_camini_sy1_jcm_12091.yaml data/taxa/archaea/aeropyrum_pernix.yaml data/taxa/archaea/aeropyrum_pernix_k1.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 714 YAML lines, 9 lineage entries, 1 LPSN nomenclature entry, 0 GTDB mappings, 1 related NCBI synonym, 2 xrefs, 1 gathered BacDive strain, 12 genome assemblies, 9 genome records, 29 related records, 5 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:229980` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping and no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:45144`, 9 checked lineage rows with no mismatches, 1 LPSN row, 1 exact BacDive source record that also names descendant strain `NCBITaxon:1198449`, 1 GOLD aggregate row with 2 organisms, 1 MADIN row, 2 native GOLD organisms, 2 StrainInfo assemblies, 7 StrainInfo related rows, 7 NCBI type-material rows, and no NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:229980` resolves to label `Aeropyrum camini`, rank `SPECIES`,
parent `NCBITaxon:56635`, genetic code `11`, source set
`ncbitaxon|lpsn|gold|madin_etal`, and taxonomy snapshot `2026-09-13`.
The generated record carries those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through genus `NCBITaxon:56635` Aeropyrum. The
bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The LPSN row `lpsn:772924` supports legitimate, validly published, correct-name
nomenclature; ATCC BAA-758, DSM 16960, and JCM 12091 type-strain designations;
AB109559; and its `GTDB:s__Aeropyrum_camini` cross-reference.

BacDive row `bacdive:4196` is filed under child strain `NCBITaxon:1198449`;
the parent species intentionally gathers it with `classified_as`. Its SY1
strain block carries BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo
links, including the two StrainInfo genome rows matched by JCM 12091.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, BacDive, GOLD, MADIN,
StrainInfo, type-material, native GOLD, seed, path, and YAML inputs, and found
no omitted NCBI merge, direct GTDB mapping, MediaDive, or BactoTraits row.

Direct species-side GOLD evidence contributes 2 organism rows. Native GOLD has
DSM 16960 and ATCC BAA-758 organisms as side evidence; no native project or
analysis rows attach directly to those two exact organisms in this snapshot.

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
`strain_count: 1` matches the single gathered BacDive SY1 strain.
The generated xrefs are the expected LPSN and GTDB identifiers.
The `MADIN` attestation counts the direct species row only.
The SY1 strain taxon owns the direct GTDB, BacDive, and MediaDive attestations.
No BactoTraits row maps directly to this species in the retained inventory.
The NCBI type-material rows mirror the three LPSN type-strain deposits.
The exact StrainInfo rows are joined through the gathered SY1 BacDive strain.
No upstream side row needs staging in kg-microbe or the seeder.
The ignored report probe included gitignored files.
