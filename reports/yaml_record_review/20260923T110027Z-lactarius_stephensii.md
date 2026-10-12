# YAML Record Review: Lactarius stephensii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lactarius_stephensii.yaml
- Started UTC: 2026-09-23T11:00:27Z
- Finished UTC: 2026-09-23T11:00:27Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lactarius_stephensii.yaml` denotes the exact NCBI species `Lactarius stephensii` as `NCBITaxon:239217`, rank `SPECIES`, under genus `NCBITaxon:34444` (`Lactarius`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lactarius_stephensii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lactarius_sanguifluus.yaml data/taxa/eukaryota/lactarius_sp_in_basidiomycete_fungi.yaml data/taxa/eukaryota/lactarius_stephensii.yaml data/taxa/eukaryota/lactarius_subdulcis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:46961` carries `NCBITaxon:239217`, label `Lactarius stephensii`, rank `SPECIES`, parent `NCBITaxon:34444`, genetic code `1`, exact synonyms `Hydnangium stephensii` and `Zelleromyces stephensii`, and the related synonyms retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lactarius`.
- `curation/seed_scope.tsv:54695` contains this identifier with reason `attested rule: Lactarius stephensii, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:18261` maps side-inventory old ID `NCBITaxon:150807` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:21971`, whose aggregate count is `2` for `NCBITaxon:239217`.
- The current native GOLD scan found no exact organism, project, or analysis rows for `NCBITaxon:239217`, so only the aggregate row currently supports the generated GOLD assertion count.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:239217` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:239217`, `just validate data/taxa/eukaryota/lactarius_stephensii.yaml`, and `just validate-strict data/taxa/eukaryota/lactarius_stephensii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lactarius_stephensii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
