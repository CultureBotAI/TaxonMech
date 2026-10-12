# YAML Record Review: Acetobacter pasteurianus IFO 3283-26

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_pasteurianus_ifo_3283_26.yaml`
- Reviewed UTC: 2026-09-26T08:17:21Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:634456` |
| label | `Acetobacter pasteurianus IFO 3283-26` |
| rank | `NO_RANK` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:438` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a compact generated NCBI no-rank child record under `Acetobacter pasteurianus`. It has source attestations from NCBITAXON, GTDB, and MADIN; one exact GTDB synonym; one GTDB `skos:closeMatch`; one GTDB xref; and no generated local strains, genome assemblies, genome records, related records, LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 555850 maps `NCBITaxon:634456` to `acetobacter_pasteurianus_ifo_3283_26`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_pasteurianus_ifo_3283_26.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_pasteurianus_ifo_3283_26.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_pasteurianus_ifo_3283_26.yaml data/taxa/bacteria/acetobacter_pasteurianus_ifo_3283_32.yaml data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3188.yaml data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3222.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 146427 has `NCBITaxon:634456`, label `Acetobacter pasteurianus IFO 3283-26`, rank `NO_RANK`, parent `NCBITaxon:438`, genetic code `11`, source set `ncbitaxon|gtdb|madin_etal`, no NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 33632 keeps the record in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, no-rank status, parent, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 146427 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 555850 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 33632 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 300217 | Supported exactly by one 31-genome `skos:closeMatch` to `GTDB:s__Acetobacter_pasteurianus`. |
| Madin et al. evidence | `data/raw/madin_taxa.tsv` line 28042 | Supported exactly by 4 trait assertions. |
| Native GOLD snapshot and processed aggregate | `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, `data/gold/analyses.jsonl.gz`, and exact `data/raw/gold_organisms.tsv` scan | Native GOLD has one exact organism/project/analysis triple for `NCBITaxon:634456`; no processed GOLD aggregate row names this record, so no GOLD source attestation is generated. |
| Empty auxiliary evidence | Exact scans of BacDive, culture-collection, raw strain, StrainInfo, LPSN, MediaDive, BactoTraits, NCBI type-material, and NCBI merged-ID surfaces for `NCBITaxon:634456` | Supported; no committed auxiliary row names this record. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the no-rank identity, the direct `Acetobacter pasteurianus` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, exact synonym, xref, and GENOME source attestation.
- Madin et al. supplies the only non-NCBI/GTDB exact auxiliary row represented as an aggregate source attestation.
- No exact same-taxon BacDive, culture collection, processed GOLD aggregate, LPSN, MediaDive, BactoTraits, StrainInfo, NCBI type-material, or NCBI merged-ID row exists in the committed processed inventories.
- With `strain_count: 0`, no BacDive-derived or overlay strain rows, and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and product sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

Native GOLD carries organism `Go0006211`, sequencing project `Gp0006211`, and one matching analysis for IFO 3283-26; these exact native rows are not promoted into a processed `GOLD` source attestation for this generated child record.
