# YAML Record Review: Mesodinium rubrum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/mesodinium_rubrum.yaml`
- Started UTC: 2026-09-23T15:24:29Z
- Finished UTC: 2026-09-23T15:24:29Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:704171`
- Label: `Mesodinium rubrum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/mesodinium_rubrum.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mesodinium_chamaeleon.yaml data/taxa/eukaryota/mesodinium_pulex.yaml data/taxa/eukaryota/mesodinium_rubrum.yaml data/taxa/eukaryota/metahyphopichia_silvanorum.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/mesodinium_rubrum.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Complete native GOLD exact scans extracted one organism row, 40 linked project rows, and 0 linked analysis rows for this taxon.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:165100` contains `NCBITaxon:704171`, label `Mesodinium rubrum`, rank `SPECIES`, parent `NCBITaxon:283646`, genetic code `29`, 1 exact synonym, and 3 related synonyms, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:56499` has exactly one scope row for `NCBITaxon:704171`; its rule names `Mesodinium rubrum` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:41695` reports `organism_count=2` for `NCBITaxon:704171`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0583112` / `Mesodinium rubrum CBJR05`; the complete join found 40 linked projects and no linked analyses.
- The direct NCBI type-material inventory scan found no rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero rows for this taxon in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 1 exact direct row and 1 exact deposit row for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv:54071` has the side-inventory old ID `NCBITaxon:283649` currently merging into `NCBITaxon:704171`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `mesodinium_rubrum` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has one exact organism row for `NCBITaxon:704171` while the committed aggregate GOLD row reports 2; this review did not alter the aggregate inventory.
