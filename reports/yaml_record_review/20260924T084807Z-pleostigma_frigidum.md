# YAML Record Review: Pleostigma frigidum

- Verdict: pass
- Target: `data/taxa/eukaryota/pleostigma_frigidum.yaml`
- Identifier: `NCBITaxon:2971676`

## Target

Reviewed the complete 87-line YAML record for `Pleostigma frigidum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pleostigma_frigidum`.

## Validation

- `just validate data/taxa/eukaryota/pleostigma_frigidum.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pleosporaceae_sp.yaml data/taxa/eukaryota/pleosporales_sp.yaml data/taxa/eukaryota/pleostigma_alpinum.yaml data/taxa/eukaryota/pleostigma_frigidum.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:580291` is the exact retained NCBITaxon row for `NCBITaxon:2971676`: label `Pleostigma frigidum`, rank `SPECIES`, parent `NCBITaxon:1206381`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:63477` contains the seeded in-scope row for `NCBITaxon:2971676` with the reason `attested rule: Pleostigma frigidum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 4 related synonyms, and 0 broad synonyms.
- All 15 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:26144`, `data/raw/ncbi_merged_ids.tsv:26149`, and `data/raw/ncbi_merged_ids.tsv:26152` map old IDs `NCBITaxon:1750813`, `NCBITaxon:1750826`, and `NCBITaxon:1750835` into `NCBITaxon:2971676`; exact anchored checks of `data/raw/ncbitaxon_taxa.tsv` found no retained rows for those old IDs.

## Evidence

- `data/raw/gold_organisms.tsv:29661` is the aggregate GOLD row for `NCBITaxon:2971676` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has no exact organism, project, or analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has seven exact holotype rows for `NCBITaxon:2971676`: `GZU-A 980`, `GZU-A-980`, `GZU-A980`, `GZU-A:980`, `GZU:A-980`, `GZU:LMCC0317`, and `LMCC0317`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2971676`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2971676`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The merged old IDs are merge metadata only for this generated record. Because those old IDs are not present in the retained NCBITaxon table, the absence of generated `replaces` edges is expected. The generated GOLD source attestation uses the aggregate GOLD row even though the local native GOLD organism, project, and analysis files have no exact rows for this NCBI taxon.
