# YAML Record Review: Russula ochroleuca

- Verdict: pass
- Target: `data/taxa/eukaryota/russula_ochroleuca.yaml`
- Identifier: `NCBITaxon:152965`

## Target

Reviewed the complete 75-line YAML record for Russula ochroleuca. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for russula_ochroleuca.

## Validation

- `just validate data/taxa/eukaryota/russula_ochroleuca.yaml` ran LinkML validation against `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/russula_ochroleuca.yaml data/taxa/eukaryota/russula_rubellipes.yaml data/taxa/eukaryota/russula_seminuda.yaml data/taxa/eukaryota/russula_sp.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv` retains `NCBITaxon:152965` at line 31870 with label `Russula ochroleuca`, rank `SPECIES`, parent `NCBITaxon:5402`, genetic code `1`, and an empty `retired_into` field.
- `data/raw/ncbitaxon_seed_scope.tsv` includes the target at line 54090 with reason `attested rule: Russula ochroleuca, 2 sources incl. NCBI`.
- The YAML preserves the NCBI synonym columns exactly: 0 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- The 13 YAML lineage entries all match the NCBI snapshot; no lineage entries were missing or mismatched.
- `data/raw/ncbi_merged_ids.tsv` has no merged-ID rows for `NCBITaxon:152965`, and no retained old IDs were available or required.

## Evidence

- The GOLD source attestation matches the aggregate `data/raw/gold_organisms.tsv` row at line 12140 for `NCBITaxon:152965`, whose `organism_count` is `2`.
- Native GOLD support was 1 analysis row, 2 organism rows, and 3 project rows; the generated YAML follows the aggregate organism count.
- `data/raw/ncbi_type_material.tsv` has 0 exact rows for `NCBITaxon:152965`, matching the absence of type-material-derived strain entries.
- BacDive had 0 exact rows for `NCBITaxon:152965`; StrainInfo had 0 direct exact JSONL rows and 0 exact deposits.

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
