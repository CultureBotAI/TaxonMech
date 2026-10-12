# YAML Record Review: Acetohalobium arabaticum DSM 5501

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetohalobium_arabaticum_dsm_5501.yaml
- Started UTC: 2026-09-26T17:43:31Z
- Finished UTC: 2026-09-26T17:43:31Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetohalobium_arabaticum_dsm_5501.yaml` |
| Identifier | `NCBITaxon:574087` |
| Label | `Acetohalobium arabaticum DSM 5501` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:28187` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:544385`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetohalobium_arabaticum_dsm_5501.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetohalobium_arabaticum_dsm_5501.yaml data/taxa/bacteria/acetohalobium_sp.yaml data/taxa/bacteria/acetomicrobium_flavidum.yaml data/taxa/bacteria/acetomicrobium_hydrogeniformans.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a source-rich generated strain record: 709 YAML lines, 10 lineage entries, 1 `skos:closeMatch` GTDB taxonomy mapping, 1 BacDive strain, 10 genome assemblies, 8 genome records, 27 related records, 1 xref, and 6 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy-path, NCBI, path, GTDB, BacDive, MediaDive, Madin, BactoTraits, culture-collection, strain assembly, genome, related-record, BV-BRC, GOLD, and ATB rows; it also found the parent `lpsn:772538` LPSN row carrying `GTDB:s__Acetohalobium_arabaticum`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:135455`, 1 GTDB mapping row, 1 native BacDive row, 2 culture-collection rows, 1 native GOLD organism with 1 project and 1 analysis, 1 MediaDive row, 1 Madin row, 1 BactoTraits row, 10 checked lineage entries with no missing rows or mismatches, and no NCBI merge or direct NCBI type-material rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:574087` resolves in the committed NCBI inventory to label
`Acetohalobium arabaticum DSM 5501`, rank `STRAIN`, parent
`NCBITaxon:28187`, exact synonyms for `Acetohalobium arabaticum str. DSM 5501`
and `Acetohalobium arabaticum strain DSM 5501`, genetic code `11`, and
taxonomy snapshot `2026-09-13`. The record carries those same identity fields
and correctly lands in the `bacteria` path bucket through `taxon_domain:
BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:28187`
Acetohalobium arabaticum. There are no retained old identifiers for this target
in the NCBI merge input.

## Evidence

The GTDB mapping is supported by `data/raw/gtdb_mappings.tsv:297193`, which
maps `GTDB:s__Acetohalobium_arabaticum` to this strain with predicate
`skos:closeMatch` and `genome_count: 1`.

The BacDive strain block is supported by `data/raw/bacdive_strains.tsv:5865`
for BacDive 5978, designation `Z-7288`, taxon `NCBITaxon:574087`, LPSN parent
name `lpsn:772538`, and the ATCC 49924 / DSM 5501 collection identifiers.
Native strain and genome tables preserve the same DSM 5501 genome through
BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, StrainInfo, and ATB rows.

The seed event is supported by `curation/seed_scope.tsv:10246`, which records
`NCBITaxon:574087` as added on `2026-09-12` with reason `attested rule:
Acetohalobium arabaticum DSM 5501, 6 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated source-rich strain
record. The bounded scan found the expected GTDB, BacDive, GOLD, MediaDive,
Madin, BactoTraits, culture-collection, and genome rows and found no LPSN row
filed directly to the strain, StrainInfo direct target rows, NCBI
type-material rows, or NCBI merge row for this target.

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

The exact source scan also found `curation/legacy_page_paths.tsv:54710`; that
is legacy route metadata and does not require a TaxonRecord field.
