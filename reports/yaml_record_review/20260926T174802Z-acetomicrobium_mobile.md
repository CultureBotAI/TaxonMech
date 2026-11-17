# YAML Record Review: Acetomicrobium mobile

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetomicrobium_mobile.yaml
- Started UTC: 2026-09-26T17:48:02Z
- Finished UTC: 2026-09-26T17:48:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetomicrobium_mobile.yaml` |
| Identifier | `NCBITaxon:97477` |
| Label | `Acetomicrobium mobile` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:49894` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:620564`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetomicrobium_mobile.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetomicrobium_hydrogeniformans_atcc_baa_1850.yaml data/taxa/bacteria/acetomicrobium_mobile.yaml data/taxa/bacteria/acetomicrobium_mobile_dsm_13181.yaml data/taxa/bacteria/acetomicrobium_sp.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a source-rich generated species record: 743 YAML lines, 9 lineage entries, 1 LPSN name, 1 BacDive type strain classified as descendant `NCBITaxon:891968`, 8 genome assemblies, 7 genome records, 29 related records, 1 xref, and 5 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier and descendant `NCBITaxon:891968` in seed, legacy-path, NCBI, path, LPSN, BacDive, GOLD, GTDB descendant, MediaDive descendant, Madin, BactoTraits descendant, NCBI type-material, culture-collection, strain assembly, genome, related-record, StrainInfo, BV-BRC, and ATB rows; found `lpsn:793977` and synonym `lpsn:773236` in the expected raw rows. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:16450`, the LPSN row at `data/raw/lpsn_names.tsv:30574`, 1 BacDive row filed through descendant strain `NCBITaxon:891968`, 3 native GOLD organisms, 1 Madin row with 5 assertions, 1 StrainInfo assembly row, 9 StrainInfo related rows, 7 NCBI type-material rows, 9 checked lineage entries with no missing rows or mismatches, and no direct GTDB, MediaDive, BactoTraits, or NCBI merge rows for this species target. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:97477` resolves in the committed NCBI inventory to label
`Acetomicrobium mobile`, rank `SPECIES`, parent `NCBITaxon:49894`, exact
synonym `Anaerobaculum mobile`, three related `Anaerobaculum`/authority
synonyms, genetic code `11`, and taxonomy snapshot `2026-09-13`. The record
carries those same identity fields and correctly lands in the `bacteria` path
bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:49894` Acetomicrobium. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The LPSN name block is supported by `data/raw/lpsn_names.tsv:30574`, including
`lpsn:793977`, the `Acetomicrobium mobile` name, valid publication flags, the
`(Menes and Muxi 2002) Ben Hania et al. 2016` authority, three publication
identifiers, `INSDC:AJ243189`, and the ATCC BAA-54 / DSM 13181 type-strain
designations. The `Anaerobaculum mobile` synonym block is supported by
`data/raw/lpsn_names.tsv:15301`.

The BacDive type strain is supported by `data/raw/bacdive_strains.tsv:17588`
for BacDive 17777, designation `NGA`, child taxon `NCBITaxon:891968`, LPSN
name `lpsn:793977`, and ATCC BAA-54 / DSM 13181 / JCM 12221 culture
collection identifiers.

The seed event is supported by `curation/seed_scope.tsv:23601`, which records
`NCBITaxon:97477` as added on `2026-09-12` with reason `attested rule:
Acetomicrobium mobile, 4 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated source-rich
species record. The bounded scan found the expected LPSN, BacDive descendant,
native GOLD, Madin, StrainInfo, NCBI type-material, and descendant genome rows
and found no direct GTDB mapping, MediaDive, BactoTraits, strain assembly,
strain genome, or NCBI merge row for the species target itself.

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

The exact source scan also found descendant `NCBITaxon:891968`, whose
strain-level page path is tracked separately at `curation/legacy_page_paths.tsv:61310`.
