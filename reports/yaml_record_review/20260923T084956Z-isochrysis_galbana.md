# YAML Record Review: Isochrysis galbana

- Repository: TaxonMech
- Record: data/taxa/eukaryota/isochrysis_galbana.yaml
- Started UTC: 2026-09-23T08:49:56Z
- Finished UTC: 2026-09-23T08:49:56Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/isochrysis_galbana.yaml` denotes `Isochrysis galbana` as `NCBITaxon:37099`, rank `SPECIES`, under parent `NCBITaxon:37098` (`Isochrysis`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/isochrysis_galbana.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/isabelozyma_rhagii.yaml data/taxa/eukaryota/ischnoderma_benzoinum.yaml data/taxa/eukaryota/isochrysis_galbana.yaml data/taxa/eukaryota/isochrysis_sp.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4199` carries `NCBITaxon:37099`, label `Isochrysis galbana`, rank `SPECIES`, parent `NCBITaxon:37098`, genetic code `1`, and the eight related synonyms emitted in YAML.
- The 9 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:52366` contains this identifier with reason `attested rule: Isochrysis galbana, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has seven side old IDs merged into this target, including `NCBITaxon:2302108`, `NCBITaxon:337098`, and `NCBITaxon:76568`; no retained retired `ncbitaxon_taxa` rows exist, so omitting `replaces` is expected.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:33599`, whose aggregate count is `4` for `NCBITaxon:37099`.
- The current native GOLD organism scan found two exact organisms, `Go0368707` for `Isochrysis galbana CCMP 1323` and `Go0692375` for `Isochrysis galbana Dm2`; only project `Gp0803325` currently joins to those exact native organism IDs, and no native analysis row joined to that project.
- Exact `data/raw/ncbi_type_material.tsv` rows record `SAG 13.92` and `SAG:13.92` as type-material designations for `Isochrysis galbana`.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`, so the NCBI type-material and exact StrainInfo deposit strings do not have a local final BacDive strain surface to emit.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- StrainInfo has six exact direct SI records and 13 exact deposits, but no final assembly, exclusion, or related-record rows for this taxon.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, StrainInfo, type-material, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:37099`, `just validate data/taxa/eukaryota/isochrysis_galbana.yaml`, and `just validate-strict data/taxa/eukaryota/isochrysis_galbana.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `isochrysis_galbana` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
