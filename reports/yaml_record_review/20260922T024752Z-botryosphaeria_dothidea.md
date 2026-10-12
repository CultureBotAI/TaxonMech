# YAML Record Review: Botryosphaeria dothidea

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/botryosphaeria_dothidea.yaml
- Started UTC: 2026-09-22T02:47:52Z
- Finished UTC: 2026-09-22T02:47:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:55169 |
| label | Botryosphaeria dothidea |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:45132 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/botryosphaeria_dothidea.yaml`. It carries four NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*botryosphaeria_dothidea.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/botryosphaeria_dothidea.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/botryosphaeria_dothidea.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 6982 has `NCBITaxon:55169`, label `Botryosphaeria dothidea`, rank `SPECIES`, direct parent `NCBITaxon:45132`, genetic code `1`, four exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52939 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Botryosphaeria` under family `Botryosphaeriaceae`.

No committed NCBI merged-ID or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 6982 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52939 | Supported exactly: `attested rule: Botryosphaeria dothidea, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 38561 | Supported exactly with 129 aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:55169`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with 129 native organisms under exact `ORGANISM NCBI TAX ID` `55169`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with 129 joined projects for those 129 native organisms. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with 129 analyses joined through those 129 native projects. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported exactly with 70 direct records and 76 deposit-taxonomy hits under `55169`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:55169`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with four culture-from-epitype designations for `Sphaeria dothidea`: `CBS 115476`, `CBS:115476`, `CMW 8000`, and `CMW:8000`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `55169`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:55169`. |

Complete exact scans of the native GOLD gzip snapshots materialized 129 organism rows, 129 joined project rows, and 129 project-joined analysis rows for this taxon.

The native StrainInfo snapshot has exact rows for this taxon, but the generated StrainInfo overlay surface is empty because this taxon has no BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Botryosphaeria` parent, four exact synonyms, two related synonyms, and four culture-from-epitype rows.
- NCBI does not supply merged-ID rows or a retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of 129.
- The local native GOLD snapshot supplies 129 exact organisms, 129 joined projects, and 129 project-joined analyses.
- StrainInfo supplies native exact rows, but no generated overlay rows, and BacDive does not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- Native GOLD analysis rows can join by project ID as well as organism ID; all 129 local native analyses for this taxon are recovered through `AP PROJECT GOLD IDS`.
- Native StrainInfo rows alone do not increase `strain_count`; only local BacDive-derived strain records participate in the generated strain surface.
- NCBI ranks `Botryosphaeria dothidea` as `SPECIES`, and the generated record follows the source rank exactly.
