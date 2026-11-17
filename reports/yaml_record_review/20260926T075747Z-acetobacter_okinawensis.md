# YAML Record Review: Acetobacter okinawensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_okinawensis.yaml`
- Reviewed UTC: 2026-09-26T07:57:47Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1076594` |
| label | `Acetobacter okinawensis` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, StrainInfo, and NCBI type-material evidence. The YAML contains one LPSN nomenclature row, two GTDB `skos:broadMatch` mappings, eight NCBI related synonyms, two xrefs, seven BacDive-derived local strains, 12 culture collection IDs, 11 genome assemblies, 6 genome records, 31 related records, and no generated definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 24158 maps `NCBITaxon:1076594` to `acetobacter_okinawensis`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_okinawensis.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_okinawensis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_okinawensis.yaml data/taxa/bacteria/acetobacter_okinawensis_jcm_25146.yaml data/taxa/bacteria/acetobacter_orientalis.yaml data/taxa/bacteria/acetobacter_orientalis_nric_0481.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 230855 has `NCBITaxon:1076594`, label `Acetobacter okinawensis`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, eight related NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 13751 keeps the species in scope. Seven old NCBI IDs merge into `NCBITaxon:1076594`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, related synonyms, merged old IDs, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 230855 and exact `data/raw/ncbi_merged_ids.tsv` scan | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 24158 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 13751 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type-strain identifiers | `data/raw/lpsn_names.tsv` line 27288 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mappings | `data/raw/gtdb_mappings.tsv` lines 2868-2869 | Supported exactly by two pooled `skos:broadMatch` mappings covering 9 total GTDB genomes. |
| BacDive, GOLD, StrainInfo, and NCBI type-material evidence | Exact BacDive, GOLD, raw strain-table, StrainInfo, and type-material scans | Supported by 7 BacDive records, `organism_count=4`, 1 StrainInfo assembly row, 7 StrainInfo related records, 1 direct StrainInfo record, 4 StrainInfo deposit hits, and 7 exact type-material rows. |
| Empty same-taxon MediaDive, BactoTraits, and Madin et al. surfaces | Exact scans for `NCBITaxon:1076594` | Supported; no committed row in those processed source tables names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, eight related synonyms, seven merged old IDs, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion and xrefs.
- GTDB supplies two intentionally broad mappings; because both are pooled `skos:broadMatch` mappings, they remain in `taxonomy_mappings` and do not become exact xrefs.
- BacDive supplies seven generated local strain blocks, including one BacDive record that also names the canonical child strain `NCBITaxon:1236501`.
- GOLD, BV-BRC, GTDB, NCBI Assembly, BacDive, and StrainInfo rows that resolve to this species or to the JCM 25146 / LMG 26457 child strain are represented as aggregate attestations or nested strain evidence as appropriate.
- No exact MediaDive, BactoTraits, Madin et al., generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The species-level broad GTDB mappings and the child-strain close mapping intentionally coexist: the species maps broadly to both `GTDB:s__Acetobacter_okinawensis` clusters, while `NCBITaxon:1236501` carries the exact child-strain `GTDB:s__Acetobacter_okinawensis` relationship.
