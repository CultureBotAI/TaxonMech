# YAML Record Review: Blastobotrys petasosporus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/blastobotrys_petasosporus.yaml
- Started UTC: 2026-09-22T01:57:33Z
- Finished UTC: 2026-09-22T01:57:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:64416 |
| label | Blastobotrys petasosporus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:43971 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/blastobotrys_petasosporus.yaml`. It carries one NCBI exact synonym, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*blastobotrys_petasosporus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/blastobotrys_petasosporus.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/blastobotrys_petasosporus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 8157 has `NCBITaxon:64416`, label `Blastobotrys petasosporus`, rank `SPECIES`, direct parent `NCBITaxon:43971`, genetic code `1`, one exact synonym, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53075 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Blastobotrys` under family `Trichomonascaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 8157 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53075 | Supported exactly: `attested rule: Blastobotrys petasosporus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 40264 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:64416`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with two native organisms, `Go0112327` and `Go0705686`, for strains YB-2093 and NRRL YB-2092. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with three projects, `Gp0114593`, `Gp0114594`, and `Gp0831738`, joined through the native organism IDs. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis row joins through exact `NCBITaxon:64416` organism or project IDs. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with seven rows on lines 244198-244204. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `64416`. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported with one exact direct StrainInfo record and one exact deposit-taxonomy match for MUCL 53778. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:64416`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:64416`. |

The local native GOLD snapshot has two exact organisms with three joined projects and no joined native analysis rows.

The NCBI type-material inventory contributes seven `type material` rows for `Trichomonascus petasosporus`, spanning CBS 9602 and NRRL YB-2092 aliases.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Blastobotrys` parent, one exact synonym, three related synonyms, and seven type-material rows.
- NCBI does not supply merged-ID rows or a retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot supplies two exact organisms with three joined projects and no joined analyses.
- Native StrainInfo has one exact direct record and one exact deposit-taxonomy hit, but the local StrainInfo overlay does not emit generated rows for this taxon.
- BacDive does not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The GOLD source attestation explicitly counts records filed directly under this taxon, not descendant taxa, and the exact native GOLD scan used direct `ORGANISM NCBI TAX ID` matches for `64416`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Blastobotrys petasosporus` as `SPECIES`, and the generated record follows the source rank exactly.
