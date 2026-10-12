# YAML Record Review: Lyophyllum montanum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lyophyllum_montanum.yaml`
- Started UTC: 2026-09-23T13:59:00Z
- Finished UTC: 2026-09-23T14:02:08Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1940298`
- Label: `Lyophyllum montanum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lyophyllum_montanum.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lyophyllum_atratum.yaml data/taxa/eukaryota/lyophyllum_decastes.yaml data/taxa/eukaryota/lyophyllum_montanum.yaml data/taxa/eukaryota/lyophyllum_shimeji.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lyophyllum_montanum.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:497911` contains `NCBITaxon:1940298`, label `Lyophyllum montanum`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 14 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- The NCBI related synonym `Lyophyllum montanum A.H. Sm., 1957` matches the YAML `synonyms`; the NCBI row has no exact synonyms.
- `curation/seed_scope.tsv:61690` has exactly one scope row for `NCBITaxon:1940298`; its rule names `Lyophyllum montanum` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:17845` reports `organism_count=1` for `NCBITaxon:1940298`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0357142` / `Lyophyllum montanum OKM 7240`, and its direct project `Gp0191686`; no native analysis rows linked to that project.
- `data/raw/ncbi_type_material.tsv:73528-73531` contains 4 exact holotype spellings for `MICH 11343`.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no exact StrainInfo records, no old merged IDs, and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lyophyllum_montanum` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
