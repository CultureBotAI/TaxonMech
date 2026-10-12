# YAML Record Review: Malassezia japonica

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/malassezia_japonica.yaml`
- Started UTC: 2026-09-23T14:23:00Z
- Finished UTC: 2026-09-23T14:25:57Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:223818`
- Label: `Malassezia japonica`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/malassezia_japonica.yaml`: exited successfully.
- `just validate-strict data/taxa/eukaryota/malassezia_equina.yaml data/taxa/eukaryota/malassezia_furfur.yaml data/taxa/eukaryota/malassezia_globosa.yaml data/taxa/eukaryota/malassezia_japonica.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/malassezia_japonica.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:43917` contains `NCBITaxon:223818`, label `Malassezia japonica`, rank `SPECIES`, parent `NCBITaxon:55193`, genetic code `1`, no exact synonyms, and one related synonym, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:54610` has exactly one scope row for `NCBITaxon:223818`; its rule names `Malassezia japonica` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:21151` reports `organism_count=2` for `NCBITaxon:223818`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same 2 organism rows, `Go0125192` / `Malassezia japonica CBS 9431` and `Go0138925` / `Malassezia japonica JCM 11963`, with one linked project and one linked analysis per organism.
- The NCBI type-material inventory has 6 type-material rows for `Malassezia japonica` covering `CBS 9431`, `JCM 11963`, and `M 9966` raw and normalized variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 3 exact direct rows and 9 deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- The bounded scan found no old merged IDs for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `malassezia_japonica` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
