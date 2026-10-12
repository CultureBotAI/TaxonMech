# YAML Record Review: Aspergillus turcosus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_turcosus.yaml
- Started UTC: 2026-09-21T22:04:01Z
- Finished UTC: 2026-09-21T22:04:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1245748 |
| label | Aspergillus turcosus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_turcosus.yaml`. It carries five related NCBI synonyms, no exact NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_turcosus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_turcosus.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_turcosus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 286464 has `NCBITaxon:1245748`, label `Aspergillus turcosus`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, five related synonyms, no exact synonyms, and source `gold`. `curation/seed_scope.tsv` line 58658 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` redirects old IDs `NCBITaxon:1245747`, `NCBITaxon:388756`, `NCBITaxon:388757`, and `NCBITaxon:388758` into `NCBITaxon:1245748`. `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 286464 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58658 | Supported exactly: `attested rule: Aspergillus turcosus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 5917 | Supported exactly with three aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1245748`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with eight rows: six culture-from-holotype rows for DTO 035-E7 and IBT 27921 variants, and two holotype rows for KACC 42091 variants. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with two organisms, two sequencing projects, and two matching native GOLD analysis rows. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1245748`. |
| Native StrainInfo exact hits | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has one direct record and one deposit-taxonomy hit under `1245748`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1245748`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1245748`. |

The native GOLD snapshot has exact organism rows on lines 279888 and 280007 for `Aspergillus turcosus HMR AF 23` and `Aspergillus turcosus HMR AF 1038` under NCBI taxon `1245748`, strains `HMR AF 23` and `HMR AF 1038`, and GOLD organisms `Go0384482` and `Go0384601`. Those organisms join to sequencing projects `Gp0235589` and `Gp0235711` on lines 156354 and 156476, and the two native GOLD analysis rows join to those projects through `AP PROJECT GOLD IDS`.

Native StrainInfo has one direct strain row and one deposit-taxonomy hit under taxon `1245748`. That native StrainInfo hit does not create generated overlay rows because StrainInfo overlays only BacDive-derived local strain entries, and there is no exact BacDive-derived local strain for this NCBI taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus subgen. Fumigati` parent, and the five related synonyms.
- NCBI has eight type-material rows for this taxon; these rows are inventory evidence and do not by themselves imply a generated local strain entry.
- The aggregate GOLD transform supplies a taxon-level organism count of three.
- The local native GOLD snapshot has two exact organisms, two linked sequencing projects, and two linked genome analyses.
- BacDive does not supply exact local strain evidence for this taxon, and the native StrainInfo exact hit has no BacDive-derived local strain to overlay.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Aspergillus turcosus` as `SPECIES`, and the generated record follows the source rank exactly.
