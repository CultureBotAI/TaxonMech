# YAML Record Review: Piromyces finnis

- Verdict: pass
- Target: `data/taxa/eukaryota/piromyces_finnis.yaml`
- Identifier: `NCBITaxon:1754191`

## Target

Reviewed the complete 75-line YAML record for `Piromyces finnis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `piromyces_finnis`.

## Validation

- `just validate data/taxa/eukaryota/piromyces_finnis.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/piromyces_cryptodigmaticus.yaml data/taxa/eukaryota/piromyces_finnis.yaml data/taxa/eukaryota/piromyces_rhizinflatus.yaml data/taxa/eukaryota/piromyces_sp.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:457973` is the exact retained NCBITaxon row for `NCBITaxon:1754191`: label `Piromyces finnis`, rank `SPECIES`, parent `NCBITaxon:4821`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:61199` contains the seeded in-scope row for `NCBITaxon:1754191` with the reason `attested rule: Piromyces finnis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:20543` maps old ID `NCBITaxon:1577477` into `NCBITaxon:1754191`; an exact anchored check of `data/raw/ncbitaxon_taxa.tsv` found no retained row for that old ID.

## Evidence

- `data/raw/gold_organisms.tsv:15253` is the aggregate GOLD row for `NCBITaxon:1754191` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:62281`, two linked project rows starting at `data/gold/projects.jsonl.gz:65309`, and two linked analysis rows starting at `data/gold/analyses.jsonl.gz:120662`.
- `data/raw/ncbi_type_material.tsv:57027` through `data/raw/ncbi_type_material.tsv:57028` contain the 2 exact NCBI type-material rows for `NCBITaxon:1754191`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1754191`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1754191`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The single merged old ID is merge metadata only for this generated record. Because `NCBITaxon:1577477` is absent from the retained NCBITaxon table, the absence of a generated `replaces` edge is expected.
