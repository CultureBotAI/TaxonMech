# YAML Record Review: Meira nashicola

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/meira_nashicola.yaml`
- Started UTC: 2026-09-23T15:01:06Z
- Finished UTC: 2026-09-23T15:01:06Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:286112`
- Label: `Meira nashicola`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/meira_nashicola.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/meira_nashicola.yaml data/taxa/eukaryota/melampsora_abietis_canadensis.yaml data/taxa/eukaryota/melampsora_aecidioides.yaml data/taxa/eukaryota/melampsora_allii_populina.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/meira_nashicola.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:58490` contains `NCBITaxon:286112`, label `Meira nashicola`, rank `SPECIES`, parent `NCBITaxon:215251`, genetic code `1`, no exact synonyms, and 3 related synonyms, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:54996` has exactly one scope row for `NCBITaxon:286112`; its rule names `Meira nashicola` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:27787` reports `organism_count=1` for `NCBITaxon:286112`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0138961` / `Meira nashicola JCM 18503`, with one linked project and one linked `Meira nashicola JCM 18503` analysis.
- The NCBI type-material inventory has 6 culture-from-holotype rows for `CBS 117161`, `MAFF 230028`, and `PFS 002` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:286112`.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:286112`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `meira_nashicola` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The committed GOLD aggregate row and the current local native GOLD JSONL exact scan both report one organism row for `NCBITaxon:286112`.
