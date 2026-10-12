# YAML Record Review: Pisolithus marmoratus

- Verdict: pass
- Target: `data/taxa/eukaryota/pisolithus_marmoratus.yaml`
- Identifier: `NCBITaxon:178871`

## Target

Reviewed the complete 81-line YAML record for `Pisolithus marmoratus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pisolithus_marmoratus`.

## Validation

- `just validate data/taxa/eukaryota/pisolithus_marmoratus.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pisolithus_capsulifer.yaml data/taxa/eukaryota/pisolithus_croceorrhizus.yaml data/taxa/eukaryota/pisolithus_marmoratus.yaml data/taxa/eukaryota/pisolithus_microcarpus.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:35850` is the exact retained NCBITaxon row for `NCBITaxon:178871`: label `Pisolithus marmoratus`, rank `SPECIES`, parent `NCBITaxon:37467`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54316` contains the seeded in-scope row for `NCBITaxon:178871` with the reason `attested rule: Pisolithus marmoratus, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:178871`.

## Evidence

- `data/raw/gold_organisms.tsv:15625` is the aggregate GOLD row for `NCBITaxon:178871` and reports `organism_count=4`, matching the YAML GOLD source attestation.
- Native GOLD has 4 exact organism rows, 11 linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:178871`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:178871`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:178871`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No additional notes.
