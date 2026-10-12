# YAML Record Review: Metarhizium frigidum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/metarhizium_frigidum.yaml`
- Started UTC: 2026-09-23T15:32:16Z
- Finished UTC: 2026-09-23T15:32:16Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:165219`
- Label: `Metarhizium frigidum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/metarhizium_frigidum.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metarhizium_brunneum.yaml data/taxa/eukaryota/metarhizium_cylindrosporum.yaml data/taxa/eukaryota/metarhizium_flavoviride.yaml data/taxa/eukaryota/metarhizium_frigidum.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/metarhizium_frigidum.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:33925` contains `NCBITaxon:165219`, label `Metarhizium frigidum`, rank `SPECIES`, parent `NCBITaxon:5529`, genetic code `1`, 1 exact synonym, and 1 related synonym, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:54217` has exactly one scope row for `NCBITaxon:165219`; its rule names `Metarhizium frigidum` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:14202` reports `organism_count=2` for `NCBITaxon:165219`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0114262` / `Metarhizium frigidum Mf4124`, with one linked project and no linked analyses.
- The NCBI type-material inventory has 2 culture-from-holotype rows for `ARSEF 4124` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:165219`.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:165219`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `metarhizium_frigidum` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has one exact organism row for `NCBITaxon:165219` while the committed aggregate GOLD row reports 2; this review did not alter the aggregate inventory.
