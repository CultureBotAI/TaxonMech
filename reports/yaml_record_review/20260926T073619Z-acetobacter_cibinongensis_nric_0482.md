# YAML Record Review: Acetobacter cibinongensis NRIC 0482

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_cibinongensis_nric_0482.yaml`
- Reviewed UTC: 2026-09-26T07:36:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1307904` |
| label | `Acetobacter cibinongensis NRIC 0482` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:146475` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial strain record for NRIC 0482 under `Acetobacter cibinongensis`. It has source attestations from NCBITAXON, GTDB, BACDIVE, and MEDIADIVE; one NCBI exact synonym; one GTDB exact synonym and xref; one GTDB `skos:closeMatch`; one BacDive-derived local strain; 6 culture collection IDs; 12 genome assemblies; 8 genome records; 38 related records; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 107649 maps `NCBITaxon:1307904` to `acetobacter_cibinongensis_nric_0482`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_cibinongensis_nric_0482.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_cibinongensis_nric_0482.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_cibinongensis.yaml data/taxa/bacteria/acetobacter_cibinongensis_nric_0482.yaml data/taxa/bacteria/acetobacter_conturbans.yaml data/taxa/bacteria/acetobacter_estunensis.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 309508 has `NCBITaxon:1307904`, label `Acetobacter cibinongensis NRIC 0482`, rank `STRAIN`, parent `NCBITaxon:146475`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|mediadive`, exact synonym `Acetobacter cibinongensis 4H-1`, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 22483 keeps the strain in scope. `data/raw/ncbi_merged_ids.tsv` line 8773 redirects old ID `NCBITaxon:1231339` into `NCBITaxon:1307904`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, exact synonym, old merged ID, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 309508 and `data/raw/ncbi_merged_ids.tsv` line 8773 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 107649 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 22483 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 17784 | Supported exactly by one 5-genome `skos:closeMatch` to `GTDB:s__Acetobacter_cibinongensis`. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 15, `data/raw/bacdive_strains.tsv` line 16, and six `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 15 materializes the single local strain with six normalized culture IDs. |
| Genome and MediaDive evidence | Exact raw scans and `data/raw/mediadive_taxa.tsv` line 2885 | Supported by 1 exact same-taxon raw assembly row, 2 exact raw genome rows, and 2 MediaDive media IDs; additional generated nested rows are inherited through the shared BacDive 15 strain identity. |
| Empty same-taxon LPSN, GOLD aggregate, Madin et al., BactoTraits, StrainInfo, and NCBI type-material surfaces | Exact scans for `NCBITaxon:1307904` | Supported; no committed row in those processed source tables names this strain as an exact target. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the exact synonym, the merged old ID, the direct `Acetobacter cibinongensis` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, one exact GTDB synonym, one xref, and a GENOME source attestation.
- BacDive supplies the canonical local strain, and the culture-collection table contributes the six normalized collection identifiers attached to that strain.
- BV-BRC, GOLD, GTDB, NCBI Assembly, StrainInfo, and BacDive evidence that resolves through BacDive 15 is represented in the nested strain block.
- MediaDive supplies the only aggregate source attestation beyond NCBI, GTDB, and BacDive.
- No exact LPSN name, processed GOLD aggregate, Madin et al., BactoTraits, StrainInfo overlay, NCBI type-material, generated definition, or curator-added causal graph is present for this strain identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The native GOLD table has one NRIC 0482 organism/project/analysis triplet, but this strain does not have its own `data/raw/gold_organisms.tsv` aggregate row; GOLD-derived nested rows are represented through the canonical BacDive strain where available.
