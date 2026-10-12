# YAML Record Review: Lankesteria abbotti

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lankesteria_abbotti.yaml
- Started UTC: 2026-09-23T11:12:26Z
- Finished UTC: 2026-09-23T11:12:26Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lankesteria_abbotti.yaml` denotes the exact NCBI species `Lankesteria abbotti` as `NCBITaxon:340204`, rank `SPECIES`, under genus `NCBITaxon:340203` (`Lankesteria`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lankesteria_abbotti.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lankesteria_abbotti.yaml data/taxa/eukaryota/lanmaoa_asiatica.yaml data/taxa/eukaryota/lanzia_echinophila.yaml data/taxa/eukaryota/lasallia_pustulata.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:69777` carries `NCBITaxon:340204`, label `Lankesteria abbotti`, rank `SPECIES`, parent `NCBITaxon:340203`, genetic code `1`, and the related synonym retained in the generated record.
- The 11 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lankesteria`.
- `curation/seed_scope.tsv:55280` contains this identifier with reason `attested rule: Lankesteria abbotti, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:340204`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:32739`, whose aggregate count is `1` for `NCBITaxon:340204`.
- The current native GOLD scan found exact organism `Go0368717` for `Lankesteria abbotti Grappler Inlet BC` and no linked native projects or analyses.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:340204` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:340204`, `just validate data/taxa/eukaryota/lankesteria_abbotti.yaml`, and `just validate-strict data/taxa/eukaryota/lankesteria_abbotti.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lankesteria_abbotti` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
