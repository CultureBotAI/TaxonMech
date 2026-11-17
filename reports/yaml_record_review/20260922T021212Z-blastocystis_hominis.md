# YAML Record Review: Blastocystis hominis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/blastocystis_hominis.yaml
- Started UTC: 2026-09-22T02:12:12Z
- Finished UTC: 2026-09-22T02:12:12Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:12968 |
| label | Blastocystis hominis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:12967 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic SAR species at `data/taxa/eukaryota/blastocystis_hominis.yaml`. It carries no NCBI exact synonyms, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*blastocystis_hominis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/blastocystis_hominis.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/blastocystis_hominis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2655 has `NCBITaxon:12968`, label `Blastocystis hominis`, rank `SPECIES`, direct parent `NCBITaxon:12967`, genetic code `1`, no exact synonyms, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 52118 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Blastocystis` under family `Blastocystidae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2655 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52118 | Supported exactly: `attested rule: Blastocystis hominis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 7254 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:12968`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with two native organisms, `Go0002360` and `Go0002361`, filed directly under `12968`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with two projects, `Gp0002360` and `Gp0002361`, joined through the native organism IDs. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with one analysis row, `Blastocystis hominis Singapore, B (sub-type 7)`, joined through project `Gp0002361`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material row mentions `NCBITaxon:12968`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `12968`. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported with sixteen exact direct StrainInfo records and sixteen exact deposit-taxonomy matches. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:12968`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:12968`. |

The local native GOLD snapshot has two exact organisms, two joined projects, and one joined native analysis row filed directly under `Blastocystis hominis`.

The NCBI type-material inventory contributes no rows for this taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Blastocystis` parent, and one related synonym.
- NCBI does not supply exact synonyms, merged-ID rows, type-material rows, or a retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies two exact organisms with two joined projects and one joined analysis.
- Native StrainInfo has sixteen exact direct records and sixteen exact deposit-taxonomy hits, but the local StrainInfo overlay does not emit generated rows for this taxon.
- BacDive does not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The GOLD source attestation explicitly counts records filed directly under this taxon, not descendant taxa, and the exact native GOLD scan used direct `ORGANISM NCBI TAX ID` matches for `12968`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Blastocystis hominis` as `SPECIES`, and the generated record follows the source rank exactly.
