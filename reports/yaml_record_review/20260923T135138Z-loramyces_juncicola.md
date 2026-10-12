# YAML Record Review: Loramyces juncicola

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/loramyces_juncicola.yaml`
- Started UTC: 2026-09-23T13:49:00Z
- Finished UTC: 2026-09-23T13:51:38Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:132173`
- Label: `Loramyces juncicola`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/loramyces_juncicola.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lophodermium_piceae.yaml data/taxa/eukaryota/lophodermium_pinastri.yaml data/taxa/eukaryota/loramyces_juncicola.yaml data/taxa/eukaryota/loramyces_macrosporus.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/loramyces_juncicola.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:25488` contains `NCBITaxon:132173`, label `Loramyces juncicola`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 15 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- The NCBI related synonym `Loramyces juncicola W. Weston, 1929` matches the YAML `synonyms`; the NCBI row has no exact synonyms.
- `curation/seed_scope.tsv:53943` has exactly one scope row for `NCBITaxon:132173`; its rule names `Loramyces juncicola` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:7816` reports `organism_count=1` for `NCBITaxon:132173`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0111675` / `Loramyces juncicola ATCC 46458`, and two direct projects, `Gp0113757` and `Gp0113758`; no native analysis rows linked to those projects.
- `data/straininfo/records.jsonl.gz` contains 2 exact StrainInfo strain records and 3 exact deposit records for NCBI taxon `132173`, but none joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no NCBI type-material rows, no old merged IDs, and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `loramyces_juncicola` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
