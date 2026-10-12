# YAML Record Review: Maudiozyma turicensis

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/maudiozyma_turicensis.yaml`
- Started UTC: 2026-09-23T14:54:08Z
- Finished UTC: 2026-09-23T14:54:08Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:432100`
- Label: `Maudiozyma turicensis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/maudiozyma_turicensis.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/maudiozyma_pseudohumilis.yaml data/taxa/eukaryota/maudiozyma_saulgeensis.yaml data/taxa/eukaryota/maudiozyma_serrabonitensis.yaml data/taxa/eukaryota/maudiozyma_turicensis.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/maudiozyma_turicensis.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:95499` contains `NCBITaxon:432100`, label `Maudiozyma turicensis`, rank `SPECIES`, parent `NCBITaxon:3162980`, genetic code `1`, 2 exact synonyms, and 3 related synonyms, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:55634` has exactly one scope row for `NCBITaxon:432100`; its rule names `Maudiozyma turicensis` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:35328` reports `organism_count=2` for `NCBITaxon:432100`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found 2 organism rows, `Go0517017` / `Kazachstania turicensis NRRL Y-48834` and `Go0705567` / `Maudiozyma turicensis NRRL Y-48835`, with one linked project per organism and one linked `Kazachstania turicensis NRRL Y-48834` analysis.
- The NCBI type-material inventory has 6 culture-from-type-material rows for `CBS 8665`, `IFO 10946`, and `NRRL Y-48834` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero rows for this taxon in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 2 exact direct rows and 8 exact deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv:98880` has the side-inventory old ID `NCBITaxon:91644` currently merging into `NCBITaxon:432100`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `maudiozyma_turicensis` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The committed GOLD aggregate row and the current local native GOLD JSONL exact scan both report 2 organism rows for `NCBITaxon:432100`.
