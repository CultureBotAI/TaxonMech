# YAML Record Review: Porostereum spadiceum

- Verdict: pass
- Target: `data/taxa/eukaryota/porostereum_spadiceum.yaml`
- Identifier: `NCBITaxon:103378`

## Target

Reviewed the complete 90-line YAML record for `Porostereum spadiceum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `porostereum_spadiceum`.

## Validation

- `just validate data/taxa/eukaryota/porostereum_spadiceum.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/porostereum_spadiceum.yaml data/taxa/eukaryota/porphyridium_aerugineum.yaml data/taxa/eukaryota/porphyridium_purpureum.yaml data/taxa/eukaryota/porpomyces_mucidus.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:18449` is the exact retained NCBITaxon row for `NCBITaxon:103378`: label `Porostereum spadiceum`, rank `SPECIES`, parent `NCBITaxon:396332`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53666` contains the seeded in-scope row for `NCBITaxon:103378` with the reason `attested rule: Porostereum spadiceum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 3 exact synonyms, 4 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:2072838` to `NCBITaxon:103378`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:452` is the aggregate GOLD row for `NCBITaxon:103378` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:103378`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 20 direct local JSONL records covering 22 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:103378`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:103378`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows. The generated GOLD source attestation is consistent with the aggregate GOLD row and two native GOLD organism rows for strain `BS34`, one under `Porostereum spadiceum` and one under `Porosterum spadiceum`.
