# YAML Record Review: Brucella melitensis bv. 1 str. M5
- Repository: TaxonMech
- Record: `data/taxa/bacteria/brucella_melitensis_bv_1_str_m5.yaml`
- Started UTC: 2026-09-22T20:31:11Z
- Finished UTC: 2026-09-22T20:32:14Z
- Verdict: needs curation

## Target
- Reviewed `NCBITaxon:1004957` / `brucella_melitensis_bv_1_str_m5`.
- The record is a `STRAIN`-rank `BACTERIA` record for `Brucella melitensis bv. 1 str. M5`.
- Parentage is the seeded NCBI placement under `NCBITaxon:644337` (`Brucella melitensis bv. 1`), with lineage through `Pseudomonadota`, `Alphaproteobacteria`, `Hyphomicrobiales`, `Brucellaceae`, `Brucella`, and `Brucella melitensis`.

## Validation
- `just validate data/taxa/bacteria/brucella_melitensis_bv_1_str_m5.yaml` completed successfully.
- `just validate-strict data/taxa/bacteria/brucella_melitensis_bv_1_str_m111.yaml data/taxa/bacteria/brucella_melitensis_bv_1_str_m28_12.yaml data/taxa/bacteria/brucella_melitensis_bv_1_str_m5.yaml data/taxa/bacteria/bacterium_lg.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was not applicable because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `id: NCBITaxon:1004957`, `label: Brucella melitensis bv. 1 str. M5`, `rank: STRAIN`, `domain: BACTERIA`, `parent: NCBITaxon:644337`, and `genetic_code: 11` match the pinned row in `data/raw/ncbitaxon_taxa.tsv`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon strain.
- The NCBI exact synonym `Brucella melitensis bv. 1 strain M5` is appropriate for this strain.
- The GTDB-derived exact synonym `Brucella melitensis` denotes a species cluster, not the biovar 1 M5 strain itself.

## Evidence
- Local same-taxon source rows for `NCBITaxon:1004957` include `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/madin_taxa.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`.
- `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Brucella_melitensis` to this NCBI strain with `skos:closeMatch` and `genome_count: 1337`.
- `data/raw/gold_organisms.tsv` contributes one organism assertion and `data/raw/madin_taxa.tsv` contributes five trait assertions.
- A gitignore-independent `rg --no-ignore --hidden` search over the same local source roots found no same-taxon ATB or StrainInfo rows.

## Completeness
- The record includes the expected NCBITAXON, GTDB, GOLD, and MADIN source attestations from the pinned source rows.
- `strain_count: 0` is consistent with the absence of same-taxon strain inventory rows in the local pinned tables.
- No curation history decision has yet narrowed or removed the GTDB species-cluster mapping on this strain.

## Findings
- Major: `GTDB:s__Brucella_melitensis` is a 1,337-genome GTDB species cluster, but the generated YAML projects it onto the single NCBI strain `NCBITaxon:1004957` as a `taxonomy_mappings` entry, an `xrefs` entry, and an `EXACT_SYNONYM` of `Brucella melitensis`. The species-level cluster should not be treated as identity-equivalent to `Brucella melitensis bv. 1 str. M5`.

## Recommended Edits
- Update `data/raw/gtdb_mappings.tsv` generation and the taxonomy-mapping/synonym projection in `src/taxonmech/seed.py` so GTDB species clusters are not emitted as exact synonyms or direct xrefs on NCBI `STRAIN` records.
- Re-seed this record after the guard is in place so `GTDB:s__Brucella_melitensis`, `s__Brucella_melitensis`, and `Brucella melitensis` are removed from `NCBITaxon:1004957` unless a manual curation event records an explicit lower-rank relationship.

## Follow-up Checks
- After the GTDB guard is fixed, confirm the record keeps its NCBI, GOLD, and MADIN attestations while losing the species-cluster synonym and direct GTDB xref.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name *-brucella_melitensis_bv_1_str_m5.md` returned no prior ignored report for this stem.
- Live NCBI and GTDB lookup were not used; local pinned source rows dated `2026-09-13` were treated as the source of truth.
