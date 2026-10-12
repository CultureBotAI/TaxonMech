# YAML Record Review: Melanotaenium endogenum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/melanotaenium_endogenum.yaml`
- Started UTC: 2026-09-23T15:18:54Z
- Finished UTC: 2026-09-23T15:18:54Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:84746`
- Label: `Melanotaenium endogenum`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/melanotaenium_endogenum.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/melanotaenium_endogenum.yaml data/taxa/eukaryota/meredithblackwellia_eburnea.yaml data/taxa/eukaryota/meredithiella_fracta.yaml data/taxa/eukaryota/meripilus_sumstinei.yaml`: exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/melanotaenium_endogenum.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:13062` contains `NCBITaxon:84746`, label `Melanotaenium endogenum`, rank `SPECIES`, parent `NCBITaxon:63260`, genetic code `1`, no exact synonyms, and no related synonyms, matching the record.
- All 12 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:53411` has exactly one scope row for `NCBITaxon:84746`; its rule names `Melanotaenium endogenum` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:43197` reports `organism_count=2` for `NCBITaxon:84746`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found 2 organism rows, `Go0110153` / `Melanotaenium endogenum CBS481.91` and `Go0111680` / `Melanotaenium endogenum CBS 481.91`, with one linked project per organism and no linked analyses.
- The direct NCBI type-material inventory scan found no rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact BacDive rows and zero rows for this taxon in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 1 exact direct row and 2 exact deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- `data/raw/ncbi_merged_ids.tsv` has no side-inventory rows that currently merge into `NCBITaxon:84746`, so the absence of `replaces` is expected.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `melanotaenium_endogenum` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- The committed GOLD aggregate row and the current local native GOLD JSONL exact scan both report 2 organism rows for `NCBITaxon:84746`.
