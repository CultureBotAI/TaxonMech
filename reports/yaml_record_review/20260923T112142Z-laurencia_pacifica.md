# YAML Record Review: Laurencia pacifica

- Repository: TaxonMech
- Record: data/taxa/eukaryota/laurencia_pacifica.yaml
- Started UTC: 2026-09-23T11:21:42Z
- Finished UTC: 2026-09-23T11:21:42Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/laurencia_pacifica.yaml` denotes the exact NCBI species `Laurencia pacifica` as `NCBITaxon:290688`, rank `SPECIES`, under genus `NCBITaxon:99900` (`Laurencia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/laurencia_pacifica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lasiosphaeris_hirsuta.yaml data/taxa/eukaryota/laurencia_pacifica.yaml data/taxa/eukaryota/laxitextum_bicolor.yaml data/taxa/eukaryota/leccinellum_crocipodium.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:59317` carries `NCBITaxon:290688`, label `Laurencia pacifica`, rank `SPECIES`, parent `NCBITaxon:99900`, genetic code `1`, and the related synonym retained in the generated record.
- The 10 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Laurencia`.
- `curation/seed_scope.tsv:55015` contains this identifier with reason `attested rule: Laurencia pacifica, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:290688`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:28392`, whose aggregate count is `1` for `NCBITaxon:290688`.
- The current native GOLD scan found no exact organism, project, or analysis rows for NCBI taxon ID `290688`; the generated GOLD assertion is supported by the maintained aggregate row.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:290688` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:290688`, `just validate data/taxa/eukaryota/laurencia_pacifica.yaml`, and `just validate-strict data/taxa/eukaryota/laurencia_pacifica.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `laurencia_pacifica` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
