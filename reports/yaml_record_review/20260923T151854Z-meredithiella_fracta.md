# YAML Record Review: Meredithiella fracta

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/meredithiella_fracta.yaml`
- Started UTC: 2026-09-23T15:18:54Z
- Finished UTC: 2026-09-23T15:18:54Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:2320247`
- Label: `Meredithiella fracta`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/meredithiella_fracta.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/melanotaenium_endogenum.yaml data/taxa/eukaryota/meredithblackwellia_eburnea.yaml data/taxa/eukaryota/meredithiella_fracta.yaml data/taxa/eukaryota/meripilus_sumstinei.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/meredithiella_fracta.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:524948` contains `NCBITaxon:2320247`, label `Meredithiella fracta`, rank `SPECIES`, parent `NCBITaxon:1739109`, genetic code `1`, 1 exact synonym, and 2 related synonyms, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:62560` has exactly one scope row for `NCBITaxon:2320247`; its rule names `Meredithiella fracta` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:21751` reports `organism_count=1` for `NCBITaxon:2320247`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0679451` / `Meredithiella fracta CBS 142645`, with one linked project and one linked `Meredithiella fracta CBS 142645` analysis.
- The NCBI type-material inventory has 2 culture-from-holotype rows for `CBS 142645` variants and 2 holotype rows for `BPI 910531` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:2320247`.
- `data/raw/ncbi_merged_ids.tsv:41178` has the side-inventory old ID `NCBITaxon:2364156` currently merging into `NCBITaxon:2320247`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `meredithiella_fracta` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The committed GOLD aggregate row and the current local native GOLD JSONL exact scan both report one organism row for `NCBITaxon:2320247`.
