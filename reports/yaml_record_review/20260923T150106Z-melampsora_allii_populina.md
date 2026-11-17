# YAML Record Review: Melampsora allii-populina

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/melampsora_allii_populina.yaml`
- Started UTC: 2026-09-23T15:01:06Z
- Finished UTC: 2026-09-23T15:01:06Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:242475`
- Label: `Melampsora allii-populina`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/melampsora_allii_populina.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/meira_nashicola.yaml data/taxa/eukaryota/melampsora_abietis_canadensis.yaml data/taxa/eukaryota/melampsora_aecidioides.yaml data/taxa/eukaryota/melampsora_allii_populina.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/melampsora_allii_populina.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:47480` contains `NCBITaxon:242475`, label `Melampsora allii-populina`, rank `SPECIES`, parent `NCBITaxon:5260`, genetic code `1`, 1 exact synonym, and no related synonyms, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:54715` has exactly one scope row for `NCBITaxon:242475`; its rule names `Melampsora allii-populina` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:22052` reports `organism_count=3` for `NCBITaxon:242475`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found 2 organism rows, `Go0047015` / `Melampsora allii-populina 12AY07` and `Go0384701` / `Melampsora allii-populina Mlp06GRE05`, with 3 linked projects and one linked `Melampsora allii-populina Mlp06GRE05` analysis.
- The direct NCBI type-material inventory scan found no rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:242475`.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:242475`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `melampsora_allii_populina` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has 2 exact organism rows for `NCBITaxon:242475` while the committed aggregate GOLD row reports 3; this review did not alter the aggregate inventory.
