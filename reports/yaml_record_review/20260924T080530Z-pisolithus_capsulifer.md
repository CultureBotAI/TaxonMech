# YAML Record Review: Pisolithus capsulifer

- Verdict: pass
- Target: `data/taxa/eukaryota/pisolithus_capsulifer.yaml`
- Identifier: `NCBITaxon:936129`

## Target

Reviewed the complete 93-line YAML record for `Pisolithus capsulifer`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pisolithus_capsulifer`.

## Validation

- `just validate data/taxa/eukaryota/pisolithus_capsulifer.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pisolithus_capsulifer.yaml data/taxa/eukaryota/pisolithus_croceorrhizus.yaml data/taxa/eukaryota/pisolithus_marmoratus.yaml data/taxa/eukaryota/pisolithus_microcarpus.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:198181` is the exact retained NCBITaxon row for `NCBITaxon:936129`: label `Pisolithus capsulifer`, rank `SPECIES`, parent `NCBITaxon:37467`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:56956` contains the seeded in-scope row for `NCBITaxon:936129` with the reason `attested rule: Pisolithus capsulifer, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 5 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:936129`.

## Evidence

- `data/raw/gold_organisms.tsv:44812` is the aggregate GOLD row for `NCBITaxon:936129` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:325545`, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:274267` through `data/raw/ncbi_type_material.tsv:274272` contain the 6 exact NCBI type-material rows for `NCBITaxon:936129`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:936129`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:936129`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The six NCBI type-material rows are equivalent holotype designations for the `Lycoperdon capsuliferum` synonym and do not imply generated strain rows.
