# YAML Record Review: Halorhabdus tiamatea SARL4B

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/halorhabdus_tiamatea_sarl4b.yaml
- Started UTC: 2026-09-27T14:15:42Z
- Finished UTC: 2026-09-27T14:15:42Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/halorhabdus_tiamatea_sarl4b.yaml` |
| Identifier | `NCBITaxon:1033806` |
| Label | `Halorhabdus tiamatea SARL4B` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:430914` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated BacDive, GOLD, GTDB, MediaDive, MADIN, and NCBI-backed
Halobacteriales strain record, with path pinned by `data/taxa/PATHS.tsv:13766`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/halorhabdus_tiamatea_sarl4b.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/candidatus_aciduliprofundum_sp_lau09_cd652.yaml data/taxa/archaea/candidatus_aciduliprofundum_sp_lau09_cd1713.yaml data/taxa/archaea/halorhabdus_tiamatea_sarl4b.yaml data/taxa/archaea/nitrososphaera_viennensis.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 448 YAML lines, 11 lineage entries, 1 GTDB mapping, 4 exact synonyms, 1 BacDive strain, 4 genome assemblies, 6 genome records, 17 related records, 6 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1033806` in the expected seed, NCBI, GTDB, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:221311`, 11 checked lineage entries with no missing rows or mismatches, 1 GTDB row at line 1373, 1 BacDive strain row at line 5769, 1 MADIN row, 1 MediaDive row, 1 retained GOLD aggregate row, 3 native GOLD organisms, 2 native GOLD projects, 2 native GOLD analyses, 2 culture-collection rows, 4 normalized assemblies, 6 normalized genome rows, 9 exact-target related rows, 0 NCBI merge rows, 0 NCBI type-material rows, and no exact-target LPSN, BactoTraits, or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1033806` resolves to `Halorhabdus tiamatea SARL4B`, rank `STRAIN`,
parent `NCBITaxon:430914`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|mediadive|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`.

The lineage is root-first and matches all 11 committed NCBI rows, ending at
species `NCBITaxon:430914` Halorhabdus tiamatea. The bounded scan found no
NCBI merge row and no retained old-id row.

## Evidence

The raw NCBI row supports the strain identity, direct species parent, genetic
code, three exact NCBI synonyms, six-source source set, and 2026-09-13
snapshot date. The seed event is supported by `curation/seed_scope.tsv:10796`.

BacDive row 5882 supports local strain `kgmicrobe.strain:bacdive_5882`, the
SARL4B designation, and DSM-18392/JCM-14471 culture IDs. Normalized assembly,
genome, and related-record rows add BacDive, BV-BRC, GOLD, and StrainInfo
side records, with source taxon IDs split between this strain and parent
species `NCBITaxon:430914`.

The retained GOLD aggregate, native GOLD organism/project/analysis rows, GTDB
mapping, MediaDive row, and MADIN row account for the remaining generated
attestations. No exact-target LPSN row is expected for this strain record.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, BacDive, GOLD, MediaDive,
MADIN, seed, path, and generated YAML inputs, and found no omitted
exact-target LPSN, BactoTraits, type-material, or StrainInfo row.

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
The BacDive strain has 2 culture-collection IDs.
The GTDB closeMatch has 2 genomes.
Native GOLD has 3 organism rows for this target.
The generated record materializes 17 related records.
No exact-target NCBI type-material row is available.
No NCBI merge row complicates identity.
Eleven NCBI lineage rows are expected.
The 448-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
