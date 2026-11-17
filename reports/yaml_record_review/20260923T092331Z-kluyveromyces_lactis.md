# YAML Record Review: Kluyveromyces lactis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kluyveromyces_lactis.yaml
- Started UTC: 2026-09-23T09:23:31Z
- Finished UTC: 2026-09-23T09:23:31Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kluyveromyces_lactis.yaml` denotes the exact NCBI species `Kluyveromyces lactis` as `NCBITaxon:28985`, rank `SPECIES`, under genus `NCBITaxon:4910` (`Kluyveromyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kluyveromyces_lactis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kluyveromyces_aestuarii.yaml data/taxa/eukaryota/kluyveromyces_dobzhanskii.yaml data/taxa/eukaryota/kluyveromyces_lactis.yaml data/taxa/eukaryota/kluyveromyces_marxianus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2995` carries `NCBITaxon:28985`, label `Kluyveromyces lactis`, rank `SPECIES`, parent `NCBITaxon:4910`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kluyveromyces`.
- `curation/seed_scope.tsv:52183` contains this identifier with reason `attested rule: Kluyveromyces lactis, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old ID `NCBITaxon:58628`, but that old ID is not present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:28259`, whose aggregate count is `4` for `NCBITaxon:28985`.
- The current native GOLD scan found exact organisms `Go0384380`, `Go0591383`, `Go0705662`, and `Go0705663`, with exact projects `Gp0235474`, `Gp0605329`, `Gp0831713`, and `Gp0831714`.
- The native GOLD analysis scan found two exact linked analyses, `Kluyveromyces lactis GG799` and `Kluyveromyces lactis CBS 2105`.
- StrainInfo has 273 exact direct rows and 462 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 12 rows for `NCBITaxon:28985` at lines 138004-138015, covering `CBS 2105` and `NRRL Y-8278` Saccharomyces drosophilarum type material, `NRRL Y-8279` Torulaspora lactis culture from neotype variants, and `ATCC 56498` / `CBS 683` Torulaspora lactis type material.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:28985`, `just validate data/taxa/eukaryota/kluyveromyces_lactis.yaml`, and `just validate-strict data/taxa/eukaryota/kluyveromyces_lactis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kluyveromyces_lactis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
