# YAML Record Review: Acetobacter aceti ATCC 23746

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_aceti_atcc_23746.yaml`
- Reviewed UTC: 2026-09-26T07:26:32Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:663932` |
| label | `Acetobacter aceti ATCC 23746` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:435` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a compact generated strain record under `Acetobacter aceti`. It has source attestations from NCBITAXON, GTDB, and MADIN; three exact synonyms, including one GTDB synonym and two NCBI synonyms; one GTDB `skos:closeMatch`; one GTDB xref; and no generated local strains, genome assemblies, genome records, related records, LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 563920 maps `NCBITaxon:663932` to `acetobacter_aceti_atcc_23746`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_aceti_atcc_23746.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_aceti_atcc_23746.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_aceti_1023.yaml data/taxa/bacteria/acetobacter_aceti_atcc_23746.yaml data/taxa/bacteria/acetobacter_aceti_nbrc_14818.yaml data/taxa/bacteria/acetobacter_aceti_nric_0242.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 153961 has `NCBITaxon:663932`, label `Acetobacter aceti ATCC 23746`, rank `STRAIN`, parent `NCBITaxon:435`, genetic code `11`, source set `ncbitaxon|gtdb|madin_etal`, exact NCBI synonyms `Acetobacter aceti str. ATCC 23746` and `Acetobacter aceti strain ATCC 23746`, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 11 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 11 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 33822 keeps the strain in scope with the reason `attested rule: Acetobacter aceti ATCC 23746, 3 sources incl. NCBI`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, two exact synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 153961 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 563920 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 33822 | Supported exactly by a single seed-scope row. |
| Lineage | 11 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 301536 | Supported exactly by one 7-genome `skos:closeMatch` to `GTDB:s__Acetobacter_aceti`. |
| Madin et al. trait attestation | `data/raw/madin_taxa.tsv` line 28660 | Supported exactly with 2 source assertions. |
| Empty BacDive, culture-collection, strain assembly, strain genome, strain related-record, StrainInfo, LPSN, BactoTraits, MediaDive, NCBI type-material, and NCBI merged-id surfaces | Exact same-taxon scans for `NCBITaxon:663932` | Supported; no row in those committed processed source tables names this strain. |
| GOLD state | Exact processed and native GOLD scans | Supported; no `data/raw/gold_organisms.tsv` aggregate row names `NCBITaxon:663932`, and the single native GOLD organism/project/analysis triplet does not produce a processed same-taxon strain evidence row. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, two exact synonyms, the direct `Acetobacter aceti` parent, and the root-first 11-ancestor lineage.
- GTDB supplies the only taxonomy mapping, one exact GTDB synonym, one xref, and a GENOME source attestation.
- Madin et al. supplies the only trait assertion aggregate.
- No exact same-taxon BacDive, culture collection, LPSN, MediaDive, BactoTraits, StrainInfo, NCBI type-material, or NCBI merged-id evidence is present, so the YAML correctly has no local strain block or nomenclature section.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The single native GOLD organism row for this NCBI strain did not have a corresponding processed `data/raw/gold_organisms.tsv` aggregate or generated raw strain row, so it is not expected to appear in the YAML.
