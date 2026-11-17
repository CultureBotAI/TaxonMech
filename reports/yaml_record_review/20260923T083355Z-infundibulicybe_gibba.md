# YAML Record Review: Infundibulicybe gibba

- Repository: TaxonMech
- Record: data/taxa/eukaryota/infundibulicybe_gibba.yaml
- Started UTC: 2026-09-23T08:33:55Z
- Finished UTC: 2026-09-23T08:34:02Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/infundibulicybe_gibba.yaml` denotes `Infundibulicybe gibba` as `NCBITaxon:378275`, rank `SPECIES`, under parent `NCBITaxon:378268` (`Infundibulicybe`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/infundibulicybe_gibba.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/immersiella_caudata.yaml data/taxa/eukaryota/imperator_rhodopurpureus.yaml data/taxa/eukaryota/incertomyces_perditus.yaml data/taxa/eukaryota/infundibulicybe_gibba.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:79429` carries `NCBITaxon:378275`, label `Infundibulicybe gibba`, rank `SPECIES`, parent `NCBITaxon:378268`, genetic code `1`, exact synonyms `Agaricus gibbus|Clitocybe gibba`, and the two related authority-bearing synonyms emitted in YAML.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:55428` contains this identifier with reason `attested rule: Infundibulicybe gibba, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:68855` has side old ID `NCBITaxon:337232 -> NCBITaxon:378275`, but no retained retired `ncbitaxon_taxa` row exists, so omitting `replaces` is expected.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:33810`, whose aggregate count is `2` for `NCBITaxon:378275`.
- The current native GOLD organism scan found exact organisms `Go0136824` for `Infundibulicybe gibba IJFM A808` and `Go0403316` for `Clitocybe gibba IJFM A808`, with projects `Gp0141674` and `Gp0294981`; analysis `Infundibulicybe gibba IJFM A808 Standard Draft` joined through `AP PROJECT GOLD IDS=Gp0141674`.
- StrainInfo has six exact SI records for this taxon, but none has a BacDive-derived local strain link; exact scans found no final strain, genome, or related-record rows to emit from those SI records.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found no type-material rows for `NCBITaxon:378275`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, StrainInfo, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:378275`, `just validate data/taxa/eukaryota/infundibulicybe_gibba.yaml`, and `just validate-strict data/taxa/eukaryota/infundibulicybe_gibba.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `infundibulicybe_gibba` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
