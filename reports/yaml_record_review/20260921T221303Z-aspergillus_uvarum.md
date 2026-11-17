# YAML Record Review: Aspergillus uvarum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_uvarum.yaml
- Started UTC: 2026-09-21T22:11:52Z
- Finished UTC: 2026-09-21T22:13:03Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:446911 |
| label | Aspergillus uvarum |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_uvarum.yaml`. It carries two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_uvarum.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_uvarum.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_uvarum.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 99440 has `NCBITaxon:446911`, label `Aspergillus uvarum`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 55678 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 99440 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55678 | Supported exactly: `attested rule: Aspergillus uvarum, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 35759 | Supported exactly with three aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:446911`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` lines 212890-212895 | Supported exactly with six rows: two culture-from-holotype rows, two holotype rows, and two type-material rows. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with three organisms, four sequencing projects, and two matching native GOLD analysis rows. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `446911`. |
| Native StrainInfo exact hits | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has three direct records and five deposit-taxonomy hits under `446911`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:446911`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:446911`. |

The local native GOLD snapshot has exact organism rows for `Aspergillus uvarum CBS 121591` on line 38662, `Aspergillus uvarum PYS010` on line 484333, and `Aspergillus uvarum PG009` on line 484334. These rows join to four sequencing projects: `Gp0047309`, `Gp0047310`, `Gp0702080`, and `Gp0702081`. Native GOLD analysis lines 445052 and 445233 join to the two newer projects through `AP PROJECT GOLD IDS`.

Native StrainInfo has three direct strain rows and five deposit-taxonomy hits under taxon `446911`. Those native StrainInfo hits do not create generated overlay rows because StrainInfo overlays only BacDive-derived local strain entries, and there is no exact BacDive-derived local strain for this NCBI taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus subgen. Circumdati` parent, and two related synonyms.
- NCBI has six type-material rows for this taxon; these rows are inventory evidence and do not by themselves imply a generated local strain entry.
- The aggregate GOLD transform supplies a taxon-level organism count of three.
- The local native GOLD snapshot has three exact organisms, four linked sequencing projects, and two linked genome analyses.
- BacDive does not supply exact local strain evidence for this taxon, and the native StrainInfo exact hits have no BacDive-derived local strain to overlay.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Aspergillus uvarum` as `SPECIES`, and the generated record follows the source rank exactly.
