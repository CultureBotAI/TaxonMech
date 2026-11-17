# YAML Record Review: Acetobacter indonesiensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_indonesiensis.yaml`
- Reviewed UTC: 2026-09-26T07:46:24Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:104101` |
| label | `Acetobacter indonesiensis` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, Madin et al., and StrainInfo evidence. The YAML contains one LPSN nomenclature row, one GTDB `skos:closeMatch`, one NCBI related synonym, two xrefs, two BacDive-derived local strains, 20 culture collection IDs, 13 genome assemblies, 11 genome records, 89 related records, and no curator-added definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 16139 maps `NCBITaxon:104101` to `acetobacter_indonesiensis`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_indonesiensis.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_indonesiensis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_indonesiensis.yaml data/taxa/bacteria/acetobacter_indonesiensis_nric_0313.yaml data/taxa/bacteria/acetobacter_lambici.yaml data/taxa/bacteria/acetobacter_lovaniensis.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 18604 has `NCBITaxon:104101`, label `Acetobacter indonesiensis`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal`, one related NCBI synonym, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 5899 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, related synonym, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 18604 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 16139 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 5899 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type-strain identifiers | `data/raw/lpsn_names.tsv` line 14805 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 1569 | Supported exactly by one 12-genome `skos:closeMatch` to `GTDB:s__Acetobacter_indonesiensis`. |
| BacDive strain identities | `data/bacdive/records.jsonl.gz` lines 18 and 23261 plus exact raw BacDive scans | Supported; BacDive 18 names the NRIC 0313 child strain, while BacDive 23488 is keyed directly to this species. |
| GOLD, MediaDive, Madin et al., StrainInfo, and NCBI type-material evidence | `data/raw/gold_organisms.tsv` line 575, `data/raw/mediadive_taxa.tsv` line 163, `data/raw/madin_taxa.tsv` line 778, and exact StrainInfo/type-material scans | Supported by `organism_count=15`, 2 MediaDive media IDs, 1 Madin et al. assertion, 1 StrainInfo assembly, 24 StrainInfo related records, 4 direct StrainInfo records, 15 StrainInfo deposit hits, and 13 exact type-material rows. |
| Raw strain evidence | Exact raw scans for `NCBITaxon:104101` | Supported by 1 species-keyed BacDive TSV row, 13 culture rows, 11 raw assemblies, 9 raw genome records, and 29 raw related records. |
| Empty same-taxon BactoTraits and NCBI merged-ID surfaces | Exact scans for `NCBITaxon:104101` | Supported; no committed BactoTraits or NCBI merged-ID row names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, one related synonym, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion and xrefs, while GTDB supplies the only taxonomy mapping.
- BacDive supplies two generated local strains, including the NRIC 0313 child strain also represented as `NCBITaxon:1307908`.
- GOLD, BV-BRC, GTDB, NCBI Assembly, StrainInfo, BacDive, MediaDive, and Madin et al. rows that resolve to this species or its canonical child strain are represented as aggregate attestations or nested strain evidence as appropriate.
- No exact BactoTraits, NCBI merged-ID, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

BacDive record 18 is strain-level for `NCBITaxon:1307908` but also names this parent species; the generated species and strain YAMLs therefore share the same BacDive 18 culture identity.
