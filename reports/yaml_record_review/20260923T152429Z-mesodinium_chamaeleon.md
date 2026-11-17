# YAML Record Review: Mesodinium chamaeleon

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/mesodinium_chamaeleon.yaml`
- Started UTC: 2026-09-23T15:24:29Z
- Finished UTC: 2026-09-23T15:24:29Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1132834`
- Label: `Mesodinium chamaeleon`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/mesodinium_chamaeleon.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mesodinium_chamaeleon.yaml data/taxa/eukaryota/mesodinium_pulex.yaml data/taxa/eukaryota/mesodinium_rubrum.yaml data/taxa/eukaryota/metahyphopichia_silvanorum.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/mesodinium_chamaeleon.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Complete native GOLD exact scans extracted one organism row, 26 linked project rows, and 0 linked analysis rows for this taxon.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:246057` contains `NCBITaxon:1132834`, label `Mesodinium chamaeleon`, rank `SPECIES`, parent `NCBITaxon:283646`, genetic code `29`, no exact synonyms, and 1 related synonym, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:57843` has exactly one scope row for `NCBITaxon:1132834`; its rule names `Mesodinium chamaeleon` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:2718` reports `organism_count=1` for `NCBITaxon:1132834`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0588179` / `Mesodinium chamaeleon NRMC1802`; the complete join found 26 linked projects and no linked analyses.
- The NCBI type-material inventory has 4 holotype rows for `C CAT-2469` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:1132834`.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:1132834`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `mesodinium_chamaeleon` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The committed GOLD aggregate row and the current local native GOLD JSONL exact scan both report one organism row for `NCBITaxon:1132834`.
