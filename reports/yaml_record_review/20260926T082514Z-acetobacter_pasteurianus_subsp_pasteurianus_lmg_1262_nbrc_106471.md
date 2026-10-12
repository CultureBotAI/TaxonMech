# YAML Record Review: Acetobacter pasteurianus subsp. pasteurianus LMG 1262 = NBRC 106471

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_pasteurianus_subsp_pasteurianus_lmg_1262_nbrc_106471.yaml`
- Reviewed UTC: 2026-09-26T08:25:14Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:940265` |
| label | `Acetobacter pasteurianus subsp. pasteurianus LMG 1262 = NBRC 106471` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:481145` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated strain record under `Acetobacter pasteurianus subsp. pasteurianus`. It has source attestations from NCBITAXON, GTDB, BACDIVE, MEDIADIVE, GOLD, MADIN, and BACTOTRAITS; one GTDB `skos:closeMatch`; nine exact synonyms; one BacDive strain with 20 culture-collection identifiers; six genome assemblies; four genome records; 83 related records; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 616623 maps `NCBITaxon:940265` to `acetobacter_pasteurianus_subsp_pasteurianus_lmg_1262_nbrc_106471`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_pasteurianus_subsp_pasteurianus_lmg_1262_nbrc_106471.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_pasteurianus_subsp_pasteurianus_lmg_1262_nbrc_106471.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3284.yaml data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3299.yaml data/taxa/bacteria/acetobacter_pasteurianus_subsp_pasteurianus.yaml data/taxa/bacteria/acetobacter_pasteurianus_subsp_pasteurianus_lmg_1262_nbrc_106471.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 200882 has `NCBITaxon:940265`, label `Acetobacter pasteurianus subsp. pasteurianus LMG 1262 = NBRC 106471`, rank `STRAIN`, parent `NCBITaxon:481145`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|mediadive|gold|madin_etal|bactotraits`, the eight NCBI exact synonyms carried in YAML, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 11 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 11 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 7145 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, snapshot date, and NCBI exact synonyms | `data/raw/ncbitaxon_taxa.tsv` line 200882 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 616623 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 7145 | Supported exactly by a single seed-scope row. |
| Lineage | 11 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 321059 | Supported exactly by one 31-genome `skos:closeMatch` to `GTDB:s__Acetobacter_pasteurianus`. |
| BacDive strain and deposits | `data/raw/bacdive_strains.tsv` line 6 and 20 `data/raw/culture_collection_strains.tsv` rows | Supported exactly for BacDive record 5, designation `Asai A-5, BU 121, Porges 38, A4`, and the 20 generated culture identifiers. |
| GOLD, MediaDive, Madin, and BactoTraits attestations | `data/raw/gold_organisms.tsv` line 44929, `data/raw/mediadive_taxa.tsv` line 14024, `data/raw/madin_taxa.tsv` line 33183, and `data/raw/bactotraits_taxa.tsv` line 9504 | Supported exactly: GOLD has three organisms; MediaDive has two media; Madin has two trait assertions; BactoTraits has one trait assertion. |
| NCBI merged IDs | `data/raw/ncbitaxon_merged.tsv` line 312 | The old `NCBITaxon:1006552` correctly redirects to current `NCBITaxon:940265`; the generated record uses only the current target ID. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter pasteurianus subsp. pasteurianus` parent, the exact 11-ancestor lineage, and eight exact strain synonyms.
- GTDB supplies the only taxonomy mapping, the GTDB exact synonym, the xref, and the GENOME source attestation.
- BacDive supplies the lone local strain and 20 culture-collection identifiers.
- GOLD supplies native evidence for `Go0016438`, `Go0565330`, and projects `Gp0016435`, `Gp0016438`, and `Gp0535689`; the generated GOLD aggregate reports three direct organisms for this NCBI strain.
- MediaDive, Madin et al., and BactoTraits source attestations all have exact same-taxon rows in the committed raw inventories.
- No exact same-taxon LPSN or StrainInfo target row exists in the committed inventories; StrainInfo entries in the generated record are scoped through BacDive culture-deposit matches.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

Several StrainInfo-related generated rows carry `bacdive_reference_conflict: true`, preserving the fact that the StrainInfo strain is linked through BacDive 5 while many of its deposits and sequences are broader `NCBITaxon:438` accessions. Those conflict markers are evidence-preserving metadata, not validation errors.
