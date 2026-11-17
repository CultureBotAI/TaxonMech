# YAML Record Review: Insectozyma sakaeoensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/insectozyma_sakaeoensis.yaml
- Started UTC: 2026-09-23T08:41:45Z
- Finished UTC: 2026-09-23T08:41:45Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/insectozyma_sakaeoensis.yaml` denotes `Insectozyma sakaeoensis` as `NCBITaxon:1217582`, rank `SPECIES`, under parent `NCBITaxon:3712553` (`Insectozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/insectozyma_sakaeoensis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/insectozyma_sakaeoensis.yaml data/taxa/eukaryota/insectozyma_verbasci.yaml data/taxa/eukaryota/insectozyma_xiaguanensis.yaml data/taxa/eukaryota/intestinozyma_alai.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:275531` carries `NCBITaxon:1217582`, label `Insectozyma sakaeoensis`, rank `SPECIES`, parent `NCBITaxon:3712553`, genetic code `12`, exact synonym `Candida sakaeoensis`, and the four related synonyms emitted in YAML.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:58440` contains this identifier with reason `attested rule: Insectozyma sakaeoensis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has side old IDs `NCBITaxon:992265` and `NCBITaxon:992266` merged into this target, but no retained retired `ncbitaxon_taxa` row exists, so omitting `replaces` is expected.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:5174`, whose aggregate count is `1` for `NCBITaxon:1217582`.
- The current native GOLD organism scan found exact organism `Go0705035` for `Candida sakaeoensis CBS 12318`, with project `Gp0831055`; no native analysis row joined to that project.
- Exact `data/raw/ncbi_type_material.tsv` rows 14534-14538 record 5 `Insectozyma sakaeoensis` holotype designations for `CBS 12318` variants and `LM078`.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`, so the NCBI type-material strings do not have a local final BacDive strain surface to emit.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, type-material, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1217582`, `just validate data/taxa/eukaryota/insectozyma_sakaeoensis.yaml`, and `just validate-strict data/taxa/eukaryota/insectozyma_sakaeoensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `insectozyma_sakaeoensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
