# YAML Record Review: Lasallia pustulata

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lasallia_pustulata.yaml
- Started UTC: 2026-09-23T11:12:26Z
- Finished UTC: 2026-09-23T11:12:26Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lasallia_pustulata.yaml` denotes the exact NCBI species `Lasallia pustulata` as `NCBITaxon:136370`, rank `SPECIES`, under genus `NCBITaxon:87266` (`Lasallia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lasallia_pustulata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lankesteria_abbotti.yaml data/taxa/eukaryota/lanmaoa_asiatica.yaml data/taxa/eukaryota/lanzia_echinophila.yaml data/taxa/eukaryota/lasallia_pustulata.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:27270` carries `NCBITaxon:136370`, label `Lasallia pustulata`, rank `SPECIES`, parent `NCBITaxon:87266`, genetic code `1`, exact synonyms `Lichen pustulatus` and `Umbilicaria pustulata`, and the related synonyms retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lasallia`.
- `curation/seed_scope.tsv:53971` contains this identifier with reason `attested rule: Lasallia pustulata, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:136370`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:8781`, whose aggregate count is `3` for `NCBITaxon:136370`.
- The current native GOLD scan found exact organism `Go0114224` for `Umbilicaria pustulata Sardinia_28052013`, project `Gp0138618`, and one native analysis row linked through `Gp0138618`.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:136370` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:136370`, `just validate data/taxa/eukaryota/lasallia_pustulata.yaml`, and `just validate-strict data/taxa/eukaryota/lasallia_pustulata.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lasallia_pustulata` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
