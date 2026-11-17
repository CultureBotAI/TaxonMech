# YAML Record Review: Acetobacter papayae JCM 25143

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_papayae_jcm_25143.yaml`
- Reviewed UTC: 2026-09-26T08:05:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1234671` |
| label | `Acetobacter papayae JCM 25143` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:1076592` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial strain record under `Acetobacter papayae`. It has NCBI, GTDB, and BacDive source attestations; one GTDB `skos:closeMatch`; five exact synonyms from NCBI and GTDB; one xref; one BacDive-derived local strain; 5 culture collection IDs; 10 genome assemblies; 8 genome records; 28 related records; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 79049 maps `NCBITaxon:1234671` to `acetobacter_papayae_jcm_25143`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_papayae_jcm_25143.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_papayae_jcm_25143.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_oryzoeni.yaml data/taxa/bacteria/acetobacter_papayae.yaml data/taxa/bacteria/acetobacter_papayae_jcm_25143.yaml data/taxa/bacteria/acetobacter_pasteurianus.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 282430 has `NCBITaxon:1234671`, label `Acetobacter papayae JCM 25143`, rank `STRAIN`, parent `NCBITaxon:1076592`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive`, four exact NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 30387 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, exact synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 282430 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 79049 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 30387 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 13411 | Supported exactly by one 7-genome `skos:closeMatch` to `GTDB:s__Acetobacter_papayae`. |
| BacDive strain identity and culture IDs | `data/bacdive/records.jsonl.gz` line 85566, `data/raw/bacdive_strains.tsv` line 85567, and five exact `data/raw/culture_collection_strains.tsv` rows | Supported; BacDive record 163331 materializes the single local strain with five normalized culture IDs. |
| GOLD, genome, and related-record evidence | Native GOLD scans and exact raw strain-table scans for `NCBITaxon:1234671` | Supported by one GOLD organism, project, and analysis; 9 exact raw assembly rows; 8 exact raw genome rows; and 20 exact raw related records. |
| Empty same-taxon LPSN, GOLD aggregate, MediaDive, Madin et al., BactoTraits, StrainInfo, NCBI type-material, and NCBI merged-ID surfaces | Exact scans for `NCBITaxon:1234671` | Supported; no committed row in those processed source tables names this strain as an exact target. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, four exact synonyms, the direct `Acetobacter papayae` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, one exact GTDB synonym, one xref, and a GENOME source attestation.
- BacDive supplies the canonical local strain, and the culture-collection table contributes the five normalized collection identifiers attached to that strain.
- GOLD, BV-BRC, GTDB, NCBI Assembly, BacDive, and StrainInfo rows that resolve through the same BacDive strain are represented in nested strain evidence as appropriate.
- No exact LPSN name, processed GOLD aggregate, MediaDive row, Madin et al. row, BactoTraits row, StrainInfo overlay, NCBI type-material row, generated definition, or curator-added causal graph is present for this strain identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

This generated strain shares BacDive record 163331 with its parent `NCBITaxon:1076592` species record.
