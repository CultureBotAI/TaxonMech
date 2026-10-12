# YAML Record Review: Acetomicrobium sp. CY-2

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetomicrobium_sp_cy_2.yaml
- Started UTC: 2026-09-26T17:53:11Z
- Finished UTC: 2026-09-26T17:53:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetomicrobium_sp_cy_2.yaml` |
| Identifier | `NCBITaxon:3238646` |
| Label | `Acetomicrobium sp. CY-2` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2627317` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:438779`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetomicrobium_sp_cy_2.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetomicrobium_sp_cy_2.yaml data/taxa/bacteria/acetomicrobium_sp_enrichment_culture.yaml data/taxa/bacteria/acetomicrobium_sp_enrichment_culture_clone_seq14_clone7ep1_ana.yaml data/taxa/bacteria/acetomicrobium_sp_enrichment_culture_clone_seq3_clone1cp1_ana.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected GTDB closeMatch shape: 73 YAML lines, 10 lineage entries, 1 `skos:closeMatch` taxonomy mapping, 1 exact GTDB synonym, 1 GTDB xref, 1 `NCBITAXON`/`NAME` attestation, 1 `GTDB`/`GENOME` attestation, and 0 strains or causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, and `data/taxa/PATHS.tsv`; also found `GTDB:s__Acetomicrobium_thermoterrenum` in the expected GTDB species/mapping and LPSN rows. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:614583`, 1 GTDB closeMatch row, 10 checked lineage entries with no missing rows or mismatches, and no LPSN, BacDive, StrainInfo, strain, NCBI type-material, NCBI merged, GOLD, MediaDive, Madin, or BactoTraits rows for this target. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:3238646` resolves in the committed NCBI inventory to label
`Acetomicrobium sp. CY-2`, rank `SPECIES`, parent `NCBITaxon:2627317`, genetic
code `11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:2627317` unclassified
Acetomicrobium. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The GTDB mapping is supported by `data/raw/gtdb_mappings.tsv:268614`, which
maps `GTDB:s__Acetomicrobium_thermoterrenum` to this target with predicate
`skos:closeMatch` and `genome_count: 5`.

The seed event is supported by `curation/seed_scope.tsv:126003`, which records
`NCBITaxon:3238646` as added on `2026-09-13` with reason `attested rule:
Acetomicrobium sp. CY-2, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated GTDB-backed
record. The bounded scan found the expected GTDB closeMatch row and no LPSN,
BacDive, StrainInfo, normalized strain, NCBI type-material, GOLD, MediaDive,
Madin, BactoTraits, or NCBI merge row for this target.

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
