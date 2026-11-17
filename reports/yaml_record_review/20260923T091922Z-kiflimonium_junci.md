# YAML Record Review: Kiflimonium junci

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kiflimonium_junci.yaml
- Started UTC: 2026-09-23T09:19:22Z
- Finished UTC: 2026-09-23T09:19:22Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kiflimonium_junci.yaml` denotes the exact NCBI species `Kiflimonium junci` as `NCBITaxon:2888297`, rank `SPECIES`, under genus `NCBITaxon:2502756` (`Kiflimonium`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kiflimonium_junci.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kickxella_alabastrina.yaml data/taxa/eukaryota/kiflimonium_junci.yaml data/taxa/eukaryota/kipferlia_bialata.yaml data/taxa/eukaryota/kirkomyces_cordensis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:568302` carries `NCBITaxon:2888297`, label `Kiflimonium junci`, rank `SPECIES`, parent `NCBITaxon:2502756`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kiflimonium`.
- `curation/seed_scope.tsv:63362` contains this identifier with reason `attested rule: Kiflimonium junci, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:28141`, whose aggregate count is `1` for `NCBITaxon:2888297`.
- The current native GOLD scan found no exact organism, project, or analysis rows for `NCBITaxon:2888297`.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 6 rows for `NCBITaxon:2888297` at lines 136639-136644, covering `CBS 148279` and `CPC 41222` cultures from holotype plus `CBS H-24825` holotype variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:2888297`, `just validate data/taxa/eukaryota/kiflimonium_junci.yaml`, and `just validate-strict data/taxa/eukaryota/kiflimonium_junci.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kiflimonium_junci` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
