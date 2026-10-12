# YAML Record Review: Acetomicrobium mobile DSM 13181

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetomicrobium_mobile_dsm_13181.yaml
- Started UTC: 2026-09-26T17:48:02Z
- Finished UTC: 2026-09-26T17:48:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetomicrobium_mobile_dsm_13181.yaml` |
| Identifier | `NCBITaxon:891968` |
| Label | `Acetomicrobium mobile DSM 13181` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:97477` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:604843`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetomicrobium_mobile_dsm_13181.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetomicrobium_hydrogeniformans_atcc_baa_1850.yaml data/taxa/bacteria/acetomicrobium_mobile.yaml data/taxa/bacteria/acetomicrobium_mobile_dsm_13181.yaml data/taxa/bacteria/acetomicrobium_sp.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a source-rich generated strain record: 736 YAML lines, 10 lineage entries, 1 `skos:closeMatch` GTDB taxonomy mapping, 1 BacDive strain, 8 genome assemblies, 7 genome records, 29 related records, 5 synonyms, 1 xref, and 7 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in seed, legacy-path, NCBI, path, GTDB, BacDive, GOLD, MediaDive, Madin, BactoTraits, culture-collection, strain assembly, genome, related-record, BV-BRC, and ATB rows; it also found the parent `lpsn:793977` LPSN row carrying the type-strain designations. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:190204`, 1 GTDB closeMatch row, 1 BacDive row, 3 culture-collection rows, 1 native GOLD organism with 1 project and 1 analysis, 1 MediaDive row, 1 Madin row, 1 BactoTraits row, 10 checked lineage entries with no missing rows or mismatches, and no NCBI merge, LPSN, direct StrainInfo, or NCBI type-material rows for this strain target. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:891968` resolves in the committed NCBI inventory to label
`Acetomicrobium mobile DSM 13181`, rank `STRAIN`, parent `NCBITaxon:97477`,
four exact `Acetomicrobium`/`Anaerobaculum` synonyms, genetic code `11`, and
taxonomy snapshot `2026-09-13`. The record carries those same identity fields
and correctly lands in the `bacteria` path bucket through `taxon_domain:
BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:97477`
Acetomicrobium mobile. There are no retained old identifiers for this target
in the NCBI merge input.

## Evidence

The GTDB mapping is supported by `data/raw/gtdb_mappings.tsv:317052`, which
maps `GTDB:s__Acetomicrobium_flavidum` to this strain with predicate
`skos:closeMatch` and `genome_count: 9`.

The BacDive strain block is supported by `data/raw/bacdive_strains.tsv:17588`
for BacDive 17777, designation `NGA`, taxon `NCBITaxon:891968`, LPSN parent
name `lpsn:793977`, and the ATCC BAA-54 / DSM 13181 / JCM 12221 collection
identifiers. Native strain and genome tables preserve the same DSM 13181
genome through BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, StrainInfo, and ATB
rows.

The seed event is supported by `curation/seed_scope.tsv:7080`, which records
`NCBITaxon:891968` as added on `2026-09-12` with reason `attested rule:
Acetomicrobium mobile DSM 13181, 7 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated source-rich strain
record. The bounded scan found the expected GTDB, BacDive, native GOLD,
MediaDive, Madin, BactoTraits, culture-collection, genome, and related-record
rows and found no LPSN row filed directly to the strain, direct StrainInfo row,
NCBI type-material row, or NCBI merge row for this target.

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

The exact source scan also found `curation/legacy_page_paths.tsv:61310`; that
is legacy route metadata and does not require a TaxonRecord field.
