# YAML Record Review: Lycoperdon perlatum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/lycoperdon_perlatum.yaml`
- Started UTC: 2026-09-23T13:56:00Z
- Finished UTC: 2026-09-23T13:58:43Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:90686`
- Label: `Lycoperdon perlatum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/lycoperdon_perlatum.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lulworthia_fucicola.yaml data/taxa/eukaryota/lunasporangiospora_selenospora.yaml data/taxa/eukaryota/lundqvistomyces_karachiensis.yaml data/taxa/eukaryota/lycoperdon_perlatum.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/lycoperdon_perlatum.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:14619` contains `NCBITaxon:90686`, label `Lycoperdon perlatum`, rank `SPECIES`, and genetic code `1`, matching the record.
- All 14 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- NCBI related synonyms `Lycoperdon perlatum Pers., 1796` and `common puffball` match the YAML `synonyms`; the NCBI row has no exact synonyms.
- `curation/seed_scope.tsv:53503` has exactly one scope row for `NCBITaxon:90686`; its rule names `Lycoperdon perlatum` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:44234` reports `organism_count=2` for `NCBITaxon:90686`, matching the YAML `GOLD` attestation.
- The native GOLD scan found one exact organism row, `Go0036371` / `Lycoperdon perlatum FP-102459-T`, and two direct projects, `Gp0036371` and `Gp0036372`; no native analysis rows linked to those projects.
- `data/raw/ncbi_type_material.tsv:271992` contains one exact isotype row for `Lycoperdon perlatum`, `PDD:8551`.
- `data/straininfo/records.jsonl.gz` contains 7 exact StrainInfo strain records and 8 exact deposit records for NCBI taxon `90686`, but none joined into generated BacDive, strain assembly, strain genome, or strain related-record rows for this record.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- The bounded scan found no old merged IDs and no generated StrainInfo overlay rows for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `lycoperdon_perlatum` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The generated GOLD count follows `data/raw/gold_organisms.tsv`; the native exact GOLD catalog currently has one organism row with two direct projects for this taxon.
