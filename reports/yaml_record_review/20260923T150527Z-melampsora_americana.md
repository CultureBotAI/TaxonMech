# YAML Record Review: Melampsora americana

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/melampsora_americana.yaml`
- Started UTC: 2026-09-23T15:05:27Z
- Finished UTC: 2026-09-23T15:05:27Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:2182807`
- Label: `Melampsora americana`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/melampsora_americana.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/melampsora_americana.yaml data/taxa/eukaryota/melampsora_larici_populina_98ag31.yaml data/taxa/eukaryota/melampsora_laricis_populina.yaml data/taxa/eukaryota/melampsora_lini.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/melampsora_americana.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:520981` contains `NCBITaxon:2182807`, label `Melampsora americana`, rank `SPECIES`, parent `NCBITaxon:5260`, genetic code `1`, no exact synonyms, and 1 related synonym, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:62458` has exactly one scope row for `NCBITaxon:2182807`; its rule names `Melampsora americana` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:20797` reports `organism_count=1` for `NCBITaxon:2182807`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0367767` / `Melampsora americana R15-033-03`, with two linked projects and one linked `Melampsora Americana R15-033-03 Standard Draft` analysis.
- The direct NCBI type-material inventory scan found no rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:2182807`.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:2182807`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `melampsora_americana` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The committed GOLD aggregate row and the current local native GOLD JSONL exact scan both report one organism row for `NCBITaxon:2182807`.
