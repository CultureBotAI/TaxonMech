# YAML Record Review: Pseudomonas bharatica CSV86

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_bharatica_csv86.yaml
- Started UTC: 2026-09-22T23:11:32Z
- Finished UTC: 2026-09-22T23:11:42Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1005395`
- Label: `Pseudomonas bharatica CSV86`
- Class/rank/domain: `TaxonRecord` / `STRAIN` / `BACTERIA`
- Parent: `NCBITaxon:2692112` / `Pseudomonas bharatica`
- Maintained owner: generated from `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/madin_taxa.tsv`, and `curation/seed_scope.tsv`

The filename is pinned by `data/taxa/PATHS.tsv:1636`, and `curation/seed_scope.tsv:26031` keeps this taxon in scope from the `2026-09-12` rule with 4 attesting sources including NCBI.

## Validation

- `just validate data/taxa/bacteria/pseudomonas_bharatica_csv86.yaml`: passed.
- `just validate-strict data/taxa/bacteria/klebsiella_sp_ok1_1_9_s2.yaml data/taxa/bacteria/ammoniphilus_sp_dim.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_oslo.yaml data/taxa/bacteria/pseudomonas_bharatica_csv86.yaml`: passed; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- `just validate-products`: skipped because this full-corpus graph-label gate has no `causal_graphs` to inspect here.
- `just validate-history`: skipped because this read-only review did not add `history/`.
- `just verify-corpus`: skipped for this report; the earlier full-corpus verifier over 625,960 records was clean, and this review did not edit `data/taxa/`.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:210298` supports the core NCBI identity: `NCBITaxon:1005395`, `Pseudomonas bharatica CSV86`, rank `STRAIN`, parent `NCBITaxon:2692112`, genetic code `11`, exact synonym `Pseudomonas putida CSV86`, `attested_by` = `ncbitaxon|gtdb|gold|madin_etal`, and snapshot `2026-09-13`. The ancestor rows for `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, `Pseudomonadales`, `Pseudomonadaceae`, `Pseudomonas`, and `Pseudomonas bharatica` are present in `data/raw/ncbitaxon_taxa.tsv`. `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the NCBI identity.

`data/raw/gtdb_mappings.tsv:858` maps `GTDB:s__Aquipseudomonas_bharatica` with `genome_count: 6` onto this NCBI strain as `skos:closeMatch`, and `data/raw/gtdb_species.tsv:11049` confirms that the GTDB source row is a species cluster. That GTDB species cluster is broader than strain `CSV86`, so the GTDB mapping, `GTDB` exact synonym `Aquipseudomonas bharatica`, and `xrefs` entry should not be projected as if the species cluster were exact to the strain.

## Evidence

The `NCBITAXON` source attestation and the `Pseudomonas putida CSV86` exact synonym are supported by `data/raw/ncbitaxon_taxa.tsv:210298`. The `GOLD` attestation count of 1 is supported by `data/raw/gold_organisms.tsv:144`, and the `MADIN` trait-assertion count of 3 is supported by `data/raw/madin_taxa.tsv:170`. The `GTDB` attestation count is numerically supported by `data/raw/gtdb_mappings.tsv:858` and `data/raw/gtdb_species.tsv:11049`, but its placement on this record is over-scoped for the narrower NCBI strain target.

## Completeness

- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 -type f '(' -name '*-pseudomonas_bharatica_csv86.md' -o ... ')' -print` probe found no prior report for this stem; `find` includes ignored reports.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/atb` and `data/straininfo` for `NCBITaxon:1005395`, `Pseudomonas bharatica CSV86`, `Pseudomonas putida CSV86`, and `pseudomonas_bharatica_csv86` found no same-taxon auxiliary source rows.
- No BacDive, AllTheBacteria, StrainInfo, or curated causal graph rows were found for this taxon. The main consequential gap is not a missing optional block; it is the over-broad GTDB species projection.

## Findings

- **Major:** `data/raw/gtdb_mappings.tsv:858` maps `GTDB:s__Aquipseudomonas_bharatica` to the NCBI strain `NCBITaxon:1005395` as `skos:closeMatch`. The seeded YAML then promotes the GTDB species to an `xrefs` entry and an `EXACT_SYNONYM` of `Aquipseudomonas bharatica`, which makes a species cluster look exact to strain `CSV86`. Future correction belongs in `data/raw/gtdb_mappings.tsv` generation and the GTDB taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`.

## Recommended Edits

- Stop projecting GTDB species clusters as close matches, `xrefs`, or exact synonyms for NCBI strain records. Regenerate `data/raw/gtdb_mappings.tsv` and reseed `NCBITaxon:1005395` so the GTDB source does not overstate the target scope.

## Follow-up Checks

After fixing the GTDB mapping/projection, rerun `just seed --only NCBITaxon:1005395`, validate the emitted Pseudomonas YAML with `just validate-strict`, run `just verify-corpus`, and confirm that the record no longer contains `GTDB:s__Aquipseudomonas_bharatica` as an exact xref or synonym unless the predicate is demonstrably narrowed to strain `CSV86`.

## Additional Notes

Live NCBI, GTDB, GOLD, and Madin lookups were unavailable; the pinned local `2026-09-13` NCBI/GTDB/GOLD/Madin projections in `data/raw/` are the reviewed source of truth.
