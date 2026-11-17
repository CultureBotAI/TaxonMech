# YAML Record Review: Platytrachelon abietis

- Verdict: pass
- Target: `data/taxa/eukaryota/platytrachelon_abietis.yaml`
- Identifier: `NCBITaxon:1289965`

## Target

Reviewed the complete 87-line YAML record for `Platytrachelon abietis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `platytrachelon_abietis`.

## Validation

- `just validate data/taxa/eukaryota/platytrachelon_abietis.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/platyophrya_macrostoma.yaml data/taxa/eukaryota/platytrachelon_abietis.yaml data/taxa/eukaryota/plectania_melastoma.yaml data/taxa/eukaryota/plectosphaerella_cucumerina.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:302391` is the exact retained NCBITaxon row for `NCBITaxon:1289965`: label `Platytrachelon abietis`, rank `SPECIES`, parent `NCBITaxon:1289964`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:58951` contains the seeded in-scope row for `NCBITaxon:1289965` with the reason `attested rule: Platytrachelon abietis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:1289965`.

## Evidence

- `data/raw/gold_organisms.tsv:6753` is the aggregate GOLD row for `NCBITaxon:1289965` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has no exact organism, project, or analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has four exact rows for `NCBITaxon:1289965`: `CBS 125235` and `CBS:125235` as cultures from holotype, plus `PRM 842974` and `PRM:842974` as holotypes.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1289965`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1289965`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation uses the aggregate GOLD row even though the local native GOLD organism, project, and analysis files have no exact rows for this NCBI taxon.
