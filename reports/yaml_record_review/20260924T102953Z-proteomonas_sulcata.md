# YAML Record Review: Proteomonas sulcata

- Verdict: pass
- Target: `data/taxa/eukaryota/proteomonas_sulcata.yaml`
- Identifier: `NCBITaxon:77928`

## Target

Reviewed the complete 54-line YAML record for `Proteomonas sulcata`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `proteomonas_sulcata`.

## Validation

- `just validate data/taxa/eukaryota/proteomonas_sulcata.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/proteomonas_sulcata.yaml data/taxa/eukaryota/protoceratium_reticulatum.yaml data/taxa/eukaryota/protocrea_farinosa.yaml data/taxa/eukaryota/protocrea_pallida.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:11349` is the exact retained NCBITaxon row for `NCBITaxon:77928`: label `Proteomonas sulcata`, rank `SPECIES`, parent `NCBITaxon:96335`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53319` contains the seeded in-scope row for `NCBITaxon:77928` with the reason `attested rule: Proteomonas sulcata, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 7 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:42706` is the aggregate GOLD row for `NCBITaxon:77928` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, 23 linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:77928`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found seven direct local JSONL records covering seven exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:77928`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:77928`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with the aggregate GOLD row and two native GOLD organism rows for `CCMP 704` and `CCMP 1175`. All 23 native GOLD project rows are linked to the `CCMP 1175` organism row.
