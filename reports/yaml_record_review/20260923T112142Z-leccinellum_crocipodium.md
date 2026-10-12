# YAML Record Review: Leccinellum crocipodium

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leccinellum_crocipodium.yaml
- Started UTC: 2026-09-23T11:21:42Z
- Finished UTC: 2026-09-23T11:21:42Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leccinellum_crocipodium.yaml` denotes the exact NCBI species `Leccinellum crocipodium` as `NCBITaxon:1355219`, rank `SPECIES`, under genus `NCBITaxon:1256249` (`Leccinellum`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leccinellum_crocipodium.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lasiosphaeris_hirsuta.yaml data/taxa/eukaryota/laurencia_pacifica.yaml data/taxa/eukaryota/laxitextum_bicolor.yaml data/taxa/eukaryota/leccinellum_crocipodium.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:327506` carries `NCBITaxon:1355219`, label `Leccinellum crocipodium`, rank `SPECIES`, parent `NCBITaxon:1256249`, genetic code `1`, exact synonyms `Boletus crocipodius Letell., 1839`, `Krombholzia crocipodia`, `Leccinum crocipodium`, and `Trachypus crocipodius`, and the related synonyms retained in the generated record.
- The 15 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Leccinellum`.
- `curation/seed_scope.tsv:59638` contains this identifier with reason `attested rule: Leccinellum crocipodium, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:7932` maps side-inventory old ID `NCBITaxon:121048` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:8627`, whose aggregate count is `1` for `NCBITaxon:1355219`.
- The current native GOLD scan found exact organism `Go0670101` for `Leccinellum crocipodium Chpx2016` and project `Gp0762175`, with no native analysis rows.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:1355219` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1355219`, `just validate data/taxa/eukaryota/leccinellum_crocipodium.yaml`, and `just validate-strict data/taxa/eukaryota/leccinellum_crocipodium.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leccinellum_crocipodium` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
