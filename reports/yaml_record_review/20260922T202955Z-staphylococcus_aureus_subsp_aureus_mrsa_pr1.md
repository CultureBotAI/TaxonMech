# YAML Record Review: Staphylococcus aureus subsp. aureus MRSA_PR1
- Repository: TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_mrsa_pr1.yaml`
- Started UTC: 2026-09-22T20:28:28Z
- Finished UTC: 2026-09-22T20:29:55Z
- Verdict: needs curation

## Target
- Reviewed `NCBITaxon:1004953` / `staphylococcus_aureus_subsp_aureus_mrsa_pr1`.
- The record is a `STRAIN`-rank `BACTERIA` record for `Staphylococcus aureus subsp. aureus MRSA_PR1`.
- Parentage is the seeded NCBI placement under `NCBITaxon:1280` (`Staphylococcus aureus`), with lineage through `Bacillota`, `Bacilli`, `Caryophanales`, `Staphylococcaceae`, and `Staphylococcus`.

## Validation
- `just validate data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_mrsa_pr1.yaml` completed successfully.
- `just validate-strict data/taxa/bacteria/streptococcus_suis_st1.yaml data/taxa/bacteria/streptococcus_suis_d12.yaml data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_mrsa_pr1.yaml data/taxa/bacteria/brucella_suis_bv_1_str_s2.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was not applicable because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `id: NCBITaxon:1004953`, `label: Staphylococcus aureus subsp. aureus MRSA_PR1`, `rank: STRAIN`, `domain: BACTERIA`, `parent: NCBITaxon:1280`, and `genetic_code: 11` match the pinned row in `data/raw/ncbitaxon_taxa.tsv`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon strain.
- The NCBI exact synonyms `Staphylococcus aureus subsp. aureus str. MRSA_PR1` and `Staphylococcus aureus subsp. aureus strain MRSA_PR1` are appropriate for this strain.
- The GTDB-derived exact synonym `Staphylococcus aureus` denotes the species cluster, not the MRSA_PR1 strain itself.

## Evidence
- Local same-taxon source rows for `NCBITaxon:1004953` include `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/madin_taxa.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`.
- `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Staphylococcus_aureus` to this NCBI strain with `skos:closeMatch` and `genome_count: 19502`.
- `data/raw/gold_organisms.tsv` contributes one organism assertion and `data/raw/madin_taxa.tsv` contributes one trait assertion.
- A gitignore-independent `rg --no-ignore --hidden` search over the same local source roots found no same-taxon ATB or StrainInfo rows.

## Completeness
- The record includes the expected NCBITAXON, GTDB, GOLD, and MADIN source attestations from the pinned source rows.
- `strain_count: 0` is consistent with the absence of same-taxon strain inventory rows in the local pinned tables.
- No curation history decision has yet narrowed or removed the GTDB species-cluster mapping on this strain.

## Findings
- Major: `GTDB:s__Staphylococcus_aureus` is a 19,502-genome GTDB species cluster, but the generated YAML projects it onto the single NCBI strain `NCBITaxon:1004953` as a `taxonomy_mappings` entry, an `xrefs` entry, and an `EXACT_SYNONYM` of `Staphylococcus aureus`. The species-level cluster should not be treated as identity-equivalent to the MRSA_PR1 strain.

## Recommended Edits
- Update `data/raw/gtdb_mappings.tsv` generation and the taxonomy-mapping/synonym projection in `src/taxonmech/seed.py` so GTDB species clusters are not emitted as exact synonyms or direct xrefs on NCBI `STRAIN` records.
- Re-seed this record after the guard is in place so `GTDB:s__Staphylococcus_aureus`, `s__Staphylococcus_aureus`, and `Staphylococcus aureus` are removed from `NCBITaxon:1004953` unless a manual curation event records an explicit lower-rank relationship.

## Follow-up Checks
- After the GTDB guard is fixed, confirm the record keeps its NCBI, GOLD, and MADIN attestations while losing the species-cluster synonym and direct GTDB xref.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name *-staphylococcus_aureus_subsp_aureus_mrsa_pr1.md` returned no prior ignored report for this stem.
- Live NCBI and GTDB lookup were not used; local pinned source rows dated `2026-09-13` were treated as the source of truth.
