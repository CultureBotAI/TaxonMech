# YAML Record Review: Proliferodiscus dingleyae

- Verdict: pass
- Target: `data/taxa/eukaryota/proliferodiscus_dingleyae.yaml`
- Identifier: `NCBITaxon:2283848`

## Target

Reviewed the complete 81-line YAML record for `Proliferodiscus dingleyae`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `proliferodiscus_dingleyae`.

## Validation

- `just validate data/taxa/eukaryota/proliferodiscus_dingleyae.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/prillingera_fragicola.yaml data/taxa/eukaryota/proboscia_alata.yaml data/taxa/eukaryota/proboscia_inermis.yaml data/taxa/eukaryota/proliferodiscus_dingleyae.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:523041` is the exact retained NCBITaxon row for `NCBITaxon:2283848`: label `Proliferodiscus dingleyae`, rank `SPECIES`, parent `NCBITaxon:47811`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:62539` contains the seeded in-scope row for `NCBITaxon:2283848` with the reason `attested rule: Proliferodiscus dingleyae, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 1 related synonym, and 0 broad synonyms.
- All 15 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:21440` is the aggregate GOLD row for `NCBITaxon:2283848` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv:91040` provides one exact `isotype` row for `NCBITaxon:2283848`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has one direct local JSONL record covering one exact deposit, `ICMP 21730`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2283848`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2283848`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with the aggregate GOLD row and the native GOLD organism row for strain `D683`. Native GOLD links that organism to project `Gp0441660`, while StrainInfo carries the exact local `ICMP 21730` culture-collection designation only.
