# YAML Record Review: Acetomicrobium thermoterrenum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetomicrobium_thermoterrenum.yaml
- Started UTC: 2026-09-26T18:13:24Z
- Finished UTC: 2026-09-26T18:13:24Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetomicrobium_thermoterrenum.yaml` |
| Identifier | `NCBITaxon:1120986` |
| Label | `Acetomicrobium thermoterrenum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:49894` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:36045`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetomicrobium_thermoterrenum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetomicrobium_sp_uba5826.yaml data/taxa/bacteria/acetomicrobium_thermoterrenum.yaml data/taxa/bacteria/acetomicrobium_thermoterrenum_dsm_13490.yaml data/taxa/bacteria/acetonema_longum.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a generated species record: 733 YAML lines, 9 lineage entries, 1 LPSN nomenclature row, 4 synonyms, 1 BacDive type strain, 11 genome assemblies, 9 genome records, 27 related records, 2 xrefs, and 5 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in seed, legacy-path, NCBI, path, LPSN, GOLD, Madin, NCBI merge, StrainInfo, and related-record rows; found its DSM 13490 strain support in BacDive, culture-collection, assembly, genome, BV-BRC, GTDB genome, GOLD, NCBI Assembly, StrainInfo, and AllTheBacteria rows. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:241961`, 1 LPSN row, 1 BacDive species/strain match, 1 GOLD aggregate with 2 native GOLD organisms, 1 Madin row, 1 NCBI merge row from `NCBITaxon:46614`, 1 species-level related-record row, StrainInfo DSM 13490/ACM 5076 deposits, 7 NCBI type-material rows, and 9 checked lineage entries with no missing rows or mismatches. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1120986` resolves in the committed NCBI inventory to label
`Acetomicrobium thermoterrenum`, rank `SPECIES`, parent `NCBITaxon:49894`,
exact synonym `Anaerobaculum thermoterrenum`, genetic code `11`, and taxonomy
snapshot `2026-09-13`. The record carries those same identity fields and
correctly lands in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:49894` Acetomicrobium. The
old identifier `NCBITaxon:46614` is retired into this target and is not
retained as a live NCBI row.

## Evidence

The LPSN row `lpsn:793978` supports the validly published correct-name
nomenclature, `DSM-13490` type-strain designation, publication and sequence
accessions, and LPSN synonym `lpsn:773237` for `Anaerobaculum thermoterrenum`.

BacDive 17778, StrainInfo strain 49477, and two native GOLD organism rows
support the RWcit2/DSM 13490/ACM 5076 type-strain surface. The strain block
also preserves DSM 13490 assembly, genome, related-record, and AllTheBacteria
evidence through the child strain `NCBITaxon:1120987`.

The seed event is supported by `curation/seed_scope.tsv:26524`, which records
`NCBITaxon:1120986` as added on `2026-09-12` with reason `attested rule:
Acetomicrobium thermoterrenum, 4 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated species record.
The bounded scan found expected NCBI, LPSN, BacDive, StrainInfo, native GOLD,
Madin, NCBI type-material, NCBI merge, and strain-linked genome rows and no
direct target rows in GTDB, MediaDive, BactoTraits, or primary strain tables
that would require additional species-level sections.

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
YAML.
