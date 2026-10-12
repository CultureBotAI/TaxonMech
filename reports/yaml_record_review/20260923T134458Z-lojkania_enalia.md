# YAML Record Review: Lojkania enalia

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lojkania_enalia.yaml`
- Started UTC: 2026-09-23T13:41:00Z
- Finished UTC: 2026-09-23T13:44:58Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:147567`
- Label: `Lojkania enalia`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lojkania_enalia.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lodderomyces_theae.yaml data/taxa/eukaryota/lojkania_enalia.yaml data/taxa/eukaryota/lollipopaia_minuta.yaml data/taxa/eukaryota/lomentospora_prolificans.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lojkania_enalia.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:30117` contains `NCBITaxon:147567`, label `Lojkania enalia`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI exact synonyms `Didymosphaerella enalia`, `Didymosphaeria enalia`, and `Verruculina enalia` plus related synonyms `Didymosphaeria enalia Kohlm., 1966` and `Lojkania enalia (Kohlm.) M.E. Barr, 1990` match the YAML `synonyms`.
- `curation/seed_scope.tsv:54049` has exactly one scope row for `NCBITaxon:147567`; its rule names `Lojkania enalia` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:11406` reports `organism_count=2` for `NCBITaxon:147567`, matching the YAML `GOLD` attestation.
- The native GOLD scan found one exact organism row, `Go0036358` / `Didymosphaeria enalia CBS 304.66`, two direct projects, `Gp0036357` and `Gp0036358`, and one linked analysis through `Gp0036357`.
- `data/straininfo/records.jsonl.gz` contains 8 exact StrainInfo strain records and 12 exact deposit records for NCBI taxon `147567`, but none joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no NCBI type-material rows and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lojkania_enalia` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- `data/raw/ncbi_merged_ids.tsv` has one exact side-inventory row, `NCBITaxon:85948 -> NCBITaxon:147567`, but the retired ID is absent from retained `data/raw/ncbitaxon_taxa.tsv` rows, so the generated YAML correctly has no `replaces` value.
- The generated GOLD count follows `data/raw/gold_organisms.tsv`; the native exact GOLD catalog currently has one organism row with two direct projects for this taxon.
