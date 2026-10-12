# YAML Record Review: Acidiplasma sp. BR-02

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidiplasma_sp_br_02.yaml
- Started UTC: 2026-09-27T09:24:21Z
- Finished UTC: 2026-09-27T09:24:21Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidiplasma_sp_br_02.yaml` |
| Identifier | `NCBITaxon:3402690` |
| Label | `Acidiplasma sp. BR-02` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2641301` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI-only species-level placeholder under
unclassified Acidiplasma, with path pinned by `data/taxa/PATHS.tsv:454981`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidiplasma_sp_br_02.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidiplasma_sp_br_02.yaml data/taxa/archaea/acidiplasma_sp_mba_1.yaml data/taxa/archaea/acidiplasma_sp_ye_1.yaml data/taxa/archaea/aciduliprofundum_boonei_t469.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 54 YAML lines, 10 lineage entries, 0 LPSN nomenclature entries, 0 GTDB mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, 1 source attestation, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:3402690` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping and no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:627613`, 10 checked lineage rows with no mismatches, 0 NCBI merge rows, and no LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN, BactoTraits, native GOLD, StrainInfo, type-material, strain-assembly, genome-record, or related-record rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:3402690` resolves to label `Acidiplasma sp. BR-02`, rank `SPECIES`,
parent `NCBITaxon:2641301`, genetic code `11`, source set `ncbitaxon`, and
taxonomy snapshot `2026-09-13`. The generated record carries those fields and
lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2641301` unclassified
Acidiplasma. The bounded scan found no NCBI merge row and no retained old-id
row.

## Evidence

NCBI supplies no exact, broad, or related synonyms for this placeholder species.
The generated record therefore correctly has no `synonyms`, `nomenclature`, or
`xrefs` section.

No auxiliary processed source row maps directly to `NCBITaxon:3402690`; the
single `NCBITAXON` name attestation is the only generated source attestation.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, seed, path, and YAML inputs, and
found no omitted NCBI merge, LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN,
BactoTraits, native GOLD, StrainInfo, type-material, or final strain rows.

The absence of strains and genome records is expected: no BacDive-derived row
or final strain overlay row is keyed to `NCBITaxon:3402690`.

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
No generated taxonomy mapping section is expected.
No generated xref section is expected.
No LPSN row maps directly to this placeholder species.
No GOLD, MediaDive, MADIN, or BactoTraits attestation is expected.
No native GOLD organism, project, or analysis row names this exact taxon.
No exact NCBI type-material row is present.
No exact BacDive source row is present.
The parent is the NCBI `unclassified Acidiplasma` bucket.
The path stem matches the pinned slug.
No upstream side row needs staging in kg-microbe or the seeder.
The ignored report probe included gitignored files.
