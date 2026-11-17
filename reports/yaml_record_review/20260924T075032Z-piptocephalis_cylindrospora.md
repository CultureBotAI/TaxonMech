# YAML Record Review: Piptocephalis cylindrospora

- Verdict: pass
- Target: `data/taxa/eukaryota/piptocephalis_cylindrospora.yaml`
- Identifier: `NCBITaxon:1907219`

## Target

Reviewed the complete 69-line YAML record for `Piptocephalis cylindrospora`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `piptocephalis_cylindrospora`.

## Validation

- `just validate data/taxa/eukaryota/piptocephalis_cylindrospora.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pinibarrenia_chlamydospora.yaml data/taxa/eukaryota/pinnaticoemansia_coronantispora.yaml data/taxa/eukaryota/piptocephalis_brijmohanii.yaml data/taxa/eukaryota/piptocephalis_cylindrospora.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:492921` is the exact retained NCBITaxon row for `NCBITaxon:1907219`: label `Piptocephalis cylindrospora`, rank `SPECIES`, parent `NCBITaxon:78916`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:61527` contains the seeded in-scope row for `NCBITaxon:1907219` with the reason `attested rule: Piptocephalis cylindrospora, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:1907219`.

## Evidence

- `data/raw/gold_organisms.tsv:17255` is the aggregate GOLD row for `NCBITaxon:1907219` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:30855`, three linked project rows starting at `data/gold/projects.jsonl.gz:24670`, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:69604` through `data/raw/ncbi_type_material.tsv:69605` contain the 2 exact NCBI type-material rows for `NCBITaxon:1907219`.
- StrainInfo has 22 direct exact JSONL rows and 40 exact deposit hits for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1907219`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1907219`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The source and generated inventories support the current record as a GOLD plus NCBITaxon seed with no generated strain assertions.
