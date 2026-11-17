# YAML Record Review: Piskurozyma yama

- Verdict: pass
- Target: `data/taxa/eukaryota/piskurozyma_yama.yaml`
- Identifier: `NCBITaxon:2878327`

## Target

Reviewed the complete 75-line YAML record for `Piskurozyma yama`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `piskurozyma_yama`.

## Validation

- `just validate data/taxa/eukaryota/piskurozyma_yama.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/piskurozyma_tuonelana.yaml data/taxa/eukaryota/piskurozyma_yama.yaml data/taxa/eukaryota/pisolithus_albus.yaml data/taxa/eukaryota/pisolithus_calongei.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:566958` is the exact retained NCBITaxon row for `NCBITaxon:2878327`: label `Piskurozyma yama`, rank `SPECIES`, parent `NCBITaxon:1851566`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:63349` contains the seeded in-scope row for `NCBITaxon:2878327` with the reason `attested rule: Piskurozyma yama, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:13391` maps old ID `NCBITaxon:1353892` into `NCBITaxon:2878327`; an exact anchored check of `data/raw/ncbitaxon_taxa.tsv` found no retained row for that old ID.

## Evidence

- `data/raw/gold_organisms.tsv:27993` is the aggregate GOLD row for `NCBITaxon:2878327` and reports `organism_count=4`, matching the YAML GOLD source attestation.
- Native GOLD has four exact organism rows and no linked project or analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:135054` through `data/raw/ncbi_type_material.tsv:135055` contain the 2 exact NCBI type-material rows for `NCBITaxon:2878327`.
- StrainInfo has 1 direct exact JSONL row and 1 exact deposit hit for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2878327`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2878327`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The single merged old ID is merge metadata only for this generated record. Because `NCBITaxon:1353892` is absent from the retained NCBITaxon table, the absence of a generated `replaces` edge is expected.
