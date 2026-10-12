# YAML Record Review: Pichia pseudolambica

- Verdict: pass
- Target: `data/taxa/eukaryota/pichia_pseudolambica.yaml`
- Identifier: `NCBITaxon:52248`

## Target

Reviewed the complete 82-line YAML record for `Pichia pseudolambica`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pichia_pseudolambica`.

## Validation

- `just validate data/taxa/eukaryota/pichia_pseudolambica.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pichia_paraexigua.yaml data/taxa/eukaryota/pichia_phayaonensis.yaml data/taxa/eukaryota/pichia_pseudocactophila.yaml data/taxa/eukaryota/pichia_pseudolambica.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:6567` is the exact retained NCBITaxon row for `NCBITaxon:52248`: label `Pichia pseudolambica`, rank `SPECIES`, parent `NCBITaxon:4919`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52858` contains the seeded in-scope row for `NCBITaxon:52248` with the reason `attested rule: Pichia pseudolambica, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 3 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:62744` maps old ID `NCBITaxon:3082068` into `NCBITaxon:52248`; an exact anchored check of `data/raw/ncbitaxon_taxa.tsv` found no retained row for that old ID.

## Evidence

- `data/raw/gold_organisms.tsv:37829` is the aggregate GOLD row for `NCBITaxon:52248` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:525726`, one linked project row at `data/gold/projects.jsonl.gz:609870`, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:227811` through `data/raw/ncbi_type_material.tsv:227817` contain the 7 exact NCBI type-material rows for `NCBITaxon:52248`.
- StrainInfo has 15 direct exact JSONL rows and 24 exact deposit hits for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:52248`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:52248`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The single merged old ID is merge metadata only for this generated record. Because `NCBITaxon:3082068` is absent from the retained NCBITaxon table, the absence of a generated `replaces` edge is expected.
