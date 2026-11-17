# YAML Record Review: Malassezia vespertilionis

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/malassezia_vespertilionis.yaml`
- Started UTC: 2026-09-23T14:30:00Z
- Finished UTC: 2026-09-23T14:33:07Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:2020962`
- Label: `Malassezia vespertilionis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/malassezia_vespertilionis.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/malassezia_slooffiae.yaml data/taxa/eukaryota/malassezia_sympodialis.yaml data/taxa/eukaryota/malassezia_vespertilionis.yaml data/taxa/eukaryota/malassezia_yamatoensis.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/malassezia_vespertilionis.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:511204` contains `NCBITaxon:2020962`, label `Malassezia vespertilionis`, rank `SPECIES`, parent `NCBITaxon:55193`, genetic code `1`, no exact synonyms, and 2 related synonyms, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:61949` has exactly one scope row for `NCBITaxon:2020962`; its rule names `Malassezia vespertilionis` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:18828` reports `organism_count=1` for `NCBITaxon:2020962`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0632146` / `Malassezia vespertilionis NWHC:44797-103`, one linked project, `Gp0645967`, and one analysis linked through `AP PROJECT GOLD IDS`.
- The NCBI type-material inventory has 4 culture-from-holotype rows for `Malassezia vespertilionis` covering `CBS 15041` and `UAMH 11924` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no exact StrainInfo direct, deposit, assembly, exclusion, or related-record rows for this taxon.
- The bounded scan and `rg --no-ignore --hidden` field-boundary search found no old merged IDs for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `malassezia_vespertilionis` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
