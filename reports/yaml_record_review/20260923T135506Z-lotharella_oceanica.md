# YAML Record Review: Lotharella oceanica

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lotharella_oceanica.yaml`
- Started UTC: 2026-09-23T13:52:00Z
- Finished UTC: 2026-09-23T13:55:06Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:641309`
- Label: `Lotharella oceanica`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lotharella_oceanica.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/loratospora_aestuarii.yaml data/taxa/eukaryota/lotharella_globosa.yaml data/taxa/eukaryota/lotharella_oceanica.yaml data/taxa/eukaryota/lotmaria_passim.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lotharella_oceanica.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:147962` contains `NCBITaxon:641309`, label `Lotharella oceanica`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 8 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI related synonyms `Lotharella oceanica S.Ota in Ota et al. 2009`, `Lotharella sp. CCMP622`, and `Lotharella sp. PJK-2009a` match the YAML `synonyms`; the NCBI row has no exact synonyms.
- `curation/seed_scope.tsv:56204` has exactly one scope row for `NCBITaxon:641309`; its rule names `Lotharella oceanica` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:40211` reports `organism_count=1` for `NCBITaxon:641309`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0095632` / `Lotharella oceanica CCMP622`, its direct project `Gp0095632`, and one linked analysis through that project.
- The bounded scan found no exact BacDive, StrainInfo, NCBI type-material, or generated strain rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no old merged IDs and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lotharella_oceanica` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
