# YAML Record Review: Lophiotrema nucula

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lophiotrema_nucula.yaml`
- Started UTC: 2026-09-23T13:45:00Z
- Finished UTC: 2026-09-23T13:48:19Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:690887`
- Label: `Lophiotrema nucula`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lophiotrema_nucula.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lophiotrema_nucula.yaml data/taxa/eukaryota/lophium_mytilinum.yaml data/taxa/eukaryota/lophodermium_australe.yaml data/taxa/eukaryota/lophodermium_nitens.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lophiotrema_nucula.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:162208` contains `NCBITaxon:690887`, label `Lophiotrema nucula`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI exact synonyms `Lophiosphaera nucula`, `Lophiostoma nucula`, and `Sphaeria nucula` plus related synonyms `Lophiotrema nucula (Fr.) Sacc., 1878` and `Sphaeria nucula Fr., 1817` match the YAML `synonyms`.
- `curation/seed_scope.tsv:56403` has exactly one scope row for `NCBITaxon:690887`; its rule names `Lophiotrema nucula` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:41401` reports `organism_count=2` for `NCBITaxon:690887`, matching the YAML `GOLD` attestation.
- The native GOLD scan found one exact organism row, `Go0036416` / `Lophiotrema nucula CBS 627.86`, and two direct projects, `Gp0036416` and `Gp0036417`; no native analysis rows linked to those projects.
- `data/straininfo/records.jsonl.gz` contains 2 exact StrainInfo strain records and 4 exact deposit records for NCBI taxon `690887`, but none joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no NCBI type-material rows, no old merged IDs, and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lophiotrema_nucula` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The generated GOLD count follows `data/raw/gold_organisms.tsv`; the native exact GOLD catalog currently has one organism row with two direct projects for this taxon.
