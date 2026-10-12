# YAML Record Review: Leccinum aurantiacum

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leccinum_aurantiacum.yaml
- Started UTC: 2026-09-23T11:24:35Z
- Finished UTC: 2026-09-23T11:24:35Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leccinum_aurantiacum.yaml` denotes the exact NCBI species `Leccinum aurantiacum` as `NCBITaxon:121046`, rank `SPECIES`, under genus `NCBITaxon:80654` (`Leccinum`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leccinum_aurantiacum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/leccinum_aurantiacum.yaml data/taxa/eukaryota/leccinum_duriusculum.yaml data/taxa/eukaryota/leccinum_sp.yaml data/taxa/eukaryota/leishmania_adleri.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:22734` carries `NCBITaxon:121046`, label `Leccinum aurantiacum`, rank `SPECIES`, parent `NCBITaxon:80654`, genetic code `1`, exact synonym `Boletus aurantiacus`, and the related synonyms retained in the generated record.
- The 15 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Leccinum`.
- `curation/seed_scope.tsv:53867` contains this identifier with reason `attested rule: Leccinum aurantiacum, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:121046`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:5012`, whose aggregate count is `1` for `NCBITaxon:121046`.
- The current native GOLD scan found no exact organism, project, or analysis rows for NCBI taxon ID `121046`; the generated GOLD assertion is supported by the maintained aggregate row.
- Exact StrainInfo scans found 3 direct strains and 5 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:121046` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:121046`, `just validate data/taxa/eukaryota/leccinum_aurantiacum.yaml`, and `just validate-strict data/taxa/eukaryota/leccinum_aurantiacum.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leccinum_aurantiacum` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
