# YAML Record Review: Magnusiomyces fungicola

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/magnusiomyces_fungicola.yaml`
- Started UTC: 2026-09-23T14:11:00Z
- Finished UTC: 2026-09-23T14:15:28Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1734004`
- Label: `Magnusiomyces fungicola`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/magnusiomyces_fungicola.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/magnaporthiopsis_incrustans.yaml data/taxa/eukaryota/magnaporthiopsis_rhizophila.yaml data/taxa/eukaryota/magnusiomyces_capitatus.yaml data/taxa/eukaryota/magnusiomyces_fungicola.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/magnusiomyces_fungicola.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:452579` contains `NCBITaxon:1734004`, label `Magnusiomyces fungicola`, rank `SPECIES`, parent `NCBITaxon:1095182`, genetic code `1`, exact synonym `Saprochaete fungicola`, and 2 related synonyms, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:61167` has exactly one scope row for `NCBITaxon:1734004`; its rule names `Magnusiomyces fungicola` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:15018` reports `organism_count=1` for `NCBITaxon:1734004`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0517197` / `Saprochaete fungicola ERS3015286`, one linked project, `Gp0441235`, and one analysis linked through `AP PROJECT GOLD IDS`.
- The NCBI type-material inventory has 2 culture-from-holotype rows and 2 holotype rows for `Saprochaete fungicola`, with both raw and normalized `CBS 625.85` / `CBS H-13668` designations. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no exact StrainInfo direct, deposit, assembly, exclusion, or related-record rows for this taxon.
- The bounded scan found no old merged IDs for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `magnusiomyces_fungicola` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
