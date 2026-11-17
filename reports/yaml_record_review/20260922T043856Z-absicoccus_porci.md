# YAML Record Review: Absicoccus porci

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/absicoccus_porci.yaml
- Started UTC: 2026-09-22T04:37:35Z
- Finished UTC: 2026-09-22T04:38:56Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2486576 |
| label | Absicoccus porci |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2718525 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/absicoccus_porci.yaml`. It carries LPSN nomenclature, one 27-genome GTDB `skos:closeMatch`, three NCBI related synonyms, GTDB and LPSN xrefs, one BacDive-derived type-strain entry with one assembly and two genome records, no causal graphs, and source attestations from NCBITAXON, LPSN, GTDB, BACDIVE, and GOLD.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 343260 maps `NCBITaxon:2486576` to slug `absicoccus_porci`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-absicoccus_porci.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/absicoccus_porci.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/absicoccus_porci.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 526289 has `NCBITaxon:2486576`, label `Absicoccus porci`, rank `SPECIES`, direct parent `NCBITaxon:2718525`, genetic code `11`, the three NCBI related synonyms represented in YAML, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, and snapshot date `2026-09-13`.

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

`data/raw/lpsn_names.tsv` line 931 supports `lpsn:5758`, the Shin et al. 2020 authority, JCM 32769 and KCTC 15747 type-strain designations, PMID/DOI publications, INSDC accession `MG931004`, and the LPSN link to `GTDB:s__Absicoccus_porci`.

`data/raw/gtdb_mappings.tsv` line 193455 maps `GTDB:s__Absicoccus_porci` to `NCBITaxon:2486576` with `skos:closeMatch`; `data/raw/gtdb_species.tsv` line 2816 records the GTDB species with 27 genomes.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 526289 | Supported exactly. |
| LPSN correct-name nomenclature and GTDB link | `data/raw/lpsn_names.tsv` line 931 | Supported exactly. |
| One close GTDB species mapping | `data/raw/gtdb_mappings.tsv` line 193455 and `data/raw/gtdb_species.tsv` line 2816 | Supported exactly. |
| BacDive local strain | `data/raw/bacdive_strains.tsv` line 86588 | Supported; BacDive 164352 has designation `YH-panp20`, taxon `NCBITaxon:2486576`, LPSN ID `lpsn:5758`, JCM/KCTC culture IDs, and type-strain flag `1`. |
| BacDive assembly and genome rows | `data/raw/strain_assemblies.tsv` line 78255 and `data/raw/strain_genome_records.tsv` lines 60855-60856 | Supported exactly by the single INSDC assembly and its IMG/BV-BRC genome links. |
| GOLD source attestation | `data/raw/gold_organisms.tsv` line 22354 | Supported with one GOLD organism. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 343260 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 17665 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct genus parent, root-first bacterial lineage, genetic code `11`, and all three generated related synonyms.
- LPSN supplies correct-name nomenclature, type-strain designations, DOI/PMID publication references, the INSDC sequence accession, and the GTDB close-match link.
- GTDB supplies one close species mapping.
- BacDive supplies the local type-strain anchor plus the single assembly and two genome records.
- GOLD contributes the directly filed organism count represented in `source_attestations`.
- With no StrainInfo overlay rows for BacDive 164352 and no curator-added `causal_graphs`, the optional related-record and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
