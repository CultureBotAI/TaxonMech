# YAML Record Review: Acetobacter pasteurianus NBRC 3188

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3188.yaml`
- Reviewed UTC: 2026-09-26T08:17:21Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1226663` |
| label | `Acetobacter pasteurianus NBRC 3188` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:438` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated strain record under `Acetobacter pasteurianus`. It has one BacDive strain, six culture-collection IDs, 10 NCBI assembly links, 8 typed genome records, 43 related records, source attestations from NCBITAXON, GTDB, and BACDIVE, one exact GTDB synonym, one GTDB `skos:closeMatch`, one GTDB xref, and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 76108 maps `NCBITaxon:1226663` to `acetobacter_pasteurianus_nbrc_3188`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_pasteurianus_nbrc_3188.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3188.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_pasteurianus_ifo_3283_26.yaml data/taxa/bacteria/acetobacter_pasteurianus_ifo_3283_32.yaml data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3188.yaml data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3222.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 279637 has `NCBITaxon:1226663`, label `Acetobacter pasteurianus NBRC 3188`, rank `STRAIN`, parent `NCBITaxon:438`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive`, no NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 30375 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 279637 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 76108 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 30375 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 12864 | Supported exactly by one 31-genome `skos:closeMatch` to `GTDB:s__Acetobacter_pasteurianus`. |
| BacDive strain identity and deposits | `data/raw/bacdive_strains.tsv` line 58293 and native BacDive record line 58292 | Supported exactly by BacDive strain `135987`, six culture-collection IDs, and a strain-level NCBI Taxonomy assignment to `1226663`. |
| NCBI, GTDB, GOLD, BV-BRC, IMG, ATB, StrainInfo, BioSample, BioProject, GOLD, and INSDC links | `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, `data/atb/*.tsv`, and `data/straininfo/*.tsv*` | Supported; all generated genome and related records preserve explicit source fields, matched deposits, GOLD organism/project chains, ATB sample evidence, or StrainInfo deposit evidence. |
| Native GOLD snapshot and processed aggregate | `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, `data/gold/analyses.jsonl.gz`, and exact `data/raw/gold_organisms.tsv` scan | Native GOLD has one exact organism/project/analysis triple for `NCBITaxon:1226663`; no processed taxon-level GOLD aggregate row names this strain, so no GOLD source attestation is generated. |
| Empty auxiliary evidence | Exact scans of LPSN, MediaDive, BactoTraits, Madin et al., NCBI type-material, and NCBI merged-ID surfaces for `NCBITaxon:1226663` | Supported; no committed auxiliary row names this strain. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter pasteurianus` parent, and the exact 10-ancestor lineage.
- GTDB supplies the only taxonomy mapping, exact synonym, xref, and taxon-level GENOME source attestation.
- BacDive supplies one generated strain, six deposits, one direct assembly, two direct genome records, and the BACDIVE source attestation.
- BV-BRC, GOLD, GTDB, NCBI Assembly, AllTheBacteria, and StrainInfo supply explicit genome or related-record links through the NBRC 3188 deposit; StrainInfo contributes six deposits, one genome row, and one 16S related sequence.
- No exact same-taxon LPSN, MediaDive, BactoTraits, Madin et al., NCBI type-material, or NCBI merged-ID row exists in the committed processed inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

Several GOLD organism related records intentionally point at the parent species taxon `NCBITaxon:438`; they are kept as strain-related GOLD organism context and are not promoted into a taxon-level `GOLD` source attestation for `NCBITaxon:1226663`.
