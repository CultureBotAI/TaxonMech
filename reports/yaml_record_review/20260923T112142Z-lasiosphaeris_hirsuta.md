# YAML Record Review: Lasiosphaeris hirsuta

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lasiosphaeris_hirsuta.yaml
- Started UTC: 2026-09-23T11:21:42Z
- Finished UTC: 2026-09-23T11:21:42Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lasiosphaeris_hirsuta.yaml` denotes the exact NCBI species `Lasiosphaeris hirsuta` as `NCBITaxon:260670`, rank `SPECIES`, under genus `NCBITaxon:260669` (`Lasiosphaeris`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lasiosphaeris_hirsuta.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lasiosphaeris_hirsuta.yaml data/taxa/eukaryota/laurencia_pacifica.yaml data/taxa/eukaryota/laxitextum_bicolor.yaml data/taxa/eukaryota/leccinellum_crocipodium.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:53256` carries `NCBITaxon:260670`, label `Lasiosphaeris hirsuta`, rank `SPECIES`, parent `NCBITaxon:260669`, genetic code `1`, exact synonyms `Lasiosphaeria hirsuta` and `Sphaeria hirsuta`, and the related synonyms retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lasiosphaeris`.
- `curation/seed_scope.tsv:54834` contains this identifier with reason `attested rule: Lasiosphaeris hirsuta, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:64835` maps side-inventory old ID `NCBITaxon:314045` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:24007`, whose aggregate count is `1` for `NCBITaxon:260670`.
- The current native GOLD scan found exact organism `Go0358440` for `Lasiosphaeris hirsuta SMH4607-1`, projects `Gp0197117` and `Gp0251461`, and one native analysis row linked through `Gp0197117`.
- Exact StrainInfo scans found 3 direct strains and 3 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:260670` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:260670`, `just validate data/taxa/eukaryota/lasiosphaeris_hirsuta.yaml`, and `just validate-strict data/taxa/eukaryota/lasiosphaeris_hirsuta.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lasiosphaeris_hirsuta` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
