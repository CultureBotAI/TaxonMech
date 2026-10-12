# YAML Record Review: Polarella glacialis

- Verdict: pass
- Target: `data/taxa/eukaryota/polarella_glacialis.yaml`
- Identifier: `NCBITaxon:89957`

## Target

Reviewed the complete 60-line YAML record for `Polarella glacialis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `polarella_glacialis`.

## Validation

- `just validate data/taxa/eukaryota/polarella_glacialis.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/podospora_striatispora.yaml data/taxa/eukaryota/podospora_tetraspora.yaml data/taxa/eukaryota/poitrasia_circinans.yaml data/taxa/eukaryota/polarella_glacialis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:14437` is the exact retained NCBITaxon row for `NCBITaxon:89957`: label `Polarella glacialis`, rank `SPECIES`, parent `NCBITaxon:89956`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53488` contains the seeded in-scope row for `NCBITaxon:89957` with the reason `attested rule: Polarella glacialis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 9 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:44079` is the aggregate GOLD row for `NCBITaxon:89957` and reports `organism_count=4`, matching the YAML GOLD source attestation.
- Native GOLD has four exact organism rows, two linked project rows, and two linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:89957`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found four direct local JSONL records covering four exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:89957`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:89957`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows. The generated GOLD source attestation is consistent with the aggregate GOLD row and the four native GOLD organism rows for the CCMP 1383 and CCMP 2088 strains.
