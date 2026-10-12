# YAML Record Review: Protocrea pallida

- Verdict: pass
- Target: `data/taxa/eukaryota/protocrea_pallida.yaml`
- Identifier: `NCBITaxon:29862`

## Target

Reviewed the complete 87-line YAML record for `Protocrea pallida`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `protocrea_pallida`.

## Validation

- `just validate data/taxa/eukaryota/protocrea_pallida.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/proteomonas_sulcata.yaml data/taxa/eukaryota/protoceratium_reticulatum.yaml data/taxa/eukaryota/protocrea_farinosa.yaml data/taxa/eukaryota/protocrea_pallida.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:3284` is the exact retained NCBITaxon row for `NCBITaxon:29862`: label `Protocrea pallida`, rank `SPECIES`, parent `NCBITaxon:555849`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52216` contains the seeded in-scope row for `NCBITaxon:29862` with the reason `attested rule: Protocrea pallida, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:29888` is the aggregate GOLD row for `NCBITaxon:29862` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has no exact organism rows, linked project rows, or linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has two exact `culture from epitype` rows for `NCBITaxon:29862`, covering `CBS 299.78` and `CBS:299.78`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:29862`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:29862`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is backed by the aggregate GOLD row; exact native GOLD organism, project, and analysis scans returned 0 rows for `NCBITaxon:29862`. The only exact culture evidence in the bounded scan was the pair of NCBI epitype aliases.
