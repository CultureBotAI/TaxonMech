# YAML Record Review: Candidozyma haemuli var. vulneris

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/candidozyma_haemuli_var_vulneris.yaml
- Started UTC: 2026-09-22T07:07:54Z
- Finished UTC: 2026-09-22T07:07:54Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1231523 |
| label | Candidozyma haemuli var. vulneris |
| rank | VARIETAS |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:45357 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal variety at `data/taxa/eukaryota/candidozyma_haemuli_var_vulneris.yaml`. It carries two NCBI exact synonyms, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*candidozyma_haemuli_var_vulneris.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/candidozyma_haemuli_var_vulneris.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/candidozyma_haemuli_var_vulneris.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 281267 has `NCBITaxon:1231523`, label `Candidozyma haemuli var. vulneris`, rank `VARIETAS`, direct parent `NCBITaxon:45357`, genetic code `12`, two exact synonyms, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 58593 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate species parent `Candidozyma haemuli` under genus `Candidozyma`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 281267 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58593 | Supported exactly: `attested rule: Candidozyma haemuli var. vulneris, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 5543 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1231523`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with two native organisms, `Go0631625` and `Go0631626`, under the source names `Candida haemuloni var. vulneris K2` and `Candida haemuloni var. vulneris K1`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with two projects, `Gp0645161` and `Gp0645162`, for the two exact organism rows. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported exactly with two analysis rows for exact organism projects. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with five rows on lines 15520-15524. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1231523`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1231523`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1231523`. |

The NCBI type-material inventory contributes five `holotype` rows under the source taxon name `Candida haemuli var. vulneris` for CNM CL-7239 spelling variants. The local native GOLD snapshot has two exact organisms, K2 and K1, with two joined projects and two joined analysis rows.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `12`, the direct `Candidozyma haemuli` parent, two exact synonyms, one related synonym, and five type-material rows.
- NCBI does not supply merged-ID rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot supplies two exact organisms with two projects and two joined analyses.
- BacDive and exact StrainInfo scans do not supply local generated strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Candidozyma haemuli var. vulneris` as `VARIETAS`, and the generated record follows the source rank exactly.
