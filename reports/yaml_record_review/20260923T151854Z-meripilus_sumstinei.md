# YAML Record Review: Meripilus sumstinei

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/meripilus_sumstinei.yaml`
- Started UTC: 2026-09-23T15:18:54Z
- Finished UTC: 2026-09-23T15:18:54Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1940299`
- Label: `Meripilus sumstinei`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/meripilus_sumstinei.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/melanotaenium_endogenum.yaml data/taxa/eukaryota/meredithblackwellia_eburnea.yaml data/taxa/eukaryota/meredithiella_fracta.yaml data/taxa/eukaryota/meripilus_sumstinei.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/meripilus_sumstinei.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:497912` contains `NCBITaxon:1940299`, label `Meripilus sumstinei`, rank `SPECIES`, parent `NCBITaxon:40445`, genetic code `1`, 3 exact synonyms, and 2 related synonyms, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:61691` has exactly one scope row for `NCBITaxon:1940299`; its rule names `Meripilus sumstinei` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:17846` reports `organism_count=1` for `NCBITaxon:1940299`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found one organism row, `Go0357144` / `Meripilus sumstinei FP 105329`, with two linked projects and one linked `Meripilus sumstinei FP 105329 Standard Draft` analysis.
- The direct NCBI type-material inventory scan found no rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero exact StrainInfo direct or deposit rows for this taxon.
- The generated BacDive, culture-collection, strain-assembly, strain-genome, strain-related-record, StrainInfo assembly, StrainInfo exclusion, and StrainInfo related-record tables have no exact rows for `NCBITaxon:1940299`.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:1940299`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `meripilus_sumstinei` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The committed GOLD aggregate row and the current local native GOLD JSONL exact scan both report one organism row for `NCBITaxon:1940299`.
