# YAML Record Review: Lasiosphaeria ovina

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lasiosphaeria_ovina.yaml
- Started UTC: 2026-09-23T11:18:46Z
- Finished UTC: 2026-09-23T11:18:46Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lasiosphaeria_ovina.yaml` denotes the exact NCBI species `Lasiosphaeria ovina` as `NCBITaxon:92902`, rank `SPECIES`, under genus `NCBITaxon:92901` (`Lasiosphaeria`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lasiosphaeria_ovina.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lasiosphaeria_hispida.yaml data/taxa/eukaryota/lasiosphaeria_miniovina.yaml data/taxa/eukaryota/lasiosphaeria_ovina.yaml data/taxa/eukaryota/lasiosphaeria_similisorbina.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:15240` carries `NCBITaxon:92902`, label `Lasiosphaeria ovina`, rank `SPECIES`, parent `NCBITaxon:92901`, genetic code `1`, exact synonym `Sphaeria ovina`, and the related synonyms retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lasiosphaeria`.
- `curation/seed_scope.tsv:53538` contains this identifier with reason `attested rule: Lasiosphaeria ovina, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:92902`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:44603`, whose aggregate count is `1` for `NCBITaxon:92902`.
- The current native GOLD scan found exact organism `Go0358433` for `Lasiosphaeria ovina CBS 958.72`, projects `Gp0197105` and `Gp0251468`, and one native analysis row linked through `Gp0197105`.
- Exact StrainInfo scans found 3 direct strains and 4 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:92902` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:92902`, `just validate data/taxa/eukaryota/lasiosphaeria_ovina.yaml`, and `just validate-strict data/taxa/eukaryota/lasiosphaeria_ovina.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lasiosphaeria_ovina` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
