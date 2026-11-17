# YAML Record Review: Leptodontidium sp. 2 PMI_412

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leptodontidium_sp_2_pmi_412.yaml
- Started UTC: 2026-09-23T12:02:40Z
- Finished UTC: 2026-09-23T12:02:40Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leptodontidium_sp_2_pmi_412.yaml` denotes the exact NCBI placeholder species `Leptodontidium sp. 2 PMI_412` as `NCBITaxon:1485227`, rank `SPECIES`, under `NCBITaxon:2639042` (`unclassified Leptodontidium`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leptodontidium_sp_2_pmi_412.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leptocylindrus_aporus.yaml data/taxa/eukaryota/leptocylindrus_danicus.yaml data/taxa/eukaryota/leptodontidium_sp_2_pmi_412.yaml data/taxa/eukaryota/leptodophora_orchidicola.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:380141` carries `NCBITaxon:1485227`, label `Leptodontidium sp. 2 PMI_412`, rank `SPECIES`, parent `NCBITaxon:2639042`, genetic code `1`, exact synonym `Leptodontium sp. PMI_412`, and snapshot `2026-09-13`.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `unclassified Leptodontidium` node.
- `curation/seed_scope.tsv:60258` contains this identifier with reason `attested rule: Leptodontidium sp. 2 PMI_412, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:1485227`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:11506`, whose aggregate count is `1` for `NCBITaxon:1485227`.
- The current native GOLD scan found exact organism `Go0040004` for `Leptodontidium sp. 2 PMI_412`, projects `Gp0040004` and `Gp0040043`, and no exact native analysis rows for this NCBI ID.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:1485227` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1485227`, `just validate data/taxa/eukaryota/leptodontidium_sp_2_pmi_412.yaml`, and `just validate-strict data/taxa/eukaryota/leptodontidium_sp_2_pmi_412.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leptodontidium_sp_2_pmi_412` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
