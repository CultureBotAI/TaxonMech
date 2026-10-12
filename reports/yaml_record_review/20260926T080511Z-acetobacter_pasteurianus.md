# YAML Record Review: Acetobacter pasteurianus

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_pasteurianus.yaml`
- Reviewed UTC: 2026-09-26T08:05:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:438` |
| label | `Acetobacter pasteurianus` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial species record with NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, Madin et al., BactoTraits, StrainInfo, and NCBI type-material evidence. The YAML contains one LPSN nomenclature row, three GTDB `skos:broadMatch` mappings, 21 exact synonyms, 31 related synonyms, two xrefs, 21 BacDive-derived local strains, 143 culture collection IDs, 76 genome assemblies, 61 genome records, 685 related records, and no generated definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 504821 maps `NCBITaxon:438` to `acetobacter_pasteurianus`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_pasteurianus.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_pasteurianus.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_oryzoeni.yaml data/taxa/bacteria/acetobacter_papayae.yaml data/taxa/bacteria/acetobacter_papayae_jcm_25143.yaml data/taxa/bacteria/acetobacter_pasteurianus.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 332 has `NCBITaxon:438`, label `Acetobacter pasteurianus`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, 21 exact NCBI synonyms, 26 related NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 188 keeps the species in scope. Four old NCBI IDs merge into `NCBITaxon:438`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, synonyms, old merged IDs, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 332 and exact `data/raw/ncbi_merged_ids.tsv` scan | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 504821 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 188 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and synonyms | `data/raw/lpsn_names.tsv` line 14813 | Supported exactly by one non-deprecated, legitimate, validly published species row with six LPSN synonym IDs. |
| GTDB mappings | `data/raw/gtdb_mappings.tsv` lines 289486-289488 | Supported exactly by three pooled `skos:broadMatch` mappings covering 47 total GTDB genomes. |
| BacDive, GOLD, MediaDive, Madin et al., BactoTraits, StrainInfo, and NCBI type-material evidence | Exact scans across committed source inventories | Supported by 21 BacDive records, `organism_count=809`, one MediaDive row with 6 media IDs, 5 Madin et al. assertions, 2 BactoTraits assertions, 7 StrainInfo assembly rows, 333 StrainInfo related rows, 106 direct StrainInfo records, 430 StrainInfo deposit hits, and 25 exact type-material rows. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, extensive synonymy, four merged old IDs, the direct `Acetobacter` parent, and the exact 9-ancestor lineage.
- LPSN supplies the correct-name nomenclature assertion, synonym cross-references, and xrefs.
- GTDB supplies three intentionally broad mappings; because each is a pooled `skos:broadMatch`, the mappings remain in `taxonomy_mappings` and do not become exact xrefs.
- BacDive supplies 21 generated local strain blocks, and the culture-collection table contributes the 143 normalized collection identifiers attached to those strains.
- GOLD, BV-BRC, GTDB, NCBI Assembly, AllTheBacteria, BacDive, StrainInfo, MediaDive, Madin et al., and BactoTraits rows that resolve to this species or its local strains are represented as aggregate attestations or nested strain evidence as appropriate.
- No generated definition or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

`Acetobacter pasteurianus` is the first very large record in this `Acetobacter` run; its nested BacDive strain block spans 21 local strains and hundreds of related records, all still validating cleanly in strict mode.
