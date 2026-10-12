# YAML Record Review: Margaritispora aquatica

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/margaritispora_aquatica.yaml`
- Started UTC: 2026-09-23T14:38:00Z
- Finished UTC: 2026-09-23T14:40:48Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:359797`
- Label: `Margaritispora aquatica`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/margaritispora_aquatica.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mammaria_echinobotryoides.yaml data/taxa/eukaryota/marasmius_fiardii.yaml data/taxa/eukaryota/margaritispora_aquatica.yaml data/taxa/eukaryota/marquandomyces_marquandii.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/margaritispora_aquatica.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:74706` contains `NCBITaxon:359797`, label `Margaritispora aquatica`, rank `SPECIES`, parent `NCBITaxon:359791`, genetic code `1`, no exact synonyms, and one related synonym, matching the record.
- All 15 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:55345` has exactly one scope row for `NCBITaxon:359797`; its rule names `Margaritispora aquatica` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:33220` reports `organism_count=1` for `NCBITaxon:359797`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found no organism, project, or analysis rows for `ORGANISM NCBI TAX ID=359797`; the committed aggregate `data/raw/gold_organisms.tsv` row is the GOLD source used by this generated YAML.
- The bounded scan found no exact NCBI type-material rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 6 exact direct rows and 10 deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- The bounded scan and `rg --no-ignore --hidden` field-boundary search found no old merged IDs for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `margaritispora_aquatica` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently does not reproduce the committed aggregate GOLD row for `NCBITaxon:359797`; this review did not alter the aggregate inventory.
