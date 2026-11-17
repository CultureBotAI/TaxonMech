# YAML Record Review: Acetobacteraceae bacterium W1.09-37

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacteraceae_bacterium_w1_09_37.yaml
- Started UTC: 2026-09-26T15:54:56Z
- Finished UTC: 2026-09-26T15:54:56Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacteraceae_bacterium_w1_09_37.yaml` |
| Identifier | `NCBITaxon:1341547` |
| Label | `Acetobacteraceae bacterium W1.09-37` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:41293` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:121730`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacteraceae_bacterium_w1_09_37.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacteraceae_bacterium_uba6159.yaml data/taxa/bacteria/acetobacteraceae_bacterium_w1_09_37.yaml data/taxa/bacteria/acetobacteraceae_bacterium_wh141.yaml data/taxa/bacteria/acetobacteraceae_bacterium_wh144.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected compact shape: 9 lineage entries, 1 `NCBITAXON`/`NAME` attestation, 0 taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 definitions, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier or exact label only in the expected `curation/seed_scope.tsv` and `data/raw/ncbitaxon_taxa.tsv` rows across `data/raw`, `curation`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `history`, and ignored `reports`. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the matching NCBI row at `data/raw/ncbitaxon_taxa.tsv:322435`, 9 checked lineage entries with no missing rows or mismatches, and no rows in GTDB, LPSN, BacDive, StrainInfo, strain, NCBI merged, GOLD, MediaDive, Madin, or BactoTraits inputs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1341547` resolves in the committed NCBI inventory to label
`Acetobacteraceae bacterium W1.09-37`, rank `SPECIES`, parent
`NCBITaxon:41293`, genetic code `11`, and taxonomy snapshot `2026-09-13`. The
record carries those same identity fields and correctly lands in the `bacteria`
path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:41293` unclassified
Acetobacteraceae. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1341547`, source label `Acetobacteraceae bacterium W1.09-37`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The seed event is supported by `curation/seed_scope.tsv:404885`, which records
`NCBITaxon:1341547` as added on `2026-09-13` with reason
`attested rule: Acetobacteraceae bacterium W1.09-37, 1 sources incl. NCBI`.

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
