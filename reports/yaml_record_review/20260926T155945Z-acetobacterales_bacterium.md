# YAML Record Review: Acetobacterales bacterium

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterales_bacterium.yaml
- Started UTC: 2026-09-26T15:59:45Z
- Finished UTC: 2026-09-26T15:59:45Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterales_bacterium.yaml` |
| Identifier | `NCBITaxon:3121644` |
| Label | `Acetobacterales bacterium` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:3121643` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:423886`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterales_bacterium.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacteraceae_bacterium_wh145.yaml data/taxa/bacteria/acetobacteraceae_bacterium_wh150.yaml data/taxa/bacteria/acetobacteraceae_bacterium_wx59.yaml data/taxa/bacteria/acetobacterales_bacterium.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected pooled GTDB shape: 8 lineage entries, 1 `NCBITAXON`/`NAME` attestation, 1 `GTDB`/`GENOME` attestation, 10 `skos:broadMatch` GTDB mappings, 0 strains, 0 definitions, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier or exact GTDB IDs in the expected `curation/seed_scope.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, and `data/raw/ncbitaxon_taxa.tsv` rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:601635`, the 10 target GTDB mapping rows at `data/raw/gtdb_mappings.tsv:262397` through `data/raw/gtdb_mappings.tsv:262406`, 8 checked lineage entries with no missing rows or mismatches, and no rows in LPSN, BacDive, StrainInfo, strain, NCBI merged, GOLD, MediaDive, Madin, or BactoTraits inputs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:3121644` resolves in the committed NCBI inventory to label
`Acetobacterales bacterium`, rank `SPECIES`, parent `NCBITaxon:3121643`,
genetic code `11`, and taxonomy snapshot `2026-09-13`. The record carries
those same identity fields and correctly lands in the `bacteria` path bucket
through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 8 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:3121643` unclassified
Acetobacterales. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:3121644`, source label `Acetobacterales bacterium`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The pooled GTDB mapping set is supported by
`data/raw/gtdb_mappings.tsv:262397` through
`data/raw/gtdb_mappings.tsv:262406`, which map 10 GTDB species to
`NCBITaxon:3121644` with predicate `skos:broadMatch` and `genome_count` 1 each:
`GTDB:s__CAIQQQ01_sp038229175`, `GTDB:s__CAMDGX01_sp038331165`,
`GTDB:s__CAMDGX01_sp964201575`, `GTDB:s__Falsiroseomonas_sp038250135`,
`GTDB:s__Humitalea_sp038249305`, `GTDB:s__Humitalea_sp038323655`,
`GTDB:s__JBBDQX01_sp040905765`, `GTDB:s__JBBROS01_sp038229135`,
`GTDB:s__JBBSIT01_sp038231995`, and `GTDB:s__Roseococcus_sp038247025`.

The corresponding species rows are present in `data/raw/gtdb_species.tsv` at
lines 25514, 29259, 29268, 61446, 74468, 74469, 103106, 103597, 103701, and
155852 with matching source IDs, labels, parents, and genome count 1. The
`GTDB` source attestation is the first mapped species, with assertion count 1,
unit `GENOME`, and notes summarizing the 9 additional pooled broad matches.

The seed event is supported by `curation/seed_scope.tsv:121175`, which records
`NCBITaxon:3121644` as added on `2026-09-13` with reason
`attested rule: Acetobacterales bacterium, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for the generated pooled GTDB record.
The bounded scan found no rows for this target in normalized GOLD, LPSN,
BacDive, StrainInfo, strain, NCBI merged, MediaDive, Madin, or BactoTraits
inputs, so the empty nomenclature, strain, definition, and causal graph
sections are consistent with the inspected normalized sources.

The broad GTDB mappings are already represented as taxonomy mappings rather
than synonyms or xrefs, matching the YAML shape for a pooled GTDB record.

The exact ignored-aware source scan found no prior history or ignored review
report mentioning this target before this report was written; ignored files
under `reports/` were included.

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
