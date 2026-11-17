# YAML Record Review: Intestinozyma alai

- Repository: TaxonMech
- Record: data/taxa/eukaryota/intestinozyma_alai.yaml
- Started UTC: 2026-09-23T08:41:45Z
- Finished UTC: 2026-09-23T08:41:45Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/intestinozyma_alai.yaml` denotes `Intestinozyma alai` as `NCBITaxon:434040`, rank `SPECIES`, under parent `NCBITaxon:3712554` (`Intestinozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/intestinozyma_alai.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/insectozyma_sakaeoensis.yaml data/taxa/eukaryota/insectozyma_verbasci.yaml data/taxa/eukaryota/insectozyma_xiaguanensis.yaml data/taxa/eukaryota/intestinozyma_alai.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:95736` carries `NCBITaxon:434040`, label `Intestinozyma alai`, rank `SPECIES`, parent `NCBITaxon:3712554`, genetic code `12`, exact synonym `Candida alai`, and the three related synonyms emitted in YAML.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:55640` contains this identifier with reason `attested rule: Intestinozyma alai, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:35382`, whose aggregate count is `1` for `NCBITaxon:434040`.
- The current native GOLD organism scan found exact organism `Go0705491` for `Candida alai NRRL Y-27739`, with project `Gp0831534`; no native analysis row joined to that project.
- Exact `data/raw/ncbi_type_material.tsv` rows 210103-210113 record 11 `Candida alai` type-material designations for `ATCC MYA-4364`, `BG 03-6-5-1-2`, `CBS 9899`, and `NRRL Y-27739` variants.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`, so the NCBI type-material strings do not have a local final BacDive strain surface to emit.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, type-material, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:434040`, `just validate data/taxa/eukaryota/intestinozyma_alai.yaml`, and `just validate-strict data/taxa/eukaryota/intestinozyma_alai.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `intestinozyma_alai` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
