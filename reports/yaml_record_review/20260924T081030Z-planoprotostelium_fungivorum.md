# YAML Record Review: Planoprotostelium fungivorum

- Verdict: pass
- Target: `data/taxa/eukaryota/planoprotostelium_fungivorum.yaml`
- Identifier: `NCBITaxon:1890364`

## Target

Reviewed the complete 70-line YAML record for `Planoprotostelium fungivorum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `planoprotostelium_fungivorum`.

## Validation

- `just validate data/taxa/eukaryota/planoprotostelium_fungivorum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/pisolithus_tympanobaculus.yaml data/taxa/eukaryota/planoprotostelium_fungivorum.yaml data/taxa/eukaryota/plasmodiophora_brassicae.yaml data/taxa/eukaryota/plasmodium_adleri_nom_inval.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:490859` is the exact retained NCBITaxon row for `NCBITaxon:1890364`: label `Planoprotostelium fungivorum`, rank `SPECIES`, parent `NCBITaxon:65007`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:61457` contains the seeded in-scope row for `NCBITaxon:1890364` with the reason `attested rule: Planoprotostelium fungivorum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 3 related synonyms, and 0 broad synonyms.
- All 9 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:1890364`.

## Evidence

- `data/raw/gold_organisms.tsv:17015` is the aggregate GOLD row for `NCBITaxon:1890364` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files each have one exact row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:1890364`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1890364`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1890364`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No additional notes.
