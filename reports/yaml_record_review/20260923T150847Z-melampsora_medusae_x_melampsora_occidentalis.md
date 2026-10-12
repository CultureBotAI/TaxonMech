# YAML Record Review: Melampsora medusae x Melampsora occidentalis

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/melampsora_medusae_x_melampsora_occidentalis.yaml`
- Started UTC: 2026-09-23T15:08:47Z
- Finished UTC: 2026-09-23T15:08:47Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1195720`
- Label: `Melampsora medusae x Melampsora occidentalis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/melampsora_medusae_x_melampsora_occidentalis.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/melampsora_medusae.yaml data/taxa/eukaryota/melampsora_medusae_x_melampsora_occidentalis.yaml data/taxa/eukaryota/melampsora_occidentalis.yaml data/taxa/eukaryota/melanconium_sp_1_nrrl_54901.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/melampsora_medusae_x_melampsora_occidentalis.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:268887` contains `NCBITaxon:1195720`, label `Melampsora medusae x Melampsora occidentalis`, rank `SPECIES`, parent `NCBITaxon:5260`, genetic code `1`, no exact synonyms, and 3 related synonyms, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:58282` has exactly one scope row for `NCBITaxon:1195720`; its rule names `Melampsora medusae x Melampsora occidentalis` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:4669` reports `organism_count=2` for `NCBITaxon:1195720`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0034307` / `Melampsora x columbiana Clatskanie`, with two linked projects and no linked analyses.
- The direct NCBI type-material inventory scan found no rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:1195720`.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:1195720`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `melampsora_medusae_x_melampsora_occidentalis` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has one exact organism row for `NCBITaxon:1195720` while the committed aggregate GOLD row reports 2; this review did not alter the aggregate inventory.
