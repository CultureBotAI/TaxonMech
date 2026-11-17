# YAML Record Review: Melanops tulasnei

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/melanops_tulasnei.yaml`
- Started UTC: 2026-09-23T15:14:06Z
- Finished UTC: 2026-09-23T15:14:06Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:371115`
- Label: `Melanops tulasnei`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/melanops_tulasnei.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/melanocarpus_albomyces.yaml data/taxa/eukaryota/melanogaster_broomeanus.yaml data/taxa/eukaryota/melanops_tulasnei.yaml data/taxa/eukaryota/melanospora_tiffanyae.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/melanops_tulasnei.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:77888` contains `NCBITaxon:371115`, label `Melanops tulasnei`, rank `SPECIES`, parent `NCBITaxon:682876`, genetic code `1`, 1 exact synonym, and 2 related synonyms, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:55389` has exactly one scope row for `NCBITaxon:371115`; its rule names `Melanops tulasnei` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:33603` reports `organism_count=1` for `NCBITaxon:371115`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0357143` / `Melanops tulasnei CBS 116805`, with two linked projects and one linked `Melanops tulasnei CBS 116805 Standard Draft` analysis.
- The NCBI type-material inventory has 2 culture-from-epitype rows for `CBS 116805` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:371115`.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:371115`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `melanops_tulasnei` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The committed GOLD aggregate row and the current local native GOLD JSONL exact scan both report one organism row for `NCBITaxon:371115`.
