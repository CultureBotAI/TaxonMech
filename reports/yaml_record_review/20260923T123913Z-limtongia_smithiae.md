# YAML Record Review: Limtongia smithiae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/limtongia_smithiae.yaml
- Started UTC: 2026-09-23T12:39:13Z
- Finished UTC: 2026-09-23T12:39:13Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/limtongia_smithiae.yaml` denotes the exact NCBI species `Limtongia smithiae` as `NCBITaxon:1125753`, rank `SPECIES`, under genus `NCBITaxon:2862419` (`Limtongia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/limtongia_smithiae.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/limonomyces_culmigenus.yaml data/taxa/eukaryota/limtongella_incommunis.yaml data/taxa/eukaryota/limtongia_smithiae.yaml data/taxa/eukaryota/limtongozyma_cylindracea.yaml` exited successfully while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:244152` carries `NCBITaxon:1125753`, label `Limtongia smithiae`, rank `SPECIES`, parent `NCBITaxon:2862419`, genetic code `1`, two exact synonyms, three related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Limtongia` genus.
- `curation/seed_scope.tsv:57762` contains this identifier with reason `attested rule: Limtongia smithiae, 2 sources incl. NCBI`.
- The side NCBI merge scan found old ID `NCBITaxon:56419` retired into `NCBITaxon:1125753`; an ignored-inclusive `rg --no-ignore --hidden` search found no retained row for that old ID in `data/raw/ncbitaxon_taxa.tsv`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:2512`, whose aggregate count is `1` for `NCBITaxon:1125753`.
- The current native GOLD scan found one exact organism row, two exact projects, and no native analysis rows for this NCBI ID.
- Exact StrainInfo scans found 2 direct strains and 10 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:7827` through `7837` contain 11 type-material spellings for `Lipomyces smithiae`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:1125753`, `just validate data/taxa/eukaryota/limtongia_smithiae.yaml`, and `just validate-strict data/taxa/eukaryota/limtongia_smithiae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `limtongia_smithiae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
