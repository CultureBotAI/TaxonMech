# YAML Record Review: Malassezia caprae

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/malassezia_caprae.yaml`
- Started UTC: 2026-09-23T14:19:00Z
- Finished UTC: 2026-09-23T14:22:12Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1381934`
- Label: `Malassezia caprae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/malassezia_caprae.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/magnusiomyces_suaveolens.yaml data/taxa/eukaryota/malassezia_caprae.yaml data/taxa/eukaryota/malassezia_cuniculi.yaml data/taxa/eukaryota/malassezia_dermatis.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/malassezia_caprae.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:337533` contains `NCBITaxon:1381934`, label `Malassezia caprae`, rank `SPECIES`, parent `NCBITaxon:55193`, genetic code `1`, no exact synonyms, and one related synonym, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:59728` has exactly one scope row for `NCBITaxon:1381934`; its rule names `Malassezia caprae` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:8965` reports `organism_count=1` for `NCBITaxon:1381934`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0124726` / `Malassezia caprae CBS 10434`, one linked project, `Gp0132988`, and one analysis linked through `AP PROJECT GOLD IDS`.
- The NCBI type-material inventory has 6 type-material rows for `Malassezia caprae` covering `CBS 10434`, `JCM 14561`, and `MA 383` raw and normalized variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no exact StrainInfo direct, deposit, assembly, exclusion, or related-record rows for this taxon.
- The bounded scan found no old merged IDs for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `malassezia_caprae` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
