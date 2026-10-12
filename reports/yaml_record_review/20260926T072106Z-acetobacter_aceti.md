# YAML Record Review: Acetobacter aceti

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_aceti.yaml`
- Reviewed UTC: 2026-09-26T07:21:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:435` |
| label | `Acetobacter aceti` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:151157` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with source attestations from NCBITAXON, LPSN, GTDB, GOLD, BacDive, MediaDive, Madin et al., and BactoTraits. The YAML contains one LPSN nomenclature row, three GTDB `skos:broadMatch` mappings, 32 synonyms, two xrefs, eight BacDive-derived local strains, 48 culture collection IDs, 37 genome assemblies, 22 genome records, 244 related records, and no curator-added definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 503780 maps `NCBITaxon:435` to `acetobacter_aceti`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_aceti.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_aceti.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetoanaerobium_sp_wjdl_y2.yaml data/taxa/bacteria/acetoanaerobium_sticklandii.yaml data/taxa/bacteria/acetoanaerobium_sticklandii_dsm_519.yaml data/taxa/bacteria/acetobacter_aceti.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 329 has `NCBITaxon:435`, label `Acetobacter aceti`, rank `SPECIES`, parent `NCBITaxon:151157`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, 15 exact NCBI synonyms, 16 related NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 372 keeps the species in scope. `data/raw/ncbi_merged_ids.tsv` lines 96406 and 96409 redirect old IDs `NCBITaxon:84364` and `NCBITaxon:84368` into `NCBITaxon:435`, and the generated YAML retains those old identifiers as equivalent identifiers.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, exact and related synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 329 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 503780 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 372 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| NCBI merged IDs | `data/raw/ncbi_merged_ids.tsv` lines 96406 and 96409 | Supported; both old NCBITaxon IDs redirect to `NCBITaxon:435`. |
| LPSN nomenclature, LPSN synonym, type-strain identifiers, and nomenclatural publication accession | `data/raw/lpsn_names.tsv` line 14794 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mappings | `data/raw/gtdb_mappings.tsv` lines 289291-289293 | Supported exactly by three pooled `skos:broadMatch` mappings covering 12 total GTDB genomes. |
| GOLD organism count and GOLD project evidence | `data/raw/gold_organisms.tsv` line 35396 plus exact native GOLD scans | Supported; the aggregate has `organism_count=293`, and the native GOLD tables contain 292 matching organism rows, 2 project rows, and 2 analysis rows for this taxon. |
| BacDive-derived strains and culture collection rows | Exact scans of `data/bacdive/records.jsonl.gz`, `data/raw/bacdive_strains.tsv`, and `data/raw/culture_collection_strains.tsv` for `NCBITaxon:435` | Supported; 8 BacDive JSON rows, 7 normalized BacDive strain rows, and 25 raw culture-collection rows resolve to 8 generated local strains and 48 culture collection IDs after canonicalization. |
| Genome and related-record evidence | Exact scans of `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, and `data/straininfo/*.tsv` for `NCBITaxon:435` | Supported; 8 raw assemblies, 6 raw genome records, 156 raw related records, 6 StrainInfo assemblies, and 109 StrainInfo related records contribute to the generated strain blocks. |
| NCBI type material, MediaDive, Madin et al., and BactoTraits attestations | `data/raw/ncbi_type_material.tsv`, `data/raw/mediadive_taxa.tsv` line 10186, `data/raw/madin_taxa.tsv` line 24096, and `data/raw/bactotraits_taxa.tsv` line 6622 | Supported; all 28 exact NCBI type-material rows are `type strain` rows, MediaDive reports one medium, Madin et al. reports 5 assertions, and BactoTraits reports 1 assertion. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the primary identity, the direct parent, 31 synonym strings, two old IDs merged into the current species ID, and the exact 10-ancestor bacterial lineage.
- LPSN supplies the correct-name nomenclature assertion, one related synonym, two xrefs, a sequence accession, a publication accession, and the type-strain identifier set for the species.
- GTDB contributes three intentionally broad species mappings; because each is a pooled `skos:broadMatch`, the mappings remain in `taxonomy_mappings` and do not become exact xrefs.
- BacDive and StrainInfo contribute the eight generated local strain blocks and their culture collection IDs, assemblies, genome records, and related records.
- GOLD, MediaDive, Madin et al., BactoTraits, BV-BRC, GTDB, NCBI Assembly, and AllTheBacteria source rows that resolve to this taxon are represented as aggregate source attestations or nested strain evidence as appropriate.
- The source scan found no generated definitions or curator-added causal graphs, matching the empty optional product sections in the YAML.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The native GOLD organism table has 292 exact rows, while `data/raw/gold_organisms.tsv` carries the generated aggregate of `organism_count=293`; the YAML records the aggregate source attestation and the strain-linked GOLD project evidence that resolve through canonical local strains.
