# YAML Record Review: Pinnaticoemansia coronantispora

- Verdict: pass
- Target: `data/taxa/eukaryota/pinnaticoemansia_coronantispora.yaml`
- Identifier: `NCBITaxon:417175`

## Target

Reviewed the complete 69-line YAML record for `Pinnaticoemansia coronantispora`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pinnaticoemansia_coronantispora`.

## Validation

- `just validate data/taxa/eukaryota/pinnaticoemansia_coronantispora.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pinibarrenia_chlamydospora.yaml data/taxa/eukaryota/pinnaticoemansia_coronantispora.yaml data/taxa/eukaryota/piptocephalis_brijmohanii.yaml data/taxa/eukaryota/piptocephalis_cylindrospora.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:91284` is the exact retained NCBITaxon row for `NCBITaxon:417175`: label `Pinnaticoemansia coronantispora`, rank `SPECIES`, parent `NCBITaxon:417174`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:55571` contains the seeded in-scope row for `NCBITaxon:417175` with the reason `attested rule: Pinnaticoemansia coronantispora, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:417175`.

## Evidence

- `data/raw/gold_organisms.tsv:34914` is the aggregate GOLD row for `NCBITaxon:417175` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:400225`, two linked project rows starting at `data/gold/projects.jsonl.gz:390225`, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:206831` through `data/raw/ncbi_type_material.tsv:206836` contain the 6 exact NCBI type-material rows for `NCBITaxon:417175`.
- StrainInfo has 1 direct exact JSONL row and 1 exact deposit hit for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:417175`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:417175`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The source and generated inventories support the current record as a GOLD plus NCBITaxon seed with no generated strain assertions.
