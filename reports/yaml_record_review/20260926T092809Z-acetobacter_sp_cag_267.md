# YAML Record Review: Acetobacter sp. CAG:267

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_sp_cag_267.yaml`
- Reviewed UTC: 2026-09-26T09:28:09Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1262684` |
| label | `Acetobacter sp. CAG:267` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:2628570` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated species record under `unclassified Acetobacter`. It has source attestations from NCBITAXON and GTDB; one GTDB `skos:closeMatch` taxonomy mapping to `GTDB:s__CAG-267_sp001917135`; one GTDB exact synonym; one GTDB xref; an exact 10-entry NCBI lineage; genetic code 11; and no strains, genome assemblies, genome records, related records, LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 89310 maps `NCBITaxon:1262684` to `acetobacter_sp_cag_267`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_sp_cag_267.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_sp_cag_267.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_sp_c12_4.yaml data/taxa/bacteria/acetobacter_sp_c9_4.yaml data/taxa/bacteria/acetobacter_sp_cag_267.yaml data/taxa/bacteria/acetobacter_sp_cag_977.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 291998 has `NCBITaxon:1262684`, label `Acetobacter sp. CAG:267`, rank `SPECIES`, parent `NCBITaxon:2628570`, genetic code `11`, source set `ncbitaxon|gtdb`, no synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 66603 keeps the species in scope, and `data/raw/gtdb_mappings.tsv` line 14560 links the NCBI taxon to `GTDB:s__CAG-267_sp001917135` with `skos:closeMatch` and `genome_count: 35`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, species rank, parent, genetic code, source set, empty synonyms, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 291998 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 89310 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 66603 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB close match, xref, and synonym | `data/raw/gtdb_mappings.tsv` line 14560 | Supported exactly; the mapping row names `GTDB:s__CAG-267_sp001917135`, carries `skos:closeMatch`, and reports 35 genomes. |
| Empty nomenclature, strain, genome, related-record, and non-GTDB auxiliary sections | Exact scans of LPSN, BacDive, culture-collection, raw strain assembly, raw strain genome, raw strain related-record, MediaDive, GOLD aggregate, Madin et al., BactoTraits, StrainInfo, NCBI type-material, and NCBI merged-ID surfaces for `NCBITaxon:1262684` | Supported; no committed processed row on those surfaces names this NCBI taxon. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the placeholder species identity, the direct `unclassified Acetobacter` parent, and the exact 10-ancestor lineage.
- GTDB supplies a single species mapping to `GTDB:s__CAG-267_sp001917135`; the YAML preserves that as a `skos:closeMatch`, an exact synonym of `CAG-267 sp001917135`, a GTDB xref, and a 35-genome source attestation.
- The native GOLD catalog has one organism row and one analysis row keyed to this taxon, but no GOLD project row and no processed `data/raw/gold_organisms.tsv` aggregate row; therefore no GOLD attestation or GOLD related record is expected in the generated YAML.
- No LPSN, BacDive, MediaDive, Madin et al., BactoTraits, StrainInfo, NCBI type-material, NCBI merged-ID, raw strain, genome, or related-record row exists for this taxon.
- With `strain_count: 0` and no curator-added `causal_graphs`, all optional local strain, genome, related-record, definition, and product sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

This is a generated `Acetobacter` placeholder species record with a GTDB species-level close match; the absence of BacDive, LPSN, processed GOLD, and StrainInfo evidence is supported by the bounded committed-source scans.
