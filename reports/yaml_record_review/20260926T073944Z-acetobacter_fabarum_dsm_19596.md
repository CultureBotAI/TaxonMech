# YAML Record Review: Acetobacter fabarum DSM 19596

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_fabarum_dsm_19596.yaml`
- Reviewed UTC: 2026-09-26T07:39:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1307906` |
| label | `Acetobacter fabarum DSM 19596` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:483199` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial strain record for DSM 19596 under `Acetobacter fabarum`. It has source attestations from NCBITAXON, GTDB, BACDIVE, MEDIADIVE, and BACTOTRAITS; one GTDB exact synonym and xref; one GTDB `skos:closeMatch`; one BacDive-derived local strain; 2 culture collection IDs; 16 genome assemblies; 11 genome records; 41 related records; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 107651 maps `NCBITaxon:1307906` to `acetobacter_fabarum_dsm_19596`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_fabarum_dsm_19596.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_fabarum_dsm_19596.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_estunensis_nric_0472.yaml data/taxa/bacteria/acetobacter_fabarum.yaml data/taxa/bacteria/acetobacter_fabarum_dsm_19596.yaml data/taxa/bacteria/acetobacter_fallax.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 309510 has `NCBITaxon:1307906`, label `Acetobacter fabarum DSM 19596`, rank `STRAIN`, parent `NCBITaxon:483199`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|mediadive|bactotraits`, no NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 15449 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 309510 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 107651 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 15449 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 17786 | Supported exactly by one 43-genome `skos:closeMatch` to `GTDB:s__Acetobacter_fabarum`. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 23, `data/raw/bacdive_strains.tsv` line 24, and two `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 23 materializes the single local strain with DSM and LMG culture IDs. |
| Genome and related-record evidence | Exact scans of raw strain tables for `NCBITaxon:1307906` | Supported by 7 raw assembly rows, 4 raw genome rows, and 10 raw related records keyed to this strain. |
| BactoTraits and MediaDive attestations | `data/raw/bactotraits_taxa.tsv` line 2339 and `data/raw/mediadive_taxa.tsv` line 2886 | Supported exactly with 5 BactoTraits assertions and 1 MediaDive medium. |
| Empty same-taxon LPSN, GOLD aggregate, Madin et al., StrainInfo, NCBI type-material, and NCBI merged-ID surfaces | Exact scans for `NCBITaxon:1307906` | Supported; no committed row in those processed source tables names this strain as an exact target. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter fabarum` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, one exact GTDB synonym, one xref, and a GENOME source attestation.
- BacDive supplies the canonical local strain, and the culture-collection table contributes the two normalized collection identifiers attached to that strain.
- BV-BRC, GOLD, GTDB, NCBI Assembly, AllTheBacteria, StrainInfo, and BacDive evidence that resolves through BacDive 23 is represented in the nested strain block.
- BactoTraits and MediaDive each supply one aggregate source attestation for the strain.
- No exact LPSN name, processed GOLD aggregate, Madin et al., StrainInfo overlay, NCBI type-material, generated definition, or curator-added causal graph is present for this strain identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

This generated strain shares BacDive record 23 with its parent `NCBITaxon:483199` species record.
