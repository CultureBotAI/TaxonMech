# YAML Record Review: Lodderomyces theae

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lodderomyces_theae.yaml`
- Started UTC: 2026-09-23T13:41:00Z
- Finished UTC: 2026-09-23T13:44:58Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1198502`
- Label: `Lodderomyces theae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lodderomyces_theae.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lodderomyces_theae.yaml data/taxa/eukaryota/lojkania_enalia.yaml data/taxa/eukaryota/lollipopaia_minuta.yaml data/taxa/eukaryota/lomentospora_prolificans.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lodderomyces_theae.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:269940` contains `NCBITaxon:1198502`, label `Lodderomyces theae`, rank `SPECIES`, and genetic code `12`, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI exact synonym `Candida theae` and related synonyms `Candida sp. G17`, `Candida sp. G31`, `Candida sp. LCF-001`, `Candida theae C.-F. Lee, 2012`, and `Lodderomyces theae C.F. Lee ex Q.M. Wang, Boekhout, Yurkov, G. Peter & F.Y. Bai, 2026` match the YAML `synonyms`.
- `curation/seed_scope.tsv:58314` has exactly one scope row for `NCBITaxon:1198502`; its rule names `Lodderomyces theae` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:4795` reports `organism_count=1` for `NCBITaxon:1198502`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0705025` / `Candida theae CBS 12239`, and its direct project `Gp0831045`; no native analysis rows linked to that project.
- `data/raw/ncbi_type_material.tsv:13224-13232` contains 9 exact rows for `NCBITaxon:1198502`, including ATCC, BCRC, and CBS culture-from-holotype aliases plus `G-17` holotype spellings.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found zero exact BacDive rows, zero exact StrainInfo records, and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lodderomyces_theae` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- `data/raw/ncbi_merged_ids.tsv` has three exact side-inventory rows into `NCBITaxon:1198502`: `NCBITaxon:907296`, `NCBITaxon:907297`, and `NCBITaxon:909672`. None is retained in `data/raw/ncbitaxon_taxa.tsv`, so the generated YAML correctly has no `replaces` value.
