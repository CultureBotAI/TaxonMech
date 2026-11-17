# YAML Record Review: Aspergillus tamarii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_tamarii.yaml
- Started UTC: 2026-09-21T21:46:13Z
- Finished UTC: 2026-09-21T21:46:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41984 |
| label | Aspergillus tamarii |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_tamarii.yaml`. It carries one exact NCBI synonym, one related NCBI synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_tamarii.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_tamarii.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_tamarii.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4906 has `NCBITaxon:41984`, label `Aspergillus tamarii`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, one exact synonym, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 52506 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:41984`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4906 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52506 | Supported exactly: `attested rule: Aspergillus tamarii, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 35029 | Supported exactly with four aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:41984`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with eight rows: four lectotype spellings for NRRL 20818, two neotype spellings for CBS 104.13, and two type-material spellings for QM 9374. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with three organisms, four sequencing projects, and three matching native GOLD analysis rows. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `41984`. |
| Native StrainInfo exact hits | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 122 direct records and 190 deposit-taxonomy hits under `41984`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:41984`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:41984`. |

The native GOLD snapshot has exact organism rows on lines 59844, 484323, and 484324 for `Aspergillus tamarii CBS 117626`, `Aspergillus tamarii PB2203`, and `Aspergillus tamarii PB2201` under NCBI taxon `41984`, strains `CBS 117626`, `PB2203`, and `PB2201`, and GOLD organisms `Go0108198`, `Go0657802`, and `Go0657803`. Those organisms join to sequencing projects `Gp0108197`, `Gp0108198`, `Gp0702070`, and `Gp0702071` on lines 61571, 61572, 527641, and 527642, and the three native GOLD analysis rows join through `AP PROJECT GOLD IDS` to `Gp0108197`, `Gp0702070`, and `Gp0702071`.

Native StrainInfo has 122 direct strain rows and 190 deposit-taxonomy hits under taxon `41984`. Those native StrainInfo hits do not create generated overlay rows because StrainInfo overlays only BacDive-derived local strain entries, and there is no exact BacDive-derived local strain for this NCBI taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus subgen. Circumdati` parent, one exact synonym, and one related synonym.
- NCBI has eight type-material rows for this taxon; these rows are inventory evidence and do not by themselves imply a generated local strain entry.
- The aggregate GOLD transform supplies a taxon-level organism count of four.
- The local native GOLD snapshot has three exact organisms, four linked sequencing projects, and three linked genome analyses.
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
- NCBI ranks `Aspergillus tamarii` as `SPECIES`, and the generated record follows the source rank exactly.
