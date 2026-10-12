# YAML Record Review: Plasmodium vivax Sal-1

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_vivax_sal_1.yaml`
- Identifier: `NCBITaxon:126793`

## Target

Reviewed the complete 78-line YAML record for `Plasmodium vivax Sal-1`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_vivax_sal_1`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_vivax_sal_1.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plasmodium_vinckei_petteri.yaml data/taxa/eukaryota/plasmodium_vinckei_vinckei.yaml data/taxa/eukaryota/plasmodium_vivax.yaml data/taxa/eukaryota/plasmodium_vivax_sal_1.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:24259` is the exact retained NCBITaxon row for `NCBITaxon:126793`: label `Plasmodium vivax Sal-1`, rank `STRAIN`, parent `NCBITaxon:5855`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53905` contains the seeded in-scope row for `NCBITaxon:126793` with the reason `attested rule: Plasmodium vivax Sal-1, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 3 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:87602` maps old ID `NCBITaxon:5856` into `NCBITaxon:126793`; an exact anchored check of `data/raw/ncbitaxon_taxa.tsv` found no retained row for that old ID.

## Evidence

- `data/raw/gold_organisms.tsv:6364` is the aggregate GOLD row for `NCBITaxon:126793` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files each have one exact row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:126793`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:126793`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:126793`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The merged old ID is merge metadata only for this generated record. Because that old ID is not present in the retained NCBITaxon table, the absence of a generated `replaces` edge is expected.
