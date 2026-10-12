# YAML Record Review: Lactifluus volemus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lactifluus_volemus.yaml
- Started UTC: 2026-09-23T11:09:43Z
- Finished UTC: 2026-09-23T11:09:43Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lactifluus_volemus.yaml` denotes the exact NCBI species `Lactifluus volemus` as `NCBITaxon:71967`, rank `SPECIES`, under genus `NCBITaxon:596919` (`Lactifluus`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lactifluus_volemus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lactifluus_subvellereus.yaml data/taxa/eukaryota/lactifluus_volemus.yaml data/taxa/eukaryota/laetiporus_sulphureus.yaml data/taxa/eukaryota/lagenidium_giganteum.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:10076` carries `NCBITaxon:71967`, label `Lactifluus volemus`, rank `SPECIES`, parent `NCBITaxon:596919`, genetic code `1`, exact synonyms `Agaricus volemus`, `Galorrheus volemus`, and `Lactarius volemus`, and the related synonyms retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lactifluus`.
- `curation/seed_scope.tsv:53232` contains this identifier with reason `attested rule: Lactifluus volemus, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:71967`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:41957`, whose aggregate count is `2` for `NCBITaxon:71967`.
- The current native GOLD scan found exact organisms `Go0136940` for `Lactarius volemus BPL652` and `Go0518075` for `Lactarius volemus MG8`.
- Expanding those exact GOLD organisms found projects `Gp0141920`, `Gp0197070`, and `Gp0442144`, plus one native analysis row linked through `Gp0442144`.
- Exact scans found four epitype rows in `data/raw/ncbi_type_material.tsv:260300-260303` for source taxon name `Agaricus volemus`, matching the type-material assertions for `GENT: Kleine 03082011`, `GENT:collector:Jesko Kleine:03082011`, `JK 03082011`, and `Jesko Kleine 03082011`.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found all four `NCBITaxon:71967` type-material rows in `data/raw/ncbi_type_material.tsv`, matching the generated epitype assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:71967`, `just validate data/taxa/eukaryota/lactifluus_volemus.yaml`, and `just validate-strict data/taxa/eukaryota/lactifluus_volemus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lactifluus_volemus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
