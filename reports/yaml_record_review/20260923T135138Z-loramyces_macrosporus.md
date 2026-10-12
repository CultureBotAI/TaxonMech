# YAML Record Review: Loramyces macrosporus

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/loramyces_macrosporus.yaml`
- Started UTC: 2026-09-23T13:49:00Z
- Finished UTC: 2026-09-23T13:51:38Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:380016`
- Label: `Loramyces macrosporus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/loramyces_macrosporus.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lophodermium_piceae.yaml data/taxa/eukaryota/lophodermium_pinastri.yaml data/taxa/eukaryota/loramyces_juncicola.yaml data/taxa/eukaryota/loramyces_macrosporus.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/loramyces_macrosporus.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:79887` contains `NCBITaxon:380016`, label `Loramyces macrosporus`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 15 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- The NCBI related synonym `Loramyces macrosporus Ingold & B. Chapman, 1952` matches the YAML `synonyms`; the NCBI row has no exact synonyms.
- `curation/seed_scope.tsv:55436` has exactly one scope row for `NCBITaxon:380016`; its rule names `Loramyces macrosporus` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:33859` reports `organism_count=1` for `NCBITaxon:380016`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0110148` / `Loramyces macrosporus CBS235.53`, and two direct projects, `Gp0110619` and `Gp0113756`; no native analysis rows linked to those projects.
- `data/raw/ncbi_type_material.tsv:199435-199438` contains 4 exact rows for `NCBITaxon:380016`, covering `CBS 235.53` culture-from-holotype spellings and `IMI 050689` type-material spellings.
- `data/straininfo/records.jsonl.gz` contains one exact StrainInfo strain record and two exact deposit records for NCBI taxon `380016`, but none joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no old merged IDs and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `loramyces_macrosporus` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
