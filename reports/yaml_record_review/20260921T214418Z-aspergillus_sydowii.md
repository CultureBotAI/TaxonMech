# YAML Record Review: Aspergillus sydowii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_sydowii.yaml
- Started UTC: 2026-09-21T21:41:24Z
- Finished UTC: 2026-09-21T21:44:18Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:75750 |
| label | Aspergillus sydowii |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_sydowii.yaml`. It carries one exact NCBI synonym, four related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_sydowii.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_sydowii.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_sydowii.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 10826 has `NCBITaxon:75750`, label `Aspergillus sydowii`, rank `SPECIES`, direct parent `NCBITaxon:2720870`, genetic code `1`, one exact synonym, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53284 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Nidulantes`.

`data/raw/ncbi_merged_ids.tsv` redirects old IDs `NCBITaxon:1248755` and `NCBITaxon:929639` into `NCBITaxon:75750`. `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 10826 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53284 | Supported exactly: `attested rule: Aspergillus sydowii, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 42413 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:75750`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with two culture-from-neotype rows for CBS 593.65 and `CBS:593.65` under the taxon name `Sterigmatocystis sydowii`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with two organisms, two sequencing projects, and one matching native GOLD analysis row. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `75750`. |
| Native StrainInfo exact hits | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 151 direct records and 184 deposit-taxonomy hits under `75750`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:75750`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:75750`. |

The native GOLD snapshot has exact organism rows on lines 8444 and 508100 for `Aspergillus sydowii CBS 593.65` and `Aspergillus sydowii Fsh102` under NCBI taxon `75750`, strains `CBS 593.65` and `Fsh102`, and GOLD organisms `Go0009567` and `Go0683469`. Those organisms join to sequencing projects `Gp0009567` and `Gp0785641` on lines 8308 and 584677, and the native GOLD analysis row on line 444059 joins through `AP PROJECT GOLD IDS` to `Gp0785641`.

Native StrainInfo has 151 direct strain rows and 184 deposit-taxonomy hits under taxon `75750`. Those native StrainInfo hits do not create generated overlay rows because StrainInfo overlays only BacDive-derived local strain entries, and there is no exact BacDive-derived local strain for this NCBI taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus subgen. Nidulantes` parent, one exact synonym, and four related synonyms.
- NCBI has two type-material rows for this taxon; these rows are inventory evidence and do not by themselves imply a generated local strain entry.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot has two exact organisms, two linked sequencing projects, and one linked genome analysis.
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
- NCBI ranks `Aspergillus sydowii` as `SPECIES`, and the generated record follows the source rank exactly.
