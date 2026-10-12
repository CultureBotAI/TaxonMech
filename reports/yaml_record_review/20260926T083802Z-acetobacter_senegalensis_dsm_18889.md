# YAML Record Review: Acetobacter senegalensis DSM 18889

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_senegalensis_dsm_18889.yaml`
- Reviewed UTC: 2026-09-26T08:38:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1307918` |
| label | `Acetobacter senegalensis DSM 18889` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:446692` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated strain record under `Acetobacter senegalensis`. It has source attestations from NCBITAXON, GTDB, BACDIVE, MEDIADIVE, and BACTOTRAITS; one GTDB `skos:closeMatch`; one GTDB exact synonym; one BacDive strain row with two culture collection identifiers; 18 generated genome assemblies; 14 generated genome records; 48 generated related records; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 107662 maps `NCBITaxon:1307918` to `acetobacter_senegalensis_dsm_18889`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_senegalensis_dsm_18889.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_senegalensis_dsm_18889.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_senegalensis.yaml data/taxa/bacteria/acetobacter_senegalensis_dsm_18889.yaml data/taxa/bacteria/acetobacter_sicerae.yaml data/taxa/bacteria/acetobacter_sp.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 309520 has `NCBITaxon:1307918`, label `Acetobacter senegalensis DSM 18889`, rank `STRAIN`, parent `NCBITaxon:446692`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|mediadive|bactotraits`, no NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 15453 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 309520 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 107662 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 15453 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping and synonym | `data/raw/gtdb_mappings.tsv` line 17796 | Supported exactly by one 10-genome `skos:closeMatch` to `GTDB:s__Acetobacter_oryzoeni`. |
| BacDive strain, culture IDs, assemblies, genome records, and related records | `data/raw/bacdive_strains.tsv` line 22, two culture-collection rows, eight same-taxon assembly rows, seven same-taxon genome-record rows, and 18 same-taxon related-record rows | Supported; BacDive 21 is the exact same-taxon source strain and also carries species-level LMG 23690 links in the same deposit cluster. |
| MediaDive and BactoTraits source attestations | `data/raw/mediadive_taxa.tsv` line 2893 and `data/raw/bactotraits_taxa.tsv` line 2344 | Supported exactly by one direct MediaDive medium assertion and 12 direct BactoTraits assertions. |
| Native GOLD context | `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, `data/gold/analyses.jsonl.gz`, and exact `data/raw/gold_organisms.tsv` scan | Native GOLD has one exact organism/project/analysis chain for DSM 18889; no processed GOLD aggregate row names this strain, so no GOLD source attestation is generated. |
| Empty auxiliary evidence | Exact scans of LPSN, Madin et al., direct StrainInfo, processed GOLD aggregate, NCBI type-material, and NCBI merged-ID surfaces for `NCBITaxon:1307918` | Supported; no committed auxiliary row directly names this strain. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter senegalensis` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, one exact synonym, one xref, and the GENOME source attestation.
- BacDive 21 supplies the direct strain row and both DSM 18889 and LMG 23690 culture identifiers; the generated strain record includes direct DSM rows plus LMG rows that belong to the same BacDive cluster.
- MediaDive and BactoTraits have committed rows keyed directly to this strain.
- Native GOLD contains exact organism/project/analysis context, but no processed GOLD aggregate row is keyed to this taxon.
- StrainInfo rows in the YAML are scoped through BacDive culture deposit matches rather than direct `NCBITaxon:1307918` target rows.
- No exact same-taxon LPSN, Madin et al., NCBI type-material, direct StrainInfo, processed GOLD aggregate, or NCBI merged-ID row exists in the committed processed inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

BacDive 21 is intentionally shared with the parent `Acetobacter senegalensis` record, where the same source cluster is classified at this strain through `classified_as: NCBITaxon:1307918`.
