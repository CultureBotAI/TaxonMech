# YAML Record Review: Salmonella enterica subsp. enterica serovar Oslo

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_oslo.yaml
- Started UTC: 2026-09-22T23:11:32Z
- Finished UTC: 2026-09-22T23:11:41Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1005394`
- Label: `Salmonella enterica subsp. enterica serovar Oslo`
- Class/rank/domain: `TaxonRecord` / `NO_RANK` / `BACTERIA`
- Parent: `NCBITaxon:59201` / `Salmonella enterica subsp. enterica`
- Maintained owner: generated from `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gold_organisms.tsv`, and `curation/seed_scope.tsv`

The filename is pinned by `data/taxa/PATHS.tsv:1635`, and `curation/seed_scope.tsv:35901` keeps this taxon in scope from the `2026-09-12` rule with 3 attesting sources including NCBI.

## Validation

- `just validate data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_oslo.yaml`: passed.
- `just validate-strict data/taxa/bacteria/klebsiella_sp_ok1_1_9_s2.yaml data/taxa/bacteria/ammoniphilus_sp_dim.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_oslo.yaml data/taxa/bacteria/pseudomonas_bharatica_csv86.yaml`: passed; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- `just validate-products`: skipped because this full-corpus graph-label gate has no `causal_graphs` to inspect here.
- `just validate-history`: skipped because this read-only review did not add `history/`.
- `just verify-corpus`: skipped for this report; the earlier full-corpus verifier over 625,960 records was clean, and this review did not edit `data/taxa/`.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:210297` supports the core NCBI identity: `NCBITaxon:1005394`, `Salmonella enterica subsp. enterica serovar Oslo`, rank `NO_RANK`, parent `NCBITaxon:59201`, genetic code `11`, `attested_by` = `ncbitaxon|gtdb|gold`, and snapshot `2026-09-13`. The ancestor rows for `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, `Enterobacterales`, `Enterobacteriaceae`, `Salmonella`, `Salmonella enterica`, and `Salmonella enterica subsp. enterica` are present in `data/raw/ncbitaxon_taxa.tsv`. `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the NCBI identity.

`data/raw/gtdb_mappings.tsv:857` maps `GTDB:s__Salmonella_enterica` with `genome_count: 21527` onto this no-rank NCBI serovar as `skos:closeMatch`, and `data/raw/gtdb_species.tsv:163163` confirms that the GTDB source row is the species cluster `s__Salmonella_enterica`. That GTDB species cluster is broader than the serovar-specific NCBI target, so the GTDB mapping, `GTDB` exact synonym `Salmonella enterica`, and `xrefs` entry should not be projected as if the species cluster were exact to serovar Oslo.

## Evidence

The `NCBITAXON` source attestation is supported by `data/raw/ncbitaxon_taxa.tsv:210297`, and the `GOLD` attestation count of 4 is supported by `data/raw/gold_organisms.tsv:143`. The `GTDB` attestation count is numerically supported by `data/raw/gtdb_mappings.tsv:857` and `data/raw/gtdb_species.tsv:163163`, but its placement on this record is over-scoped for the narrower no-rank serovar target.

## Completeness

- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 -type f '(' -name '*-salmonella_enterica_subsp_enterica_serovar_oslo.md' -o ... ')' -print` probe found no prior report for this stem; `find` includes ignored reports.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/atb` and `data/straininfo` for `NCBITaxon:1005394`, `Salmonella enterica subsp. enterica serovar Oslo`, and `salmonella_enterica_subsp_enterica_serovar_oslo` found no same-taxon auxiliary source rows.
- No BacDive, AllTheBacteria, StrainInfo, or curated causal graph rows were found for this taxon. The main consequential gap is not a missing optional block; it is the over-broad GTDB species projection.

## Findings

- **Major:** `data/raw/gtdb_mappings.tsv:857` maps `GTDB:s__Salmonella_enterica` to the no-rank serovar `NCBITaxon:1005394` as `skos:closeMatch`. The seeded YAML then promotes the GTDB species to an `xrefs` entry and an `EXACT_SYNONYM` of `Salmonella enterica`, which makes a species cluster look exact to the narrower serovar. Future correction belongs in `data/raw/gtdb_mappings.tsv` generation and the GTDB taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`.

## Recommended Edits

- Stop projecting GTDB species clusters as close matches, `xrefs`, or exact synonyms for NCBI serovar/no-rank descendants of that species. Regenerate `data/raw/gtdb_mappings.tsv` and reseed `NCBITaxon:1005394` so the GTDB source does not overstate the target scope.

## Follow-up Checks

After fixing the GTDB mapping/projection, rerun `just seed --only NCBITaxon:1005394`, validate the emitted Salmonella YAML with `just validate-strict`, run `just verify-corpus`, and confirm that the record no longer contains `GTDB:s__Salmonella_enterica` as an exact xref or synonym unless the predicate is demonstrably narrowed to the serovar target.

## Additional Notes

Live NCBI, GTDB, and GOLD lookups were unavailable; the pinned local `2026-09-13` NCBI/GTDB/GOLD projections in `data/raw/` are the reviewed source of truth.
