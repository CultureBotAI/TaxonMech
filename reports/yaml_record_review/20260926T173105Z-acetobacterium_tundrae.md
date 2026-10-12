# YAML Record Review: Acetobacterium tundrae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_tundrae.yaml
- Started UTC: 2026-09-26T17:31:05Z
- Finished UTC: 2026-09-26T17:31:05Z
- Verdict: fail

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_tundrae.yaml` |
| Identifier | `NCBITaxon:132932` |
| Label | `Acetobacterium tundrae` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:33951` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:116722`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_tundrae.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_sp_z.yaml data/taxa/bacteria/acetobacterium_submarinus.yaml data/taxa/bacteria/acetobacterium_tundrae.yaml data/taxa/bacteria/acetobacterium_wieringae.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a dense generated record: 952 YAML lines, 9 lineage entries, 1 LPSN name, 1 GTDB `skos:closeMatch`, 2 BacDive strains, 16 genome assemblies, 12 genome records, 34 related records, 2 xrefs, 2 NCBITaxon synonyms, and 8 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found the target identifier in seed, legacy-path, NCBI, BacDive, StrainInfo, GOLD, GTDB, MediaDive, Madin, BactoTraits, ATB, and path rows across the raw, curation, auxiliary, history, and ignored report trees; found `lpsn:772532` and `GTDB:s__Acetobacterium_tundrae` in the expected LPSN and GTDB raw rows. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:25766`, the LPSN row at `data/raw/lpsn_names.tsv:14828`, the GTDB mapping at `data/raw/gtdb_mappings.tsv:19161`, 2 BacDive rows, 1 GOLD aggregate row covering 3 native GOLD organisms, 1 MediaDive row, 1 Madin row with 2 assertions, 1 BactoTraits row with 2 assertions, 10 StrainInfo target rows, 8 NCBI type-material rows, 9 checked lineage entries with no missing rows or mismatches, and no retained old NCBI IDs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:132932` resolves in the committed NCBI inventory to label
`Acetobacterium tundrae`, rank `SPECIES`, parent `NCBITaxon:33951`, exact
synonym `Acetobacterium aff. tundrae DSM 9173`, related synonym
`Acetobacterium tundrae Simankova et al. 2001`, genetic code `11`, and
taxonomy snapshot `2026-09-13`. The record carries those same identity fields
and correctly lands in the `bacteria` path bucket through `taxon_domain:
BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:33951` Acetobacterium. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The LPSN name block is supported by `data/raw/lpsn_names.tsv:14828`, including
`lpsn:772532`, the `Acetobacterium tundrae` name, valid publication flags, the
`Simankova et al. 2001` authority, the LPSN URL, three publication IDs,
`INSDC:AJ297449`, and the type-strain designations.

The GTDB mapping is supported by `data/raw/gtdb_mappings.tsv:19161`, which maps
`GTDB:s__Acetobacterium_tundrae` to `NCBITaxon:132932` with predicate
`skos:closeMatch` and `genome_count: 2`. BacDive, GOLD, MediaDive, Madin, and
BactoTraits source-attestation counts all match their corresponding bounded
raw rows.

The seed event is supported by `curation/seed_scope.tsv:2084`, which records
`NCBITaxon:132932` as added on `2026-09-12` with reason `attested rule:
Acetobacterium tundrae, 8 sources incl. NCBI`.

## Completeness

The generated record pulls in all expected source families for the target:
LPSN nomenclature, one GTDB closeMatch, BacDive strains, StrainInfo records,
GOLD organism/project/analysis-derived evidence, MediaDive, Madin, BactoTraits,
BV-BRC, NCBI Assembly, and AllTheBacteria-linked genome or related records.

An ignored-file-inclusive `find` under `reports/yaml_record_review` returned no
existing Markdown report for this stem before this report was written.

## Findings

- Major: `kgmicrobe.strain:bacdive_7537` is marked as a type strain even
  though NCBI explicitly excludes `DSM 917` as type material for
  `NCBITaxon:132932`. The YAML sets `is_type_strain: true` on
  `bacdive_7537`, whose culture IDs include `kgmicrobe.strain:DSM-917`; the
  committed NCBI type-material table lists `DSM 917`, `DSM-917`, `DSM917`, and
  `DSM:917` as `not considered type`, while it lists `DSM 9173` / `DSM:9173`
  as the type strain for this taxon.

- Blocker: 0
- Major: 1
- Minor: 0

## Recommended Edits

Regenerate or patch the upstream strain-merge/type-material logic so
`kgmicrobe.strain:bacdive_7537` / `DSM-917` is not treated as an
`Acetobacterium tundrae` type strain when `data/raw/ncbi_type_material.tsv`
excludes that designation. Keep `kgmicrobe.strain:bacdive_5411` / `DSM-9173`
as the type strain.

## Follow-up Checks

After the source-generation fix, rerun `just validate` and `just
validate-strict` for `data/taxa/bacteria/acetobacterium_tundrae.yaml`, then
re-check the record summary for exactly one retained `Acetobacterium tundrae`
type strain.

## Additional Notes

The exact source scan also found `curation/legacy_page_paths.tsv:15823`; that
is legacy route metadata and does not require a TaxonRecord field.
