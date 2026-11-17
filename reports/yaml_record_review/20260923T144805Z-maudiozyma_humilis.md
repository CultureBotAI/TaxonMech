# YAML Record Review: Maudiozyma humilis

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/maudiozyma_humilis.yaml`
- Started UTC: 2026-09-23T14:45:00Z
- Finished UTC: 2026-09-23T14:48:05Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:51915`
- Label: `Maudiozyma humilis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/maudiozyma_humilis.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/maudiozyma_barnettii.yaml data/taxa/eukaryota/maudiozyma_bulderi.yaml data/taxa/eukaryota/maudiozyma_exigua.yaml data/taxa/eukaryota/maudiozyma_humilis.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/maudiozyma_humilis.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:6525` contains `NCBITaxon:51915`, label `Maudiozyma humilis`, rank `SPECIES`, parent `NCBITaxon:3162980`, genetic code `1`, 4 exact synonyms, and 5 related synonyms, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:52842` has exactly one scope row for `NCBITaxon:51915`; its rule names `Maudiozyma humilis` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:37683` reports `organism_count=3` for `NCBITaxon:51915`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found 2 organism rows, `Go0705259` / `Maudiozyma humilis NRRL Y-17074` and `Go0705624` / `Maudiozyma humilis NRRL Y-7245`, with one linked project per organism and no linked analyses.
- The NCBI type-material inventory has 14 culture-from-holotype rows for `Candida milleri` variants and 18 culture-from-type-material rows for `Torulopsis humilis` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 39 exact direct rows and 77 deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv` has 2 side-inventory old IDs, `NCBITaxon:1903128` and `NCBITaxon:58625`, that currently merge into `NCBITaxon:51915`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `maudiozyma_humilis` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has 2 exact organism rows for `NCBITaxon:51915` while the committed aggregate GOLD row reports 3; this review did not alter the aggregate inventory.
