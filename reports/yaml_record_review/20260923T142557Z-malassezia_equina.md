# YAML Record Review: Malassezia equina

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/malassezia_equina.yaml`
- Started UTC: 2026-09-23T14:23:00Z
- Finished UTC: 2026-09-23T14:25:57Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1381935`
- Label: `Malassezia equina`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/malassezia_equina.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/malassezia_equina.yaml data/taxa/eukaryota/malassezia_furfur.yaml data/taxa/eukaryota/malassezia_globosa.yaml data/taxa/eukaryota/malassezia_japonica.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/malassezia_equina.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:337534` contains `NCBITaxon:1381935`, label `Malassezia equina`, rank `SPECIES`, parent `NCBITaxon:55193`, genetic code `1`, no exact synonyms, and 2 related synonyms, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:59729` has exactly one scope row for `NCBITaxon:1381935`; its rule names `Malassezia equina` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:8966` reports `organism_count=1` for `NCBITaxon:1381935`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0125187` / `Malassezia equina CBS 9969`, one linked project, `Gp0133467`, and one analysis linked through `AP PROJECT GOLD IDS`.
- The NCBI type-material inventory has 6 rows for `Malassezia equina` covering culture-from-holotype `CBS 9969`, isotype `JCM 14562`, and type-material `MA 146` raw and normalized variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no exact StrainInfo direct, deposit, assembly, exclusion, or related-record rows for this taxon.
- `data/raw/ncbi_merged_ids.tsv:18799` records side-inventory old ID `NCBITaxon:152348` merging into `NCBITaxon:1381935`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `malassezia_equina` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
