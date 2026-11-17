# YAML Record Review: Acetobacterium sp. MES1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_sp_mes1.yaml
- Started UTC: 2026-09-26T17:14:42Z
- Finished UTC: 2026-09-26T17:14:42Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_sp_mes1.yaml` |
| Identifier | `NCBITaxon:1899015` |
| Label | `Acetobacterium sp. MES1` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2638182` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:299670`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_sp_mes1.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_sp_ls2.yaml data/taxa/bacteria/acetobacterium_sp_mes1.yaml data/taxa/bacteria/acetobacterium_sp_mic10c02.yaml data/taxa/bacteria/acetobacterium_sp_mic12c01.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected GTDB/MADIN-backed seeded shape: 78 YAML lines, 10 lineage entries, 1 `NCBITAXON`/`NAME`, 1 `GTDB`/`GENOME`, and 1 `MADIN`/`TRAIT_ASSERTION` attestation, 1 `skos:closeMatch` taxonomy mapping, 1 GTDB exact synonym, 1 xref, 0 strains, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in `curation/seed_scope.tsv`, `curation/legacy_page_paths.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, and `data/taxa/PATHS.tsv`; found `GTDB:s__Acetobacterium_wieringae` in `data/raw/gtdb_species.tsv`, LPSN, and all same-species GTDB mappings. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:491901`, the target GTDB mapping at `data/raw/gtdb_mappings.tsv:85891`, 1 MADIN row with `assertion_count: 2`, 10 checked lineage entries with no missing rows or mismatches, and no BacDive, StrainInfo, strain, NCBI type-material, NCBI merged, GOLD, MediaDive, or BactoTraits rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1899015` resolves in the committed NCBI inventory to label
`Acetobacterium sp. MES1`, rank `SPECIES`, parent `NCBITaxon:2638182`,
genetic code `11`, and taxonomy snapshot `2026-09-13`. The record carries
those same identity fields and correctly lands in the `bacteria` path bucket
through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2638182` unclassified
Acetobacterium. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1899015`, source label `Acetobacterium sp. MES1`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB close-match is supported by `data/raw/gtdb_mappings.tsv:85891`, which
maps `GTDB:s__Acetobacterium_wieringae` to `NCBITaxon:1899015` with predicate
`skos:closeMatch` and `genome_count: 11`. The same GTDB species has close
matches to two other unclassified NCBI taxa and a broad match to the LPSN type
species `NCBITaxon:52694`, so this record correctly carries the GTDB species
as a mapping/xref plus exact synonym and not as nomenclature.

The MADIN source attestation is supported by `data/raw/madin_taxa.tsv:18772`,
which records 2 trait assertions for `NCBITaxon:1899015`.

The seed event is supported by `curation/seed_scope.tsv:47994`, which records
`NCBITaxon:1899015` as added on `2026-09-12` with reason `attested rule:
Acetobacterium sp. MES1, 3 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated GTDB/MADIN-backed
record. The bounded scan found no GOLD, BacDive, StrainInfo, normalized strain,
NCBI type-material, MediaDive, or BactoTraits row for this target; the direct
non-NCBI target rows are already summarized by the one GTDB mapping/synonym/xref
and the MADIN `TRAIT_ASSERTION` source attestation.

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

The exact source scan also found `curation/legacy_page_paths.tsv:29886` for
MES1; that is legacy route metadata and does not require a TaxonRecord field.
