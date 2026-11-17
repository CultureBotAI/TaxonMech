# YAML Record Review: Linnemannia sp.

- Repository: TaxonMech
- Record: data/taxa/eukaryota/linnemannia_sp.yaml
- Started UTC: 2026-09-23T13:03:46Z
- Finished UTC: 2026-09-23T13:03:46Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/linnemannia_sp.yaml` denotes the exact NCBI species `Linnemannia sp.` as `NCBITaxon:2810449`, rank `SPECIES`, under the NCBI placeholder parent `NCBITaxon:2810448` (`unclassified Linnemannia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/linnemannia_sp.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/linnemannia_sp.yaml data/taxa/eukaryota/linnemannia_zychae.yaml data/taxa/eukaryota/lipomyces_arxii.yaml data/taxa/eukaryota/lipomyces_chichibuensis.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:558407` carries `NCBITaxon:2810449`, label `Linnemannia sp.`, rank `SPECIES`, parent `NCBITaxon:2810448`, genetic code `1`, no synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in `NCBITaxon:2810448` (`unclassified Linnemannia`) under the expected `Linnemannia` genus.
- `curation/seed_scope.tsv:63278` contains this identifier with reason `attested rule: Linnemannia sp., 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:2810449`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:26976`, whose aggregate count is `3` for `NCBITaxon:2810449`.
- The native GOLD scan found three exact organisms for this NCBI ID: `Go0583252` for strain `MGC 79`, `Go0583273` for strain `WA 18942`, and `Go0583332` for strain `JL 2`.
- The native GOLD projects scan found one project for each of those three exact GOLD organisms and no analyses linked through their project IDs.
- Exact BacDive and StrainInfo scans found no rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- The exact NCBI type-material scan found no `data/raw/ncbi_type_material.tsv` rows for `NCBITaxon:2810449`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:2810449`, `just validate data/taxa/eukaryota/linnemannia_sp.yaml`, and `just validate-strict data/taxa/eukaryota/linnemannia_sp.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `linnemannia_sp` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
