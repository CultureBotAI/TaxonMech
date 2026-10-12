# YAML Record Review: Piromyces cryptodigmaticus

- Verdict: pass
- Target: `data/taxa/eukaryota/piromyces_cryptodigmaticus.yaml`
- Identifier: `NCBITaxon:1231726`

## Target

Reviewed the complete 69-line YAML record for `Piromyces cryptodigmaticus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `piromyces_cryptodigmaticus`.

## Validation

- `just validate data/taxa/eukaryota/piromyces_cryptodigmaticus.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/piromyces_cryptodigmaticus.yaml data/taxa/eukaryota/piromyces_finnis.yaml data/taxa/eukaryota/piromyces_rhizinflatus.yaml data/taxa/eukaryota/piromyces_sp.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:281311` is the exact retained NCBITaxon row for `NCBITaxon:1231726`: label `Piromyces cryptodigmaticus`, rank `SPECIES`, parent `NCBITaxon:4821`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:58595` contains the seeded in-scope row for `NCBITaxon:1231726` with the reason `attested rule: Piromyces cryptodigmaticus, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:1231726`.

## Evidence

- `data/raw/gold_organisms.tsv:5549` is the aggregate GOLD row for `NCBITaxon:1231726` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files have no exact rows for this target.
- `data/raw/ncbi_type_material.tsv:15525` through `data/raw/ncbi_type_material.tsv:15528` contain the 4 exact NCBI type-material rows for `NCBITaxon:1231726`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1231726`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1231726`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The GOLD evidence for this record is present in the aggregate `data/raw/gold_organisms.tsv` inventory; the local native GOLD organism, project, and analysis JSONL scans have no exact rows for the target.
