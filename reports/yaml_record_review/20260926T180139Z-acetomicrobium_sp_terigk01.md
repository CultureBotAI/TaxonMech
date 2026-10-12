# YAML Record Review: Acetomicrobium sp. TERIGK01

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetomicrobium_sp_terigk01.yaml
- Started UTC: 2026-09-26T18:01:39Z
- Finished UTC: 2026-09-26T18:01:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetomicrobium_sp_terigk01.yaml` |
| Identifier | `NCBITaxon:467136` |
| Label | `Acetomicrobium sp. TERIGK01` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2627317` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:512341`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetomicrobium_sp_terigk01.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetomicrobium_sp_s15_dsm_107314.yaml data/taxa/bacteria/acetomicrobium_sp_teri_001.yaml data/taxa/bacteria/acetomicrobium_sp_terigk01.yaml data/taxa/bacteria/acetomicrobium_sp_terigk02.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected compact NCBITaxon-only shape: 58 YAML lines, 10 lineage entries, 1 exact NCBITaxon synonym, 1 `NCBITAXON`/`NAME` attestation, 0 taxonomy mappings, 0 strains, 0 xrefs, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier only in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, and `data/taxa/PATHS.tsv` rows across the raw, curation, catalog, BacDive, BV-BRC, GOLD, SeqCode, StrainInfo, ATB, history, and ignored report trees. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:104371`, 10 checked lineage entries with no missing rows or mismatches, and no rows in LPSN, GTDB, BacDive, StrainInfo, strain, NCBI type-material, NCBI merged, GOLD, MediaDive, Madin, or BactoTraits inputs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:467136` resolves in the committed NCBI inventory to label
`Acetomicrobium sp. TERIGK01`, rank `SPECIES`, parent `NCBITaxon:2627317`,
exact synonym `Anaerobaculum sp. TERIGK01`, genetic code `11`, and taxonomy
snapshot `2026-09-13`. The record carries those same identity fields and
correctly lands in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:2627317` unclassified
Acetomicrobium. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:467136`, source label `Acetomicrobium sp. TERIGK01`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The seed event is supported by `curation/seed_scope.tsv:216976`, which records
`NCBITaxon:467136` as added on `2026-09-13` with reason `attested rule:
Acetomicrobium sp. TERIGK01, 1 sources incl. NCBI`.

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
