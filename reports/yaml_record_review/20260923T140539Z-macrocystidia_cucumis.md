# YAML Record Review: Macrocystidia cucumis

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/macrocystidia_cucumis.yaml`
- Started UTC: 2026-09-23T14:03:00Z
- Finished UTC: 2026-09-23T14:05:39Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:182055`
- Label: `Macrocystidia cucumis`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/macrocystidia_cucumis.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/macrobiotophthora_vermicola.yaml data/taxa/eukaryota/macrocystidia_cucumis.yaml data/taxa/eukaryota/macrocystis_pyrifera.yaml data/taxa/eukaryota/macrolepiota_dolichaula.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/macrocystidia_cucumis.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:36437` contains `NCBITaxon:182055`, label `Macrocystidia cucumis`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 14 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI exact synonym `Agaricus cucumis` plus related synonyms `Agaricus cucumis Pers., 1796` and `Macrocystidia cucumis (Pers.) Joss., 1934` match the YAML `synonyms`.
- `curation/seed_scope.tsv:54365` has exactly one scope row for `NCBITaxon:182055`; its rule names `Macrocystidia cucumis` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:16151` reports `organism_count=1` for `NCBITaxon:182055`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0140030` / `Macrocystidia cucumis KM177596`, its direct project `Gp0145124`, and one linked analysis through that project.
- `data/straininfo/records.jsonl.gz` contains one exact StrainInfo strain record and one exact deposit record for NCBI taxon `182055`, but neither joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no NCBI type-material rows, no old merged IDs, and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `macrocystidia_cucumis` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
