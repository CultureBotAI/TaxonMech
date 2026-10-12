# YAML Record Review: Wolbachia endosymbiont of Sycoscapter moneres

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/wolbachia_endosymbiont_of_sycoscapter_moneres.yaml
- Started UTC: 2026-10-02T09:48:43Z
- Finished UTC: 2026-10-02T09:48:43Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017175` |
| Label | `Wolbachia endosymbiont of Sycoscapter moneres` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2640676` |
| Parent label | `unclassified Wolbachia` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` only |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_sycoscapter_moneres.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/vibrio_sp_bsw21697.yaml data/taxa/bacteria/vibrio_sp_bsw21772.yaml data/taxa/bacteria/vibrio_sp_bsw21773.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_sycoscapter_moneres.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 57 lines, 11 lineage entries, 0 strains, 0 synonyms, 0 xrefs, and 1 `NCBITAXON` attestation. |
| Direct raw-source and lineage scans for this YAML | Pass: found the expected seed and NCBI rows, confirmed all 11 lineage rows, and found no auxiliary rows for `NCBITaxon:1017175`. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*wolbachia_endosymbiont_of_sycoscapter_moneres.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1017175)([^0-9]\|$)' data/raw curation data/taxa/bacteria/wolbachia_endosymbiont_of_sycoscapter_moneres.yaml` | Pass: all checked occurrences trace to `seed_scope.tsv`, `ncbitaxon_taxa.tsv`, and this generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10264 maps `NCBITaxon:1017175` to `wolbachia_endosymbiont_of_sycoscapter_moneres`.
- `curation/seed_scope.tsv` row 319148 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218599 names `NCBITaxon:1017175` as `Wolbachia endosymbiont of Sycoscapter moneres`.
- The YAML identifier, label, rank, parent taxon, and genetic code agree with that raw NCBI row.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a direct NCBI Taxonomy seed.

## Evidence

- The sole source attestation is `NCBITAXON`, `source_id: NCBITaxon:1017175`, `source_label: Wolbachia endosymbiont of Sycoscapter moneres`, `assertion_count: 1`, and `assertion_unit: NAME`.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:2640676` / `unclassified Wolbachia`.
- The generated curation event accurately reports a 2026-09-13 seed from committed inventories.
- No synonym, xref, strain, genome, GOLD, LPSN, GTDB, MADIN, MediaDive, BacDive, BactoTraits, or StrainInfo evidence is asserted.

## Completeness

- The record is complete for a one-source NCBITaxon seed.
- `strain_count: 0` is supported by the direct exact-ID scan over `data/raw/` for the exact taxon.
- The raw-source scan found no auxiliary source rows that should have materialized as nomenclature, mappings, strain records, or related records.
- No causal graph is expected for this generated taxon-only record.
- No empty optional fields are required.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_sycoscapter_moneres.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_sycoscapter_moneres.yaml`.
- Re-run a bounded or direct exact-ID source scan after any refresh of `data/raw/` or `curation/seed_scope.tsv`.

## Additional Notes

- The source scans used `--no-ignore --hidden`, so ignored files were included.
- `taxonmech_bounded_scan.py` hung on this YAML, so this review used direct exact-ID and lineage raw-row checks instead.
- TaxonMech preserves the NCBI placement under `unclassified Wolbachia`; this review does not infer a host-based placement.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10264 |
| `curation/seed_scope.tsv` | 319148 |
| `data/raw/ncbitaxon_taxa.tsv` | 218599 |
| `data/taxa/bacteria/wolbachia_endosymbiont_of_sycoscapter_moneres.yaml` | 1 and 46 |

- Direct absence checks covered `data/raw/`, `curation/seed_scope.tsv`, and the generated YAML for `NCBITaxon:1017175`.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/wolbachia_endosymbiont_of_sycoscapter_moneres.yaml`.
- The generated record has no top-level `nomenclature`, `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, or `causal_graphs` blocks.
- The review found no maintained upstream row that disagrees with the YAML payload.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/wolbachia_endosymbiont_of_sycoscapter_moneres.yaml` directly.
