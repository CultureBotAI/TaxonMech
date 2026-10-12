# YAML Record Review: Malassezia nana

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/malassezia_nana.yaml`
- Started UTC: 2026-09-23T14:26:00Z
- Finished UTC: 2026-09-23T14:29:21Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:180528`
- Label: `Malassezia nana`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/malassezia_nana.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/malassezia_nana.yaml data/taxa/eukaryota/malassezia_obtusa.yaml data/taxa/eukaryota/malassezia_pachydermatis.yaml data/taxa/eukaryota/malassezia_restricta.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/malassezia_nana.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:36238` contains `NCBITaxon:180528`, label `Malassezia nana`, rank `SPECIES`, parent `NCBITaxon:55193`, genetic code `1`, no exact synonyms, and 6 related synonyms, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:54334` has exactly one scope row for `NCBITaxon:180528`; its rule names `Malassezia nana` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:15848` reports `organism_count=2` for `NCBITaxon:180528`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same 2 organism rows, `Go0125533` / `Malassezia nana CBS 9557` and `Go0138926` / `Malassezia nana JCM 12085`, with one linked project and one linked analysis per organism.
- The NCBI type-material inventory has 6 type-material rows for `Malassezia nana` covering `CBS 9557`, `JCM 12085`, and `NUSV 1003` raw and normalized variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 5 exact direct rows and 12 deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv` has 5 side-inventory old IDs, `NCBITaxon:224746`, `NCBITaxon:224747`, `NCBITaxon:224748`, `NCBITaxon:224749`, and `NCBITaxon:233857`, that currently merge into `NCBITaxon:180528`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `malassezia_nana` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
