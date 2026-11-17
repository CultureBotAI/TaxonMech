# YAML Record Review: Ischnoderma benzoinum

- Repository: TaxonMech
- Record: data/taxa/eukaryota/ischnoderma_benzoinum.yaml
- Started UTC: 2026-09-23T08:49:56Z
- Finished UTC: 2026-09-23T08:49:56Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/ischnoderma_benzoinum.yaml` denotes `Ischnoderma benzoinum` as `NCBITaxon:139424`, rank `SPECIES`, under parent `NCBITaxon:139423` (`Ischnoderma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/ischnoderma_benzoinum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/isabelozyma_rhagii.yaml data/taxa/eukaryota/ischnoderma_benzoinum.yaml data/taxa/eukaryota/isochrysis_galbana.yaml data/taxa/eukaryota/isochrysis_sp.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:28173` carries `NCBITaxon:139424`, label `Ischnoderma benzoinum`, rank `SPECIES`, parent `NCBITaxon:139423`, genetic code `1`, exact synonym `Boletus benzoinus`, and the two related authority-bearing synonyms emitted in YAML.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:54007` contains this identifier with reason `attested rule: Ischnoderma benzoinum, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:9313`, whose aggregate count is `1` for `NCBITaxon:139424`.
- The current native GOLD organism scan found exact organism `Go0609061` for `Ischnoderma benzoinum IVC119`, with projects `Gp0620585` and `Gp0620586`; no native analysis row joined to those projects.
- StrainInfo has exact direct rows for 9 SI records and 12 exact deposits under this taxon, but no StrainInfo assembly, exclusion, or related-record rows and no exact BacDive-derived final strain rows.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found no type-material rows for `NCBITaxon:139424`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, StrainInfo, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:139424`, `just validate data/taxa/eukaryota/ischnoderma_benzoinum.yaml`, and `just validate-strict data/taxa/eukaryota/ischnoderma_benzoinum.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `ischnoderma_benzoinum` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
