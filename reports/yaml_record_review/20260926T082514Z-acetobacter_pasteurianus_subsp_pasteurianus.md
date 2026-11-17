# YAML Record Review: Acetobacter pasteurianus subsp. pasteurianus

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_pasteurianus_subsp_pasteurianus.yaml`
- Reviewed UTC: 2026-09-26T08:25:14Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:481145` |
| label | `Acetobacter pasteurianus subsp. pasteurianus` |
| rank | `SUBSPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:438` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated subspecies record under `Acetobacter pasteurianus`. It has source attestations from NCBITAXON, GTDB, BACDIVE, and GOLD; two GTDB `skos:broadMatch` mappings; one NCBITaxon related synonym; two BacDive strain rows, one filed directly here and one classified at descendant `NCBITaxon:940265`; 26 generated genome assemblies; 20 generated genome records; 190 generated related records; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 515533 maps `NCBITaxon:481145` to `acetobacter_pasteurianus_subsp_pasteurianus`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_pasteurianus_subsp_pasteurianus.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_pasteurianus_subsp_pasteurianus.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3284.yaml data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3299.yaml data/taxa/bacteria/acetobacter_pasteurianus_subsp_pasteurianus.yaml data/taxa/bacteria/acetobacter_pasteurianus_subsp_pasteurianus_lmg_1262_nbrc_106471.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 107416 has `NCBITaxon:481145`, label `Acetobacter pasteurianus subsp. pasteurianus`, rank `SUBSPECIES`, parent `NCBITaxon:438`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|gold`, the single related synonym carried in YAML, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 55789 keeps the subspecies in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, subspecies rank, parent, genetic code, source set, snapshot date, and related synonym | `data/raw/ncbitaxon_taxa.tsv` line 107416 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 515533 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 55789 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mappings | `data/raw/gtdb_mappings.tsv` lines 291987-291988 | Supported exactly by broad matches to `GTDB:s__Acetobacter_oryzoeni` and `GTDB:s__Acetobacter_pasteurianus`; the YAML preserves their pooled `skos:broadMatch` scope. |
| BacDive direct and descendant strains | Native BacDive taxon assignments plus `data/raw/bacdive_strains.tsv` line 5 and culture-collection rows for BacDive 4 | Supported; BacDive 4 is direct to this subspecies, and BacDive 5 is retained as a descendant classified at `NCBITaxon:940265`. |
| GOLD direct organisms | `data/raw/gold_organisms.tsv` line 36762 and native GOLD organism/project/analysis rows | Supported exactly for two direct GOLD organisms, `Go0396247` / `Gp0260645` and `Go0396543` / `Gp0260972`. |
| Empty auxiliary evidence | Exact scans of LPSN, MediaDive, Madin et al., BactoTraits, NCBI merged-ID, and same-taxon StrainInfo surfaces for `NCBITaxon:481145` | Supported; no committed row directly keys those auxiliary sources to this NCBI subspecies. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the subspecies identity, the direct `Acetobacter pasteurianus` parent, the exact 10-ancestor lineage, and one related synonym.
- GTDB supplies two broad species mappings, and the record keeps those as `skos:broadMatch` rather than presenting them as equivalence.
- BacDive direct and descendant accounting explains `strain_count: 2`: BacDive 4 is filed directly here, and BacDive 5 is filed under child strain `NCBITaxon:940265`.
- GOLD supplies a direct two-organism aggregate plus native organism/project/analysis rows for the two SRCM strain projects under this subspecies.
- NCBI type-material rows exist for this subspecies; the generated record intentionally does not infer BacDive type-strain flags from that NCBI-only surface.
- No exact same-taxon LPSN, MediaDive, Madin et al., BactoTraits, NCBI merged-ID, or StrainInfo row exists in the committed inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The record mixes evidence attached directly to `NCBITaxon:481145` with strain evidence retained from descendant `NCBITaxon:940265`; the YAML keeps that distinction with `classified_as: NCBITaxon:940265` on the BacDive 5 strain row.
