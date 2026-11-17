# YAML Record Review: Acetobacterium sp. K1/6

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_sp_k1_6.yaml
- Started UTC: 2026-09-26T17:10:53Z
- Finished UTC: 2026-09-26T17:10:53Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_sp_k1_6.yaml` |
| Identifier | `NCBITaxon:3055467` |
| Label | `Acetobacterium sp. K1/6` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2638182` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:413464`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_sp_k1_6.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_sp_hawd4.yaml data/taxa/bacteria/acetobacterium_sp_k1_6.yaml data/taxa/bacteria/acetobacterium_sp_kb_1.yaml data/taxa/bacteria/acetobacterium_sp_ls1.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected GTDB-backed seeded shape: 73 YAML lines, 10 lineage entries, 1 `NCBITAXON`/`NAME` attestation, 1 `GTDB`/`GENOME` attestation, 1 `skos:closeMatch` taxonomy mapping, 1 GTDB exact synonym, 1 xref, 0 strains, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, and `data/taxa/PATHS.tsv`; found `GTDB:s__Acetobacterium_carbinolicum` in `data/raw/gtdb_species.tsv`, LPSN, all five same-species GTDB mappings, and prior ignored review notes. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:590948`, the target GTDB mapping at `data/raw/gtdb_mappings.tsv:253600`, 10 checked lineage entries with no missing rows or mismatches, and no BacDive, StrainInfo, strain, NCBI type-material, NCBI merged, GOLD, MediaDive, Madin, or BactoTraits rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:3055467` resolves in the committed NCBI inventory to label
`Acetobacterium sp. K1/6`, rank `SPECIES`, parent `NCBITaxon:2638182`,
genetic code `11`, and taxonomy snapshot `2026-09-13`. The record carries
those same identity fields and correctly lands in the `bacteria` path bucket
through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2638182` unclassified
Acetobacterium. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:3055467`, source label `Acetobacterium sp. K1/6`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB close-match is supported by `data/raw/gtdb_mappings.tsv:253600`,
which maps `GTDB:s__Acetobacterium_carbinolicum` to `NCBITaxon:3055467` with
predicate `skos:closeMatch` and `genome_count: 6`. The same GTDB species has
five total NCBI mappings in the raw table and an LPSN row for the type species
`NCBITaxon:52690`, so this record correctly carries the GTDB species as a
mapping/xref plus exact synonym and not as nomenclature.

The seed event is supported by `curation/seed_scope.tsv:117835`, which records
`NCBITaxon:3055467` as added on `2026-09-13` with reason `attested rule:
Acetobacterium sp. K1/6, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated GTDB-backed
record. The bounded scan found no GOLD, BacDive, StrainInfo, normalized strain,
NCBI type-material, MediaDive, Madin, or BactoTraits row for this target, and
the only direct non-NCBI target row was the one GTDB closeMatch already present
as the taxonomy mapping, exact synonym, xref, and GTDB source attestation.

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
