# YAML Record Review: Lentinula detonsa

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lentinula_detonsa.yaml
- Started UTC: 2026-09-23T11:49:19Z
- Finished UTC: 2026-09-23T11:49:19Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lentinula_detonsa.yaml` denotes the exact NCBI species `Lentinula detonsa` as `NCBITaxon:2804962`, rank `SPECIES`, under genus `NCBITaxon:5352` (`Lentinula`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lentinula_detonsa.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lentinula_aff_detonsa.yaml data/taxa/eukaryota/lentinula_aff_lateritia.yaml data/taxa/eukaryota/lentinula_boryana.yaml data/taxa/eukaryota/lentinula_detonsa.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:557875` carries `NCBITaxon:2804962`, label `Lentinula detonsa`, rank `SPECIES`, parent `NCBITaxon:5352`, genetic code `1`, exact synonym `Lentinus detonsus`, two related synonyms, and snapshot `2026-09-13`.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lentinula` genus.
- `curation/seed_scope.tsv:63271` contains this identifier with reason `attested rule: Lentinula detonsa, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:2804962`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:26884`, whose aggregate count is `1` for `NCBITaxon:2804962`.
- The current native GOLD scan found exact organism `Go0367545` for `Lentinula detonsa TFB7810`, linked projects `Gp0207843` and `Gp0436656`, and no linked native GOLD analysis rows.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:124556` and `:124557` contain neotype spellings `TENN 53824` and `TENN:52824` for `NCBITaxon:2804962`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:2804962`, `just validate data/taxa/eukaryota/lentinula_detonsa.yaml`, and `just validate-strict data/taxa/eukaryota/lentinula_detonsa.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lentinula_detonsa` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
