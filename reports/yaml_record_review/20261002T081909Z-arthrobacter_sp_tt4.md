# YAML Record Review: Arthrobacter sp. TT4

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/arthrobacter_sp_tt4.yaml
- Started UTC: 2026-10-02T08:19:09Z
- Finished UTC: 2026-10-02T08:19:09Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1016963` |
| Label | `Arthrobacter sp. TT4` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:235627` |
| Parent label | `unclassified Arthrobacter` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` only |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/arthrobacter_sp_tt4.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/arthrobacter_sp_pp12.yaml data/taxa/bacteria/arthrobacter_sp_ss14.yaml data/taxa/bacteria/arthrobacter_sp_tt4.yaml data/taxa/bacteria/arthrobacter_sp_wx11.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 53 lines, 10 lineage entries, 0 strains, 0 synonyms, 0 xrefs, and 1 `NCBITAXON` attestation. |
| `taxonmech_bounded_scan.py data/taxa/bacteria/arthrobacter_sp_tt4.yaml` | Pass: found the expected seed and NCBI rows, confirmed 10 lineage rows, and found no native GOLD organism, project, or analysis rows. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*arthrobacter_sp_tt4.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1016963)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to `PATHS.tsv`, `seed_scope.tsv`, `ncbitaxon_taxa.tsv`, and this generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` maps `NCBITaxon:1016963` to `arthrobacter_sp_tt4`.
- `curation/seed_scope.tsv` row 319055 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218491 names `NCBITaxon:1016963` as `Arthrobacter sp. TT4`.
- The YAML identifier, label, rank, parent taxon, and genetic code agree with that raw NCBI row.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a direct NCBI Taxonomy seed.

## Evidence

- The sole source attestation is `NCBITAXON`, `source_id: NCBITaxon:1016963`, `source_label: Arthrobacter sp. TT4`, `assertion_count: 1`, and `assertion_unit: NAME`.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:235627` / `unclassified Arthrobacter`.
- The generated curation event accurately reports a 2026-09-13 seed from committed inventories.
- No synonym, xref, strain, genome, GOLD, LPSN, GTDB, MADIN, MediaDive, BacDive, BactoTraits, or StrainInfo evidence is asserted.

## Completeness

- The record is complete for a one-source NCBITaxon seed.
- `strain_count: 0` is supported by the absence of BacDive and StrainInfo rows for the exact taxon.
- The bounded scan found no auxiliary source rows that should have materialized as nomenclature, mappings, strain records, or related records.
- No causal graph is expected for this generated taxon-only record.
- No empty optional fields are required.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/arthrobacter_sp_tt4.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/arthrobacter_sp_tt4.yaml`.
- Re-run the bounded source scan after any refresh of `data/raw/` or `curation/seed_scope.tsv`.

## Additional Notes

- The source scans used `--no-ignore --hidden`, so ignored files were included.
- The 2026-09-13 NCBI snapshot is the only source named by the raw NCBI row.
- TaxonMech preserves the NCBI placement under `unclassified Arthrobacter`; this review does not infer a named species.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10155 |
| `curation/seed_scope.tsv` | 319055 |
| `data/raw/ncbitaxon_taxa.tsv` | 218491 |
| `data/taxa/bacteria/arthrobacter_sp_tt4.yaml` | 1 and 43 |

- Bounded absence checks covered these generated-data joins:

| Source family | Checked inventory |
|---|---|
| NCBI merges and type material | `data/raw/ncbi_merged_ids.tsv`, `data/raw/ncbi_type_material.tsv` |
| BacDive | `data/raw/bacdive_strains.tsv` |
| GOLD | `data/raw/gold_organisms.tsv` and native organism, project, and analysis tables |
| Auxiliary name and trait sources | GTDB, LPSN, MADIN, MediaDive, and BactoTraits raw tables |
| StrainInfo and strain-genome joins | Culture-collection, assembly, genome-record, and related-record tables |

- The generated record has no top-level `nomenclature`, `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, or `causal_graphs` blocks.
- The review found no maintained upstream row that disagrees with the YAML payload.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/arthrobacter_sp_tt4.yaml` directly.
