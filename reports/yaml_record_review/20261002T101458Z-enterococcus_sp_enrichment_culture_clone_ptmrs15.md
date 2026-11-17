# YAML Record Review: Enterococcus sp. enrichment culture clone PTmrs15

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs15.yaml
- Started UTC: 2026-10-02T10:14:58Z
- Finished UTC: 2026-10-02T10:14:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017190` |
| Label | `Enterococcus sp. enrichment culture clone PTmrs15` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:167971` |
| Parent label | `environmental samples` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` only |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs15.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs14.yaml data/taxa/bacteria/spirosoma_escalantus.yaml data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs15.yaml data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs16.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the generated corpus reproduced exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 54 lines, 10 lineage entries, 0 strains, 0 synonyms, 0 xrefs, and 1 `NCBITAXON` attestation. |
| Direct raw-source and lineage scans for this YAML | Pass: found the expected seed and NCBI rows, confirmed all 10 lineage rows, and found no auxiliary rows for `NCBITaxon:1017190`. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*enterococcus_sp_enrichment_culture_clone_ptmrs15.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1017190)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to `PATHS.tsv`, `seed_scope.tsv`, `ncbitaxon_taxa.tsv`, and this generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10275 maps `NCBITaxon:1017190` to `enterococcus_sp_enrichment_culture_clone_ptmrs15`.
- `curation/seed_scope.tsv` row 319154 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218609 names `NCBITaxon:1017190` as `Enterococcus sp. enrichment culture clone PTmrs15`.
- The YAML identifier, label, rank, parent taxon, and genetic code agree with that raw NCBI row.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a direct NCBI Taxonomy seed.

## Evidence

- The sole source attestation is `NCBITAXON`, `source_id: NCBITaxon:1017190`, `source_label: Enterococcus sp. enrichment culture clone PTmrs15`, `assertion_count: 1`, and `assertion_unit: NAME`.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:167971` / `environmental samples`.
- The generated curation event accurately reports a 2026-09-13 seed from committed inventories.
- No synonym, xref, strain, genome, GOLD, LPSN, GTDB, MADIN, MediaDive, BacDive, AllTheBacteria, StrainInfo, or other auxiliary evidence is asserted.

## Completeness

- The record is complete for a one-source NCBITaxon seed.
- `strain_count: 0` is supported by the direct exact-ID scan over maintained source tables for the exact taxon.
- The raw-source scan found no auxiliary source rows that should have materialized as nomenclature, mappings, strain records, related records, or genome records.
- The scan found no native GOLD organism, project, or analysis rows for this exact taxon.
- No causal graph is expected for this generated taxon-only record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs15.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs15.yaml`.
- Re-run `just verify-corpus`.
- Re-run a bounded or direct exact-ID source scan after any refresh of `data/raw/` or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- `taxonmech_bounded_scan.py` hung on this YAML and was interrupted; this review used direct exact-ID and lineage raw-row checks instead.
- TaxonMech preserves the NCBI placement under `environmental samples`; this review does not infer a named-species placement.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10275 |
| `curation/seed_scope.tsv` | 319154 |
| `data/raw/ncbitaxon_taxa.tsv` | 218609 |
| `data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs15.yaml` | 1 and 43 |

- Direct absence checks covered `data/raw/`, `curation/seed_scope.tsv`, and the generated YAML for `NCBITaxon:1017190`.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs15.yaml`.
- The generated record has no top-level `nomenclature`, `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs15.yaml` directly.
