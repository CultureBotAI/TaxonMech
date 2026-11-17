# YAML Record Review: Lyophyllum atratum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lyophyllum_atratum.yaml`
- Started UTC: 2026-09-23T13:59:00Z
- Finished UTC: 2026-09-23T14:02:08Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:117065`
- Label: `Lyophyllum atratum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lyophyllum_atratum.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lyophyllum_atratum.yaml data/taxa/eukaryota/lyophyllum_decastes.yaml data/taxa/eukaryota/lyophyllum_montanum.yaml data/taxa/eukaryota/lyophyllum_shimeji.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lyophyllum_atratum.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:21676` contains `NCBITaxon:117065`, label `Lyophyllum atratum`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 14 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI exact synonyms `Agaricus atratus` and `Tephrocybe atrata` plus related synonyms `Agaricus atratus Fr., 1818`, `Lyophyllum atratum (Fr.) Singer, 1943`, and `Tephrocybe atrata (Fr.) Donk, 1962` match the YAML `synonyms`.
- `curation/seed_scope.tsv:53832` has exactly one scope row for `NCBITaxon:117065`; its rule names `Lyophyllum atratum` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:3683` reports `organism_count=1` for `NCBITaxon:117065`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0370982` / `Lyophyllum atratum CBS 144462`, and its direct project `Gp0325671`; no native analysis rows linked to that project.
- `data/straininfo/records.jsonl.gz` contains 4 exact StrainInfo strain records and 4 exact deposit records for NCBI taxon `117065`, but none joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no NCBI type-material rows and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lyophyllum_atratum` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- `data/raw/ncbi_merged_ids.tsv` has one exact side-inventory row, `NCBITaxon:71894 -> NCBITaxon:117065`, but the retired ID is absent from retained `data/raw/ncbitaxon_taxa.tsv` rows, so the generated YAML correctly has no `replaces` value.
