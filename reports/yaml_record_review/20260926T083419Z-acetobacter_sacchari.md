# YAML Record Review: Acetobacter sacchari

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_sacchari.yaml`
- Reviewed UTC: 2026-09-26T08:34:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:2661687` |
| label | `Acetobacter sacchari` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated species record under `Acetobacter`. It has source attestations from NCBITAXON, LPSN, GTDB, BACDIVE, and GOLD; one LPSN nomenclature row; one GTDB `skos:closeMatch`; two NCBITaxon related synonyms; one BacDive strain row with four culture collection identifiers; 7 generated genome assemblies; 5 generated genome records; 13 generated related records; and no definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 360168 maps `NCBITaxon:2661687` to `acetobacter_sacchari`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_sacchari.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_sacchari.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_pomorum.yaml data/taxa/bacteria/acetobacter_pomorum_dm001.yaml data/taxa/bacteria/acetobacter_pomorum_dsm_11825.yaml data/taxa/bacteria/acetobacter_sacchari.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 541055 has `NCBITaxon:2661687`, label `Acetobacter sacchari`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, two NCBITaxon related synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 18369 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, species rank, parent, genetic code, source set, snapshot date, and related synonyms | `data/raw/ncbitaxon_taxa.tsv` line 541055 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 360168 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 18369 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature | `data/raw/lpsn_names.tsv` line 588 | Supported; LPSN carries this as the correct name, links `GTDB:s__Acetobacter_sacchari`, and supplies accession `INSDC:LC103252`. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 204983 | Supported exactly by one 1-genome `skos:closeMatch` to `GTDB:s__Acetobacter_sacchari`. |
| BacDive strain, culture IDs, assemblies, genome records, and related records | `data/raw/bacdive_strains.tsv` line 89567, four culture-collection rows, seven assembly rows, five genome-record rows, and 13 related-record rows | Supported; BacDive 167334 is the exact species-keyed strain row for the TBRC 11175-linked genome evidence. |
| GOLD source attestation | `data/raw/gold_organisms.tsv` line 24423 and native GOLD organism/project/analysis rows | Supported; GOLD has one direct organism aggregate and one exact native organism/project/analysis chain for TBRC 11175. |
| Empty auxiliary evidence | Exact scans of MediaDive, Madin et al., BactoTraits, StrainInfo, and NCBI merged-ID surfaces for `NCBITaxon:2661687` | Supported; no committed row directly keys those auxiliary sources to this NCBI species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, the direct `Acetobacter` parent, the exact 9-ancestor lineage, and two related synonyms.
- LPSN supplies the correct-name nomenclature row and the `GTDB:s__Acetobacter_sacchari` xref; its committed row has no `type_strain_ids`, so the BacDive strain is not marked as a type strain from LPSN.
- GTDB supplies the only taxonomy mapping as `skos:closeMatch`.
- BacDive 167334 supplies one direct strain row, four culture collection identifiers, and the strain-genome links around TBRC 11175.
- GOLD supplies one processed organism aggregate and one native organism/project/analysis chain.
- NCBI type-material rows exist for this species; the generated record intentionally does not infer BacDive type-strain flags from that NCBI-only surface.
- No exact same-taxon MediaDive, Madin et al., BactoTraits, StrainInfo, or NCBI merged-ID row exists in the committed inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The BacDive designation contains a non-ASCII soft hyphen in the source YAML. It is schema-valid and source-preserving; no generated-field edit is recommended.
