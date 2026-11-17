# YAML Record Review: Leccinum duriusculum

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leccinum_duriusculum.yaml
- Started UTC: 2026-09-23T11:24:35Z
- Finished UTC: 2026-09-23T11:24:35Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leccinum_duriusculum.yaml` denotes the exact NCBI species `Leccinum duriusculum` as `NCBITaxon:121049`, rank `SPECIES`, under genus `NCBITaxon:80654` (`Leccinum`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leccinum_duriusculum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/leccinum_aurantiacum.yaml data/taxa/eukaryota/leccinum_duriusculum.yaml data/taxa/eukaryota/leccinum_sp.yaml data/taxa/eukaryota/leishmania_adleri.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:22735` carries `NCBITaxon:121049`, label `Leccinum duriusculum`, rank `SPECIES`, parent `NCBITaxon:80654`, genetic code `1`, exact synonym `Boletus duriusculus`, and the related synonyms retained in the generated record.
- The 15 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Leccinum`.
- `curation/seed_scope.tsv:53868` contains this identifier with reason `attested rule: Leccinum duriusculum, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:7917` and `data/raw/ncbi_merged_ids.tsv:7918` map side-inventory old IDs `NCBITaxon:121018` and `NCBITaxon:121019` into this current taxon, but no retained raw NCBI taxon rows exist for those old IDs, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:5013`, whose aggregate count is `1` for `NCBITaxon:121049`.
- The current native GOLD scan found no exact organism, project, or analysis rows for NCBI taxon ID `121049`; the generated GOLD assertion is supported by the maintained aggregate row.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:121049` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:121049`, `just validate data/taxa/eukaryota/leccinum_duriusculum.yaml`, and `just validate-strict data/taxa/eukaryota/leccinum_duriusculum.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leccinum_duriusculum` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
