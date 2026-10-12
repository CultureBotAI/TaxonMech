# YAML Record Review: Achromobacter sp. GbtcB20

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_sp_gbtcb20.yaml
- Started UTC: 2026-09-27T06:32:53Z
- Finished UTC: 2026-09-27T06:32:53Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_sp_gbtcb20.yaml` |
| Identifier | `NCBITaxon:2824765` |
| Label | `Achromobacter sp. GbtcB20` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2626865` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

This generated seeded record comes from NCBI and GTDB inputs. Its path is
pinned by `data/taxa/PATHS.tsv:381390`; all seeded fields are owned by the
seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_sp_gbtcb20.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_sp_gb72.yaml data/taxa/bacteria/achromobacter_sp_gbtcb20.yaml data/taxa/bacteria/achromobacter_sp_gcr1.yaml data/taxa/bacteria/achromobacter_sp_gd03932.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected GTDB-backed seeded shape: 73 YAML lines, 10 lineage entries, 1 `NCBITAXON`/`NAME` attestation, 1 `GTDB`/`GENOME` attestation, 1 `skos:closeMatch` taxonomy mapping, 1 GTDB exact synonym, 1 xref, 0 strains, and 0 causal graphs. |
| Boundary-guarded exact ID-only local scan | Found this identifier in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:561213`, the target GTDB mapping at `data/raw/gtdb_mappings.tsv:223182`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, no native GOLD organism, project, or analysis rows, and no BacDive, StrainInfo, strain, NCBI type-material, LPSN, GOLD aggregate, MediaDive, MADIN, or BactoTraits rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:2824765` resolves in the committed NCBI inventory to label
`Achromobacter sp. GbtcB20`, rank `SPECIES`, parent `NCBITaxon:2626865`,
genetic code `11`, source set `ncbitaxon|gtdb`, and taxonomy snapshot
`2026-09-13`. The record carries those same identity fields and correctly lands
in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2626865` unclassified
Achromobacter. The bounded scan found no NCBI merge row and no retained old-id
row that would change the active identifier.

## Evidence

The raw NCBI row supports the `NCBITAXON` attestation: source ID
`NCBITaxon:2824765`, label `Achromobacter sp. GbtcB20`, snapshot `2026-09-13`.

The GTDB close-match is supported by `data/raw/gtdb_mappings.tsv:223182`, which
maps `GTDB:s__Achromobacter_mucicolens` to `NCBITaxon:2824765` with predicate
`skos:closeMatch` and `genome_count: 44`. The generated taxonomy mapping, GTDB
xref, exact synonym `Achromobacter mucicolens`, and 44-genome GTDB source
attestation exactly reflect that row.

The seed event is supported by `curation/seed_scope.tsv:105541`, which records
`NCBITaxon:2824765` as added on `2026-09-13` with reason `attested rule:
Achromobacter sp. GbtcB20, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated GTDB-backed record.
The exact and bounded scans account for the expected NCBI, GTDB, seed, path,
and generated YAML inputs, and found no omitted NCBI merge, NCBI type-material,
LPSN, GOLD, BacDive, MediaDive, MADIN, BactoTraits, StrainInfo, ATB,
culture-collection, normalized strain, normalized assembly, normalized genome,
normalized related-record, or StrainInfo exclusion row for this taxon.

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

This was a read-only generated-record review; it did not edit YAML or inputs.
