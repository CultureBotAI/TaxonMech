# YAML Record Review: Polycladomyces subterraneus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/polycladomyces_subterraneus.yaml
- Started UTC: 2026-10-02T08:41:28Z
- Finished UTC: 2026-10-02T08:41:28Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1016997` |
| Label | `Polycladomyces subterraneus` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1348505` |
| Parent label | `Polycladomyces` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `1` |
| Source attestations | `NCBITAXON`, `LPSN`, `GTDB`, `BACDIVE`, `GOLD` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/polycladomyces_subterraneus.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/moraxella_sp_5484.yaml data/taxa/bacteria/moraxella_sp_623.yaml data/taxa/bacteria/polycladomyces_subterraneus.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_paratyphi_b_str_spb7.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 147 lines, 9 lineage entries, 1 nomenclature record, 1 taxonomy mapping, 2 synonyms, 2 xrefs, 1 BacDive strain, 1 genome assembly, 2 genome records, and 5 source attestations. |
| `taxonmech_bounded_scan.py data/taxa/bacteria/polycladomyces_subterraneus.yaml` | Not applicable: the NCBI-only helper exited with `NCBI source mismatch` because the record intentionally combines NCBITaxon, LPSN, GTDB, BacDive, and GOLD evidence. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*polycladomyces_subterraneus.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1016997)([^0-9]\|$)' data curation` plus source-specific row scans | Pass: the checked NCBI, LPSN, GTDB, BacDive, GOLD, type-material, culture-collection, and strain-genome rows agree with the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10179 maps `NCBITaxon:1016997` to `polycladomyces_subterraneus`.
- `curation/seed_scope.tsv` row 14820 keeps this species in scope with an attested five-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218515 names the same species, parent genus, rank, genetic code, NCBI synonyms, and source set `ncbitaxon|gtdb|bacdive|lpsn|gold`.
- The LPSN row `lpsn:795853` links the name to `NCBITaxon:1016997`, `GTDB:s__Polycladomyces_subterraneus`, type strain `kgmicrobe.strain:NBRC-109332`, PMID `28840818`, two DOI citations, and sequence `INSDC:JF694784`.
- The generated `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the directly attested NCBI species.

## Evidence

- `source_attestations` accurately summarize the five asserted source families: NCBITaxon name, LPSN name, GTDB genome, BacDive strain, and GOLD organism.
- The LPSN nomenclature block preserves the Maneewong et al. authority, validly published and legitimate correct-name status, publication CURIEs, sequence accession, and NBRC type-strain designation from `data/raw/lpsn_names.tsv`.
- `data/raw/gtdb_species.tsv` row 142515 and `data/raw/gtdb_mappings.tsv` row 1171 support the close GTDB species mapping with `genome_count: 1`.
- `data/raw/bacdive_strains.tsv` row 63000 supports strain `kgmicrobe.strain:bacdive_140715` and its BCC, KSR, and NBRC culture-collection identifiers.
- `data/raw/strain_assemblies.tsv` row 46502 and `data/raw/strain_genome_records.tsv` rows 36462-36463 support the BacDive INSDC assembly plus IMG and PATRIC genome records.
- `data/raw/gold_organisms.tsv` row 289 supports the direct GOLD `ORGANISM` assertion count of 1.

## Completeness

- The single BacDive strain is represented, including its three culture-collection identifiers and all three genome links from the maintained strain join tables.
- NCBI type-material rows 1075-1081 and culture-collection rows 8594, 123008, and 133831 support the type-strain placement asserted in the YAML.
- The record has no maintained MediaDive, MADIN, or BactoTraits attestation in the NCBI source set, and none is asserted.
- No causal graph is expected for this generated taxon identity record.
- No empty optional fields are required.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/polycladomyces_subterraneus.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/polycladomyces_subterraneus.yaml`.
- Re-run the source-specific raw-row scans after any refresh of `data/raw/` or `curation/seed_scope.tsv`.

## Additional Notes

- The source scans used `--no-ignore --hidden`, so ignored files were included.
- The GTDB xref appears both in `taxonomy_mappings` and top-level `xrefs`, matching the raw LPSN and GTDB mapping rows.
- The two NCBI synonyms are related synonyms, not LPSN homotypic synonyms.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10179 |
| `curation/seed_scope.tsv` | 14820 |
| `data/raw/ncbitaxon_taxa.tsv` | 218515 |
| `data/raw/lpsn_names.tsv` | 32157 |
| `data/raw/gtdb_species.tsv` | 142515 |
| `data/raw/gtdb_mappings.tsv` | 1171 |
| `data/raw/gold_organisms.tsv` | 289 |
| `data/raw/bacdive_strains.tsv` | 63000 |
| `data/raw/strain_assemblies.tsv` | 46502 |
| `data/raw/strain_genome_records.tsv` | 36462 and 36463 |
| `data/raw/ncbi_type_material.tsv` | 1075-1081 |
| `data/raw/culture_collection_strains.tsv` | 8594, 123008, 133831 |
| `data/taxa/bacteria/polycladomyces_subterraneus.yaml` | 1, 114, 120, 126, 132, and 137 |
