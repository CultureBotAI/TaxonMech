# YAML Record Review: Metarhizium anisopliae

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/metarhizium_anisopliae.yaml`
- Started UTC: 2026-09-23T15:28:11Z
- Finished UTC: 2026-09-23T15:28:11Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:5530`
- Label: `Metarhizium anisopliae`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/metarhizium_anisopliae.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/metapochonia_bulbillosa.yaml data/taxa/eukaryota/metarhizium_acridum.yaml data/taxa/eukaryota/metarhizium_acridum_cqma_102.yaml data/taxa/eukaryota/metarhizium_anisopliae.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/metarhizium_anisopliae.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Focused StrainInfo JSONL extraction completed for this taxon's 193 exact direct rows and 234 exact deposit rows.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2455` contains `NCBITaxon:5530`, label `Metarhizium anisopliae`, rank `SPECIES`, parent `NCBITaxon:5529`, genetic code `1`, 5 exact synonyms, and 4 related synonyms, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:52026` has exactly one scope row for `NCBITaxon:5530`; its rule names `Metarhizium anisopliae` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:38616` reports `organism_count=4` for `NCBITaxon:5530`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found 3 organism rows, `Go0040301` / `Metarhizium anisopliae ARSEF 2575`, `Go0095309` / `Metarhizium anisopliae E6`, and `Go0631369` / `Metarhizium anisopliae JEF-290`, with one linked project per organism and 2 linked analyses.
- The direct NCBI type-material inventory scan found no rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero rows for this taxon in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 193 exact direct rows and 234 exact deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv` has 6 side-inventory old IDs currently merging into `NCBITaxon:5530`, including `NCBITaxon:1208604`, `NCBITaxon:1208605`, `NCBITaxon:1208606`, `NCBITaxon:2081990`, `NCBITaxon:2081991`, and `NCBITaxon:92636`; the bounded scan found no retained old IDs in the generated NCBI taxa feed, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `metarhizium_anisopliae` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has 3 exact organism rows for `NCBITaxon:5530` while the committed aggregate GOLD row reports 4; this review did not alter the aggregate inventory.
