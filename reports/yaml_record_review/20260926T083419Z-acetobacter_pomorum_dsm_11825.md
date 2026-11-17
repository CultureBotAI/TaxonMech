# YAML Record Review: Acetobacter pomorum DSM 11825

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_pomorum_dsm_11825.yaml`
- Reviewed UTC: 2026-09-26T08:34:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1307917` |
| label | `Acetobacter pomorum DSM 11825` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:65959` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated strain record under `Acetobacter pomorum`. It has source attestations from NCBITAXON, GTDB, BACDIVE, MEDIADIVE, and BACTOTRAITS; one GTDB `skos:closeMatch`; one GTDB exact synonym; one BacDive strain row with three culture collection identifiers; 8 generated genome assemblies; 13 generated genome records; 35 generated related records; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 107661 maps `NCBITaxon:1307917` to `acetobacter_pomorum_dsm_11825`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_pomorum_dsm_11825.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_pomorum_dsm_11825.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_pomorum.yaml data/taxa/bacteria/acetobacter_pomorum_dm001.yaml data/taxa/bacteria/acetobacter_pomorum_dsm_11825.yaml data/taxa/bacteria/acetobacter_sacchari.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 309519 has `NCBITaxon:1307917`, label `Acetobacter pomorum DSM 11825`, rank `STRAIN`, parent `NCBITaxon:65959`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|mediadive|bactotraits`, no NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 15452 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 309519 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 107661 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 15452 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping and synonym | `data/raw/gtdb_mappings.tsv` line 17795 | Supported exactly by one 3-genome `skos:closeMatch` to `GTDB:s__Acetobacter_pomorum`. |
| BacDive strain, culture IDs, assemblies, genome records, and related records | `data/raw/bacdive_strains.tsv` line 12, three culture-collection rows, eight assembly rows, eight genome-record rows, and 26 related-record rows | Supported; BacDive 11 is the exact same-taxon source strain for the three culture collection identifiers and downstream genome links. |
| MediaDive and BactoTraits source attestations | `data/raw/mediadive_taxa.tsv` line 2892 and `data/raw/bactotraits_taxa.tsv` line 2343 | Supported exactly by two direct MediaDive medium assertions and five direct BactoTraits assertions. |
| Native GOLD context | `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, `data/gold/analyses.jsonl.gz`, and exact `data/raw/gold_organisms.tsv` scan | Native GOLD has one exact organism, two exact projects, and two exact analysis rows for DSM 11825; no processed GOLD aggregate row names this strain, so no GOLD source attestation is generated. |
| Empty auxiliary evidence | Exact scans of LPSN, Madin et al., NCBI type-material, direct StrainInfo, processed GOLD aggregate, and NCBI merged-ID surfaces for `NCBITaxon:1307917` | Supported; no committed auxiliary row directly names this strain. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter pomorum` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, one exact synonym, one xref, and the GENOME source attestation.
- BacDive 11 supplies the exact same-taxon strain evidence, three culture collection identifiers, eight generated genome assemblies, eight direct genome records, and 26 direct related records.
- MediaDive and BactoTraits have committed rows keyed directly to this strain.
- Native GOLD contains exact organism/project/analysis context, but no processed GOLD aggregate row is keyed to this taxon.
- StrainInfo rows in the YAML are scoped through BacDive culture deposit matches from the parent species context rather than direct `NCBITaxon:1307917` target rows.
- No exact same-taxon LPSN, Madin et al., NCBI type-material, direct StrainInfo, processed GOLD aggregate, or NCBI merged-ID row exists in the committed processed inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

BacDive 11 is also represented on the parent `Acetobacter pomorum` record as a type-strain child row classified at `NCBITaxon:1307917`; this strain record carries the exact same-taxon view of that evidence.
