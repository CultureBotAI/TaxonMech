# YAML Record Review: Platyophrya macrostoma

- Verdict: pass
- Target: `data/taxa/eukaryota/platyophrya_macrostoma.yaml`
- Identifier: `NCBITaxon:938130`

## Target

Reviewed the complete 66-line YAML record for `Platyophrya macrostoma`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `platyophrya_macrostoma`.

## Validation

- `just validate data/taxa/eukaryota/platyophrya_macrostoma.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/platyophrya_macrostoma.yaml data/taxa/eukaryota/platytrachelon_abietis.yaml data/taxa/eukaryota/plectania_melastoma.yaml data/taxa/eukaryota/plectosphaerella_cucumerina.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:199128` is the exact retained NCBITaxon row for `NCBITaxon:938130`: label `Platyophrya macrostoma`, rank `SPECIES`, parent `NCBITaxon:88562`, genetic code `6`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:56964` contains the seeded in-scope row for `NCBITaxon:938130` with the reason `attested rule: Platyophrya macrostoma, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 11 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:938130`.

## Evidence

- `data/raw/gold_organisms.tsv:44852` is the aggregate GOLD row for `NCBITaxon:938130` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row and no linked project or analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:938130`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has one exact local JSONL record, `siID 350768`, carrying the `ATCC 50265` deposit.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:938130`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:938130`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hit has no corresponding BacDive or generated StrainInfo overlay row, so the generated YAML correctly remains a zero-strain record.
