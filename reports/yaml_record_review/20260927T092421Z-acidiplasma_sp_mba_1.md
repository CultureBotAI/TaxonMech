# YAML Record Review: Acidiplasma sp. MBA-1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidiplasma_sp_mba_1.yaml
- Started UTC: 2026-09-27T09:24:21Z
- Finished UTC: 2026-09-27T09:24:21Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidiplasma_sp_mba_1.yaml` |
| Identifier | `NCBITaxon:1293648` |
| Label | `Acidiplasma sp. MBA-1` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2641301` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI placeholder species with one GTDB closeMatch and
path pinned by `data/taxa/PATHS.tsv:101784`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidiplasma_sp_mba_1.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidiplasma_sp_br_02.yaml data/taxa/archaea/acidiplasma_sp_mba_1.yaml data/taxa/archaea/acidiplasma_sp_ye_1.yaml data/taxa/archaea/aciduliprofundum_boonei_t469.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 73 YAML lines, 10 lineage entries, 0 LPSN nomenclature entries, 1 GTDB mapping, 1 GTDB exact synonym, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, 2 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1293648` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, GTDB, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:303930`, 10 checked lineage rows with no mismatches, 1 GTDB mapping row, 1 native GOLD organism/project/analysis chain as side evidence, 0 NCBI merge rows, and no LPSN, BacDive, MediaDive, retained GOLD, MADIN, BactoTraits, StrainInfo, type-material, strain-assembly, genome-record, or related-record rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1293648` resolves to label `Acidiplasma sp. MBA-1`, rank `SPECIES`,
parent `NCBITaxon:2641301`, genetic code `11`, source set `ncbitaxon|gtdb`, and
taxonomy snapshot `2026-09-13`. The generated record carries those fields and
lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2641301` unclassified
Acidiplasma. The bounded scan found no NCBI merge row and no retained old-id
row.

## Evidence

GTDB mapping row 16870 maps `GTDB:s__Acidiplasma_aeolicum` to this NCBI record
with `skos:closeMatch` and 17 genomes. The generated record preserves that
mapping, adds the GTDB label as an exact synonym, and exposes a single GTDB xref.

NCBI supplies no exact, broad, or related synonyms for MBA-1. The exact native
GOLD organism/project/analysis chain is side evidence only because no BacDive
or final strain row is keyed to `NCBITaxon:1293648`.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, native GOLD, seed, path, and
YAML inputs, and found no omitted NCBI merge, LPSN, BacDive, MediaDive,
retained GOLD, MADIN, BactoTraits, StrainInfo, type-material, or strain rows.

The absence of strains and genome records is expected: no BacDive-derived row
or final strain overlay row is keyed to `NCBITaxon:1293648`.

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
`strain_count: 0` is expected without a retained BacDive or normalized strain row.
The retained GTDB closeMatch is the committed kg-microbe mapping.
No generated LPSN xref is expected.
No retained GOLD aggregate row maps directly to this exact taxon.
The native GOLD chain does not create a strain without a local strain inventory row.
No generated MediaDive attestation is expected.
No generated BactoTraits attestation is expected.
No generated BacDive attestation is expected.
No exact NCBI type-material row is present.
No upstream side row needs staging in kg-microbe or the seeder.
The ignored report probe included gitignored files.
