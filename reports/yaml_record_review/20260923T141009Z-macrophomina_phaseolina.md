# YAML Record Review: Macrophomina phaseolina

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/macrophomina_phaseolina.yaml`
- Started UTC: 2026-09-23T14:06:00Z
- Finished UTC: 2026-09-23T14:10:09Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:35725`
- Label: `Macrophomina phaseolina`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/macrophomina_phaseolina.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/macrophomina_phaseolina.yaml data/taxa/eukaryota/macrotyphula_juncea.yaml data/taxa/eukaryota/macroventuria_anomochaeta.yaml data/taxa/eukaryota/madagascaria_erythrocladioides.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/macrophomina_phaseolina.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:3936` contains `NCBITaxon:35725`, label `Macrophomina phaseolina`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- All 5 NCBI exact synonyms and all 7 NCBI related synonyms match the YAML `synonyms`.
- `curation/seed_scope.tsv:52296` has exactly one scope row for `NCBITaxon:35725`; its rule names `Macrophomina phaseolina` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:33124` reports `organism_count=11` for `NCBITaxon:35725`, matching the YAML `GOLD` attestation.
- Exact native GOLD expansion found 11 organism rows in `data/gold/organisms.jsonl.gz`, 12 direct projects in `data/gold/projects.jsonl.gz`, and 10 linked analyses in `data/gold/analyses.jsonl.gz` through exact `AP PROJECT GOLD IDS`.
- `data/raw/ncbi_type_material.tsv:192558-192561` contains 4 exact culture-from-epitype spellings for `Macrophoma phaseolina` / `CBS 205.47`.
- `data/straininfo/records.jsonl.gz` contains 62 exact StrainInfo strain records and 74 exact deposit records for NCBI taxon `35725`, but none joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `macrophomina_phaseolina` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- `data/raw/ncbi_merged_ids.tsv` has one exact side-inventory row, `NCBITaxon:348105 -> NCBITaxon:35725`, but the retired ID is absent from retained `data/raw/ncbitaxon_taxa.tsv` rows, so the generated YAML correctly has no `replaces` value.
