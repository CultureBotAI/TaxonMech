# YAML Record Review: Lasiosphaeria deviata

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lasiosphaeria_deviata.yaml
- Started UTC: 2026-09-23T11:15:42Z
- Finished UTC: 2026-09-23T11:15:42Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lasiosphaeria_deviata.yaml` denotes the exact NCBI species `Lasiosphaeria deviata` as `NCBITaxon:2850740`, rank `SPECIES`, under genus `NCBITaxon:92901` (`Lasiosphaeria`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lasiosphaeria_deviata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lasiodiplodia_citricola.yaml data/taxa/eukaryota/lasiodiplodia_pseudotheobromae.yaml data/taxa/eukaryota/lasiodiplodia_theobromae.yaml data/taxa/eukaryota/lasiosphaeria_deviata.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:564513` carries `NCBITaxon:2850740`, label `Lasiosphaeria deviata`, rank `SPECIES`, parent `NCBITaxon:92901`, genetic code `1`, and the related synonyms retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lasiosphaeria`.
- `curation/seed_scope.tsv:63309` contains this identifier with reason `attested rule: Lasiosphaeria deviata, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:2850740`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:27643`, whose aggregate count is `1` for `NCBITaxon:2850740`.
- The current native GOLD scan found exact organism `Go0651410` for `Lasiosphaeria deviata ANM Acc 1003` and two linked projects, `Gp0688314` and `Gp0699273`, with no native analysis rows.
- Exact scans found 13 rows in `data/raw/ncbi_type_material.tsv:131714-131726`: four culture-from-holotype `CBS 148319` variants, five holotype specimen variants, and four isotype `ILLS 00121498` variants.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found all 13 `NCBITaxon:2850740` type-material rows in `data/raw/ncbi_type_material.tsv`, matching the generated culture-from-holotype, holotype, and isotype assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:2850740`, `just validate data/taxa/eukaryota/lasiosphaeria_deviata.yaml`, and `just validate-strict data/taxa/eukaryota/lasiosphaeria_deviata.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lasiosphaeria_deviata` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- The exact `data/raw/ncbi_type_material.tsv` expansion used `rg --no-ignore --hidden`, so ignored files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
