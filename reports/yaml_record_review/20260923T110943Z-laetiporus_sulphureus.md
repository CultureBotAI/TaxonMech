# YAML Record Review: Laetiporus sulphureus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/laetiporus_sulphureus.yaml
- Started UTC: 2026-09-23T11:09:43Z
- Finished UTC: 2026-09-23T11:09:43Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/laetiporus_sulphureus.yaml` denotes the exact NCBI species `Laetiporus sulphureus` as `NCBITaxon:5630`, rank `SPECIES`, under genus `NCBITaxon:5629` (`Laetiporus`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/laetiporus_sulphureus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lactifluus_subvellereus.yaml data/taxa/eukaryota/lactifluus_volemus.yaml data/taxa/eukaryota/laetiporus_sulphureus.yaml data/taxa/eukaryota/lagenidium_giganteum.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2503` carries `NCBITaxon:5630`, label `Laetiporus sulphureus`, rank `SPECIES`, parent `NCBITaxon:5629`, genetic code `1`, exact synonyms `Laetiporus sulfureus` and `Sporotrichum versisporum`, and the related synonyms retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Laetiporus`.
- `curation/seed_scope.tsv:52048` contains this identifier with reason `attested rule: Laetiporus sulphureus, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:5630`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:38881`, whose aggregate count is `2` for `NCBITaxon:5630`.
- The current native GOLD scan found exact organisms `Go0025525` for `Laetiporus sulphureus 93-53 ss-1` and `Go0518076` for `Laetiporus sulphureus MG138`.
- Expanding those exact GOLD organisms found 14 projects: `Gp0025525`, `Gp0255026`, `Gp0255027`, `Gp0255028`, `Gp0255029`, `Gp0255030`, `Gp0255031`, `Gp0255032`, `Gp0255033`, `Gp0255034`, `Gp0255035`, `Gp0255036`, `Gp0255037`, and `Gp0442145`.
- The native GOLD analysis scan found one exact row for `Laetiporus sulphureus MG138`, linked through `Gp0442145`.
- Exact StrainInfo scans found 56 direct strains and 79 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.
- Exact scans found two reference-material rows in `data/raw/ncbi_type_material.tsv:235764-235765` for source taxon name `Boletus sulphureus Bull., 1789`, matching the type-material assertions for `CFMR:CT-1` and `CFMR:CT:1`.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found all two `NCBITaxon:5630` type-material rows in `data/raw/ncbi_type_material.tsv`, matching the generated reference-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:5630`, `just validate data/taxa/eukaryota/laetiporus_sulphureus.yaml`, and `just validate-strict data/taxa/eukaryota/laetiporus_sulphureus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `laetiporus_sulphureus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Native GOLD organism and project evidence was expanded from exact IDs in `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, and `data/gold/analyses.jsonl.gz`.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
