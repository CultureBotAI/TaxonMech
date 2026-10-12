# YAML Record Review: Acetobacter nitrogenifigens DSM 23921 = NBRC 105050

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_nitrogenifigens_dsm_23921_nbrc_105050.yaml`
- Reviewed UTC: 2026-09-26T07:53:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1120919` |
| label | `Acetobacter nitrogenifigens DSM 23921 = NBRC 105050` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:285268` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial strain record under `Acetobacter nitrogenifigens`. It has NCBI, GTDB, GOLD, BacDive, and Madin et al. source attestations; one GTDB `skos:closeMatch`; eight exact synonyms from GTDB and NCBI; one xref; one BacDive-derived local strain; 9 culture collection IDs; 23 genome assemblies; 17 genome records; 55 related records; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 35982 maps `NCBITaxon:1120919` to `acetobacter_nitrogenifigens_dsm_23921_nbrc_105050`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_nitrogenifigens_dsm_23921_nbrc_105050.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_nitrogenifigens_dsm_23921_nbrc_105050.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_nitrogenifigens.yaml data/taxa/bacteria/acetobacter_nitrogenifigens_dsm_23921_nbrc_105050.yaml data/taxa/bacteria/acetobacter_oeni.yaml data/taxa/bacteria/acetobacter_oeni_lmg_21952.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 241898 has `NCBITaxon:1120919`, label `Acetobacter nitrogenifigens DSM 23921 = NBRC 105050`, rank `STRAIN`, parent `NCBITaxon:285268`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|gold|madin_etal`, seven exact NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 14902 keeps the strain in scope. `data/raw/ncbi_merged_ids.tsv` line 11675 redirects old ID `NCBITaxon:1307911` into `NCBITaxon:1120919`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, exact synonyms, old merged ID, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 241898 and `data/raw/ncbi_merged_ids.tsv` line 11675 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 35982 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 14902 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 4394 | Supported exactly by one 3-genome `skos:closeMatch` to `GTDB:s__Acetobacter_nitrogenifigens`. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 20, `data/raw/bacdive_strains.tsv` line 21, and 9 `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive 20 materializes the single local strain with nine normalized culture IDs. |
| GOLD, genome, related-record, and Madin evidence | `data/raw/gold_organisms.tsv` line 2159, exact raw strain-table scans, and `data/raw/madin_taxa.tsv` line 3031 | Supported by `organism_count=1`, 23 raw assembly rows, 17 raw genome rows, 48 raw related records, and 4 Madin et al. assertions. |
| Empty same-taxon LPSN, MediaDive, BactoTraits, StrainInfo, NCBI type-material, and retained old-ID surfaces | Exact scans for `NCBITaxon:1120919` | Supported; no committed row in those processed source tables names this strain as an exact target. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, seven exact synonyms, one merged old ID, the direct `Acetobacter nitrogenifigens` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, one exact GTDB synonym, one xref, and a GENOME source attestation.
- BacDive supplies the canonical local strain, and the culture-collection table contributes the nine normalized collection identifiers attached to that strain.
- GOLD, BV-BRC, GTDB, NCBI Assembly, BacDive, and Madin et al. rows that resolve to this strain are represented as aggregate attestations or nested strain evidence as appropriate.
- No exact LPSN name, MediaDive row, BactoTraits row, StrainInfo overlay, NCBI type-material row, generated definition, or curator-added causal graph is present for this strain identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

This generated strain shares BacDive record 20 with its parent `NCBITaxon:285268` species record.
