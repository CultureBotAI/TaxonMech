# YAML Record Review: Lyophyllum decastes

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lyophyllum_decastes.yaml`
- Started UTC: 2026-09-23T13:59:00Z
- Finished UTC: 2026-09-23T14:02:08Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:64660`
- Label: `Lyophyllum decastes`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lyophyllum_decastes.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lyophyllum_atratum.yaml data/taxa/eukaryota/lyophyllum_decastes.yaml data/taxa/eukaryota/lyophyllum_montanum.yaml data/taxa/eukaryota/lyophyllum_shimeji.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lyophyllum_decastes.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:8227` contains `NCBITaxon:64660`, label `Lyophyllum decastes`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 14 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI exact synonym `Agaricus decastes` plus related synonyms `Agaricus decastes Fr., 1818`, `Lyophyllum decastes (Fr.) Singer, 1949`, and `fried chicken mushroom` match the YAML `synonyms`.
- `curation/seed_scope.tsv:53120` has exactly one scope row for `NCBITaxon:64660`; its rule names `Lyophyllum decastes` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:40378` reports `organism_count=3` for `NCBITaxon:64660`, matching the YAML `GOLD` attestation.
- The native GOLD scan found one exact organism row, `Go0384823` / `Lyophyllum decastes JCM 30590`, its direct project `Gp0235952`, and one linked analysis through that project.
- `data/straininfo/records.jsonl.gz` contains 24 exact StrainInfo strain records and 35 exact deposit records for NCBI taxon `64660`, but none joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no NCBI type-material rows, no old merged IDs, and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lyophyllum_decastes` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The generated GOLD count follows `data/raw/gold_organisms.tsv`; the native exact GOLD catalog currently has one organism row with one direct project for this taxon.
