# YAML Record Review: Ruyongia ponderosae

- Verdict: pass
- Target: `data/taxa/eukaryota/ruyongia_ponderosae.yaml`
- Identifier: `NCBITaxon:135456`

## Target

Reviewed the complete 79-line YAML record for Ruyongia ponderosae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for ruyongia_ponderosae.

## Validation

- `just validate data/taxa/eukaryota/ruyongia_ponderosae.yaml` ran LinkML validation against `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ruyongia_namnaoensis.yaml data/taxa/eukaryota/ruyongia_ponderosae.yaml data/taxa/eukaryota/ruyongia_tratensis.yaml data/taxa/eukaryota/saccharata_proteae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv` retains `NCBITaxon:135456` at line 27024 with label `Ruyongia ponderosae`, rank `SPECIES`, parent `NCBITaxon:3712559`, genetic code `1`, and an empty `retired_into` field.
- `data/raw/ncbitaxon_seed_scope.tsv` includes the target at line 53964 with reason `attested rule: Ruyongia ponderosae, 2 sources incl. NCBI`.
- The YAML preserves the NCBI synonym columns exactly: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- The 13 YAML lineage entries all match the NCBI snapshot; no lineage entries were missing or mismatched.
- `data/raw/ncbi_merged_ids.tsv` has no merged-ID rows for `NCBITaxon:135456`, and no retained old IDs were available or required.

## Evidence

- The GOLD source attestation matches the aggregate `data/raw/gold_organisms.tsv` row at line 8615 for `NCBITaxon:135456`, whose `organism_count` is `1`.
- Native GOLD support was 2 analysis rows, 1 organism row, and 2 project rows; the generated YAML follows the aggregate organism count.
- `data/raw/ncbi_type_material.tsv` has 6 exact rows for `NCBITaxon:135456` at lines 25383-25388, all naming `Candida ponderosae` type material.
- BacDive had 0 exact rows for `NCBITaxon:135456`; StrainInfo had 2 direct exact JSONL rows and 4 exact deposits, but no local generated StrainInfo overlay rows materialized for this target.

## Completeness

- Generated raw strain tables had 0 exact rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source scans all returned 0 exact rows across `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlays had 0 exact rows across `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No YAML edits were made during this read-only generated-record review.
