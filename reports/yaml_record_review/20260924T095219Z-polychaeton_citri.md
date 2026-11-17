# YAML Record Review: Polychaeton citri

- Verdict: pass
- Target: `data/taxa/eukaryota/polychaeton_citri.yaml`
- Identifier: `NCBITaxon:705562`

## Target

Reviewed the complete 87-line YAML record for `Polychaeton citri`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `polychaeton_citri`.

## Validation

- `just validate data/taxa/eukaryota/polychaeton_citri.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/polychaeton_citri.yaml data/taxa/eukaryota/polychytrium_aggregatum.yaml data/taxa/eukaryota/polymyxa_betae.yaml data/taxa/eukaryota/polyphilus_sieberi.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:165159` is the exact retained NCBITaxon row for `NCBITaxon:705562`: label `Polychaeton citri`, rank `SPECIES`, parent `NCBITaxon:705561`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:56500` contains the seeded in-scope row for `NCBITaxon:705562` with the reason `attested rule: Polychaeton citri, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:41698` is the aggregate GOLD row for `NCBITaxon:705562` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:705562`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:705562`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:705562`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with both the aggregate GOLD row and the native GOLD row for `Polychaeton citri CBS 116435`. No exact BacDive, StrainInfo, or type-material evidence needed to be materialized into the zero-strain YAML.
