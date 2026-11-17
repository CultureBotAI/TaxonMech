# YAML Record Review: Malassezia pachydermatis

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/malassezia_pachydermatis.yaml`
- Started UTC: 2026-09-23T14:26:00Z
- Finished UTC: 2026-09-23T14:29:21Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:77020`
- Label: `Malassezia pachydermatis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/malassezia_pachydermatis.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/malassezia_nana.yaml data/taxa/eukaryota/malassezia_obtusa.yaml data/taxa/eukaryota/malassezia_pachydermatis.yaml data/taxa/eukaryota/malassezia_restricta.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/malassezia_pachydermatis.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:11088` contains `NCBITaxon:77020`, label `Malassezia pachydermatis`, rank `SPECIES`, parent `NCBITaxon:55193`, genetic code `1`, exact synonym `Pityrosporum pachydermatis`, and 2 related synonyms, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:53306` has exactly one scope row for `NCBITaxon:77020`; its rule names `Malassezia pachydermatis` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:42668` reports `organism_count=1` for `NCBITaxon:77020`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0124727` / `Malassezia pachydermatis CBS 1879`, with 2 linked projects, `Gp0132989` and `Gp0143141`, and one analysis per project.
- The NCBI type-material inventory has 2 culture-from-neotype rows for `Pityrosporum pachydermatis` / `CBS 1879`, including the normalized `CBS:1879` variant. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 43 exact direct rows and 54 deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- The bounded scan found no old merged IDs for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `malassezia_pachydermatis` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
