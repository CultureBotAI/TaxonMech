# YAML Record Review: Blastocystis sp. subtype 4

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/blastocystis_sp_subtype_4.yaml
- Started UTC: 2026-09-22T02:17:37Z
- Finished UTC: 2026-09-22T02:17:37Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:944170 |
| label | Blastocystis sp. subtype 4 |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:944171 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic SAR species at `data/taxa/eukaryota/blastocystis_sp_subtype_4.yaml`. It carries three NCBI exact synonyms, no NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*blastocystis_sp_subtype_4.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/blastocystis_sp_subtype_4.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/blastocystis_sp_subtype_4.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 201674 has `NCBITaxon:944170`, label `Blastocystis sp. subtype 4`, rank `SPECIES`, direct parent `NCBITaxon:944171`, genetic code `1`, three exact synonyms, no related synonyms, and source `gold`. `curation/seed_scope.tsv` line 57015 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Blastocystis sp. subtypes` under genus `Blastocystis`.

The exact NCBI merged-ID side scan maps old `NCBITaxon:1529846` to this taxon, but no retained retired-row evidence points at the record, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 201674 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 57015 | Supported exactly: `attested rule: Blastocystis sp. subtype 4, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| NCBI merged old ID | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported with one side-inventory old ID, `NCBITaxon:1529846`, remapped to `NCBITaxon:944170`; no retained retired row generates a YAML `replaces` value. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 44986 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:944170`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with two native organisms, `Go0103364` and `Go0113805`, for strains ST4 and BT1. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with two projects, `Gp0103364` and `Gp0117467`, joined through the native organism IDs. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with two analysis rows, `Blastocystis sp. ST4` and `Blastocystis sp. subtype 4 BT1`, joined through the native project IDs. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material row mentions `NCBITaxon:944170`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `944170`. |
| Empty native StrainInfo surface | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has no direct records or deposit-taxonomy hits under `944170`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:944170`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:944170`. |

The local native GOLD snapshot has two exact organisms with two joined projects and two joined native analysis rows.

The NCBI type-material inventory contributes no rows for this subtype.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Blastocystis sp. subtypes` parent, and three exact synonyms.
- NCBI also supplies one merged side-inventory old ID, but no retained retired row that would generate `replaces`.
- NCBI does not supply related synonyms or type-material rows.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot supplies two exact organisms with two joined projects and two joined analyses.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The GOLD source attestation explicitly counts records filed directly under this taxon, not descendant taxa, and the exact native GOLD scan used direct `ORGANISM NCBI TAX ID` matches for `944170`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Blastocystis sp. subtype 4` as `SPECIES`, and the generated record follows the source rank exactly.
