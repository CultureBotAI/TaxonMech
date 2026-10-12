# YAML Record Review: Leishmania guyanensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leishmania_guyanensis.yaml
- Started UTC: 2026-09-23T11:30:53Z
- Finished UTC: 2026-09-23T11:30:53Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leishmania_guyanensis.yaml` denotes the exact NCBI species `Leishmania guyanensis` as `NCBITaxon:5670`, rank `SPECIES`, under `NCBITaxon:38579` (`Leishmania guyanensis species complex`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leishmania_guyanensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leishmania_chagasi.yaml data/taxa/eukaryota/leishmania_donovani.yaml data/taxa/eukaryota/leishmania_enriettii.yaml data/taxa/eukaryota/leishmania_guyanensis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2527` carries `NCBITaxon:5670`, label `Leishmania guyanensis`, rank `SPECIES`, parent `NCBITaxon:38579`, genetic code `1`, exact synonyms `Leishmania (Viannia) guyanensis`, `Leishmania brasiliensis guyanensis`, `Leishmania brazilienis guyanensis`, and `Leishmania braziliensis guyanensis`, and the related synonym retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leishmania guyanensis species complex`.
- `curation/seed_scope.tsv:52062` contains this identifier with reason `attested rule: Leishmania guyanensis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:97444` maps side-inventory old ID `NCBITaxon:87235` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:39022`, whose aggregate count is `2` for `NCBITaxon:5670`.
- The current native GOLD scan found exact organisms `Go0047086`, `Go0572621`, and `Go0574633`, eight linked projects, and three native analysis rows.
- Exact StrainInfo scans found 1 direct strain and 1 deposit for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:5670` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:5670`, `just validate data/taxa/eukaryota/leishmania_guyanensis.yaml`, and `just validate-strict data/taxa/eukaryota/leishmania_guyanensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leishmania_guyanensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Native GOLD project evidence was expanded from exact IDs in `data/gold/organisms.jsonl.gz` and `data/gold/projects.jsonl.gz`.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
