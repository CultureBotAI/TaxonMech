# YAML Record Review: Maudiozyma barnettii

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/maudiozyma_barnettii.yaml`
- Started UTC: 2026-09-23T14:45:00Z
- Finished UTC: 2026-09-23T14:48:05Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:61262`
- Label: `Maudiozyma barnettii`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/maudiozyma_barnettii.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/maudiozyma_barnettii.yaml data/taxa/eukaryota/maudiozyma_bulderi.yaml data/taxa/eukaryota/maudiozyma_exigua.yaml data/taxa/eukaryota/maudiozyma_humilis.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/maudiozyma_barnettii.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7769` contains `NCBITaxon:61262`, label `Maudiozyma barnettii`, rank `SPECIES`, parent `NCBITaxon:3162980`, genetic code `1`, 2 exact synonyms, and 2 related synonyms, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:53030` has exactly one scope row for `NCBITaxon:61262`; its rule names `Maudiozyma barnettii` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:39855` reports `organism_count=2` for `NCBITaxon:61262`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same 2 organism rows, `Go0631621` / `Kazachstania barnettii CLIB 433` and `Go0705403` / `Maudiozyma barnettii NRRL Y-27223`, with one linked project per organism and one linked analysis.
- The NCBI type-material inventory has 11 type-material rows for `Maudiozyma barnettii` covering `AS 2.2405`, `CBS 5648`, `CGMCC:2.2405`, `DBVPG 6365`, and `NRRL Y-17918` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 8 exact direct rows and 27 deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv:86478` records side-inventory old ID `NCBITaxon:56412` merging into `NCBITaxon:61262`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `maudiozyma_barnettii` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
