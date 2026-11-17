# YAML Record Review: Plectania melastoma

- Verdict: pass
- Target: `data/taxa/eukaryota/plectania_melastoma.yaml`
- Identifier: `NCBITaxon:1280572`

## Target

Reviewed the complete 93-line YAML record for `Plectania melastoma`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plectania_melastoma`.

## Validation

- `just validate data/taxa/eukaryota/plectania_melastoma.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/platyophrya_macrostoma.yaml data/taxa/eukaryota/platytrachelon_abietis.yaml data/taxa/eukaryota/plectania_melastoma.yaml data/taxa/eukaryota/plectosphaerella_cucumerina.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:298987` is the exact retained NCBITaxon row for `NCBITaxon:1280572`: label `Plectania melastoma`, rank `SPECIES`, parent `NCBITaxon:36919`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:58888` contains the seeded in-scope row for `NCBITaxon:1280572` with the reason `attested rule: Plectania melastoma, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 6 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:1280572`.

## Evidence

- `data/raw/gold_organisms.tsv:6534` is the aggregate GOLD row for `NCBITaxon:1280572` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:1280572`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has one exact local JSONL record, `siID 173885`, carrying the `CBS 918.72` deposit.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1280572`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1280572`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hit has no corresponding BacDive or generated StrainInfo overlay row, so the generated YAML correctly remains a zero-strain record.
