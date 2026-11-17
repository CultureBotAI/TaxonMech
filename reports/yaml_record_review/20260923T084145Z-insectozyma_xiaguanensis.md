# YAML Record Review: Insectozyma xiaguanensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/insectozyma_xiaguanensis.yaml
- Started UTC: 2026-09-23T08:41:45Z
- Finished UTC: 2026-09-23T08:41:45Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/insectozyma_xiaguanensis.yaml` denotes `Insectozyma xiaguanensis` as `NCBITaxon:1586249`, rank `SPECIES`, under parent `NCBITaxon:3712553` (`Insectozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/insectozyma_xiaguanensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/insectozyma_sakaeoensis.yaml data/taxa/eukaryota/insectozyma_verbasci.yaml data/taxa/eukaryota/insectozyma_xiaguanensis.yaml data/taxa/eukaryota/intestinozyma_alai.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:410515` carries `NCBITaxon:1586249`, label `Insectozyma xiaguanensis`, rank `SPECIES`, parent `NCBITaxon:3712553`, genetic code `12`, exact synonym `Candida xiaguanensis F.L. Hui & X.J. Liu, 2016`, and the two related synonyms emitted in YAML.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:60538` contains this identifier with reason `attested rule: Insectozyma xiaguanensis, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:12817`, whose aggregate count is `1` for `NCBITaxon:1586249`.
- The current native GOLD organism scan found exact organism `Go0705082` for `Candida xiaguanensis CBS 13923`, with project `Gp0831103`; no native analysis row joined to that project.
- Exact `data/raw/ncbi_type_material.tsv` rows 44618-44623 record 6 `Candida xiaguanensis` type-material designations for `CICC 33056`, `NYNU 1488`, and `CBS 13923` variants.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`, so the NCBI type-material strings do not have a local final BacDive strain surface to emit.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, type-material, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1586249`, `just validate data/taxa/eukaryota/insectozyma_xiaguanensis.yaml`, and `just validate-strict data/taxa/eukaryota/insectozyma_xiaguanensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `insectozyma_xiaguanensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
