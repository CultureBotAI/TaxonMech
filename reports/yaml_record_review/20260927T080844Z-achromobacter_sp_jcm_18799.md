# YAML Record Review: Achromobacter sp. JCM 18799

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_sp_jcm_18799.yaml
- Started UTC: 2026-09-27T08:08:44Z
- Finished UTC: 2026-09-27T08:08:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_sp_jcm_18799.yaml` |
| Identifier | `NCBITaxon:1295134` |
| Label | `Achromobacter sp. JCM 18799` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2626865` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record backed by NCBI and BacDive strain evidence.
Its path is pinned by `data/taxa/PATHS.tsv:102650`, and reviewed seeded fields
belong to the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_sp_jcm_18799.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_sp_jcm_18799.yaml data/taxa/bacteria/achromobacter_sp_jcm_28247.yaml data/taxa/bacteria/achromobacter_sp_jcm_28260.yaml data/taxa/bacteria/achromobacter_sp_jcm_28658.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 426 YAML lines, 10 lineage entries, 1 NCBI and 1 BacDive source attestation, 1 NCBI exact synonym, 0 nomenclature entries, 0 taxonomy mappings, 1 BacDive strain, 1 culture-collection ID, 8 genome assemblies, 6 genome records, 20 related records, and 0 causal graphs. |
| Boundary-guarded exact ID-only local scan | Found this identifier in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no GTDB mapping row; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:304782`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 1 exact BacDive taxon hit, 1 raw BacDive strain row, 1 culture-collection row, 8 normalized assembly rows, 6 normalized genome rows, 20 normalized related rows, native GOLD organism `Go0094263`, project `Gp0094263`, and analysis `Ga0128361`, and no NCBI type-material, StrainInfo, LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1295134` resolves in the committed NCBI inventory to label
`Achromobacter sp. JCM 18799`, rank `SPECIES`, parent `NCBITaxon:2626865`,
genetic code `11`, source set `ncbitaxon|bacdive`, and snapshot `2026-09-13`.
The generated record carries those same identity fields and lands correctly in
the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2626865` unclassified
Achromobacter. The bounded scan found no NCBI merge row and no retained old-id
row that would change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation and the `Alcaligenes
faecalis JCM 18799` exact synonym. BacDive row 162299 supports the `BACDIVE`
attestation, seeded `kgmicrobe.strain:bacdive_162299` strain, and JCM-18799 ID.

The strain block is supported by one BacDive INSDC assembly, two BV-BRC assembly
matches, two GOLD assembly matches, three NCBI Assembly matches, two BacDive
genome-record assertions, two GOLD IMG assertions, two BV-BRC PATRIC assertions,
and 20 BioProject, BioSample, GOLD analysis, organism, and project rows.

Native GOLD side evidence mirrors the normalized GOLD records: organism
`Go0094263`, project `Gp0094263`, and one Achromobacter sp. JCM 18799 analysis.
No same-taxon LPSN, GTDB, MediaDive, MADIN, or BactoTraits row was present.

## Completeness

The exact and bounded scans account for expected NCBI, BacDive, GOLD, BV-BRC,
NCBI Assembly, IMG/PATRIC, BioProject, BioSample, seed, path, and generated YAML
inputs. They found no omitted NCBI merge, NCBI type-material, LPSN, GTDB,
MediaDive, MADIN, BactoTraits, StrainInfo, ATB, or StrainInfo exclusion row.

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

This was a read-only generated-record review. It did not append a curation
event, promote `mapping_status`, write a history record, or touch the seeded
YAML, and it found no upstream side rows to stage for follow-up curation.
