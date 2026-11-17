# YAML Record Review: Limonomyces culmigenus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/limonomyces_culmigenus.yaml
- Started UTC: 2026-09-23T12:39:13Z
- Finished UTC: 2026-09-23T12:39:13Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/limonomyces_culmigenus.yaml` denotes the exact NCBI species `Limonomyces culmigenus` as `NCBITaxon:228944`, rank `SPECIES`, under genus `NCBITaxon:228942` (`Limonomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/limonomyces_culmigenus.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/limonomyces_culmigenus.yaml data/taxa/eukaryota/limtongella_incommunis.yaml data/taxa/eukaryota/limtongia_smithiae.yaml data/taxa/eukaryota/limtongozyma_cylindracea.yaml` exited successfully while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:44799` carries `NCBITaxon:228944`, label `Limonomyces culmigenus`, rank `SPECIES`, parent `NCBITaxon:228942`, genetic code `1`, one exact synonym, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Limonomyces` genus.
- `curation/seed_scope.tsv:54634` contains this identifier with reason `attested rule: Limonomyces culmigenus, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:228944`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:21465`, whose aggregate count is `1` for `NCBITaxon:228944`.
- The current native GOLD scan found one exact organism row, one exact project, and one native analysis row linked through `AP PROJECT GOLD IDS`.
- Exact StrainInfo scans found 2 direct strains and 4 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no NCBI type-material rows for `NCBITaxon:228944`, matching the absence of embedded type-material evidence.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:228944`, `just validate data/taxa/eukaryota/limonomyces_culmigenus.yaml`, and `just validate-strict data/taxa/eukaryota/limonomyces_culmigenus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `limonomyces_culmigenus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
