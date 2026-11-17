# YAML Record Review: Streptococcus suis ST1
- Repository: TaxonMech
- Record: `data/taxa/bacteria/streptococcus_suis_st1.yaml`
- Started UTC: 2026-09-22T20:28:28Z
- Finished UTC: 2026-09-22T20:29:55Z
- Verdict: needs curation

## Target
- Reviewed `NCBITaxon:1004951` / `streptococcus_suis_st1`.
- The record is a `STRAIN`-rank `BACTERIA` record for `Streptococcus suis ST1`.
- Parentage is the seeded NCBI placement under `NCBITaxon:1307` (`Streptococcus suis`), with lineage through `Bacillota`, `Bacilli`, `Lactobacillales`, `Streptococcaceae`, and `Streptococcus`.

## Validation
- `just validate data/taxa/bacteria/streptococcus_suis_st1.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/streptococcus_suis_st1.yaml data/taxa/bacteria/streptococcus_suis_d12.yaml data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_mrsa_pr1.yaml data/taxa/bacteria/brucella_suis_bv_1_str_s2.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was not applicable because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `id: NCBITaxon:1004951`, `label: Streptococcus suis ST1`, `rank: STRAIN`, `domain: BACTERIA`, `parent: NCBITaxon:1307`, and `genetic_code: 11` match the pinned row in `data/raw/ncbitaxon_taxa.tsv`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon strain.
- The NCBI exact synonyms `Streptococcus suis str. ST1` and `Streptococcus suis strain ST1` are appropriate for this strain.
- The GTDB-derived exact synonym `Streptococcus suis` denotes the species cluster, not strain ST1 itself.

## Evidence
- Local same-taxon source rows for `NCBITaxon:1004951` include `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`.
- `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Streptococcus_suis` to this NCBI strain with `skos:closeMatch` and `genome_count: 2003`.
- `data/raw/madin_taxa.tsv` contributes one trait assertion.
- A gitignore-independent `rg --no-ignore --hidden` search over `data/raw`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv` found no same-taxon ATB, GOLD, or StrainInfo rows.

## Completeness
- The record includes the expected NCBITAXON, GTDB, and MADIN source attestations from the pinned source rows.
- `strain_count: 0` is consistent with the absence of same-taxon strain inventory rows in the local pinned tables.
- No curation history decision has yet narrowed or removed the GTDB species-cluster mapping on this strain.

## Findings
- Major: `GTDB:s__Streptococcus_suis` is a 2,003-genome GTDB species cluster, but the generated YAML projects it onto the single NCBI strain `NCBITaxon:1004951` as a `taxonomy_mappings` entry, an `xrefs` entry, and an `EXACT_SYNONYM` of `Streptococcus suis`. The species-level cluster should not be treated as identity-equivalent to the ST1 strain.

## Recommended Edits
- Update `data/raw/gtdb_mappings.tsv` generation and the taxonomy-mapping/synonym projection in `src/taxonmech/seed.py` so GTDB species clusters are not emitted as exact synonyms or direct xrefs on NCBI `STRAIN` records.
- Re-seed this record after the guard is in place so `GTDB:s__Streptococcus_suis`, `s__Streptococcus_suis`, and `Streptococcus suis` are removed from `NCBITaxon:1004951` unless a manual curation event records an explicit lower-rank relationship.

## Follow-up Checks
- After the GTDB guard is fixed, confirm the record keeps its NCBI and MADIN attestations while losing the species-cluster synonym and direct GTDB xref.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name *-streptococcus_suis_st1.md` returned no prior ignored report for this stem.
- Live NCBI and GTDB lookup were not used; local pinned source rows dated `2026-09-13` were treated as the source of truth.
