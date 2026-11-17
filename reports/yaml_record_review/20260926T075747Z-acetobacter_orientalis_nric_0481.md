# YAML Record Review: Acetobacter orientalis NRIC 0481

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_orientalis_nric_0481.yaml`
- Reviewed UTC: 2026-09-26T07:57:47Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1307913` |
| label | `Acetobacter orientalis NRIC 0481` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:146474` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial strain record under `Acetobacter orientalis`. It has NCBI, GTDB, BacDive, and MediaDive source attestations; one GTDB `skos:closeMatch`; two exact synonyms from NCBI and GTDB; one xref; one BacDive-derived local strain; 7 culture collection IDs; 20 genome assemblies; 10 genome records; 60 related records; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 107658 maps `NCBITaxon:1307913` to `acetobacter_orientalis_nric_0481`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_orientalis_nric_0481.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_orientalis_nric_0481.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_okinawensis.yaml data/taxa/bacteria/acetobacter_okinawensis_jcm_25146.yaml data/taxa/bacteria/acetobacter_orientalis.yaml data/taxa/bacteria/acetobacter_orientalis_nric_0481.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 309516 has `NCBITaxon:1307913`, label `Acetobacter orientalis NRIC 0481`, rank `STRAIN`, parent `NCBITaxon:146474`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|mediadive`, one exact NCBI synonym, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 22485 keeps the strain in scope. `data/raw/ncbi_merged_ids.tsv` line 8775 redirects old ID `NCBITaxon:1231341` into `NCBITaxon:1307913`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, exact synonym, old merged ID, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 309516 and `data/raw/ncbi_merged_ids.tsv` line 8775 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 107658 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 22485 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 17792 | Supported exactly by one 47-genome `skos:closeMatch` to `GTDB:s__Acetobacter_orientalis`. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 16, `data/raw/bacdive_strains.tsv` line 17, and seven exact `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 16 materializes the single local strain with seven normalized culture IDs. |
| Genome and MediaDive evidence | Exact raw strain-table scans for `NCBITaxon:1307913`, native GOLD scans, and `data/raw/mediadive_taxa.tsv` line 2891 | Supported by direct BacDive genome rows, 1 native GOLD organism, 1 GOLD project, 1 GOLD analysis, and 2 MediaDive media IDs. |
| Empty same-taxon LPSN, GOLD aggregate, Madin et al., BactoTraits, StrainInfo, and NCBI type-material surfaces | Exact scans for `NCBITaxon:1307913` | Supported; no committed row in those processed source tables names this strain as an exact target. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, one exact synonym, one merged old ID, the direct `Acetobacter orientalis` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, one exact GTDB synonym, one xref, and a GENOME source attestation.
- BacDive supplies the canonical local strain, and the culture-collection table contributes the seven normalized collection identifiers attached to that strain.
- GOLD, BV-BRC, GTDB, NCBI Assembly, BacDive, and StrainInfo rows that resolve through the shared BacDive 16 culture identity are represented in nested strain evidence as appropriate.
- MediaDive supplies one aggregate source attestation for the strain.
- No exact LPSN name, processed GOLD aggregate, Madin et al. row, BactoTraits row, StrainInfo overlay, NCBI type-material row, generated definition, or curator-added causal graph is present for this strain identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

This generated strain shares BacDive record 16 with its parent `NCBITaxon:146474` species record.
