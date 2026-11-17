# YAML Record Review: Pleosporales sp.

- Verdict: pass
- Target: `data/taxa/eukaryota/pleosporales_sp.yaml`
- Identifier: `NCBITaxon:1755443`

## Target

Reviewed the complete 74-line YAML record for `Pleosporales sp.`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pleosporales_sp`.

## Validation

- `just validate data/taxa/eukaryota/pleosporales_sp.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pleosporaceae_sp.yaml data/taxa/eukaryota/pleosporales_sp.yaml data/taxa/eukaryota/pleostigma_alpinum.yaml data/taxa/eukaryota/pleostigma_frigidum.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:458020` is the exact retained NCBITaxon row for `NCBITaxon:1755443`: label `Pleosporales sp.`, rank `SPECIES`, parent `NCBITaxon:92862`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:61207` contains the seeded in-scope row for `NCBITaxon:1755443` with the reason `attested rule: Pleosporales sp., 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 0 related synonyms, and 0 broad synonyms.
- All 15 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:1755443`.

## Evidence

- `data/raw/gold_organisms.tsv:15265` is the aggregate GOLD row for `NCBITaxon:1755443` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:1755443`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1755443`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1755443`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No additional notes.
