# YAML Record Review: Metarhizium acridum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/metarhizium_acridum.yaml`
- Started UTC: 2026-09-23T15:28:11Z
- Finished UTC: 2026-09-23T15:28:11Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:92637`
- Label: `Metarhizium acridum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/metarhizium_acridum.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metapochonia_bulbillosa.yaml data/taxa/eukaryota/metarhizium_acridum.yaml data/taxa/eukaryota/metarhizium_acridum_cqma_102.yaml data/taxa/eukaryota/metarhizium_anisopliae.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/metarhizium_acridum.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:15148` contains `NCBITaxon:92637`, label `Metarhizium acridum`, rank `SPECIES`, parent `NCBITaxon:5529`, genetic code `1`, 2 exact synonyms, and 1 related synonym, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:53535` has exactly one scope row for `NCBITaxon:92637`; its rule names `Metarhizium acridum` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:44546` reports `organism_count=2` for `NCBITaxon:92637`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0631234` / `Metarhizium acridum ARSEF 324`, with one linked project and one linked `Metarhizium acridum ARSEF 324` analysis.
- The NCBI type-material inventory has 2 type-material rows for `ARSEF 7486` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:92637`.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:92637`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `metarhizium_acridum` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has one exact organism row for `NCBITaxon:92637` while the committed aggregate GOLD row reports 2; this review did not alter the aggregate inventory.
