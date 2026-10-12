# YAML Record Review: Lactarius trivialis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lactarius_trivialis.yaml
- Started UTC: 2026-09-23T11:03:17Z
- Finished UTC: 2026-09-23T11:03:17Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lactarius_trivialis.yaml` denotes the exact NCBI species `Lactarius trivialis` as `NCBITaxon:217427`, rank `SPECIES`, under genus `NCBITaxon:34444` (`Lactarius`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lactarius_trivialis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lactarius_tabidus.yaml data/taxa/eukaryota/lactarius_trivialis.yaml data/taxa/eukaryota/lactarius_vividus.yaml data/taxa/eukaryota/lactifluus_echinatus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:42860` carries `NCBITaxon:217427`, label `Lactarius trivialis`, rank `SPECIES`, parent `NCBITaxon:34444`, genetic code `1`, exact synonym `Agaricus trivialis`, and the related synonyms retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lactarius`.
- `curation/seed_scope.tsv:54570` contains this identifier with reason `attested rule: Lactarius trivialis, 2 sources incl. NCBI`.
- The side-inventory NCBI merged-ID scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:20758`, whose aggregate count is `1` for `NCBITaxon:217427`.
- The current native GOLD scan found exact organism `Go0518074` for `Lactarius trivialis MG71`.
- Expanding that exact GOLD organism found project `Gp0442143` and one native analysis row linked through that project ID.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:217427` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:217427`, `just validate data/taxa/eukaryota/lactarius_trivialis.yaml`, and `just validate-strict data/taxa/eukaryota/lactarius_trivialis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lactarius_trivialis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
