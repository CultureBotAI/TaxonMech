# YAML Record Review: Lasiosphaeria miniovina

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lasiosphaeria_miniovina.yaml
- Started UTC: 2026-09-23T11:18:46Z
- Finished UTC: 2026-09-23T11:18:46Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lasiosphaeria_miniovina.yaml` denotes the exact NCBI species `Lasiosphaeria miniovina` as `NCBITaxon:1954250`, rank `SPECIES`, under genus `NCBITaxon:92901` (`Lasiosphaeria`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lasiosphaeria_miniovina.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lasiosphaeria_hispida.yaml data/taxa/eukaryota/lasiosphaeria_miniovina.yaml data/taxa/eukaryota/lasiosphaeria_ovina.yaml data/taxa/eukaryota/lasiosphaeria_similisorbina.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:504198` carries `NCBITaxon:1954250`, label `Lasiosphaeria miniovina`, rank `SPECIES`, parent `NCBITaxon:92901`, genetic code `1`, and the related synonyms retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lasiosphaeria`.
- `curation/seed_scope.tsv:61709` contains this identifier with reason `attested rule: Lasiosphaeria miniovina, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:1954250`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:17938`, whose aggregate count is `1` for `NCBITaxon:1954250`.
- The current native GOLD scan found exact organism `Go0358435` for `Lasiosphaeria miniovina SMH2392-1A`, projects `Gp0197112` and `Gp0251466`, and one native analysis row linked through `Gp0197112`.
- Exact scans found two holotype rows in `data/raw/ncbi_type_material.tsv:74451-74452` for `SMH 2392 (F)` variants.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found all two `NCBITaxon:1954250` type-material rows in `data/raw/ncbi_type_material.tsv`, matching the generated holotype assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1954250`, `just validate data/taxa/eukaryota/lasiosphaeria_miniovina.yaml`, and `just validate-strict data/taxa/eukaryota/lasiosphaeria_miniovina.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lasiosphaeria_miniovina` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
