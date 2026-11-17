# YAML Record Review: Alteromonas macleodii str. 'Balearic Sea AD45'
- Repository: TaxonMech
- Record: `data/taxa/bacteria/alteromonas_macleodii_str_balearic_sea_ad45.yaml`
- Started UTC: 2026-09-22T20:14:00Z
- Finished UTC: 2026-09-22T20:15:42Z
- Verdict: needs curation

## Target
- Reviewed `NCBITaxon:1004787` / `alteromonas_macleodii_str_balearic_sea_ad45`.
- The record is a `STRAIN`-rank `BACTERIA` record for `Alteromonas macleodii str. 'Balearic Sea AD45'`.
- Parentage is the seeded NCBI placement under `NCBITaxon:28108` (`Alteromonas macleodii`), with lineage through `Pseudomonadota`, `Gammaproteobacteria`, `Alteromonadales`, `Alteromonadaceae`, and `Alteromonas`.

## Validation
- `just validate data/taxa/bacteria/alteromonas_macleodii_str_balearic_sea_ad45.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/alteromonas_mediterranea_de1.yaml data/taxa/bacteria/alteromonas_macleodii_str_balearic_sea_ad45.yaml data/taxa/bacteria/alteromonas_macleodii_str_english_channel_673.yaml data/taxa/bacteria/cytophagales_bacterium_b6.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was not applicable because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `id: NCBITaxon:1004787`, `label: Alteromonas macleodii str. 'Balearic Sea AD45'`, `rank: STRAIN`, `domain: BACTERIA`, `parent: NCBITaxon:28108`, and `genetic_code: 11` match the pinned row in `data/raw/ncbitaxon_taxa.tsv`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon strain.
- The NCBI synonym `Alteromonas macleodii strain 'Balearic Sea AD45'` is appropriate for this strain.
- The GTDB-derived exact synonym `Alteromonas macleodii` denotes the species cluster, not the Balearic Sea AD45 strain itself.

## Evidence
- Local same-taxon source rows for `NCBITaxon:1004787` include `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/madin_taxa.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`.
- `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Alteromonas_macleodii` to this NCBI strain with `skos:closeMatch` and `genome_count: 195`; the same GTDB species also maps to the parent NCBI species `NCBITaxon:28108`.
- `data/raw/gold_organisms.tsv` contributes one organism assertion and `data/raw/madin_taxa.tsv` contributes five trait assertions.
- A gitignore-independent `rg --no-ignore --hidden` search over `data/raw`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv` found no ATB or StrainInfo rows for this exact NCBI taxon.

## Completeness
- The record includes the expected NCBITAXON, GTDB, GOLD, and MADIN source attestations from the pinned source rows.
- `strain_count: 0` is consistent with the absence of same-taxon strain inventory rows in the local pinned tables.
- No curation history decision has yet narrowed or removed the GTDB species-cluster mapping on this strain.

## Findings
- Major: `GTDB:s__Alteromonas_macleodii` is a 195-genome GTDB species cluster, but the generated YAML projects it onto the single NCBI strain `NCBITaxon:1004787` as a `taxonomy_mappings` entry, an `xrefs` entry, and an `EXACT_SYNONYM` of `Alteromonas macleodii`. The species-level cluster should not be treated as identity-equivalent to the Balearic Sea AD45 strain.

## Recommended Edits
- Update `data/raw/gtdb_mappings.tsv` generation and the taxonomy-mapping/synonym projection in `src/taxonmech/seed.py` so GTDB species clusters are not emitted as exact synonyms or direct xrefs on NCBI `STRAIN` records.
- Re-seed this record after the guard is in place so `GTDB:s__Alteromonas_macleodii`, `s__Alteromonas_macleodii`, and `Alteromonas macleodii` are removed from `NCBITaxon:1004787` unless a manual curation event records an explicit lower-rank relationship.

## Follow-up Checks
- After the GTDB guard is fixed, confirm the record keeps its NCBI, GOLD, and MADIN attestations while losing the species-cluster synonym and direct GTDB xref.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name *-alteromonas_macleodii_str_balearic_sea_ad45.md` returned no prior ignored report for this stem.
- Live NCBI and GTDB lookup were not used; local pinned source rows dated `2026-09-13` were treated as the source of truth.
