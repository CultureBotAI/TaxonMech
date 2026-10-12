# YAML Record Review: Spirosoma escalantus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/spirosoma_escalantus.yaml
- Started UTC: 2026-10-02T10:14:58Z
- Finished UTC: 2026-10-02T10:14:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:101719` |
| Label | `Spirosoma escalantus` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:107` |
| Parent label | `Spirosoma` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `1` |
| Source attestations | `NCBITAXON`, `BACDIVE`, `MEDIADIVE`, `GOLD` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/spirosoma_escalantus.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs14.yaml data/taxa/bacteria/spirosoma_escalantus.yaml data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs15.yaml data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs16.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the generated corpus reproduced exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 168 lines, 11 lineage entries, 1 BacDive strain, 2 NCBITaxon synonyms, 0 xrefs, and 4 source attestations. |
| Direct raw-source and lineage scans for this YAML | Pass: found the expected NCBI, BacDive, MediaDive, GOLD, culture-collection, StrainInfo, and related-record rows; confirmed all 11 lineage rows; and found no LPSN or GTDB rows for `NCBITaxon:101719`. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*spirosoma_escalantus.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(101719)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to the maintained source rows, `PATHS.tsv`, `seed_scope.tsv`, and this generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10274 maps `NCBITaxon:101719` to `spirosoma_escalantus`.
- `curation/seed_scope.tsv` row 21868 keeps this taxon in scope with an attested multi-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17645 names `NCBITaxon:101719` as `Spirosoma escalantus`.
- The YAML identifier, label, rank, parent taxon, synonyms, and genetic code agree with the raw NCBI row.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the directly seeded `NCBITaxon:101719` record.

## Evidence

- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:107` / `Spirosoma`, and each lineage taxon is present in `data/raw/ncbitaxon_taxa.tsv`.
- NCBI contributes the primary name plus the exact synonym `'Spirosoma escalantus'` and related synonym `Spirosoma sp. HDK201`.
- `data/raw/bacdive_strains.tsv` row 55135 contributes `kgmicrobe.strain:bacdive_132824` / `bacdive:132824`, designation `HDK201`, and collection links to `kgmicrobe.strain:ATCC-BAA-766` and `kgmicrobe.strain:DSM-15885`.
- `data/raw/culture_collection_strains.tsv` rows 8057 and 67094 link `ATCC-BAA-766` and `DSM-15885` back to `NCBITaxon:101719`.
- `data/raw/strain_related_records.tsv` rows 72684-72687 attach GOLD organism records `gold:Go0627236` and `gold:Go0627237` through both culture-collection-id and strain-field evidence.
- `data/straininfo/strain_links.tsv` row 13999 attaches StrainInfo strain `397515` and deposit `904149` to `kgmicrobe.strain:DSM-15885`.
- `data/raw/mediadive_taxa.tsv` row 70 supplies the single MediaDive medium assertion.
- `data/raw/gold_organisms.tsv` row 296 supplies the GOLD organism assertion count preserved in `source_attestations`.

## Completeness

- The BacDive strain, two culture collection identifiers, four GOLD relationship rows, and two StrainInfo relationship rows from the maintained inventories are represented in the single generated strain block.
- `strain_count: 1` agrees with the one BacDive strain row for the exact taxon.
- The exact scan found no LPSN or GTDB rows, so no local `nomenclature` or `taxonomy_mappings` blocks are expected.
- No xrefs, genome assemblies, direct genome records, AllTheBacteria rows, or causal graphs are asserted for this generated record.
- The record is complete for its current seeded NCBI, BacDive, MediaDive, GOLD, and StrainInfo evidence.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/spirosoma_escalantus.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/spirosoma_escalantus.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10274 |
| `curation/seed_scope.tsv` | 21868 |
| `data/raw/ncbitaxon_taxa.tsv` | 17645 |
| `data/raw/mediadive_taxa.tsv` | 70 |
| `data/raw/gold_organisms.tsv` | 296 |
| `data/raw/bacdive_strains.tsv` | 55135 |
| `data/raw/culture_collection_strains.tsv` | 8057 and 67094 |
| `data/raw/strain_related_records.tsv` | 72684-72687 |
| `data/straininfo/strain_links.tsv` | 13999 |
| `data/taxa/bacteria/spirosoma_escalantus.yaml` | 1, 42, 52, 60, 122, and 141 |

- Direct absence checks covered `data/`, `curation/`, and the generated YAML for `NCBITaxon:101719`.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/spirosoma_escalantus.yaml`.
- The generated record has no top-level `nomenclature`, `taxonomy_mappings`, `xrefs`, `genomes`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/spirosoma_escalantus.yaml` directly.
