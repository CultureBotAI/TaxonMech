# YAML Record Review: Magnusiomyces magnusii

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/magnusiomyces_magnusii.yaml`
- Started UTC: 2026-09-23T14:16:00Z
- Finished UTC: 2026-09-23T14:18:51Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:43963`
- Label: `Magnusiomyces magnusii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/magnusiomyces_magnusii.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/magnusiomyces_magnusii.yaml data/taxa/eukaryota/magnusiomyces_magnusii_cbs_234_85.yaml data/taxa/eukaryota/magnusiomyces_paraingens.yaml data/taxa/eukaryota/magnusiomyces_starmeri.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/magnusiomyces_magnusii.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:5280` contains `NCBITaxon:43963`, label `Magnusiomyces magnusii`, rank `SPECIES`, parent `NCBITaxon:1095182`, genetic code `1`, 4 exact synonyms, and 5 related synonyms, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:52549` has exactly one scope row for `NCBITaxon:43963`; its rule names `Magnusiomyces magnusii` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:35520` reports `organism_count=1` for `NCBITaxon:43963`, matching the YAML `GOLD` attestation and its note that descendant taxa are not gathered.
- The native GOLD scan found the same single organism row, `Go0705296` / `Magnusiomyces magnusii NRRL Y-17563`, and one linked project, `Gp0831332`; no native analysis rows are linked to that project or organism.
- The NCBI type-material inventory has 5 culture-from-holotype rows for `Endomyces magnusii` / `NRRL Y-17563` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 12 exact direct rows and 28 deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv:81526` records side-inventory old ID `NCBITaxon:48740` merging into `NCBITaxon:43963`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `magnusiomyces_magnusii` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
