# YAML Record Review: Macrotyphula juncea

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/macrotyphula_juncea.yaml`
- Started UTC: 2026-09-23T14:06:00Z
- Finished UTC: 2026-09-23T14:10:09Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:139093`
- Label: `Macrotyphula juncea`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/macrotyphula_juncea.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/macrophomina_phaseolina.yaml data/taxa/eukaryota/macrotyphula_juncea.yaml data/taxa/eukaryota/macroventuria_anomochaeta.yaml data/taxa/eukaryota/madagascaria_erythrocladioides.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/macrotyphula_juncea.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:28092` contains `NCBITaxon:139093`, label `Macrotyphula juncea`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 14 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI exact synonym `Clavaria triuncialis var. juncea` plus related synonyms `Clavaria triuncialis var. juncea Alb. & Schwein., 1805` and `Macrotyphula juncea (Alb. & Schwein.) Berthier, 1974` match the YAML `synonyms`.
- `curation/seed_scope.tsv:53999` has exactly one scope row for `NCBITaxon:139093`; its rule names `Macrotyphula juncea` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:9227` reports `organism_count=1` for `NCBITaxon:139093`, matching the YAML `GOLD` attestation.
- The bounded native GOLD scan found no exact organism, project, or analysis rows for this NCBI ID in the retained `data/gold/*.jsonl.gz` catalogs.
- `data/straininfo/records.jsonl.gz` contains 2 exact StrainInfo strain records and 2 exact deposit records for NCBI taxon `139093`, but none joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no NCBI type-material rows, no old merged IDs, and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `macrotyphula_juncea` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The generated GOLD count follows `data/raw/gold_organisms.tsv`; the current native exact GOLD catalog does not contain rows under `ORGANISM NCBI TAX ID = 139093`.
