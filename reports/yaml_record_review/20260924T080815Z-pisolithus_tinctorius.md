# YAML Record Review: Pisolithus tinctorius

- Verdict: pass
- Target: `data/taxa/eukaryota/pisolithus_tinctorius.yaml`
- Identifier: `NCBITaxon:37468`

## Target

Reviewed the complete 81-line YAML record for `Pisolithus tinctorius`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pisolithus_tinctorius`.

## Validation

- `just validate data/taxa/eukaryota/pisolithus_tinctorius.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pisolithus_orientalis.yaml data/taxa/eukaryota/pisolithus_sp.yaml data/taxa/eukaryota/pisolithus_thermaeus.yaml data/taxa/eukaryota/pisolithus_tinctorius.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4246` is the exact retained NCBITaxon row for `NCBITaxon:37468`: label `Pisolithus tinctorius`, rank `SPECIES`, parent `NCBITaxon:37467`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52372` contains the seeded in-scope row for `NCBITaxon:37468` with the reason `attested rule: Pisolithus tinctorius, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:37468`.

## Evidence

- `data/raw/gold_organisms.tsv:33689` is the aggregate GOLD row for `NCBITaxon:37468` and reports `organism_count=25`, matching the YAML GOLD source attestation.
- Native GOLD has 18 exact organism rows, 20 linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:37468`.
- `data/straininfo/records.jsonl.gz` has 9 exact direct StrainInfo rows and 12 exact deposit rows for this NCBI taxon across lines 69305, 90039, 90358, 196784, 197826, 198738, 199235, 199994, 201248, and 204309.
- BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:37468`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:37468`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The aggregate GOLD inventory reports 25 organisms, while the local native GOLD organism JSONL has 18 exact rows for this NCBI taxon; generated GOLD source attestations use the aggregate row. The exact StrainInfo JSONL rows do not emit overlay rows because StrainInfo overlays are limited to BacDive-derived local strains.
