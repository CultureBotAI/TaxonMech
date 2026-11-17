# YAML Record Review: Fimbriimonas ginsengisoli
- Repository: TaxonMech
- Record: `data/taxa/bacteria/fimbriimonas_ginsengisoli.yaml`
- Started UTC: 2026-09-22T20:33:22Z
- Finished UTC: 2026-09-22T20:37:08Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1005039` / `fimbriimonas_ginsengisoli`.
- The record is a generated `SPECIES`-rank `BACTERIA` record for `Fimbriimonas ginsengisoli` under `NCBITaxon:1005038` (`Fimbriimonas`).
- The record is seeded from NCBI Taxonomy, LPSN, GTDB, BacDive, and linked GOLD evidence.

## Validation
- `just validate data/taxa/bacteria/fimbriimonas_ginsengisoli.yaml` completed successfully.
- `just validate-strict data/taxa/bacteria/flexibacter_sp.yaml data/taxa/bacteria/fimbriimonas_ginsengisoli.yaml data/taxa/bacteria/streptococcus_suis_ss12.yaml data/taxa/bacteria/streptococcus_suis_d9.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005039`, `label: Fimbriimonas ginsengisoli`, `rank: SPECIES`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:1005038`, and `genetic_code: 11` match the exact NCBI source row.
- LPSN name `lpsn:790021` is attached to the same NCBI taxon as a legitimate, validly published, correct `SPECIES` name with authority `Im et al. 2012`, type strain `JCM-17079`, the expected DOI/PMID publication identifiers, and 16S accession `INSDC:GQ339893`.
- The GTDB taxonomy mapping to `GTDB:s__JACOSL01_sp016179045` is a `skos:closeMatch` to a one-genome GTDB species cluster in `data/raw/gtdb_mappings.tsv`.
- The LPSN-provided `GTDB:s__Fimbriimonas_ginsengisoli` value is retained as an `xrefs` item, while the actual GTDB taxonomy mapping follows the local GTDB mapping row to `GTDB:s__JACOSL01_sp016179045`.

## Evidence
- Exact-ID gitignore-independent `rg --no-ignore --hidden` searches across `data/raw`, `data/atb`, and `data/straininfo` found the expected same-taxon rows in `data/raw/ncbitaxon_taxa.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, and `data/raw/ncbi_type_material.tsv`.
- The one BacDive strain entry, `bacdive_161921`, carries the two culture deposits from the BacDive row and is correctly marked as a type strain because its `JCM-17079` deposit matches the LPSN type-strain designation and the local NCBI type-material aliases.
- The GOLD-backed `GCA`, IMG, BioProject, GOLD analysis, GOLD organism, and GOLD project records all stay on descendant taxon `NCBITaxon:661478` (`Fimbriimonas ginsengisoli Gsoil 348`) and preserve the `JCM 17079` organism culture-collection match.
- The exact NCBI row for the descendant `NCBITaxon:661478` was not treated as a same-taxon source row for the species record; it only explains the linked strain-genome evidence classified under that strain.

## Completeness
- `strain_count: 1` equals the single direct BacDive row for `NCBITaxon:1005039`.
- `source_attestations` correctly summarize NCBITAXON, LPSN, GTDB, and BACDIVE evidence, with a one-genome GTDB count and a one-strain BacDive count.
- No MediaDive, BactoTraits, StrainInfo, ATB, or direct NCBI Assembly rows were found for the exact `NCBITaxon:1005039` species ID in the local pinned source search, and those sections are correspondingly absent.

## Findings
- No findings.

## Recommended Edits
- None.

## Follow-up Checks
- None required for this record.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-fimbriimonas_ginsengisoli.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI, LPSN, GTDB, BacDive, and GOLD lookups were not used; pinned local rows in `data/raw/` were treated as the source of truth.
