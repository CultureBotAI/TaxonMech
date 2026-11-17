# YAML Record Review: Lophium mytilinum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lophium_mytilinum.yaml`
- Started UTC: 2026-09-23T13:45:00Z
- Finished UTC: 2026-09-23T13:48:19Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:390894`
- Label: `Lophium mytilinum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lophium_mytilinum.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lophiotrema_nucula.yaml data/taxa/eukaryota/lophium_mytilinum.yaml data/taxa/eukaryota/lophodermium_australe.yaml data/taxa/eukaryota/lophodermium_nitens.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lophium_mytilinum.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:82588` contains `NCBITaxon:390894`, label `Lophium mytilinum`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI exact synonym `Hysterium mytilinum` and related synonyms `Hysterium mytilinum Pers., 1801` and `Lophium mytilinum P. Karst., 1873` match the YAML `synonyms`.
- `curation/seed_scope.tsv:55472` has exactly one scope row for `NCBITaxon:390894`; its rule names `Lophium mytilinum` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:34097` reports `organism_count=1` for `NCBITaxon:390894`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0036356` / `Lophium mytilinum CBS 269.34`, three direct projects, and one linked analysis through `Gp0036355`.
- `data/straininfo/records.jsonl.gz` contains one exact StrainInfo strain record and one exact deposit record for NCBI taxon `390894`, but neither joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no NCBI type-material rows, no old merged IDs, and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lophium_mytilinum` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
