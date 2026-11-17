# YAML Record Review: Lophodermium nitens

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lophodermium_nitens.yaml`
- Started UTC: 2026-09-23T13:45:00Z
- Finished UTC: 2026-09-23T13:48:19Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:190466`
- Label: `Lophodermium nitens`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lophodermium_nitens.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lophiotrema_nucula.yaml data/taxa/eukaryota/lophium_mytilinum.yaml data/taxa/eukaryota/lophodermium_australe.yaml data/taxa/eukaryota/lophodermium_nitens.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lophodermium_nitens.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:37831` contains `NCBITaxon:190466`, label `Lophodermium nitens`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 15 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI related synonyms `Lophodermium nitens Darker, 1932` and `Lophodermium sp. CBS 127941` match the YAML `synonyms`; the NCBI row has no exact synonyms.
- `curation/seed_scope.tsv:54404` has exactly one scope row for `NCBITaxon:190466`; its rule names `Lophodermium nitens` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:17220` reports `organism_count=2` for `NCBITaxon:190466`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same 2 exact organism rows, 3 direct projects, and one linked analysis through project `Gp0141669`.
- `data/straininfo/records.jsonl.gz` contains 2 exact StrainInfo strain records and 2 exact deposit records for NCBI taxon `190466`, but none joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no NCBI type-material rows and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lophodermium_nitens` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- `data/raw/ncbi_merged_ids.tsv` has one exact side-inventory row, `NCBITaxon:1031570 -> NCBITaxon:190466`, but the retired ID is absent from retained `data/raw/ncbitaxon_taxa.tsv` rows, so the generated YAML correctly has no `replaces` value.
