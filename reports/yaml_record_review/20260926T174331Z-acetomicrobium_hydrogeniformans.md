# YAML Record Review: Acetomicrobium hydrogeniformans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetomicrobium_hydrogeniformans.yaml
- Started UTC: 2026-09-26T17:43:31Z
- Finished UTC: 2026-09-26T17:43:31Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetomicrobium_hydrogeniformans.yaml` |
| Identifier | `NCBITaxon:649746` |
| Label | `Acetomicrobium hydrogeniformans` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:49894` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:559730`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetomicrobium_hydrogeniformans.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetohalobium_arabaticum_dsm_5501.yaml data/taxa/bacteria/acetohalobium_sp.yaml data/taxa/bacteria/acetomicrobium_flavidum.yaml data/taxa/bacteria/acetomicrobium_hydrogeniformans.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a source-rich generated record: 566 YAML lines, 9 lineage entries, 1 LPSN name, 3 `skos:broadMatch` GTDB taxonomy mappings, 1 BacDive type strain, 6 genome assemblies, 9 genome records, 22 related records, 5 synonyms, and 6 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier and descendant `NCBITaxon:592015` in seed, legacy-path, NCBI, path, LPSN, GTDB, BacDive, GOLD, MediaDive, Madin, BactoTraits, NCBI type-material, culture-collection, strain assembly, genome, related-record, StrainInfo, BV-BRC, and ATB rows; found `lpsn:793979` and synonym `lpsn:789815` in the expected raw rows. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:150084`, the LPSN row at `data/raw/lpsn_names.tsv:30576`, 3 GTDB broadMatch rows, one BacDive row filed through descendant strain `NCBITaxon:592015`, 2 native GOLD organisms, 1 Madin row with 16 assertions, 2 species-level StrainInfo related rows, 7 NCBI type-material rows, 9 checked lineage entries with no missing rows or mismatches, and no retained old NCBI IDs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:649746` resolves in the committed NCBI inventory to label
`Acetomicrobium hydrogeniformans`, rank `SPECIES`, parent
`NCBITaxon:49894`, exact synonyms for quoted `Acetomicrobium
hydrogeniformans` and `Anaerobaculum hydrogeniformans`, related synonyms for
the two author-bearing forms, genetic code `11`, and taxonomy snapshot
`2026-09-13`. The record carries those same identity fields and correctly lands
in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:49894` Acetomicrobium. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The LPSN name block is supported by `data/raw/lpsn_names.tsv:30576`, including
`lpsn:793979`, the `Acetomicrobium hydrogeniformans` name, valid publication
flags, the `(Maune and Tanner 2012) Ben Hania et al. 2016` authority, three
publication identifiers, `INSDC:FJ862996`, and the ATCC BAA-1850 / DSM 22491
type-strain designations. The `Anaerobaculum hydrogeniformans` synonym block is
supported by `data/raw/lpsn_names.tsv:26830`.

The three GTDB taxonomy mappings are supported by adjacent
`data/raw/gtdb_mappings.tsv:300713` through `:300715` rows and cover 11 pooled
genomes in total. The generated GTDB source attestation correctly records the
largest component, `GTDB:s__Acetomicrobium_thermoterrenum`, with 5 genomes and
notes that two further GTDB species pool onto the same NCBI species.

The seed event is supported by `curation/seed_scope.tsv:25041`, which records
`NCBITaxon:649746` as added on `2026-09-12` with reason `attested rule:
Acetomicrobium hydrogeniformans, 4 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated source-rich
record. The bounded scan found the expected LPSN, GTDB, BacDive descendant,
native GOLD, Madin, StrainInfo, NCBI type-material, and descendant genome rows
and found no direct MediaDive, BactoTraits, strain assembly, strain genome, or
NCBI merge row for the species target itself.

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

The exact source scan also found descendant `NCBITaxon:592015`, whose
strain-level page path is tracked separately at `curation/legacy_page_paths.tsv:55175`.
