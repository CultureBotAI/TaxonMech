# YAML Record Review: Gordonia iterans
- Repository: TaxonMech
- Record: `data/taxa/bacteria/gordonia_iterans.yaml`
- Started UTC: 2026-09-22T20:23:48Z
- Finished UTC: 2026-09-22T20:25:21Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1004901` / `gordonia_iterans`.
- The record is a `SPECIES`-rank `BACTERIA` record for `Gordonia iterans`.
- Parentage is the seeded NCBI placement under `NCBITaxon:2053` (`Gordonia`), with lineage through `Actinomycetota`, `Actinomycetes`, `Mycobacteriales`, and `Gordoniaceae`.

## Validation
- `just validate data/taxa/bacteria/gordonia_iterans.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/gordonia_iterans.yaml data/taxa/bacteria/pedobacter_sp_neau_w8.yaml data/taxa/bacteria/aeromonas_sp_a1_2011.yaml data/taxa/bacteria/aeromonas_sp_a19_2011.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was not applicable because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `id: NCBITaxon:1004901`, `label: Gordonia iterans`, `rank: SPECIES`, `domain: BACTERIA`, `parent: NCBITaxon:2053`, and `genetic_code: 11` match the pinned row in `data/raw/ncbitaxon_taxa.tsv`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon species.
- The three NCBI related synonyms in the record, `Gordonia iterans Kang et al. 2014`, `Gordonia sp. CCUG 60728`, and `Gordonia sp. IFM 10348`, match the related-synonym cell in the pinned NCBI row.
- The LPSN nomenclature entry preserves `lpsn:792201`, the `Gordonia iterans` correct-name status, `Kang et al. 2014` authority, the two DOI references, the PMID, the `INSDC:AB624257` sequence accession, and the LPSN URL.

## Evidence
- Local same-taxon source rows for `NCBITaxon:1004901` include `data/raw/ncbitaxon_taxa.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, `data/straininfo/strain_links.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`.
- `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Gordonia_iterans` to this NCBI species with `skos:closeMatch` and `genome_count: 1`; the YAML carries the matching mapping, GTDB xref, and GTDB source attestation.
- `data/raw/bacdive_strains.tsv` contributes one direct same-taxon BacDive strain, `kgmicrobe.strain:bacdive_168191`, with culture-collection IDs `CCTCC-M2011245`, `IFM%2010348`, and `NCCB-100436`; those three IDs are also present in the NCBI culture-collection table and type-material dump.
- `data/raw/gold_organisms.tsv` contributes one organism assertion for `NCBITaxon:1004901`.

## Completeness
- `strain_count: 1` matches the single direct BacDive strain row for `NCBITaxon:1004901`.
- A StrainInfo `CCUG 60728` link also names `NCBITaxon:1004901`, but its paired BacDive row and the `CCUG-60728` culture-collection row both belong to `NCBITaxon:198437`; it is therefore not an unambiguous same-record strain that should appear beside `bacdive_168191`.
- The record includes all unambiguous NCBITAXON, LPSN, GTDB, BACDIVE, and GOLD source attestations found for this species.

## Findings
- No findings.

## Recommended Edits
- None.

## Follow-up Checks
- None required for this record.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name *-gordonia_iterans.md` returned no prior ignored report for this stem.
- Live NCBI, LPSN, GTDB, BacDive, and StrainInfo lookups were not used; the local pinned rows dated `2026-09-13` were treated as the source of truth.
