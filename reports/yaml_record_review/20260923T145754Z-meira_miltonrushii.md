# YAML Record Review: Meira miltonrushii

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/meira_miltonrushii.yaml`
- Started UTC: 2026-09-23T14:57:54Z
- Finished UTC: 2026-09-23T14:57:54Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1280837`
- Label: `Meira miltonrushii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/meira_miltonrushii.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mayamaea_atomus.yaml data/taxa/eukaryota/megacollybia_marginata.yaml data/taxa/eukaryota/meira_geulakonigae.yaml data/taxa/eukaryota/meira_miltonrushii.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/meira_miltonrushii.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:299042` contains `NCBITaxon:1280837`, label `Meira miltonrushii`, rank `SPECIES`, parent `NCBITaxon:215251`, genetic code `1`, no exact synonyms, and 2 related synonyms, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:58890` has exactly one scope row for `NCBITaxon:1280837`; its rule names `Meira miltonrushii` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:6544` reports `organism_count=2` for `NCBITaxon:1280837`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0091359` / `Meira miltonrushii MCA 3882`, with two linked projects and no linked analyses.
- The NCBI type-material inventory has 5 culture-from-holotype rows for `ATCC MYA-4883` and `CBS 12591` variants, plus 5 holotype rows for `MCA 3882` and `NRRL Y-48820` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:1280837`.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:1280837`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `meira_miltonrushii` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has one exact organism row for `NCBITaxon:1280837` while the committed aggregate GOLD row reports 2; this review did not alter the aggregate inventory.
