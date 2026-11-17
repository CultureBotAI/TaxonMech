# YAML Record Review: Leishmania braziliensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leishmania_braziliensis.yaml
- Started UTC: 2026-09-23T11:27:11Z
- Finished UTC: 2026-09-23T11:27:11Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leishmania_braziliensis.yaml` denotes the exact NCBI species `Leishmania braziliensis` as `NCBITaxon:5660`, rank `SPECIES`, under `NCBITaxon:37617` (`Leishmania braziliensis species complex`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leishmania_braziliensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leishmania_aethiopica.yaml data/taxa/eukaryota/leishmania_amazonensis.yaml data/taxa/eukaryota/leishmania_braziliensis.yaml data/taxa/eukaryota/leishmania_braziliensis_mhom_br_75_m2904.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2520` carries `NCBITaxon:5660`, label `Leishmania braziliensis`, rank `SPECIES`, parent `NCBITaxon:37617`, genetic code `1`, exact synonyms `Leishmania (V.) braziliensis`, `Leishmania (Viannia) braziliensis`, and `Leishmania viannia`, and the related synonym retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leishmania braziliensis species complex`.
- `curation/seed_scope.tsv:52056` contains this identifier with reason `attested rule: Leishmania braziliensis, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:5660`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:38993`, whose aggregate count is `2` for `NCBITaxon:5660`.
- The source-attestation note `Records filed directly under this taxon; descendant taxa are not gathered.` matches the exact scan: the current native GOLD rows for `NCBITaxon:5660` are `Go0518236` and `Go0574632`, each with one project and one native analysis row, while the strain-level `NCBITaxon:420245` record is separate.
- Exact StrainInfo scans found 5 direct strains and 5 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:5660` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:5660`, `just validate data/taxa/eukaryota/leishmania_braziliensis.yaml`, and `just validate-strict data/taxa/eukaryota/leishmania_braziliensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leishmania_braziliensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
