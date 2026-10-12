# YAML Record Review: Melanocarpus albomyces

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/melanocarpus_albomyces.yaml`
- Started UTC: 2026-09-23T15:14:06Z
- Finished UTC: 2026-09-23T15:14:06Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:204285`
- Label: `Melanocarpus albomyces`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/melanocarpus_albomyces.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/melanocarpus_albomyces.yaml data/taxa/eukaryota/melanogaster_broomeanus.yaml data/taxa/eukaryota/melanops_tulasnei.yaml data/taxa/eukaryota/melanospora_tiffanyae.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/melanocarpus_albomyces.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Focused StrainInfo JSONL extraction completed for this taxon's 12 exact direct rows and 20 exact deposit rows.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:40324` contains `NCBITaxon:204285`, label `Melanocarpus albomyces`, rank `SPECIES`, parent `NCBITaxon:113631`, genetic code `1`, 2 exact synonyms, and 2 related synonyms, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:54483` has exactly one scope row for `NCBITaxon:204285`; its rule names `Melanocarpus albomyces` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:19372` reports `organism_count=1` for `NCBITaxon:204285`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0020954` / `Melanocarpus albomyces ATCC 16460`, with one linked project and no linked analyses.
- The NCBI type-material inventory has 2 culture-from-type-material rows for `ATCC 16460` variants and 2 type-material rows for `CBS 638.94` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero rows for this taxon in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 12 exact direct rows and 20 exact deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:204285`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `melanocarpus_albomyces` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The committed GOLD aggregate row and the current local native GOLD JSONL exact scan both report one organism row for `NCBITaxon:204285`.
