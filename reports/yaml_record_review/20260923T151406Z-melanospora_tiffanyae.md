# YAML Record Review: Melanospora tiffanyae

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/melanospora_tiffanyae.yaml`
- Started UTC: 2026-09-23T15:14:06Z
- Finished UTC: 2026-09-23T15:14:06Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:2038071`
- Label: `Melanospora tiffanyae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/melanospora_tiffanyae.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/melanocarpus_albomyces.yaml data/taxa/eukaryota/melanogaster_broomeanus.yaml data/taxa/eukaryota/melanops_tulasnei.yaml data/taxa/eukaryota/melanospora_tiffanyae.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/melanospora_tiffanyae.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Complete native GOLD exact scans extracted 2 organism rows, 16 linked project rows, and 0 linked analysis rows for this taxon.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:512871` contains `NCBITaxon:2038071`, label `Melanospora tiffanyae`, rank `SPECIES`, parent `NCBITaxon:40615`, genetic code `1`, 1 exact synonym, and no related synonyms, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:62129` has exactly one scope row for `NCBITaxon:2038071`; its rule names `Melanospora tiffanyae` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:19276` reports `organism_count=4` for `NCBITaxon:2038071`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found 2 organism rows, `Go0039164` and `Go0385300`, both labeled `Melanospora tiffanyae F1KG0001`; the complete join found 16 linked projects and no linked analyses.
- The direct NCBI type-material inventory scan found no rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero rows for this taxon in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 1 exact direct row and 2 exact deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv:18995` has the side-inventory old ID `NCBITaxon:152779` currently merging into `NCBITaxon:2038071`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `melanospora_tiffanyae` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has 2 exact organism rows for `NCBITaxon:2038071` while the committed aggregate GOLD row reports 4; this review did not alter the aggregate inventory.
