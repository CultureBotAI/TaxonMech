# YAML Record Review: Pisolithus thermaeus

- Verdict: pass
- Target: `data/taxa/eukaryota/pisolithus_thermaeus.yaml`
- Identifier: `NCBITaxon:2136032`

## Target

Reviewed the complete 78-line YAML record for `Pisolithus thermaeus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pisolithus_thermaeus`.

## Validation

- `just validate data/taxa/eukaryota/pisolithus_thermaeus.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/pisolithus_orientalis.yaml data/taxa/eukaryota/pisolithus_sp.yaml data/taxa/eukaryota/pisolithus_thermaeus.yaml data/taxa/eukaryota/pisolithus_tinctorius.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:518921` is the exact retained NCBITaxon row for `NCBITaxon:2136032`: label `Pisolithus thermaeus`, rank `SPECIES`, parent `NCBITaxon:37467`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:62376` contains the seeded in-scope row for `NCBITaxon:2136032` with the reason `attested rule: Pisolithus thermaeus, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:2136032`.

## Evidence

- `data/raw/gold_organisms.tsv:20307` is the aggregate GOLD row for `NCBITaxon:2136032` and reports `organism_count=8`, matching the YAML GOLD source attestation.
- Native GOLD has 8 exact organism rows, 14 linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv:85365` through `data/raw/ncbi_type_material.tsv:85366` contain the 2 exact NCBI type-material rows for `NCBITaxon:2136032`.
- `data/straininfo/records.jsonl.gz:282843` contains one exact direct StrainInfo row and one exact StrainInfo deposit row for this NCBI taxon.
- BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2136032`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2136032`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL row does not emit overlay rows because StrainInfo overlays are limited to BacDive-derived local strains.
