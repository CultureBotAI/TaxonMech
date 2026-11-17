# YAML Record Review: Acetothermia bacterium JGI G03_019

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetothermia_bacterium_jgi_g03_019.yaml
- Started UTC: 2026-09-26T18:35:40Z
- Finished UTC: 2026-09-26T18:35:40Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetothermia_bacterium_jgi_g03_019.yaml` |
| Identifier | `NCBITaxon:1448078` |
| Label | `Acetothermia bacterium JGI G03_019` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1046990` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:166796`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetothermia_bacterium_jgi_g03_019.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetothermia_bacterium_jgi_g03_019.yaml data/taxa/bacteria/acetothermia_bacterium_jgi_h02_002.yaml data/taxa/bacteria/acetothermia_bacterium_scgc_aaa255_c06.yaml data/taxa/bacteria/acetothermia_bacterium_uba2187.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected compact NCBITaxon-only shape: 45 YAML lines, 7 lineage entries, 1 `NCBITAXON`/`NAME` attestation, 0 synonyms, 0 taxonomy mappings, 0 strains, 0 xrefs, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:364921`, 1 native compressed GOLD organism with 1 project and 0 analyses, 7 checked lineage entries with no missing rows or mismatches, and no normalized GOLD aggregate, LPSN, GTDB, BacDive, StrainInfo, strain, NCBI type-material, NCBI merged, MediaDive, Madin, or BactoTraits rows for this target. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1448078` resolves in the committed NCBI inventory to label
`Acetothermia bacterium JGI G03_019`, rank `SPECIES`, parent
`NCBITaxon:1046990`, genetic code `11`, and taxonomy snapshot `2026-09-13`.
The record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 7 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:1046990` unclassified
Candidatus Bipolaricaulota. There are no retained old identifiers for this
target in the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1448078`, source label `Acetothermia bacterium JGI G03_019`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The seed event is supported by `curation/seed_scope.tsv:437046`, which records
`NCBITaxon:1448078` as added on `2026-09-13` with reason `attested rule:
Acetothermia bacterium JGI G03_019, 1 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated NCBITaxon-only
record. The bounded scan found this target only in NCBI and seed rows among
normalized sources and found no LPSN, GTDB, BacDive, StrainInfo, normalized
strain, normalized GOLD aggregate, NCBI type-material, MediaDive, Madin, or
BactoTraits row that would support additional sections. The raw compressed
GOLD organism and project rows for this identifier are not represented in the
normalized `data/raw/gold_organisms.tsv` aggregate consumed here.

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
