# YAML Record Review: Pluteus cervinus

- Verdict: pass
- Target: `data/taxa/eukaryota/pluteus_cervinus.yaml`
- Identifier: `NCBITaxon:181527`

## Target

Reviewed the complete 84-line YAML record for `Pluteus cervinus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pluteus_cervinus`.

## Validation

- `just validate data/taxa/eukaryota/pluteus_cervinus.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plocamium_pacificum.yaml data/taxa/eukaryota/pluteus_cervinus.yaml data/taxa/eukaryota/pneumocystis_canis.yaml data/taxa/eukaryota/pneumocystis_carinii.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:36376` is the exact retained NCBITaxon row for `NCBITaxon:181527`: label `Pluteus cervinus`, rank `SPECIES`, parent `NCBITaxon:68743`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54356` contains the seeded in-scope row for `NCBITaxon:181527` with the reason `attested rule: Pluteus cervinus, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:181527`.

## Evidence

- `data/raw/gold_organisms.tsv:16078` is the aggregate GOLD row for `NCBITaxon:181527` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has two exact epitype rows for `NCBITaxon:181527`, both filed under `Agaricus cervinus`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has one exact strain record covering three exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:181527`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:181527`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact type-material rows are NCBI designations that do not appear as generated strain rows, and the exact StrainInfo JSONL hit likewise has no corresponding BacDive or generated StrainInfo overlay row. The generated GOLD source attestation is consistent with both the aggregate GOLD row and the single native GOLD organism row for `Pluteus cervinus NL-1719`.
