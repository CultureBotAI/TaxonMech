# YAML Record Review: Aciduliprofundum boonei T469

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/aciduliprofundum_boonei_t469.yaml
- Started UTC: 2026-09-27T09:24:21Z
- Finished UTC: 2026-09-27T09:24:21Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/aciduliprofundum_boonei_t469.yaml` |
| Identifier | `NCBITaxon:439481` |
| Label | `Aciduliprofundum boonei T469` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:379547` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI strain record with GTDB, BacDive, MediaDive, GOLD,
MADIN, BactoTraits, and StrainInfo strain-side evidence, with path pinned by
`data/taxa/PATHS.tsv:505271`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/aciduliprofundum_boonei_t469.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidiplasma_sp_br_02.yaml data/taxa/archaea/acidiplasma_sp_mba_1.yaml data/taxa/archaea/acidiplasma_sp_ye_1.yaml data/taxa/archaea/aciduliprofundum_boonei_t469.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 214 YAML lines, 8 lineage entries, 0 LPSN nomenclature entries, 1 GTDB mapping, 4 exact synonyms, 1 xref, 1 BacDive strain, 2 genome assemblies, 3 genome records, 4 related records, 7 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:439481` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, GTDB, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:97574`, 8 checked lineage rows with no mismatches, 1 GTDB mapping row, 1 exact BacDive row, 1 GOLD aggregate row, 1 MediaDive row, 1 MADIN row with 7 assertions, 1 BactoTraits row, 2 native GOLD organisms, 2 raw BacDive assemblies, 3 BacDive genome records, 2 GOLD related rows, and no NCBI merge, LPSN, exact StrainInfo, or NCBI type-material rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:439481` resolves to label `Aciduliprofundum boonei T469`, rank
`STRAIN`, parent `NCBITaxon:379547`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|mediadive|gold|madin_etal|bactotraits`, and taxonomy
snapshot `2026-09-13`. The generated record carries those fields and lands in
`ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 8 stored
taxa, from `NCBITaxon:1` root through species `NCBITaxon:379547` Candidatus
Aciduliprofundum boonei. The bounded scan found no NCBI merge row and no
retained old-id row.

## Evidence

BacDive row `bacdive:23434` supplies strain T469 with deposit DSM 19572. The
strain block carries two BacDive NCBI assemblies, three BacDive IMG/PATRIC
genome records, two GOLD organism related rows, and two StrainInfo related rows
joined through DSM 19572.

GTDB maps `GTDB:s__Aciduliprofundum_boonei` with 6 genomes; NCBI contributes
three exact strain synonyms; retained GOLD supplies the 1-organism attestation;
MediaDive contributes 1 medium; MADIN contributes 7 traits; and BactoTraits
contributes 1 trait assertion.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, BacDive, MediaDive, GOLD,
Madin, BactoTraits, native GOLD, StrainInfo overlay, seed, path, and YAML inputs,
and found no omitted NCBI merge, LPSN, exact StrainInfo, or type-material row.

The exact native GOLD organism `Go0608798` supplies the two retained GOLD
related rows by the culture-collection and organism-strain source fields.
`Go0004786` and its two projects remain side evidence without a DSM 19572 match.

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
`strain_count: 1` matches the single exact BacDive T469 strain.
No LPSN nomenclature or LPSN xref is expected for this strain taxon.
The generated xref is the retained GTDB species.
The StrainInfo rows use source taxon `NCBITaxon:379547` but the exact BacDive strain.
No direct NCBI Assembly, BV-BRC overlay, or GTDB genome overlay row is emitted.
The ignored report probe included gitignored files.
