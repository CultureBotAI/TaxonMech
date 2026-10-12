# YAML Record Review: Absicoccus intestinalis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/absicoccus_intestinalis.yaml
- Started UTC: 2026-09-22T04:37:35Z
- Finished UTC: 2026-09-22T04:38:55Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2926319 |
| label | Absicoccus intestinalis |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2718525 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/absicoccus_intestinalis.yaml`. It carries LPSN nomenclature, one two-genome GTDB `skos:closeMatch`, three NCBI related synonyms, GTDB and LPSN xrefs, one BacDive-derived type-strain entry with two StrainInfo related records, no causal graphs, and source attestations from NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, and GOLD.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 393497 maps `NCBITaxon:2926319` to slug `absicoccus_intestinalis`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-absicoccus_intestinalis.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/absicoccus_intestinalis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/absicoccus_intestinalis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 572694 has `NCBITaxon:2926319`, label `Absicoccus intestinalis`, rank `SPECIES`, direct parent `NCBITaxon:2718525`, genetic code `11`, the three NCBI related synonyms represented in YAML, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:1239` Bacillota, `PHYLUM` | line 955 |
| `NCBITaxon:526524` Erysipelotrichia, `CLASS` | line 120147 |
| `NCBITaxon:526525` Erysipelotrichales, `ORDER` | line 120148 |
| `NCBITaxon:128827` Erysipelotrichaceae, `FAMILY` | line 24654 |
| `NCBITaxon:2718525` Absicoccus, `GENUS` | line 546863 |

`data/raw/lpsn_names.tsv` line 10701 supports `lpsn:69450`, the Hitch et al. 2025 authority, DSM 114836 and JCM 37183 type-strain designations, PMID/DOI publications, INSDC accession `ON006466`, and the LPSN link to `GTDB:s__Absicoccus_intestinalis`.

`data/raw/gtdb_mappings.tsv` line 235051 maps `GTDB:s__Absicoccus_intestinalis` to `NCBITaxon:2926319` with `skos:closeMatch`; `data/raw/gtdb_species.tsv` line 2815 records the GTDB species with two genomes.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 572694 | Supported exactly. |
| LPSN correct-name nomenclature and GTDB link | `data/raw/lpsn_names.tsv` line 10701 | Supported exactly. |
| One close GTDB species mapping | `data/raw/gtdb_mappings.tsv` line 235051 and `data/raw/gtdb_species.tsv` line 2815 | Supported exactly. |
| BacDive local strain | `data/raw/bacdive_strains.tsv` line 97746 | Supported; BacDive 175515 has designation `CLA-KB-P134`, taxon `NCBITaxon:2926319`, LPSN ID `lpsn:69450`, and DSM 114836/JCM 37183 culture IDs. |
| StrainInfo overlay | `data/straininfo/strain_links.tsv` line 76354 | Supported; the DSM 114836 deposit generates both the StrainInfo deposit and StrainInfo strain related records. |
| MediaDive and GOLD source attestations | `data/raw/mediadive_taxa.tsv` line 8354 and `data/raw/gold_organisms.tsv` line 28782 | Supported with two MediaDive media and one GOLD organism. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 393497 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 13534 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct genus parent, root-first bacterial lineage, genetic code `11`, and all three generated related synonyms.
- LPSN supplies correct-name nomenclature, type-strain designations, DOI/PMID publication references, the INSDC sequence accession, and the GTDB close-match link.
- GTDB, BacDive, StrainInfo, MediaDive, and GOLD source rows are represented by the mapping, local strain, two related records, and source attestations present in the YAML.
- No same-taxon source row in the committed TSV inventories supplies assembly or genome links for BacDive 175515, and the generated type-strain entry is therefore correctly limited to culture-collection IDs plus StrainInfo related records.
- With no curator-added `causal_graphs`, the optional causal-graph section is correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
