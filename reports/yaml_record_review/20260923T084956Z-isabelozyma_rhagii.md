# YAML Record Review: Isabelozyma rhagii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/isabelozyma_rhagii.yaml
- Started UTC: 2026-09-23T08:49:56Z
- Finished UTC: 2026-09-23T08:49:56Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/isabelozyma_rhagii.yaml` denotes `Isabelozyma rhagii` as `NCBITaxon:2879429`, rank `SPECIES`, under parent `NCBITaxon:3312684` (`Isabelozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/isabelozyma_rhagii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/isabelozyma_rhagii.yaml data/taxa/eukaryota/ischnoderma_benzoinum.yaml data/taxa/eukaryota/isochrysis_galbana.yaml data/taxa/eukaryota/isochrysis_sp.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:567031` carries `NCBITaxon:2879429`, label `Isabelozyma rhagii`, rank `SPECIES`, parent `NCBITaxon:3312684`, genetic code `12`, four exact synonyms, and the five related authority-bearing synonyms emitted in YAML.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:63355` contains this identifier with reason `attested rule: Isabelozyma rhagii, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:79028` has side old ID `NCBITaxon:45581 -> NCBITaxon:2879429`, but no retained retired `ncbitaxon_taxa` row exists, so omitting `replaces` is expected.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:28020`, whose aggregate count is `1` for `NCBITaxon:2879429`.
- The current native GOLD organism scan found exact organism `Go0517044` for `Hyphopichia rhagii NRRL Y-2594`, with project `Gp0441082` and analysis `Hyphopichia rhagii NRRL Y-2594` joined through `AP PROJECT GOLD IDS=Gp0441082`.
- Exact `data/raw/ncbi_type_material.tsv` rows 135363-135382 record 20 `Candida rhagii` or `Candida tropicalis var. rhagii` type-material designations for `MUCL 29933`, `ATCC 22983`, `BCRC/CCRC 22428`, `CBS 4237`, `DBVPG 6153`, `IFO 10308`, `JCM 9839`, `NRRL Y-2594`, and `UCD 61-20` variants.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`, so the NCBI type-material and exact StrainInfo deposit strings do not have a local final BacDive strain surface to emit.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- StrainInfo has seven exact direct SI records and 25 exact deposits, but no final assembly, exclusion, or related-record rows for this taxon.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, StrainInfo, type-material, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:2879429`, `just validate data/taxa/eukaryota/isabelozyma_rhagii.yaml`, and `just validate-strict data/taxa/eukaryota/isabelozyma_rhagii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `isabelozyma_rhagii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
