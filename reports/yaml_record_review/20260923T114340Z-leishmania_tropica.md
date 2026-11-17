# YAML Record Review: Leishmania tropica

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leishmania_tropica.yaml
- Started UTC: 2026-09-23T11:43:40Z
- Finished UTC: 2026-09-23T11:43:40Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leishmania_tropica.yaml` denotes the exact NCBI species `Leishmania tropica` as `NCBITaxon:5666`, rank `SPECIES`, under `NCBITaxon:38584` (`Leishmania tropica species complex`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leishmania_tropica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leishmania_tarentolae.yaml data/taxa/eukaryota/leishmania_tropica.yaml data/taxa/eukaryota/leishmania_turanica.yaml data/taxa/eukaryota/lentamyces_parricida.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2525` carries `NCBITaxon:5666`, label `Leishmania tropica`, rank `SPECIES`, parent `NCBITaxon:38584`, genetic code `1`, exact synonym `Leishmania (Leishmania) tropica`, two related synonyms, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leishmania tropica species complex`.
- `curation/seed_scope.tsv:52060` contains this identifier with reason `attested rule: Leishmania tropica, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:5666`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:39016`, whose aggregate count is `4` for `NCBITaxon:5666`.
- The current native GOLD scan found four exact organisms, four linked projects, and four native analysis rows for this NCBI ID.
- Exact StrainInfo scans found five direct strains and five deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:5666` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:5666`, `just validate data/taxa/eukaryota/leishmania_tropica.yaml`, and `just validate-strict data/taxa/eukaryota/leishmania_tropica.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leishmania_tropica` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
