# YAML Record Review: Acetobacterium sp. enrichment culture

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_sp_enrichment_culture.yaml
- Started UTC: 2026-09-26T16:17:08Z
- Finished UTC: 2026-09-26T16:17:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_sp_enrichment_culture.yaml` |
| Identifier | `NCBITaxon:1756343` |
| Label | `Acetobacterium sp. enrichment culture` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:97900` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:264922`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_sp_enrichment_culture.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_sp_bmc07.yaml data/taxa/bacteria/acetobacterium_sp_enrichment_culture.yaml data/taxa/bacteria/acetobacterium_sp_enrichment_culture_clone_06_1235251_102.yaml data/taxa/bacteria/acetobacterium_sp_enrichment_culture_clone_06_1235251_105.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected compact NCBITaxon-only shape: 54 YAML lines, 10 lineage entries, 1 `NCBITAXON`/`NAME` attestation, 0 synonyms, 0 taxonomy mappings, 0 strains, 0 xrefs, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, and `data/taxa/PATHS.tsv` rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:458376`, 10 checked lineage entries with no missing rows or mismatches, and no rows in LPSN, GTDB, BacDive, StrainInfo, strain, NCBI type-material, NCBI merged, GOLD, MediaDive, Madin, or BactoTraits inputs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1756343` resolves in the committed NCBI inventory to label
`Acetobacterium sp. enrichment culture`, rank `SPECIES`, parent
`NCBITaxon:97900`, genetic code `11`, and taxonomy snapshot `2026-09-13`. The
record carries those same identity fields and correctly lands in the `bacteria`
path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:97900` environmental samples.
There are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1756343`, source label `Acetobacterium sp. enrichment culture`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The seed event is supported by `curation/seed_scope.tsv:520947`, which records
`NCBITaxon:1756343` as added on `2026-09-13` with reason
`attested rule: Acetobacterium sp. enrichment culture, 1 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated NCBITaxon-only
record. The bounded scan found this target only in NCBI and seed rows and
found no LPSN, GTDB, BacDive, StrainInfo, normalized strain, NCBI
type-material, GOLD, MediaDive, Madin, or BactoTraits row that would support
additional nomenclature, mapping, strain, xref, definition, genome, or causal
graph sections.

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
