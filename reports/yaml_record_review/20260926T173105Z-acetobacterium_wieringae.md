# YAML Record Review: Acetobacterium wieringae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_wieringae.yaml
- Started UTC: 2026-09-26T17:31:05Z
- Finished UTC: 2026-09-26T17:31:05Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_wieringae.yaml` |
| Identifier | `NCBITaxon:52694` |
| Label | `Acetobacterium wieringae` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:33951` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:528684`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_wieringae.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_sp_z.yaml data/taxa/bacteria/acetobacterium_submarinus.yaml data/taxa/bacteria/acetobacterium_tundrae.yaml data/taxa/bacteria/acetobacterium_wieringae.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a dense generated record: 676 YAML lines, 9 lineage entries, 1 LPSN name, 2 GTDB `skos:broadMatch` taxonomy mappings, 1 BacDive strain, 7 genome assemblies, 7 genome records, 30 related records, 2 xrefs, 1 NCBITaxon synonym, and 7 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found the target identifier in seed, legacy-path, NCBI, BacDive, StrainInfo, GOLD, GTDB, MediaDive, BactoTraits, and path rows across the raw, curation, auxiliary, history, and ignored report trees; found `lpsn:772533`, `GTDB:s__Acetobacterium_wieringae`, and `GTDB:s__Acetobacterium_wieringae_A` in the expected LPSN and GTDB raw rows. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:6621`, the LPSN row at `data/raw/lpsn_names.tsv:14829`, 2 GTDB mapping rows at `data/raw/gtdb_mappings.tsv:294939` and `:294940`, 1 BacDive row, 1 GOLD aggregate row covering 8 organisms, 1 MediaDive row, 1 BactoTraits row with 2 assertions, 8 StrainInfo target rows, 11 NCBI type-material rows, 9 checked lineage entries with no missing rows or mismatches, and no retained old NCBI IDs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:52694` resolves in the committed NCBI inventory to label
`Acetobacterium wieringae`, rank `SPECIES`, parent `NCBITaxon:33951`, related
synonym `Acetobacterium wieringae Braun and Gottschalk 1983`, genetic code
`11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:33951` Acetobacterium. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The LPSN name block is supported by `data/raw/lpsn_names.tsv:14829`, including
`lpsn:772533`, the `Acetobacterium wieringae` name, valid publication flags,
the `Braun and Gottschalk 1983` authority, the LPSN URL, DOI publication,
`INSDC:X96955`, and four type-strain designations.

The GTDB broad matches are supported by `data/raw/gtdb_mappings.tsv:294939`
for `GTDB:s__Acetobacterium_wieringae` with `genome_count: 11` and
`data/raw/gtdb_mappings.tsv:294940` for `GTDB:s__Acetobacterium_wieringae_A`
with `genome_count: 1`. Both rows map to `NCBITaxon:52694` with predicate
`skos:broadMatch`, and the primary `GTDB:s__Acetobacterium_wieringae` species
also maps to three non-type NCBI taxa in the raw GTDB table.

BacDive, GOLD, MediaDive, and BactoTraits source-attestation counts all match
their corresponding bounded raw rows. The BacDive type strain and StrainInfo
deposit rows are consistent with the NCBI type-material designations for
`ATCC 43740`, `DSM 1911`, and `JCM 2380`.

The seed event is supported by `curation/seed_scope.tsv:5693`, which records
`NCBITaxon:52694` as added on `2026-09-12` with reason `attested rule:
Acetobacterium wieringae, 7 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated source-rich
record. The generated record pulls in the expected LPSN nomenclature, GTDB
broad matches, BacDive/StrainInfo type-strain evidence, GOLD evidence,
MediaDive, BactoTraits, BV-BRC, NCBI Assembly, and related NCBI/GOLD records
for the target, and the bounded scan found no Madin row or NCBI merge row.

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

The exact source scan also found `curation/legacy_page_paths.tsv:53071`; that
is legacy route metadata and does not require a TaxonRecord field.
