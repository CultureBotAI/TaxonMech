# YAML Record Review: Pisolithus microcarpus

- Verdict: pass
- Target: `data/taxa/eukaryota/pisolithus_microcarpus.yaml`
- Identifier: `NCBITaxon:178872`

## Target

Reviewed the complete 81-line YAML record for `Pisolithus microcarpus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pisolithus_microcarpus`.

## Validation

- `just validate data/taxa/eukaryota/pisolithus_microcarpus.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pisolithus_capsulifer.yaml data/taxa/eukaryota/pisolithus_croceorrhizus.yaml data/taxa/eukaryota/pisolithus_marmoratus.yaml data/taxa/eukaryota/pisolithus_microcarpus.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:35851` is the exact retained NCBITaxon row for `NCBITaxon:178872`: label `Pisolithus microcarpus`, rank `SPECIES`, parent `NCBITaxon:37467`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54317` contains the seeded in-scope row for `NCBITaxon:178872` with the reason `attested rule: Pisolithus microcarpus, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:178872`.

## Evidence

- `data/raw/gold_organisms.tsv:15626` is the aggregate GOLD row for `NCBITaxon:178872` and reports `organism_count=40`, matching the YAML GOLD source attestation.
- Native GOLD has 39 exact organism rows, 97 linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:178872`.
- `data/straininfo/records.jsonl.gz` has 7 exact direct StrainInfo rows for this NCBI taxon, each with an exact deposit row: lines 234960, 234961, 236246, 236287, 236288, 236648, and 236652.
- BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:178872`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:178872`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The aggregate GOLD inventory reports 40 organisms, while the local native GOLD organism JSONL has 39 exact rows for this NCBI taxon; generated GOLD source attestations use the aggregate row. The seven exact StrainInfo JSONL rows do not emit overlay rows because StrainInfo overlays are limited to BacDive-derived local strains.
