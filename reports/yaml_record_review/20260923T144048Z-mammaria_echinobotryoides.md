# YAML Record Review: Mammaria echinobotryoides

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/mammaria_echinobotryoides.yaml`
- Started UTC: 2026-09-23T14:38:00Z
- Finished UTC: 2026-09-23T14:40:48Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:2081584`
- Label: `Mammaria echinobotryoides`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/mammaria_echinobotryoides.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mammaria_echinobotryoides.yaml data/taxa/eukaryota/marasmius_fiardii.yaml data/taxa/eukaryota/margaritispora_aquatica.yaml data/taxa/eukaryota/marquandomyces_marquandii.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/mammaria_echinobotryoides.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:517666` contains `NCBITaxon:2081584`, label `Mammaria echinobotryoides`, rank `SPECIES`, parent `NCBITaxon:2081583`, genetic code `1`, no exact synonyms, and 2 related synonyms, matching the record.
- All 16 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:62281` has exactly one scope row for `NCBITaxon:2081584`; its rule names `Mammaria echinobotryoides` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:19917` reports `organism_count=1` for `NCBITaxon:2081584`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0651390` / `Mammaria echinobotryoides IMI 141550`, with 2 linked projects, `Gp0688294` and `Gp0699285`; no native analysis rows are linked to those projects or the organism.
- The bounded scan found no exact NCBI type-material rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 18 exact direct rows and 45 deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- The bounded scan and `rg --no-ignore --hidden` field-boundary search found no old merged IDs for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `mammaria_echinobotryoides` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
