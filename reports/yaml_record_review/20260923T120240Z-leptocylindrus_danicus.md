# YAML Record Review: Leptocylindrus danicus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leptocylindrus_danicus.yaml
- Started UTC: 2026-09-23T12:02:40Z
- Finished UTC: 2026-09-23T12:02:40Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leptocylindrus_danicus.yaml` denotes the exact NCBI species `Leptocylindrus danicus` as `NCBITaxon:163516`, rank `SPECIES`, under genus `NCBITaxon:163515` (`Leptocylindrus`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leptocylindrus_danicus.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/leptocylindrus_aporus.yaml data/taxa/eukaryota/leptocylindrus_danicus.yaml data/taxa/eukaryota/leptodontidium_sp_2_pmi_412.yaml data/taxa/eukaryota/leptodophora_orchidicola.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:33573` carries `NCBITaxon:163516`, label `Leptocylindrus danicus`, rank `SPECIES`, parent `NCBITaxon:163515`, genetic code `1`, related synonym `Leptocylindrus danicus Cleve, 1889`, and snapshot `2026-09-13`.
- The 11 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leptocylindrus` genus.
- `curation/seed_scope.tsv:54201` contains this identifier with reason `attested rule: Leptocylindrus danicus, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:163516`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:14007`, whose aggregate count is `3` for `NCBITaxon:163516`.
- The current native GOLD scan found exact organisms `Go0368719` and `Go0368720` and no exact native project or analysis rows for this NCBI ID.
- Exact StrainInfo scans found two direct strains and three deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:163516` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:163516`, `just validate data/taxa/eukaryota/leptocylindrus_danicus.yaml`, and `just validate-strict data/taxa/eukaryota/leptocylindrus_danicus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leptocylindrus_danicus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
