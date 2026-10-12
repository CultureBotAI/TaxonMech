# YAML Record Review: Mayamaea atomus

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/mayamaea_atomus.yaml`
- Started UTC: 2026-09-23T14:57:54Z
- Finished UTC: 2026-09-23T14:57:54Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:431391`
- Label: `Mayamaea atomus`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/mayamaea_atomus.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mayamaea_atomus.yaml data/taxa/eukaryota/megacollybia_marginata.yaml data/taxa/eukaryota/meira_geulakonigae.yaml data/taxa/eukaryota/meira_miltonrushii.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/mayamaea_atomus.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:95156` contains `NCBITaxon:431391`, label `Mayamaea atomus`, rank `SPECIES`, parent `NCBITaxon:431390`, genetic code `1`, 4 exact synonyms, and 2 related synonyms, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:55632` has exactly one scope row for `NCBITaxon:431391`; its rule names `Mayamaea atomus` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:35316` reports `organism_count=1` for `NCBITaxon:431391`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found no organism, project, or analysis rows for `NCBITaxon:431391`.
- The direct NCBI type-material inventory scan found no rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:431391`.
- `data/raw/ncbi_merged_ids.tsv:61037` has the side-inventory old ID `NCBITaxon:303464` currently merging into `NCBITaxon:431391`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `mayamaea_atomus` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has 0 exact organism rows for `NCBITaxon:431391` while the committed aggregate GOLD row reports 1; this review did not alter the aggregate inventory.
