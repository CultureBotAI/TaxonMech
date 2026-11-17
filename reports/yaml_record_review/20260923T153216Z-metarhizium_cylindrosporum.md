# YAML Record Review: Metarhizium cylindrosporum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/metarhizium_cylindrosporum.yaml`
- Started UTC: 2026-09-23T15:32:16Z
- Finished UTC: 2026-09-23T15:32:16Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:180591`
- Label: `Metarhizium cylindrosporum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/metarhizium_cylindrosporum.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metarhizium_brunneum.yaml data/taxa/eukaryota/metarhizium_cylindrosporum.yaml data/taxa/eukaryota/metarhizium_flavoviride.yaml data/taxa/eukaryota/metarhizium_frigidum.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/metarhizium_cylindrosporum.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Focused StrainInfo JSONL extraction completed for this taxon's 1 exact direct row and 2 exact deposit rows.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:36252` contains `NCBITaxon:180591`, label `Metarhizium cylindrosporum`, rank `SPECIES`, parent `NCBITaxon:5529`, genetic code `1`, 3 exact synonyms, and 1 related synonym, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:54335` has exactly one scope row for `NCBITaxon:180591`; its rule names `Metarhizium cylindrosporum` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:15891` reports `organism_count=1` for `NCBITaxon:180591`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found no organism, project, or analysis rows for `NCBITaxon:180591`.
- The NCBI type-material inventory has 2 holotype rows for `ACCC 30114` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero rows for this taxon in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 1 exact direct row and 2 exact deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv:2557` and `data/raw/ncbi_merged_ids.tsv:77543` have side-inventory old IDs `NCBITaxon:1076440` and `NCBITaxon:43343` currently merging into `NCBITaxon:180591`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `metarhizium_cylindrosporum` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has 0 exact organism rows for `NCBITaxon:180591` while the committed aggregate GOLD row reports 1; this review did not alter the aggregate inventory.
