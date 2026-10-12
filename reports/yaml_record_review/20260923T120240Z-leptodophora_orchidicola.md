# YAML Record Review: Leptodophora orchidicola

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leptodophora_orchidicola.yaml
- Started UTC: 2026-09-23T12:02:40Z
- Finished UTC: 2026-09-23T12:02:40Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leptodophora_orchidicola.yaml` denotes the exact NCBI species `Leptodophora orchidicola` as `NCBITaxon:1732013`, rank `SPECIES`, under genus `NCBITaxon:2938194` (`Leptodophora`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leptodophora_orchidicola.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/leptocylindrus_aporus.yaml data/taxa/eukaryota/leptocylindrus_danicus.yaml data/taxa/eukaryota/leptodontidium_sp_2_pmi_412.yaml data/taxa/eukaryota/leptodophora_orchidicola.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:451466` carries `NCBITaxon:1732013`, label `Leptodophora orchidicola`, rank `SPECIES`, parent `NCBITaxon:2938194`, genetic code `1`, exact synonyms `Cadophora orchidicola` and `Leptodontidium orchidicola`, three related synonyms, and snapshot `2026-09-13`.
- The 15 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leptodophora` genus.
- `curation/seed_scope.tsv:61166` contains this identifier with reason `attested rule: Leptodophora orchidicola, 2 sources incl. NCBI`.
- The side NCBI merge scan found old ID `NCBITaxon:75375` retired into `NCBITaxon:1732013`, but no retained retired rows were present, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:15009`, whose aggregate count is `1` for `NCBITaxon:1732013`.
- The current native GOLD scan found exact organism `Go0529089` for `Leptodontidium orchidicola CORFU0008`, projects `Gp0457397` and `Gp0466639`, and no exact native analysis rows for this NCBI ID.
- Exact StrainInfo scans found 19 direct strains and 23 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:55445` through `55448` contain four holotype spellings of `UAMH 5422` for `NCBITaxon:1732013`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1732013`, `just validate data/taxa/eukaryota/leptodophora_orchidicola.yaml`, and `just validate-strict data/taxa/eukaryota/leptodophora_orchidicola.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leptodophora_orchidicola` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
