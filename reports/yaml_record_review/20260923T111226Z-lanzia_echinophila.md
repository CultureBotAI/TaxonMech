# YAML Record Review: Lanzia echinophila

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lanzia_echinophila.yaml
- Started UTC: 2026-09-23T11:12:26Z
- Finished UTC: 2026-09-23T11:12:26Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lanzia_echinophila.yaml` denotes the exact NCBI species `Lanzia echinophila` as `NCBITaxon:1424426`, rank `SPECIES`, under genus `NCBITaxon:54683` (`Lanzia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lanzia_echinophila.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lankesteria_abbotti.yaml data/taxa/eukaryota/lanmaoa_asiatica.yaml data/taxa/eukaryota/lanzia_echinophila.yaml data/taxa/eukaryota/lasallia_pustulata.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:355120` carries `NCBITaxon:1424426`, label `Lanzia echinophila`, rank `SPECIES`, parent `NCBITaxon:54683`, genetic code `1`, exact synonyms `Ciboria echinophila`, `Hymenoscyphus echinophilus`, `Peziza echinophila`, `Phialea echinophila`, `Rutstroemia echinophila`, and `Sclerotinia echinophila`, and the related synonyms retained in the generated record.
- The 15 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lanzia`.
- `curation/seed_scope.tsv:60092` contains this identifier with reason `attested rule: Lanzia echinophila, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:1424426`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:10211`, whose aggregate count is `1` for `NCBITaxon:1424426`.
- The current native GOLD scan found exact organism `Go0106363` for `Lanzia echinophila CBS 111548`, project `Gp0106363`, and one native analysis row linked through `Gp0106363`.
- Exact StrainInfo scans found 3 direct strains and 3 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:1424426` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1424426`, `just validate data/taxa/eukaryota/lanzia_echinophila.yaml`, and `just validate-strict data/taxa/eukaryota/lanzia_echinophila.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lanzia_echinophila` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
