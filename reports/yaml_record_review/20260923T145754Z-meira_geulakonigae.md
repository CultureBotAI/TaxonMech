# YAML Record Review: Meira geulakonigae

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/meira_geulakonigae.yaml`
- Started UTC: 2026-09-23T14:57:54Z
- Finished UTC: 2026-09-23T14:57:54Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:215253`
- Label: `Meira geulakonigae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/meira_geulakonigae.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mayamaea_atomus.yaml data/taxa/eukaryota/megacollybia_marginata.yaml data/taxa/eukaryota/meira_geulakonigae.yaml data/taxa/eukaryota/meira_miltonrushii.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/meira_geulakonigae.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:42380` contains `NCBITaxon:215253`, label `Meira geulakonigae`, rank `SPECIES`, parent `NCBITaxon:215251`, genetic code `1`, 1 exact synonym, and 1 related synonym, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:54548` has exactly one scope row for `NCBITaxon:215253`; its rule names `Meira geulakonigae` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:20376` reports `organism_count=1` for `NCBITaxon:215253`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found no organism, project, or analysis rows for `NCBITaxon:215253`.
- The NCBI type-material inventory has 4 culture-from-holotype rows for `AS004` and `CBS 110052` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero rows for this taxon in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 1 exact direct row and 4 exact deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:215253`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `meira_geulakonigae` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has 0 exact organism rows for `NCBITaxon:215253` while the committed aggregate GOLD row reports 1; this review did not alter the aggregate inventory.
