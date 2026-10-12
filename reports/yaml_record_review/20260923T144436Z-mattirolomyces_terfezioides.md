# YAML Record Review: Mattirolomyces terfezioides

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/mattirolomyces_terfezioides.yaml`
- Started UTC: 2026-09-23T14:41:00Z
- Finished UTC: 2026-09-23T14:44:36Z
- Verdict: pass

## Target

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:74857`
- Label: `Mattirolomyces terfezioides`
- Rank/domain: `SPECIES` / `EUKARYOTA`
- Maintained status: generated from committed inventories and `curation/seed_scope.tsv`; future changes belong in upstream inventory generation or scope inputs, not by hand-editing this YAML.

## Validation

- `just validate data/taxa/eukaryota/mattirolomyces_terfezioides.yaml`: reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/martensiomyces_pterosporus.yaml data/taxa/eukaryota/martiniozyma_asiatica_nom_inval.yaml data/taxa/eukaryota/mastigamoeba_balamuthi.yaml data/taxa/eukaryota/mattirolomyces_terfezioides.yaml`: scanned 4 files with 0 files with `ERROR` and 0 total `ERROR` rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/mattirolomyces_terfezioides.yaml`: completed against NCBI, seed-scope, GOLD, BacDive, StrainInfo, generated strain, and auxiliary raw inventories.
- Full `just validate-history` and `just verify-corpus`: already passed on this checkout; not rerun per generated record.
- `just validate-products`: not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:10649` contains `NCBITaxon:74857`, label `Mattirolomyces terfezioides`, rank `SPECIES`, parent `NCBITaxon:665167`, genetic code `1`, 2 exact synonyms, and 2 related synonyms, matching the record.
- All 13 lineage entries in the YAML were present in `data/raw/ncbitaxon_taxa.tsv` with matching labels and ranks.
- `curation/seed_scope.tsv:53273` has exactly one scope row for `NCBITaxon:74857`; its rule names `Mattirolomyces terfezioides` with 2 sources including NCBI.

## Evidence

- The `NCBITAXON` source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row and carries the expected 2026-09-13 snapshot note.
- `data/raw/gold_organisms.tsv:42256` reports `organism_count=3` for `NCBITaxon:74857`, matching the YAML `GOLD` attestation.
- The current local native GOLD JSONL exact scan found 2 organism rows, `Go0036316` / `Mattirolomyces terfezioides MT.BST` and `Go0564611` / `Mattirolomyces terfezioides MAT_tt4AIII`, with 3 linked projects and no linked analyses.
- The bounded scan found no exact NCBI type-material rows for this taxon.

## Completeness

- `strain_count: 0` is consistent with zero exact rows in the generated BacDive, culture-collection, strain-assembly, strain-genome, and strain-related-record raw tables.
- StrainInfo has 1 exact direct row and 1 deposit row for this taxon, but no rows for this taxon are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no generated StrainInfo overlay is missing from the YAML.
- The bounded scan and `rg --no-ignore --hidden` field-boundary search found no old merged IDs for this taxon.
- The bounded scan found no exact LPSN, GTDB, Madin, BactoTraits, or MediaDive auxiliary rows for this taxon, so the absence of `nomenclature`, `taxonomy_mappings`, and non-NCBI trait fields is expected.
- Ignored-file coverage: `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 ...` covered the ignored `reports/` tree and found no prior `mattirolomyces_terfezioides` review report before this one was written.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- No corrective validator is needed for this record.

## Additional Notes

- Native GOLD JSONL currently has 2 exact organism rows for `NCBITaxon:74857` while the committed aggregate GOLD row reports 3; this review did not alter the aggregate inventory.
