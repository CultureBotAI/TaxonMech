# YAML Record Review: Acetoanaerobium sp. WJDL-Y2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetoanaerobium_sp_wjdl_y2.yaml`
- Reviewed UTC: 2026-09-26T07:21:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1382918` |
| label | `Acetoanaerobium sp. WJDL-Y2` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:2628769` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a compact NCBI-only seeded bacterial species record. It has one NCBITAXON name attestation and intentionally has no taxonomy mappings, nomenclature, synonyms, xrefs, local strains, genome assemblies, genome records, related records, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 138571 maps `NCBITaxon:1382918` to `acetoanaerobium_sp_wjdl_y2`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetoanaerobium_sp_wjdl_y2.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetoanaerobium_sp_wjdl_y2.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetoanaerobium_sp_wjdl_y2.yaml data/taxa/bacteria/acetoanaerobium_sticklandii.yaml data/taxa/bacteria/acetoanaerobium_sticklandii_dsm_519.yaml data/taxa/bacteria/acetobacter_aceti.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 337946 has `NCBITaxon:1382918`, label `Acetoanaerobium sp. WJDL-Y2`, rank `SPECIES`, parent `NCBITaxon:2628769`, genetic code `11`, source set `ncbitaxon`, no exact, broad, or related synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 418979 keeps the taxon in scope with the reason `attested rule: Acetoanaerobium sp. WJDL-Y2, 1 sources incl. NCBI`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, rank, parent, genetic code, empty synonym slots, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 337946 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 138571 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 418979 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| Empty GTDB, LPSN, Madin et al., MediaDive, and BactoTraits surfaces | Exact scans of `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/mediadive_taxa.tsv`, and `data/raw/bactotraits_taxa.tsv` for `NCBITaxon:1382918` | Supported; all six surfaces had 0 exact same-taxon rows. |
| Empty BacDive, culture-collection, strain assembly, strain genome, and strain related-record surfaces | Exact scans of `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` for `NCBITaxon:1382918` | Supported; all five target-row scans returned 0 rows. |
| Empty GOLD, StrainInfo, NCBI type-material, and NCBI merged-id surfaces | Exact scans of `data/raw/gold_organisms.tsv`, the native GOLD organisms/projects/analyses TSVs, `data/straininfo/*.tsv`, `data/raw/ncbi_type_material.tsv`, and `data/raw/ncbi_merged_ids.tsv` | Supported; no committed auxiliary row names this NCBI taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the identifier, label, rank, direct parent, genetic code `11`, root-first bacterial lineage, and the single NCBITAXON source attestation.
- The seed scope includes the taxon through the attested-source rule using that NCBI evidence.
- No exact same-taxon GTDB, LPSN, BacDive, MediaDive, GOLD, Madin et al., BactoTraits, ATB, or StrainInfo row exists in the committed source inventories.
- With `strain_count: 0`, no BacDive-derived or overlay strain rows, and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and product sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI snapshot that seeded the record.
