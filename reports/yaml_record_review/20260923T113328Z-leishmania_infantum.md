# YAML Record Review: Leishmania infantum

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leishmania_infantum.yaml
- Started UTC: 2026-09-23T11:33:28Z
- Finished UTC: 2026-09-23T11:33:28Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leishmania_infantum.yaml` denotes the exact NCBI species `Leishmania infantum` as `NCBITaxon:5671`, rank `SPECIES`, under `NCBITaxon:38574` (`Leishmania donovani species complex`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leishmania_infantum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/leishmania_infantum.yaml data/taxa/eukaryota/leishmania_infantum_jpcm5.yaml data/taxa/eukaryota/leishmania_lainsoni.yaml data/taxa/eukaryota/leishmania_major_strain_friedlin.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2528` carries `NCBITaxon:5671`, label `Leishmania infantum`, rank `SPECIES`, parent `NCBITaxon:38574`, genetic code `1`, exact synonyms `Leishmania (Leishmania) infantum` and `Leishmania donovani infantum`, and the related synonym retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leishmania donovani species complex`.
- `curation/seed_scope.tsv:52063` contains this identifier with reason `attested rule: Leishmania infantum, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:86591` maps side-inventory old ID `NCBITaxon:5662` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:39023`, whose aggregate count is `1` for `NCBITaxon:5671`.
- The source-attestation note `Records filed directly under this taxon; descendant taxa are not gathered.` matches the exact scan: the current native GOLD scan found direct organism `Go0449074` for `Leishmania infantum TR01/Lin_TR01`, project `Gp0313476`, and one native analysis row, while the `JPCM5` child strain is represented by `NCBITaxon:435258`.
- Exact StrainInfo scans found 3 direct strains and 3 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:5671` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:5671`, `just validate data/taxa/eukaryota/leishmania_infantum.yaml`, and `just validate-strict data/taxa/eukaryota/leishmania_infantum.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leishmania_infantum` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
