# YAML Record Review: Pilasporangium apinafurcum

- Verdict: pass
- Target: `data/taxa/eukaryota/pilasporangium_apinafurcum.yaml`
- Identifier: `NCBITaxon:1635159`

## Target

Reviewed the complete 70-line YAML record for `Pilasporangium apinafurcum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pilasporangium_apinafurcum`.

## Validation

- `just validate data/taxa/eukaryota/pilasporangium_apinafurcum.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pilaira_moreaui_var_caucasica.yaml data/taxa/eukaryota/pilasporangium_apinafurcum.yaml data/taxa/eukaryota/pilatotrama_ljubarskyi.yaml data/taxa/eukaryota/pilobolus_umbonatus.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:425650` is the exact retained NCBITaxon row for `NCBITaxon:1635159`: label `Pilasporangium apinafurcum`, rank `SPECIES`, parent `NCBITaxon:1635158`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:60943` contains the seeded in-scope row for `NCBITaxon:1635159` with the reason `attested rule: Pilasporangium apinafurcum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 10 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:86380` maps old ID `NCBITaxon:561257` into `NCBITaxon:1635159`; an exact anchored check of `data/raw/ncbitaxon_taxa.tsv` found no retained row for that old ID.

## Evidence

- `data/raw/gold_organisms.tsv:14006` is the aggregate GOLD row for `NCBITaxon:1635159` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, two linked project rows, and two linked analysis rows for this target.
- The NCBI type-material inventory has no exact rows for `NCBITaxon:1635159`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1635159`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1635159`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The single merged old ID is merge metadata only for this generated record. Because `NCBITaxon:561257` is absent from the retained NCBITaxon table, the absence of a generated `replaces` edge is expected.
