# YAML Record Review: Plectosphaerella cucumerina

- Verdict: pass
- Target: `data/taxa/eukaryota/plectosphaerella_cucumerina.yaml`
- Identifier: `NCBITaxon:40658`

## Target

Reviewed the complete 99-line YAML record for `Plectosphaerella cucumerina`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plectosphaerella_cucumerina`.

## Validation

- `just validate data/taxa/eukaryota/plectosphaerella_cucumerina.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/platyophrya_macrostoma.yaml data/taxa/eukaryota/platytrachelon_abietis.yaml data/taxa/eukaryota/plectania_melastoma.yaml data/taxa/eukaryota/plectosphaerella_cucumerina.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4667` is the exact retained NCBITaxon row for `NCBITaxon:40658`: label `Plectosphaerella cucumerina`, rank `SPECIES`, parent `NCBITaxon:40657`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52449` contains the seeded in-scope row for `NCBITaxon:40658` with the reason `attested rule: Plectosphaerella cucumerina, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 5 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:40658`.

## Evidence

- `data/raw/gold_organisms.tsv:34632` is the aggregate GOLD row for `NCBITaxon:40658` and reports `organism_count=3`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, four linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has four exact rows for `NCBITaxon:40658`: `CBS 131739` and `CBS:131739` as cultures from neotype, plus `CBS H-20896` and `CBS:H-20896` as neotypes.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 72 exact local JSONL records covering 94 deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:40658`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:40658`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows, so the generated YAML correctly remains a zero-strain record. The aggregate GOLD inventory reports 3 organisms, while the local native GOLD organism JSONL has 2 exact rows and 4 linked native project rows for this NCBI taxon; generated GOLD source attestations use the aggregate row.
