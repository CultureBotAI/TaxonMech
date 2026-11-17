# YAML Record Review: Malassezia obtusa

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/malassezia_obtusa.yaml`
- Started UTC: 2026-09-23T14:26:00Z
- Finished UTC: 2026-09-23T14:29:21Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:76774`
- Label: `Malassezia obtusa`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/malassezia_obtusa.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/malassezia_nana.yaml data/taxa/eukaryota/malassezia_obtusa.yaml data/taxa/eukaryota/malassezia_pachydermatis.yaml data/taxa/eukaryota/malassezia_restricta.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/malassezia_obtusa.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:11029` contains `NCBITaxon:76774`, label `Malassezia obtusa`, rank `SPECIES`, parent `NCBITaxon:55193`, genetic code `1`, no exact synonyms, and one related synonym, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:53299` has exactly one scope row for `NCBITaxon:76774`; its rule names `Malassezia obtusa` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:42602` reports `organism_count=1` for `NCBITaxon:76774`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0125193` / `Malassezia obtusa CBS 7876`, one linked project, `Gp0133473`, and one analysis linked through `AP PROJECT GOLD IDS`.
- The NCBI type-material inventory has 3 culture-from-type-material rows for `ATCC MYA-4610` variants and 2 type-material rows for `CBS 7876` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 2 exact direct rows and 4 deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv:37961` records side-inventory old ID `NCBITaxon:2136298` merging into `NCBITaxon:76774`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `malassezia_obtusa` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
