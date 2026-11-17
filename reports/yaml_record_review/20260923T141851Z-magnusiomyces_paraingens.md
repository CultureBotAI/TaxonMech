# YAML Record Review: Magnusiomyces paraingens

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/magnusiomyces_paraingens.yaml`
- Started UTC: 2026-09-23T14:16:00Z
- Finished UTC: 2026-09-23T14:18:51Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:2606893`
- Label: `Magnusiomyces paraingens`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/magnusiomyces_paraingens.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/magnusiomyces_magnusii.yaml data/taxa/eukaryota/magnusiomyces_magnusii_cbs_234_85.yaml data/taxa/eukaryota/magnusiomyces_paraingens.yaml data/taxa/eukaryota/magnusiomyces_starmeri.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/magnusiomyces_paraingens.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:536324` contains `NCBITaxon:2606893`, label `Magnusiomyces paraingens`, rank `SPECIES`, parent `NCBITaxon:1095182`, genetic code `1`, 3 exact synonyms, and 4 related synonyms, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:62899` has exactly one scope row for `NCBITaxon:2606893`; its rule names `Magnusiomyces paraingens` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:24017` reports `organism_count=1` for `NCBITaxon:2606893`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0631683` / `Saprochaete ingens CBS 517.90`, one linked project, `Gp0645231`, and one analysis linked through `AP PROJECT GOLD IDS`.
- The NCBI type-material inventory has 2 culture-from-type-material rows for `Candida ingens` / `CBS 517.90`, including the normalized `CBS:517.90` variant. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 29 exact direct rows and 36 deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv:78049` records side-inventory old ID `NCBITaxon:44084` merging into `NCBITaxon:2606893`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `magnusiomyces_paraingens` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
