# YAML Record Review: Metarhizium brunneum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/metarhizium_brunneum.yaml`
- Started UTC: 2026-09-23T15:32:16Z
- Finished UTC: 2026-09-23T15:32:16Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:500148`
- Label: `Metarhizium brunneum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/metarhizium_brunneum.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metarhizium_brunneum.yaml data/taxa/eukaryota/metarhizium_cylindrosporum.yaml data/taxa/eukaryota/metarhizium_flavoviride.yaml data/taxa/eukaryota/metarhizium_frigidum.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/metarhizium_brunneum.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Focused StrainInfo JSONL extraction completed for this taxon's 7 exact direct rows and 10 exact deposit rows.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:113488` contains `NCBITaxon:500148`, label `Metarhizium brunneum`, rank `SPECIES`, parent `NCBITaxon:5529`, genetic code `1`, no exact synonyms, and 1 related synonym, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:55850` has exactly one scope row for `NCBITaxon:500148`; its rule names `Metarhizium brunneum` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:37298` reports `organism_count=3` for `NCBITaxon:500148`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0593108` / `Metarhizium brunneum 4556`, with one linked project and one linked `Metarhizium brunneum 4556` analysis.
- The NCBI type-material inventory has 8 culture-from-epitype rows for `ARSEF 2107`, `CBS 316.51`, `IMI 014746`, and `NRRL 1944` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero rows for this taxon in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 7 exact direct rows and 10 exact deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:500148`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `metarhizium_brunneum` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has one exact organism row for `NCBITaxon:500148` while the committed aggregate GOLD row reports 3; this review did not alter the aggregate inventory.
