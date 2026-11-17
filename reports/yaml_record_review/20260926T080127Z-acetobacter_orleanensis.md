# YAML Record Review: Acetobacter orleanensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_orleanensis.yaml`
- Reviewed UTC: 2026-09-26T08:01:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:104099` |
| label | `Acetobacter orleanensis` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, Madin et al., StrainInfo, and NCBI type-material evidence. The YAML contains one LPSN nomenclature row, one GTDB `skos:closeMatch`, seven exact synonyms, nine related synonyms, two xrefs, one BacDive-derived type-strain block, 18 culture collection IDs, 30 genome assemblies, 23 genome records, 134 related records, and no generated definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 16137 maps `NCBITaxon:104099` to `acetobacter_orleanensis`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_orleanensis.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_orleanensis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_orleanensis.yaml data/taxa/bacteria/acetobacter_orleanensis_jcm_7639.yaml data/taxa/bacteria/acetobacter_orleanensis_nric_0473.yaml data/taxa/bacteria/acetobacter_oryzifermentans.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 18602 has `NCBITaxon:104099`, label `Acetobacter orleanensis`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|lpsn|gold|madin_etal`, seven exact NCBI synonyms, eight related NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 21028 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 18602 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 16137 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 21028 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature, LPSN synonym, and type-strain identifiers | `data/raw/lpsn_names.tsv` line 14812 | Supported exactly by one non-deprecated, legitimate, validly published species row. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 1566 | Supported exactly by one 5-genome `skos:closeMatch` to `GTDB:s__Acetobacter_orleanensis`. |
| BacDive, GOLD, Madin et al., StrainInfo, and NCBI type-material evidence | `data/bacdive/records.jsonl.gz` line 8, `data/raw/gold_organisms.tsv` line 572, `data/raw/madin_taxa.tsv` line 776, and exact StrainInfo/type-material scans | Supported by BacDive record 8, `organism_count=6`, one Madin et al. assertion, 4 StrainInfo assembly rows, 55 StrainInfo related records, 2 direct StrainInfo records, 31 StrainInfo deposit hits, and 23 exact type-material rows. |
| Empty same-taxon MediaDive, BactoTraits, and NCBI merged-ID surfaces | Exact scans for `NCBITaxon:104099` | Supported; no committed row in those processed source tables names this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, exact and related synonyms, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion, one LPSN exact synonym, and xrefs; GTDB supplies the only taxonomy mapping.
- BacDive supplies the single generated type-strain block, and the culture-collection table contributes the 18 normalized collection identifiers attached to that strain.
- GOLD, BV-BRC, GTDB, NCBI Assembly, AllTheBacteria, BacDive, StrainInfo, and Madin et al. rows that resolve to this species, to BacDive 8, or to the canonical child strain are represented as aggregate attestations or nested strain evidence as appropriate.
- No exact MediaDive row, BactoTraits row, NCBI merged ID, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

BacDive record 8 is the shared local-strain anchor for this species and the `NCBITaxon:1231342` child strain.
