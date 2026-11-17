# YAML Record Review: Plasmodium vinckei lentum

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_vinckei_lentum.yaml`
- Identifier: `NCBITaxon:138297`

## Target

Reviewed the complete 69-line YAML record for `Plasmodium vinckei lentum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_vinckei_lentum`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_vinckei_lentum.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plasmodium_relictum.yaml data/taxa/eukaryota/plasmodium_vinckei.yaml data/taxa/eukaryota/plasmodium_vinckei_brucechwatti.yaml data/taxa/eukaryota/plasmodium_vinckei_lentum.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:27777` is the exact retained NCBITaxon row for `NCBITaxon:138297`: label `Plasmodium vinckei lentum`, rank `SUBSPECIES`, parent `NCBITaxon:5860`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53990` contains the seeded in-scope row for `NCBITaxon:138297` with the reason `attested rule: Plasmodium vinckei lentum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:138297`.

## Evidence

- `data/raw/gold_organisms.tsv:8996` is the aggregate GOLD row for `NCBITaxon:138297` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files each have one exact row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:138297`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:138297`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:138297`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No additional notes.
