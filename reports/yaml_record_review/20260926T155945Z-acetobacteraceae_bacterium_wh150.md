# YAML Record Review: Acetobacteraceae bacterium WH150

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacteraceae_bacterium_wh150.yaml
- Started UTC: 2026-09-26T15:59:45Z
- Finished UTC: 2026-09-26T15:59:45Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacteraceae_bacterium_wh150.yaml` |
| Identifier | `NCBITaxon:542299` |
| Label | `Acetobacteraceae bacterium WH150` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:41293` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:534241`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacteraceae_bacterium_wh150.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacteraceae_bacterium_wh145.yaml data/taxa/bacteria/acetobacteraceae_bacterium_wh150.yaml data/taxa/bacteria/acetobacteraceae_bacterium_wx59.yaml data/taxa/bacteria/acetobacterales_bacterium.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected compact shape: 9 lineage entries, 1 `NCBITAXON`/`NAME` attestation, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 definitions, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier or exact label only in the expected `curation/seed_scope.tsv` and `data/raw/ncbitaxon_taxa.tsv` rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:125594`, 9 checked lineage entries with no missing rows or mismatches, and no rows in GTDB, LPSN, BacDive, StrainInfo, strain, NCBI merged, GOLD, MediaDive, Madin, or BactoTraits inputs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:542299` resolves in the committed NCBI inventory to label
`Acetobacteraceae bacterium WH150`, rank `SPECIES`, parent `NCBITaxon:41293`,
genetic code `11`, and taxonomy snapshot `2026-09-13`. The record carries
those same identity fields and correctly lands in the `bacteria` path bucket
through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:41293` unclassified
Acetobacteraceae. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:542299`, source label `Acetobacteraceae bacterium WH150`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The seed event is supported by `curation/seed_scope.tsv:236131`, which records
`NCBITaxon:542299` as added on `2026-09-13` with reason
`attested rule: Acetobacteraceae bacterium WH150, 1 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for the generated NCBITaxon-only
record. The bounded scan found no rows for this target in GTDB, normalized GOLD,
LPSN, BacDive, StrainInfo, strain, NCBI merged, MediaDive, Madin, or
BactoTraits inputs, so the empty taxonomy mapping, nomenclature, strain,
definition, and causal graph sections are consistent with the inspected
normalized sources.

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
