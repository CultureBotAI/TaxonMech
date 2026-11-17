# YAML Record Review: Maudiozyma serrabonitensis

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/maudiozyma_serrabonitensis.yaml`
- Started UTC: 2026-09-23T14:54:08Z
- Finished UTC: 2026-09-23T14:54:08Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1392788`
- Label: `Maudiozyma serrabonitensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/maudiozyma_serrabonitensis.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/maudiozyma_pseudohumilis.yaml data/taxa/eukaryota/maudiozyma_saulgeensis.yaml data/taxa/eukaryota/maudiozyma_serrabonitensis.yaml data/taxa/eukaryota/maudiozyma_turicensis.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/maudiozyma_serrabonitensis.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:341782` contains `NCBITaxon:1392788`, label `Maudiozyma serrabonitensis`, rank `SPECIES`, parent `NCBITaxon:3162980`, genetic code `1`, 1 exact synonym, and 5 related synonyms, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:59835` has exactly one scope row for `NCBITaxon:1392788`; its rule names `Maudiozyma serrabonitensis` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:9292` reports `organism_count=1` for `NCBITaxon:1392788`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0705711` / `Maudiozyma serrabonitensis UFMG-CM-Y273`, with one linked project and no linked analyses.
- The NCBI type-material inventory has 4 culture-from-type-material rows for `CBS 14236` and `UFMG-CM-Y273` variants, plus 4 holotype rows for `CLIB 1783` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:1392788`.
- `data/raw/ncbi_merged_ids.tsv:28311` and `data/raw/ncbi_merged_ids.tsv:28312` have side-inventory old IDs `NCBITaxon:1789686` and `NCBITaxon:1789687` currently merging into `NCBITaxon:1392788`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `maudiozyma_serrabonitensis` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The committed GOLD aggregate row and the current local native GOLD JSONL exact scan both report one organism row for `NCBITaxon:1392788`.
