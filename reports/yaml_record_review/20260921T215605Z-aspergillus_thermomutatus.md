# YAML Record Review: Aspergillus thermomutatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_thermomutatus.yaml
- Started UTC: 2026-09-21T21:55:20Z
- Finished UTC: 2026-09-21T21:56:05Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41047 |
| label | Aspergillus thermomutatus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_thermomutatus.yaml`. It carries two exact NCBI synonyms, three related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_thermomutatus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_thermomutatus.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_thermomutatus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4758 has `NCBITaxon:41047`, label `Aspergillus thermomutatus`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, two exact synonyms, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52457 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:41047`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4758 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52457 | Supported exactly: `attested rule: Aspergillus thermomutatus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34711 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:41047`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with four culture-from-type-material rows for CBS 208.92 and NRRL 20748 variants under the taxon name `Aspergillus fischeri var. thermomutatus`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with two organisms, four sequencing projects, and one matching native GOLD analysis row. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `41047`. |
| Native StrainInfo exact hits | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 45 direct records and 59 deposit-taxonomy hits under `41047`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:41047`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:41047`. |

The native GOLD snapshot has exact organism rows on lines 59791 and 279885 for `Aspergillus thermomutatus CBS 207.92` and `Aspergillus thermomutatus HMR AF 39` under NCBI taxon `41047`, strains `CBS 207.92` and `HMR AF 39`, and GOLD organisms `Go0108088` and `Go0384479`. Those organisms join to sequencing projects `Gp0108087`, `Gp0108088`, `Gp0235586`, and `Gp0248678` on lines 61467, 61468, 156351, and 164124, and the native GOLD analysis row on line 131208 joins through `AP PROJECT GOLD IDS` to `Gp0235586`.

Native StrainInfo has 45 direct strain rows and 59 deposit-taxonomy hits under taxon `41047`. Those native StrainInfo hits do not create generated overlay rows because StrainInfo overlays only BacDive-derived local strain entries, and there is no exact BacDive-derived local strain for this NCBI taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus subgen. Fumigati` parent, two exact synonyms, and three related synonyms.
- NCBI has four type-material rows for this taxon; these rows are inventory evidence and do not by themselves imply a generated local strain entry.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot has two exact organisms, four linked sequencing projects, and one linked genome analysis.
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
- NCBI ranks `Aspergillus thermomutatus` as `SPECIES`, and the generated record follows the source rank exactly.
