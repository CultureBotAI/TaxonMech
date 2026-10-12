# YAML Record Review: Ruyongia tratensis

- Verdict: pass
- Target: `data/taxa/eukaryota/ruyongia_tratensis.yaml`
- Identifier: `NCBITaxon:942860`

## Target

Reviewed the complete 83-line YAML record for Ruyongia tratensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for ruyongia_tratensis.

## Validation

- `just validate data/taxa/eukaryota/ruyongia_tratensis.yaml` ran LinkML validation against `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ruyongia_namnaoensis.yaml data/taxa/eukaryota/ruyongia_ponderosae.yaml data/taxa/eukaryota/ruyongia_tratensis.yaml data/taxa/eukaryota/saccharata_proteae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv` retains `NCBITaxon:942860` at line 201298 with label `Ruyongia tratensis`, rank `SPECIES`, parent `NCBITaxon:3712559`, genetic code `1`, and an empty `retired_into` field.
- `data/raw/ncbitaxon_seed_scope.tsv` includes the target at line 57012 with reason `attested rule: Ruyongia tratensis, 2 sources incl. NCBI`.
- The YAML preserves the NCBI synonym columns exactly: 1 exact synonym, 3 related synonyms, and 0 broad synonyms.
- The 13 YAML lineage entries all match the NCBI snapshot; no lineage entries were missing or mismatched.
- `data/raw/ncbi_merged_ids.tsv` has no merged-ID rows for `NCBITaxon:942860`, and no retained old IDs were available or required.

## Evidence

- The GOLD source attestation matches the aggregate `data/raw/gold_organisms.tsv` row at line 44970 for `NCBITaxon:942860`, whose `organism_count` is `1`.
- Native GOLD support was 0 analysis rows, 1 organism row, and 1 project row; the generated YAML follows the aggregate organism count.
- `data/raw/ncbi_type_material.tsv` has 14 exact rows for `NCBITaxon:942860` at lines 274700-274713, all naming `Wickerhamomyces tratensis` type material.
- BacDive had 0 exact rows for `NCBITaxon:942860`; StrainInfo had 0 direct exact JSONL rows and 0 exact deposits.

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
