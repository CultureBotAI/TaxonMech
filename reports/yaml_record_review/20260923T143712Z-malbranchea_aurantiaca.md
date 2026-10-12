# YAML Record Review: Malbranchea aurantiaca

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/malbranchea_aurantiaca.yaml`
- Started UTC: 2026-09-23T14:34:00Z
- Finished UTC: 2026-09-23T14:37:12Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:78605`
- Label: `Malbranchea aurantiaca`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/malbranchea_aurantiaca.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/malawimonas_californiana_nom_ined.yaml data/taxa/eukaryota/malbranchea_aurantiaca.yaml data/taxa/eukaryota/malbranchea_cinnamomea.yaml data/taxa/eukaryota/mallocybe_terrigena.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/malbranchea_aurantiaca.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:11499` contains `NCBITaxon:78605`, label `Malbranchea aurantiaca`, rank `SPECIES`, parent `NCBITaxon:5040`, genetic code `1`, no exact synonyms, and one related synonym, matching the record.
- All 15 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:53327` has exactly one scope row for `NCBITaxon:78605`; its rule names `Malbranchea aurantiaca` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:42751` reports `organism_count=1` for `NCBITaxon:78605`, matching the YAML `GOLD` attestation.
- The native GOLD scan found the same single organism row, `Go0098942` / `Malbranchea aurantiaca RRC1813`, and one linked project, `Gp0098942`; no native analysis rows are linked to that project or organism.
- The NCBI type-material inventory has 11 type-material rows for `Malbranchea aurantiaca` covering `ATCC 34524`, `CBS 127.77`, `IFM 41301`, `IMI 211195`, and `UAMH 3599` variants. These rows are source evidence only and do not emit generated strain rows by themselves.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 27 exact direct rows and 32 deposit rows for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- The bounded scan and `rg --no-ignore --hidden` field-boundary search found no old merged IDs for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `malbranchea_aurantiaca` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

None.
