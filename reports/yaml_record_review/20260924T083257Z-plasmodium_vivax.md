# YAML Record Review: Plasmodium vivax

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_vivax.yaml`
- Identifier: `NCBITaxon:5855`

## Target

Reviewed the complete 76-line YAML record for `Plasmodium vivax`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_vivax`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_vivax.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plasmodium_vinckei_petteri.yaml data/taxa/eukaryota/plasmodium_vinckei_vinckei.yaml data/taxa/eukaryota/plasmodium_vivax.yaml data/taxa/eukaryota/plasmodium_vivax_sal_1.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2596` is the exact retained NCBITaxon row for `NCBITaxon:5855`: label `Plasmodium vivax`, rank `SPECIES`, parent `NCBITaxon:418103`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52098` contains the seeded in-scope row for `NCBITaxon:5855` with the reason `attested rule: Plasmodium vivax, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 3 related synonyms, and 0 broad synonyms.
- All 11 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:5855`.

## Evidence

- `data/raw/gold_organisms.tsv:39495` is the aggregate GOLD row for `NCBITaxon:5855` and reports `organism_count=4`, matching the YAML GOLD source attestation.
- Native GOLD has five exact organism rows, 193 linked project rows, and five linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:5855`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found seven exact local JSONL records, all represented as ATCC deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:5855`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:5855`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The aggregate GOLD inventory reports 4 organisms, while the local native GOLD organism JSONL has 5 exact rows and 193 linked native project rows for this NCBI taxon; generated GOLD source attestations use the aggregate row. The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows, so the generated YAML correctly remains a zero-strain record.
