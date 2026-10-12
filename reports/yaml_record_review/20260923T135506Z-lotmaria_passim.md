# YAML Record Review: Lotmaria passim

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lotmaria_passim.yaml`
- Started UTC: 2026-09-23T13:52:00Z
- Finished UTC: 2026-09-23T13:55:06Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1620387`
- Label: `Lotmaria passim`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lotmaria_passim.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/loratospora_aestuarii.yaml data/taxa/eukaryota/lotharella_globosa.yaml data/taxa/eukaryota/lotharella_oceanica.yaml data/taxa/eukaryota/lotmaria_passim.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lotmaria_passim.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:418301` contains `NCBITaxon:1620387`, label `Lotmaria passim`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 11 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- The 15 NCBI related synonyms in `data/raw/ncbitaxon_taxa.tsv` match the 15 YAML `synonyms`; the NCBI row has no exact synonyms.
- `curation/seed_scope.tsv:60920` has exactly one scope row for `NCBITaxon:1620387`; its rule names `Lotmaria passim` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:13866` reports `organism_count=2` for `NCBITaxon:1620387`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same two exact organism rows, `Go0384649` / `Lotmaria passim ATCC PRA-403` and `Go0384676` / `Lotmaria passim ATCC PRA-422`, their two direct projects, and two linked analyses through those projects.
- The bounded scan found no exact BacDive, StrainInfo, NCBI type-material, or generated strain rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lotmaria_passim` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- `data/raw/ncbi_merged_ids.tsv` has 14 exact side-inventory rows into `NCBITaxon:1620387`, from `NCBITaxon:1521168` and `NCBITaxon:1529294` through `NCBITaxon:1529306`. None is retained in `data/raw/ncbitaxon_taxa.tsv`, so the generated YAML correctly has no `replaces` value.
