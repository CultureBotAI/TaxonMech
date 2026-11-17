# YAML Record Review: Lomentospora prolificans

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lomentospora_prolificans.yaml`
- Started UTC: 2026-09-23T13:41:00Z
- Finished UTC: 2026-09-23T13:44:58Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:41688`
- Label: `Lomentospora prolificans`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lomentospora_prolificans.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lodderomyces_theae.yaml data/taxa/eukaryota/lojkania_enalia.yaml data/taxa/eukaryota/lollipopaia_minuta.yaml data/taxa/eukaryota/lomentospora_prolificans.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lomentospora_prolificans.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4863` contains `NCBITaxon:41688`, label `Lomentospora prolificans`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI exact synonyms `Scedosporium inflatum` and `Scedosporium prolificans` plus related synonyms `Lomentospora prolificans Hennebert & B.G. Desai, 1974` and `Scedosporium inflatum Malloch & Salkin, 1984` match the YAML `synonyms`.
- `curation/seed_scope.tsv:52477` has exactly one scope row for `NCBITaxon:41688`; its rule names `Lomentospora prolificans` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:34909` reports `organism_count=1` for `NCBITaxon:41688`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0449679` / `Lomentospora prolificans JHH-5317`, its direct project `Gp0314089`, and one linked analysis through that project.
- `data/raw/ncbi_type_material.tsv:206777-206790` contains 14 exact rows for `NCBITaxon:41688`, including direct `Lomentospora prolificans` type-material spellings and `Scedosporium inflatum` culture-from-holotype aliases.
- `data/straininfo/records.jsonl.gz` contains 57 exact StrainInfo strain records and 64 exact deposit records for NCBI taxon `41688`, but none joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lomentospora_prolificans` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- `data/raw/ncbi_merged_ids.tsv` has one exact side-inventory row, `NCBITaxon:66830 -> NCBITaxon:41688`, but the retired ID is absent from retained `data/raw/ncbitaxon_taxa.tsv` rows, so the generated YAML correctly has no `replaces` value.
