# YAML Record Review: Pleostigma lichenophilum

- Verdict: pass
- Target: `data/taxa/eukaryota/pleostigma_lichenophilum.yaml`
- Identifier: `NCBITaxon:2971677`

## Target

Reviewed the complete 84-line YAML record for `Pleostigma lichenophilum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pleostigma_lichenophilum`.

## Validation

- `just validate data/taxa/eukaryota/pleostigma_lichenophilum.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pleostigma_lichenophilum.yaml data/taxa/eukaryota/pleurosigma_sp.yaml data/taxa/eukaryota/pleurotus_abalonus.yaml data/taxa/eukaryota/pleurotus_abieticola.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:580292` is the exact retained NCBITaxon row for `NCBITaxon:2971677`: label `Pleostigma lichenophilum`, rank `SPECIES`, parent `NCBITaxon:1206381`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:63478` contains the seeded in-scope row for `NCBITaxon:2971677` with the reason `attested rule: Pleostigma lichenophilum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- All 15 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:26145` and `data/raw/ncbi_merged_ids.tsv:26154` map old IDs `NCBITaxon:1750816` and `NCBITaxon:1750845` into `NCBITaxon:2971677`; exact anchored checks of `data/raw/ncbitaxon_taxa.tsv` found no retained rows for those old IDs.

## Evidence

- `data/raw/gold_organisms.tsv:29662` is the aggregate GOLD row for `NCBITaxon:2971677` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has no exact organism, project, or analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has six exact holotype rows for `NCBITaxon:2971677`: `GZU-A 952`, `GZU-A-952`, `GZU-A952`, `GZU-A:952`, `GZU:LMCC0289`, and `LMCC0289`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2971677`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2971677`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The merged old IDs are merge metadata only for this generated record. Because those old IDs are not present in the retained NCBITaxon table, the absence of generated `replaces` edges is expected. The generated GOLD source attestation uses the aggregate GOLD row even though the local native GOLD organism, project, and analysis files have no exact rows for this NCBI taxon.
