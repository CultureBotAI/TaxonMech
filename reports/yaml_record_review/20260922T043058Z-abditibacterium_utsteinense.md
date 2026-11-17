# YAML Record Review: Abditibacterium utsteinense

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abditibacterium_utsteinense.yaml
- Started UTC: 2026-09-22T04:28:00Z
- Finished UTC: 2026-09-22T04:30:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1960156 |
| label | Abditibacterium utsteinense |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2109263 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abditibacterium_utsteinense.yaml`. It carries LPSN nomenclature, one GTDB `skos:closeMatch`, NCBI related synonyms, one BacDive-derived type-strain entry with BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo assembly/genome/related-record evidence, and source attestations from NCBITAXON, LPSN, GTDB, BACDIVE, MEDIADIVE, and GOLD.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 312937 maps `NCBITaxon:1960156` to slug `abditibacterium_utsteinense`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abditibacterium_utsteinense.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abditibacterium_utsteinense.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abditibacterium_utsteinense.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 504456 has `NCBITaxon:1960156`, label `Abditibacterium utsteinense`, rank `SPECIES`, direct parent `NCBITaxon:2109263`, genetic code `11`, related synonyms `Abditibacterium utsteinense Tahon et al. 2018` and `bacterium LMG 29911`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:2109258` Abditibacteriota, `PHYLUM` | line 518358 |
| `NCBITaxon:2109259` Abditibacteriia, `CLASS` | line 518359 |
| `NCBITaxon:2109260` Abditibacteriales, `ORDER` | line 518360 |
| `NCBITaxon:2109261` Abditibacteriaceae, `FAMILY` | line 518361 |
| `NCBITaxon:2109263` Abditibacterium, `GENUS` | line 518362 |

`curation/seed_scope.tsv` line 12889 keeps this taxon in scope through the attested-source rule.

`data/raw/lpsn_names.tsv` line 33110 supports the LPSN nomenclature: `lpsn:797965`, species name `Abditibacterium utsteinense`, authority `Tahon et al. 2018`, correct-name status, the `NCBITaxon:1960156` and `GTDB:s__Abditibacterium_utsteinense` cross-references, DSM 105287 and LMG 29911 type-strain designations, PMID 29475572, DOI publications, and the KY386500 sequence accession.

`data/raw/gtdb_mappings.tsv` line 109273 maps `GTDB:s__Abditibacterium_utsteinense` to `NCBITaxon:1960156` with `skos:closeMatch`; `data/raw/gtdb_species.tsv` line 2806 records the GTDB species as a one-genome species in genus `GTDB:g__Abditibacterium`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, related synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 504456 | Supported exactly. |
| LPSN nomenclature, valid publication, type strains, publications, sequence accession, and GTDB link | `data/raw/lpsn_names.tsv` line 33110 | Supported exactly. |
| One close GTDB species mapping | `data/raw/gtdb_mappings.tsv` line 109273 and `data/raw/gtdb_species.tsv` line 2806 | Supported exactly. |
| BacDive source strain | `data/raw/bacdive_strains.tsv` line 81889 | Supported; BacDive strain 159652 has designation `R-68213`, taxon `NCBITaxon:1960156`, LPSN ID `lpsn:797965`, DSM 105287 and LMG 29911 culture IDs, and type-strain flag `0`. |
| MediaDive and GOLD source attestations | `data/raw/mediadive_taxa.tsv` line 6165 and `data/raw/gold_organisms.tsv` line 18014 | Supported exactly with one medium and two GOLD organism records. |
| Assembly and genome rows attached to the local BacDive strain | `data/raw/strain_assemblies.tsv` lines 68579-68587, `data/raw/strain_genome_records.tsv` lines 53255-53260, and `data/straininfo/assemblies.tsv` line 5352 | Supported; all rows carry `NCBITaxon:1960156` and the expected LMG 29911, DSM 105287, GTDB, NCBI, BV-BRC, GOLD, and StrainInfo identifiers. |
| Related records attached to the local BacDive strain | `data/raw/strain_related_records.tsv` lines 213586-213607 and `data/straininfo/strain_links.tsv` lines 58749-58750 | Supported; the YAML preserves the expected BioProject, BioSample, GOLD analysis, GOLD organism, GOLD project, StrainInfo strain, and StrainInfo deposit references. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 312937 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 12889 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the identity, direct genus parent, root-first bacterial lineage, genetic code `11`, two related synonyms, and the NCBITAXON source attestation.
- LPSN supplies validly published correct-name nomenclature, authority text, type-strain designations, DOI/PMID publication references, an INSDC sequence accession, and the GTDB close-match link.
- GTDB supplies the one close species mapping and both GenBank and RefSeq assembly links for LMG 29911.
- BacDive supplies the local type-strain anchor, and BV-BRC, GOLD, NCBI Assembly, GTDB, and StrainInfo source rows all join onto that same local strain through LMG 29911 and DSM 105287.
- MediaDive and GOLD supply source attestations that are represented in `source_attestations`; neither supplies additional same-taxon TaxonRecord fields beyond the seeded counts and strain evidence already present.
- With no curator-added `causal_graphs`, the optional causal-graph section is correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
