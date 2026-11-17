# YAML Record Review: Biscogniauxia sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/biscogniauxia_sp.yaml
- Started UTC: 2026-09-22T01:16:11Z
- Finished UTC: 2026-09-22T01:16:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1896107 |
| label | Biscogniauxia sp. |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2614605 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/biscogniauxia_sp.yaml`. It carries no NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*biscogniauxia_sp.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/biscogniauxia_sp.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/biscogniauxia_sp.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 491424 has `NCBITaxon:1896107`, label `Biscogniauxia sp.`, rank `SPECIES`, direct parent `NCBITaxon:2614605`, genetic code `1`, no exact or related synonyms, and source `gold`. `curation/seed_scope.tsv` line 61480 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `unclassified Biscogniauxia` under genus `Biscogniauxia`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 491424 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61480 | Supported exactly: `attested rule: Biscogniauxia sp., 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 17101 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1896107`. |
| Empty native GOLD organism evidence | Exact native GOLD organism scan | Supported; no native GOLD organism row was filed directly under `NCBITaxon:1896107` in the current local snapshot. |
| Empty native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; no native GOLD project row joins through an exact `NCBITaxon:1896107` organism ID. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis row joins through an exact `NCBITaxon:1896107` organism or project ID. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no exact type-material row was filed under `NCBITaxon:1896107`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1896107`. |
| Empty native StrainInfo surface | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has no direct records or deposit-taxonomy hits under `1896107`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1896107`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1896107`. |

The current local native GOLD snapshot has no exact organism, project, or analysis rows filed under taxon ID `1896107`. The raw aggregate GOLD inventory nevertheless carries one taxon-level count for this record, and the generated source attestation follows that aggregate input.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and the direct `unclassified Biscogniauxia` parent.
- NCBI does not supply synonyms, merged-ID rows, or type-material rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot does not supply exact organism, project, or analysis rows under this taxon ID.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The GOLD source attestation explicitly counts records filed directly under this taxon, not descendant taxa, and the exact native GOLD scan used direct `ORGANISM NCBI TAX ID` matches for `1896107`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Biscogniauxia sp.` as `SPECIES`, and the generated record follows the source rank exactly.
