# YAML Record Review: Lipomyces starkeyi NRRL Y-11557

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lipomyces_starkeyi_nrrl_y_11557.yaml
- Started UTC: 2026-09-23T13:17:35Z
- Finished UTC: 2026-09-23T13:17:35Z
- Verdict: pass

## Target

Generated eukaryote strain record `data/taxa/eukaryota/lipomyces_starkeyi_nrrl_y_11557.yaml` denotes the exact NCBI strain `Lipomyces starkeyi NRRL Y-11557` as `NCBITaxon:675824`, rank `STRAIN`, under species `NCBITaxon:29829` (`Lipomyces starkeyi`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lipomyces_starkeyi_nrrl_y_11557.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lipomyces_spencermartinsiae.yaml data/taxa/eukaryota/lipomyces_starkeyi.yaml data/taxa/eukaryota/lipomyces_starkeyi_nrrl_y_11557.yaml data/taxa/eukaryota/lipomyces_tetrasporus.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:157421` carries `NCBITaxon:675824`, label `Lipomyces starkeyi NRRL Y-11557`, rank `STRAIN`, parent `NCBITaxon:29829`, genetic code `1`, no synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lipomyces starkeyi` species.
- `curation/seed_scope.tsv:56368` contains this identifier with reason `attested rule: Lipomyces starkeyi NRRL Y-11557, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:675824`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:41066`, whose aggregate count is `7` for `NCBITaxon:675824`.
- The full native GOLD organism scan found six exact organisms for this NCBI ID: `Go0000708`, `Go0608131`, `Go0608133`, `Go0608134`, `Go0608135`, and `Go0608136`.
- The native GOLD projects scan found three linked projects for `Go0000708`; the native GOLD analyses scan found two rows linked through `Gp0000708`.
- Exact BacDive and StrainInfo scans found no rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- The exact NCBI type-material scan found no `data/raw/ncbi_type_material.tsv` rows for `NCBITaxon:675824`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:675824`, `just validate data/taxa/eukaryota/lipomyces_starkeyi_nrrl_y_11557.yaml`, and `just validate-strict data/taxa/eukaryota/lipomyces_starkeyi_nrrl_y_11557.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lipomyces_starkeyi_nrrl_y_11557` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
