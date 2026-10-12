# YAML Record Review: Lentinellus vulpinus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lentinellus_vulpinus.yaml
- Started UTC: 2026-09-23T11:46:19Z
- Finished UTC: 2026-09-23T11:46:19Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lentinellus_vulpinus.yaml` denotes the exact NCBI species `Lentinellus vulpinus` as `NCBITaxon:156609`, rank `SPECIES`, under genus `NCBITaxon:5354` (`Lentinellus`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lentinellus_vulpinus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lentamyces_zychae.yaml data/taxa/eukaryota/lentinellus_vulpinus.yaml data/taxa/eukaryota/lentinula_aciculospora.yaml data/taxa/eukaryota/lentinula_aff_boryana.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:32523` carries `NCBITaxon:156609`, label `Lentinellus vulpinus`, rank `SPECIES`, parent `NCBITaxon:5354`, genetic code `1`, exact synonym `Agaricus vulpinus`, two related synonyms, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lentinellus` genus.
- `curation/seed_scope.tsv:54131` contains this identifier with reason `attested rule: Lentinellus vulpinus, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:156609`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:12578`, whose aggregate count is `1` for `NCBITaxon:156609`.
- The current native GOLD scan found exact organism `Go0111669` for `Lentinellus vulpinus AHS73672-sp`, linked projects `Gp0113744` and `Gp0113745`, and no linked native GOLD analysis rows.
- Exact StrainInfo scans found four direct strains and four deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:156609` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:156609`, `just validate data/taxa/eukaryota/lentinellus_vulpinus.yaml`, and `just validate-strict data/taxa/eukaryota/lentinellus_vulpinus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lentinellus_vulpinus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
