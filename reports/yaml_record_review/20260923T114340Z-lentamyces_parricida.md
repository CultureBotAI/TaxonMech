# YAML Record Review: Lentamyces parricida

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lentamyces_parricida.yaml
- Started UTC: 2026-09-23T11:43:40Z
- Finished UTC: 2026-09-23T11:43:40Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lentamyces_parricida.yaml` denotes the exact NCBI species `Lentamyces parricida` as `NCBITaxon:327271`, rank `SPECIES`, under genus `NCBITaxon:565135` (`Lentamyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lentamyces_parricida.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leishmania_tarentolae.yaml data/taxa/eukaryota/leishmania_tropica.yaml data/taxa/eukaryota/leishmania_turanica.yaml data/taxa/eukaryota/lentamyces_parricida.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:66868` carries `NCBITaxon:327271`, label `Lentamyces parricida`, rank `SPECIES`, parent `NCBITaxon:565135`, genetic code `1`, exact synonyms `Absidia parricida` and `Lentamyces parricidus`, two related synonyms, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lentamyces` genus.
- `curation/seed_scope.tsv:55230` contains this identifier with reason `attested rule: Lentamyces parricida, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:327271`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:32187`, whose aggregate count is `1` for `NCBITaxon:327271`.
- The current native GOLD scan found exact organism `Go0515110` for `Lentamyces parricida NRRL 2409` and three linked projects: `Gp0435870`, `Gp0435871`, and `Gp0455841`. It found no linked native GOLD analysis rows.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:327271` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:327271`, `just validate data/taxa/eukaryota/lentamyces_parricida.yaml`, and `just validate-strict data/taxa/eukaryota/lentamyces_parricida.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lentamyces_parricida` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
