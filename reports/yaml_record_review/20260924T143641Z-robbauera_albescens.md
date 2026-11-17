# YAML Record Review: Robbauera albescens

- Verdict: pass
- Target: `data/taxa/eukaryota/robbauera_albescens.yaml`
- Identifier: `NCBITaxon:58915`

## Target

Reviewed the complete 76-line YAML record for Robbauera albescens. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for robbauera_albescens.

## Validation

- `just validate data/taxa/eukaryota/robbauera_albescens.yaml` ran LinkML validation against `TaxonRecord` and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/rigidoporus_microporus.yaml data/taxa/eukaryota/robbauera_albescens.yaml data/taxa/eukaryota/rodentomyces_reticulatus.yaml data/taxa/eukaryota/roesleria_subterranea.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv` retains `NCBITaxon:58915` at line 7443 with label `Robbauera albescens`, rank `SPECIES`, parent `NCBITaxon:1804768`, genetic code `1`, and an empty `retired_into` field.
- `data/raw/ncbitaxon_seed_scope.tsv` includes the target at line 52999 with reason `attested rule: Robbauera albescens, 2 sources incl. NCBI`.
- The YAML preserves the NCBI synonym columns exactly: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- The 12 YAML lineage entries all match the NCBI snapshot; no lineage entries were missing or mismatched.
- `data/raw/ncbi_merged_ids.tsv` has no merged-ID rows for `NCBITaxon:58915`, and no retained old IDs were available or required.

## Evidence

- The GOLD source attestation matches the aggregate `data/raw/gold_organisms.tsv` row at line 39573 for `NCBITaxon:58915`, whose `organism_count` is `2`.
- Native GOLD support was 0 analysis rows, 2 organism rows, and 2 project rows; the generated YAML follows the aggregate organism count.
- `data/raw/ncbi_type_material.tsv` has 6 exact rows for `NCBITaxon:58915` at lines 239825-239830, all naming `Tilletiopsis albescens` type material.
- BacDive had 0 exact rows for `NCBITaxon:58915`; StrainInfo had 11 direct exact JSONL rows and 20 exact deposits, but no local generated StrainInfo overlay rows materialized for this target.

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
