# YAML Record Review: Meredithblackwellia eburnea

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/meredithblackwellia_eburnea.yaml`
- Started UTC: 2026-09-23T15:18:54Z
- Finished UTC: 2026-09-23T15:18:54Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1323573`
- Label: `Meredithblackwellia eburnea`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/meredithblackwellia_eburnea.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/melanotaenium_endogenum.yaml data/taxa/eukaryota/meredithblackwellia_eburnea.yaml data/taxa/eukaryota/meredithiella_fracta.yaml data/taxa/eukaryota/meripilus_sumstinei.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/meredithblackwellia_eburnea.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Complete native GOLD exact scans extracted one organism row, 6 linked project rows, and 0 linked analysis rows for this taxon.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:315262` contains `NCBITaxon:1323573`, label `Meredithblackwellia eburnea`, rank `SPECIES`, parent `NCBITaxon:1323572`, genetic code `1`, no exact synonyms, and 2 related synonyms, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:59457` has exactly one scope row for `NCBITaxon:1323573`; its rule names `Meredithblackwellia eburnea` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:7851` reports `organism_count=1` for `NCBITaxon:1323573`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0036544` / `Meredithblackwellia eburnea MCA 4105`; the complete join found 6 linked projects and no linked analyses.
- The NCBI type-material inventory has 8 culture-from-holotype rows for `CBS 12589`, `MCA 4105`, and `NRRL Y-48821` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:1323573`.
- `data/raw/ncbi_merged_ids.tsv:11108` has the side-inventory old ID `NCBITaxon:1292360` currently merging into `NCBITaxon:1323573`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `meredithblackwellia_eburnea` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The committed GOLD aggregate row and the current local native GOLD JSONL exact scan both report one organism row for `NCBITaxon:1323573`.
