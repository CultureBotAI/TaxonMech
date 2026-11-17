# YAML Record Review: Podospora petrogale

- Verdict: pass
- Target: `data/taxa/eukaryota/podospora_petrogale.yaml`
- Identifier: `NCBITaxon:183709`

## Target

Reviewed the complete 87-line YAML record for `Podospora petrogale`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `podospora_petrogale`.

## Validation

- `just validate data/taxa/eukaryota/podospora_petrogale.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/podospora_inquinata.yaml data/taxa/eukaryota/podospora_minicauda.yaml data/taxa/eukaryota/podospora_petrogale.yaml data/taxa/eukaryota/podospora_platensis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:36592` is the exact retained NCBITaxon row for `NCBITaxon:183709`: label `Podospora petrogale`, rank `SPECIES`, parent `NCBITaxon:5144`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54375` contains the seeded in-scope row for `NCBITaxon:183709` with the reason `attested rule: Podospora petrogale, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:3127127` to `NCBITaxon:183709`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:16289` is the aggregate GOLD row for `NCBITaxon:183709` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has nine exact type-material rows for `NCBITaxon:183709`, all filed under `Podospora petrogale`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found one direct local JSONL record covering two exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:183709`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:183709`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact type-material rows cover five NCBI culture-from-type-material designations for `ATCC MYA-1392` and `CBS 109409`, plus four isotype designations for `PDD 73850` and `WELTU 684`. The exact StrainInfo row likewise covers `CBS 109409` and `ATCC MYA-1392`, but none of those rows generated BacDive or StrainInfo overlay records.
