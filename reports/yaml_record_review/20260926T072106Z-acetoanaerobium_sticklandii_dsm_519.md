# YAML Record Review: Acetoanaerobium sticklandii DSM 519

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetoanaerobium_sticklandii_dsm_519.yaml`
- Reviewed UTC: 2026-09-26T07:21:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:499177` |
| label | `Acetoanaerobium sticklandii DSM 519` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:1511` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated bacterial strain record for the DSM 519 strain of `Acetoanaerobium sticklandii`. It has source attestations from NCBITAXON, BACDIVE, MEDIADIVE, MADIN, and BACTOTRAITS, one exact NCBI synonym, one BacDive-derived local strain, 6 culture collection IDs, 10 genome assemblies, 7 genome records, 43 related records, and no LPSN nomenclature, GTDB taxonomy mappings, xrefs, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 521434 maps `NCBITaxon:499177` to `acetoanaerobium_sticklandii_dsm_519`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetoanaerobium_sticklandii_dsm_519.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetoanaerobium_sticklandii_dsm_519.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetoanaerobium_sp_wjdl_y2.yaml data/taxa/bacteria/acetoanaerobium_sticklandii.yaml data/taxa/bacteria/acetoanaerobium_sticklandii_dsm_519.yaml data/taxa/bacteria/acetobacter_aceti.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 113216 has `NCBITaxon:499177`, label `Acetoanaerobium sticklandii DSM 519`, rank `STRAIN`, parent `NCBITaxon:1511`, genetic code `11`, source set `ncbitaxon|bacdive|mediadive|madin_etal|bactotraits`, exact synonym `Clostridium sticklandii DSM 519`, no broad or related synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 14455 keeps the strain in scope. The exact same-taxon auxiliary rows are `data/raw/bacdive_strains.tsv` line 2618, `data/raw/bactotraits_taxa.tsv` line 7184, `data/raw/mediadive_taxa.tsv` line 10896, and `data/raw/madin_taxa.tsv` line 25521.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, exact synonym, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 113216 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 521434 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 14455 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| BacDive strain identity and culture IDs | `data/raw/bacdive_strains.tsv` line 2618 and six `data/raw/culture_collection_strains.tsv` rows keyed to `NCBITaxon:499177` | Supported; the BacDive 2717 strain carries ATCC, BCRC, CCUG, DSM, JCM, and NCIMB culture collection IDs. |
| BV-BRC strain-level genome evidence | `data/raw/strain_assemblies.tsv` lines 117678-117679 and `data/raw/strain_genome_records.tsv` lines 94608-94609 | Supported; both exact same-taxon assembly and genome rows are keyed to `NCBITaxon:499177`. |
| Related strain records | Exact scan of `data/raw/strain_related_records.tsv` for `NCBITaxon:499177` | Supported by 4 exact raw related-record rows. |
| BacDive JSON evidence | `data/bacdive/records.jsonl.gz` line 2617 | Supported; BacDive record 2717 names both species `NCBITaxon:1511` and strain `NCBITaxon:499177`. |
| BactoTraits, MediaDive, and Madin et al. attestations | `data/raw/bactotraits_taxa.tsv` line 7184, `data/raw/mediadive_taxa.tsv` line 10896, and `data/raw/madin_taxa.tsv` line 25521 | Supported exactly with 2 BactoTraits assertions, 2 MediaDive media IDs, and 6 Madin et al. assertions. |
| Empty same-taxon GTDB, LPSN, GOLD, StrainInfo, NCBI type-material, and NCBI merged-id surfaces | Exact scans for `NCBITaxon:499177` | Supported; no committed row names this strain as an exact GTDB, LPSN, GOLD, StrainInfo, NCBI type-material, or merged-id target. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the strain identity, the direct species parent, one exact synonym, and the exact 10-ancestor bacterial lineage.
- BacDive supplies the canonical local strain, and the culture-collection table contributes the six normalized collection identifiers attached to that strain.
- Exact BV-BRC rows support the two same-taxon raw genome rows, while the generator also aggregates genome assemblies, genome records, and related records for the same canonical BacDive 2717 strain identity.
- BactoTraits, MediaDive, and Madin et al. each supply one aggregate source attestation for the strain.
- No exact LPSN name, GTDB mapping, GOLD organism, StrainInfo overlay, NCBI type-material, ATB, or NCBI merged-id evidence is present for the strain NCBI identifier, and the YAML correctly has no LPSN nomenclature, taxonomy mapping, xref, definition, or causal-graph sections.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The generated species record for `NCBITaxon:1511` and this generated strain record both point at BacDive record 2717. The exact NCBI target differs, but the local strain block represents the same DSM 519 culture collection identity.
