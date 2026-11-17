# YAML Record Review: Lunasporangiospora selenospora

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lunasporangiospora_selenospora.yaml`
- Started UTC: 2026-09-23T13:56:00Z
- Finished UTC: 2026-09-23T13:58:43Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:979761`
- Label: `Lunasporangiospora selenospora`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lunasporangiospora_selenospora.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lulworthia_fucicola.yaml data/taxa/eukaryota/lunasporangiospora_selenospora.yaml data/taxa/eukaryota/lundqvistomyces_karachiensis.yaml data/taxa/eukaryota/lycoperdon_perlatum.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lunasporangiospora_selenospora.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:204276` contains `NCBITaxon:979761`, label `Lunasporangiospora selenospora`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI exact synonym `Mortierella selenospora` and related synonyms `Lunasporangiospora selenospora (W. Gams) Vandepol & Bonito, 2020` and `Mortierella selenospora W. Gams, 1976` match the YAML `synonyms`.
- `curation/seed_scope.tsv:57059` has exactly one scope row for `NCBITaxon:979761`; its rule names `Lunasporangiospora selenospora` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:45201` reports `organism_count=3` for `NCBITaxon:979761`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same 3 exact organism rows and 5 direct projects in `data/gold/*.jsonl.gz`; no native analysis rows linked to those projects.
- `data/raw/ncbi_type_material.tsv:275942-275943` contains 2 exact type-material spellings for `Mortierella selenospora` / `CBS 811.68`.
- `data/straininfo/records.jsonl.gz` contains 2 exact StrainInfo strain records and 2 exact deposit records for NCBI taxon `979761`, but none joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no old merged IDs and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lunasporangiospora_selenospora` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
