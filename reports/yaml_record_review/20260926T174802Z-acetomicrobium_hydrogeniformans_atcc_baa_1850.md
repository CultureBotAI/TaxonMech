# YAML Record Review: Acetomicrobium hydrogeniformans ATCC BAA-1850

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetomicrobium_hydrogeniformans_atcc_baa_1850.yaml
- Started UTC: 2026-09-26T17:48:02Z
- Finished UTC: 2026-09-26T17:48:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetomicrobium_hydrogeniformans_atcc_baa_1850.yaml` |
| Identifier | `NCBITaxon:592015` |
| Label | `Acetomicrobium hydrogeniformans ATCC BAA-1850` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:649746` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:549371`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetomicrobium_hydrogeniformans_atcc_baa_1850.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetomicrobium_hydrogeniformans_atcc_baa_1850.yaml data/taxa/bacteria/acetomicrobium_mobile.yaml data/taxa/bacteria/acetomicrobium_mobile_dsm_13181.yaml data/taxa/bacteria/acetomicrobium_sp.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a generated strain record: 524 YAML lines, 10 lineage entries, 1 `skos:closeMatch` GTDB taxonomy mapping, 1 BacDive strain, 6 genome assemblies, 9 genome records, 22 related records, 5 synonyms, 1 xref, and 6 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in seed, legacy-path, NCBI, path, GTDB, BacDive, GOLD, MediaDive, Madin, BactoTraits, culture-collection, strain assembly, genome, related-record, BV-BRC, and ATB rows; found `GTDB:s__Acetomicrobium_thermoterrenum` in the expected raw GTDB rows. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:140367`, 1 GTDB closeMatch row, 1 BacDive row, 2 culture-collection rows, 1 native GOLD organism with 1 project and 2 analyses, 1 MediaDive row, 1 Madin row, 1 BactoTraits row, 10 checked lineage entries with no missing rows or mismatches, and no NCBI merge, LPSN, direct StrainInfo, or NCBI type-material rows for this strain target. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:592015` resolves in the committed NCBI inventory to label
`Acetomicrobium hydrogeniformans ATCC BAA-1850`, rank `STRAIN`, parent
`NCBITaxon:649746`, four exact `Anaerobaculum` synonyms, genetic code `11`,
and taxonomy snapshot `2026-09-13`. The record carries those same identity
fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:649746`
Acetomicrobium hydrogeniformans. There are no retained old identifiers for
this target in the NCBI merge input.

## Evidence

The GTDB mapping is supported by `data/raw/gtdb_mappings.tsv:298063`, which
maps `GTDB:s__Acetomicrobium_thermoterrenum` to this strain with predicate
`skos:closeMatch` and `genome_count: 5`.

The BacDive strain block is supported by `data/raw/bacdive_strains.tsv:17590`
for BacDive 17779, designation `OS1`, taxon `NCBITaxon:592015`, LPSN parent
name `lpsn:793979`, and the ATCC BAA-1850 / DSM 22491 collection identifiers.
The native strain and genome tables preserve the same ATCC BAA-1850 genomes
through BacDive, BV-BRC, GOLD, and related-record rows.

The seed event is supported by `curation/seed_scope.tsv:10278`, which records
`NCBITaxon:592015` as added on `2026-09-12` with reason `attested rule:
Acetomicrobium hydrogeniformans ATCC BAA-1850, 6 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated strain record.
The bounded scan found the expected GTDB, BacDive, native GOLD, MediaDive,
Madin, BactoTraits, culture-collection, genome, and related-record rows and
found no LPSN row filed directly to the strain, direct StrainInfo row, NCBI
type-material row, or NCBI merge row for this target.

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

The exact source scan also found `curation/legacy_page_paths.tsv:55175`; that
is legacy route metadata and does not require a TaxonRecord field.
