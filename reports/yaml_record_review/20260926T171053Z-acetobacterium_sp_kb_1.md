# YAML Record Review: Acetobacterium sp. KB-1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_sp_kb_1.yaml
- Started UTC: 2026-09-26T17:10:53Z
- Finished UTC: 2026-09-26T17:10:53Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_sp_kb_1.yaml` |
| Identifier | `NCBITaxon:2184575` |
| Label | `Acetobacterium sp. KB-1` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2638182` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:332752`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_sp_kb_1.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_sp_hawd4.yaml data/taxa/bacteria/acetobacterium_sp_k1_6.yaml data/taxa/bacteria/acetobacterium_sp_kb_1.yaml data/taxa/bacteria/acetobacterium_sp_ls1.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected GTDB/GOLD-backed seeded shape: 78 YAML lines, 10 lineage entries, 1 `NCBITAXON`/`NAME`, 1 `GTDB`/`GENOME`, and 1 `GOLD`/`ORGANISM` attestation, 1 `skos:closeMatch` taxonomy mapping, 1 GTDB exact synonym, 1 xref, 0 strains, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in `curation/seed_scope.tsv`, `curation/legacy_page_paths.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/gtdb_mappings.tsv`, and `data/taxa/PATHS.tsv`; found `GTDB:s__Acetobacterium_carbinolicum` in `data/raw/gtdb_species.tsv`, LPSN, all five same-species GTDB mappings, and prior ignored review notes. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:521207`, the target GTDB mapping at `data/raw/gtdb_mappings.tsv:171793`, 1 GOLD aggregate row, one native GOLD organism/project/analysis chain, 10 checked lineage entries with no missing rows or mismatches, and no BacDive, StrainInfo, strain, NCBI type-material, NCBI merged, MediaDive, Madin, or BactoTraits rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:2184575` resolves in the committed NCBI inventory to label
`Acetobacterium sp. KB-1`, rank `SPECIES`, parent `NCBITaxon:2638182`,
genetic code `11`, and taxonomy snapshot `2026-09-13`. The record carries
those same identity fields and correctly lands in the `bacteria` path bucket
through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2638182` unclassified
Acetobacterium. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:2184575`, source label `Acetobacterium sp. KB-1`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB close-match is supported by `data/raw/gtdb_mappings.tsv:171793`,
which maps `GTDB:s__Acetobacterium_carbinolicum` to `NCBITaxon:2184575` with
predicate `skos:closeMatch` and `genome_count: 6`. The same GTDB species has
five total NCBI mappings in the raw table and an LPSN row for the type species
`NCBITaxon:52690`, so this record correctly carries the GTDB species as a
mapping/xref plus exact synonym and not as nomenclature.

The GOLD attestation is supported by `data/raw/gold_organisms.tsv:20827` and
the native GOLD chain: organism `Go0552264` on line 390543, project
`Gp0504565` on line 364278, and analysis `Acetobacterium sp. KB-1 KB-1` on
line 285647.

The seed event is supported by `curation/seed_scope.tsv:48695`, which records
`NCBITaxon:2184575` as added on `2026-09-12` with reason `attested rule:
Acetobacterium sp. KB-1, 3 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated GTDB/GOLD-backed
record. The bounded scan found no BacDive, StrainInfo, normalized strain, NCBI
type-material, MediaDive, Madin, or BactoTraits row for this target; the direct
non-NCBI target rows are already summarized by the one GTDB mapping/synonym/xref
and the GOLD `ORGANISM` source attestation.

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

The exact source scan also found `curation/legacy_page_paths.tsv:33920` for
KB-1; that is legacy route metadata and does not require a TaxonRecord field.
