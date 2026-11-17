# YAML Record Review: Isabelozyma heimii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/isabelozyma_heimii.yaml
- Started UTC: 2026-09-23T08:47:24Z
- Finished UTC: 2026-09-23T08:47:24Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/isabelozyma_heimii.yaml` denotes `Isabelozyma heimii` as `NCBITaxon:507511`, rank `SPECIES`, under parent `NCBITaxon:3312684` (`Isabelozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/isabelozyma_heimii.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/irpex_rosettiformis.yaml data/taxa/eukaryota/isabelozyma_gotoi.yaml data/taxa/eukaryota/isabelozyma_heimii.yaml data/taxa/eukaryota/isabelozyma_pseudorhagii.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:115344` carries `NCBITaxon:507511`, label `Isabelozyma heimii`, rank `SPECIES`, parent `NCBITaxon:3312684`, genetic code `12`, exact synonyms `Hyphopichia heimii (Pignal) Kurtzman, 2005|Pichia heimii`, and the two related synonyms emitted in YAML.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:55859` contains this identifier with reason `attested rule: Isabelozyma heimii, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has side old IDs `NCBITaxon:3312685` and `NCBITaxon:45503` merged into this target, but no retained retired `ncbitaxon_taxa` row exists, so omitting `replaces` is expected.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:37447`, whose aggregate count is `1` for `NCBITaxon:507511`.
- The current native GOLD organism scan found exact organism `Go0517069` for `Hyphopichia heimii NRRL Y-7502`, with projects `Gp0441107` and `Gp0780290`; two native analyses joined to those same two project IDs.
- Exact `data/raw/ncbi_type_material.tsv` rows 225579-225596 record 18 `Pichia heimii` culture-from-type-material or type-material designations for `CBS 6139`, `MUCL 31929`, `NRRL Y-7502`, `ATCC 22387`, `BCRC/CCRC 20410`, `IFO 1686`, `LY 1465`, and `NCYC 949` variants.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`, so the NCBI type-material and exact StrainInfo deposit strings do not have a local final BacDive strain surface to emit.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- StrainInfo has two exact direct SI records and nine exact deposits, but no final assembly, exclusion, or related-record rows for this taxon.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, StrainInfo, type-material, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:507511`, `just validate data/taxa/eukaryota/isabelozyma_heimii.yaml`, and `just validate-strict data/taxa/eukaryota/isabelozyma_heimii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `isabelozyma_heimii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
