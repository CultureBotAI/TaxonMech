# YAML Record Review: Acetobacter orleanensis JCM 7639

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_orleanensis_jcm_7639.yaml`
- Reviewed UTC: 2026-09-26T08:01:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1231342` |
| label | `Acetobacter orleanensis JCM 7639` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:104099` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial strain record under `Acetobacter orleanensis`. It has NCBI, GTDB, BacDive, MediaDive, and BactoTraits source attestations; one GTDB `skos:closeMatch`; one GTDB exact synonym; one xref; one BacDive-derived local strain; 18 culture collection IDs; 30 genome assemblies; 23 genome records; 134 related records; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 77704 maps `NCBITaxon:1231342` to `acetobacter_orleanensis_jcm_7639`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_orleanensis_jcm_7639.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_orleanensis_jcm_7639.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_orleanensis.yaml data/taxa/bacteria/acetobacter_orleanensis_jcm_7639.yaml data/taxa/bacteria/acetobacter_orleanensis_nric_0473.yaml data/taxa/bacteria/acetobacter_oryzifermentans.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 281125 has `NCBITaxon:1231342`, label `Acetobacter orleanensis JCM 7639`, rank `STRAIN`, parent `NCBITaxon:104099`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|mediadive|bactotraits`, no NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 15253 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 281125 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 77704 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 15253 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 13208 | Supported exactly by one 5-genome `skos:closeMatch` to `GTDB:s__Acetobacter_orleanensis`. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 8, `data/raw/bacdive_strains.tsv` line 9, and 18 exact `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 8 materializes the single local strain with 18 normalized culture IDs. |
| Direct genome, BactoTraits, and MediaDive evidence | Exact raw strain-table scans for `NCBITaxon:1231342`, `data/raw/bactotraits_taxa.tsv` line 1887, and `data/raw/mediadive_taxa.tsv` line 2306 | Supported by the direct BacDive assembly/genome rows, 4 BactoTraits assertions, and 3 MediaDive media IDs. |
| Empty same-taxon LPSN, GOLD aggregate, Madin et al., StrainInfo, NCBI type-material, and NCBI merged-ID surfaces | Exact scans for `NCBITaxon:1231342` | Supported; no committed row in those processed source tables names this strain as an exact target. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter orleanensis` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, one exact GTDB synonym, one xref, and a GENOME source attestation.
- BacDive supplies the canonical local strain, and the culture-collection table contributes the 18 normalized collection identifiers attached to that strain.
- GOLD, BV-BRC, GTDB, NCBI Assembly, AllTheBacteria, BacDive, and StrainInfo rows that resolve through the shared BacDive 8 culture identity are represented in nested strain evidence as appropriate.
- BactoTraits and MediaDive each supply one aggregate source attestation for the strain.
- No exact LPSN name, processed GOLD aggregate, Madin et al. row, StrainInfo overlay, NCBI type-material row, generated definition, or curator-added causal graph is present for this strain identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

This generated strain shares BacDive record 8 with its parent `NCBITaxon:104099` species record.
