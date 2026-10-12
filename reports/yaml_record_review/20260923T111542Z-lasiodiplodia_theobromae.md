# YAML Record Review: Lasiodiplodia theobromae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lasiodiplodia_theobromae.yaml
- Started UTC: 2026-09-23T11:15:42Z
- Finished UTC: 2026-09-23T11:15:42Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lasiodiplodia_theobromae.yaml` denotes the exact NCBI species `Lasiodiplodia theobromae` as `NCBITaxon:45133`, rank `SPECIES`, under genus `NCBITaxon:66739` (`Lasiodiplodia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lasiodiplodia_theobromae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lasiodiplodia_citricola.yaml data/taxa/eukaryota/lasiodiplodia_pseudotheobromae.yaml data/taxa/eukaryota/lasiodiplodia_theobromae.yaml data/taxa/eukaryota/lasiosphaeria_deviata.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:5492` carries `NCBITaxon:45133`, label `Lasiodiplodia theobromae`, rank `SPECIES`, parent `NCBITaxon:66739`, genetic code `1`, exact synonyms `Botryodiplodia theobromae`, `Botryosphaeria rhodina`, `Diplodia gossypina`, and `Physalospora rhodina`, and the related synonyms retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lasiodiplodia`.
- `curation/seed_scope.tsv:52604` contains this identifier with reason `attested rule: Lasiodiplodia theobromae, 2 sources incl. NCBI`.
- Four `data/raw/ncbi_merged_ids.tsv` rows map side-inventory old IDs `NCBITaxon:1620406`, `NCBITaxon:2906518`, `NCBITaxon:502207`, and `NCBITaxon:66740` into this current taxon, but no retained raw NCBI taxon rows exist for those old IDs, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:35864`, whose aggregate count is `8` for `NCBITaxon:45133`.
- The current native GOLD scan found eight exact organisms: `Go0098872`, `Go0384577`, `Go0632129`, `Go0677962`, `Go0677965`, `Go0677966`, `Go0677967`, and `Go0685757`.
- Expanding those exact GOLD organisms found eight projects, one per organism, and seven native analysis rows linked through all exact projects except `Gp0098872`.
- Exact StrainInfo scans found 98 direct strains and 120 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.
- Exact scans found two culture-from-neotype rows in `data/raw/ncbi_type_material.tsv:213610-213611` for source taxon name `Botryodiplodia theobromae`, matching the generated type-material assertions for `CBS 164.96` variants.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found all two `NCBITaxon:45133` type-material rows in `data/raw/ncbi_type_material.tsv`, matching the generated culture-from-neotype assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:45133`, `just validate data/taxa/eukaryota/lasiodiplodia_theobromae.yaml`, and `just validate-strict data/taxa/eukaryota/lasiodiplodia_theobromae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lasiodiplodia_theobromae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Native GOLD organism, project, and analysis evidence was expanded from exact IDs in `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, and `data/gold/analyses.jsonl.gz`.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
