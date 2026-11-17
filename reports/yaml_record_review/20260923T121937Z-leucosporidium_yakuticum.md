# YAML Record Review: Leucosporidium yakuticum

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leucosporidium_yakuticum.yaml
- Started UTC: 2026-09-23T12:19:37Z
- Finished UTC: 2026-09-23T12:19:37Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leucosporidium_yakuticum.yaml` denotes the exact NCBI species `Leucosporidium yakuticum` as `NCBITaxon:231218`, rank `SPECIES`, under genus `NCBITaxon:5277` (`Leucosporidium`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leucosporidium_yakuticum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/leucosporidium_scottii.yaml data/taxa/eukaryota/leucosporidium_yakuticum.yaml data/taxa/eukaryota/leyanella_arenaria.yaml data/taxa/eukaryota/liangdongia_berthetii.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:45431` carries `NCBITaxon:231218`, label `Leucosporidium yakuticum`, rank `SPECIES`, parent `NCBITaxon:5277`, genetic code `1`, exact synonyms `Leucosporidiella yakutica` and `Rhodotorula yakutica`, two related synonyms, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leucosporidium` genus.
- `curation/seed_scope.tsv:54655` contains this identifier with reason `attested rule: Leucosporidium yakuticum, 2 sources incl. NCBI`.
- The side NCBI merge scan found old ID `NCBITaxon:1495456` retired into `NCBITaxon:231218`; an ignored-inclusive `rg --no-ignore --hidden` search found no retained row for that old ID in `data/raw/ncbitaxon_taxa.tsv`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:21664`, whose aggregate count is `3` for `NCBITaxon:231218`.
- The current native GOLD scan found exact organisms `Go0647368`, `Go0647369`, and `Go0647370`, projects `Gp0683435`, `Gp0683436`, and `Gp0683437`, and three native analysis rows linked through `AP PROJECT GOLD IDS` to those projects.
- Exact StrainInfo scans found 2 direct strains and 5 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:92472` through `92476` contain five type-material spellings for `Rhodotorula yakutica`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:231218`, `just validate data/taxa/eukaryota/leucosporidium_yakuticum.yaml`, and `just validate-strict data/taxa/eukaryota/leucosporidium_yakuticum.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leucosporidium_yakuticum` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
