# YAML Record Review: Melampsora laricis-populina

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/melampsora_laricis_populina.yaml`
- Started UTC: 2026-09-23T15:05:27Z
- Finished UTC: 2026-09-23T15:05:27Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:203908`
- Label: `Melampsora laricis-populina`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/melampsora_laricis_populina.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/melampsora_americana.yaml data/taxa/eukaryota/melampsora_larici_populina_98ag31.yaml data/taxa/eukaryota/melampsora_laricis_populina.yaml data/taxa/eukaryota/melampsora_lini.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/melampsora_laricis_populina.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Complete native GOLD exact scans extracted 83 organism rows, 174 linked project rows, and 0 linked analysis rows for this taxon.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:40252` contains `NCBITaxon:203908`, label `Melampsora laricis-populina`, rank `SPECIES`, parent `NCBITaxon:5260`, genetic code `1`, no exact synonyms, and 3 related synonyms, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:54481` has exactly one scope row for `NCBITaxon:203908`; its rule names `Melampsora laricis-populina` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:19298` reports `organism_count=82` for `NCBITaxon:203908`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found 83 organism rows for `NCBITaxon:203908`, including `Go0088810` / `Melampsora laricis-populina 98AG31`, `Go0088811` / `Melampsora laricis-populina 98AG31 S1 X 98AG31-A087 Mapping Population`, and `Go0095660` / `Melampsora laricis-populina`; the complete join found 174 linked projects and no linked analyses.
- The direct NCBI type-material inventory scan found no rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:203908`.
- `data/raw/ncbi_merged_ids.tsv:91181` has the side-inventory old ID `NCBITaxon:666663` currently merging into `NCBITaxon:203908`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `melampsora_laricis_populina` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has 83 exact organism rows for `NCBITaxon:203908` while the committed aggregate GOLD row reports 82; this review did not alter the aggregate inventory.
