# YAML Record Review: Aureobasidium mangrovei

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aureobasidium_mangrovei.yaml
- Started UTC: 2026-09-21T22:47:30Z
- Finished UTC: 2026-09-21T22:48:28Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2895399 |
| label | Aureobasidium mangrovei |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5579 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/aureobasidium_mangrovei.yaml`. It carries one related NCBI synonym, no exact NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aureobasidium_mangrovei.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aureobasidium_mangrovei.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aureobasidium_mangrovei.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 568745 has `NCBITaxon:2895399`, label `Aureobasidium mangrovei`, rank `SPECIES`, direct parent `NCBITaxon:5579`, genetic code `1`, one related synonym, no exact synonyms, and source `gold`. `curation/seed_scope.tsv` line 63364 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aureobasidium` under `Saccotheciaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 568745 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 63364 | Supported exactly: `attested rule: Aureobasidium mangrovei, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 28222 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:2895399`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 137606-137609 | Supported exactly with four `typematerial.dmp` holotype and culture-from-holotype designations. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with `Go0642130` for strain `SARA-138H` on line 471832. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with project `Gp0669133` on line 500728. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis row joins back to this organism or project in the local snapshot. |
| Native StrainInfo evidence | Exact native StrainInfo direct and deposit-taxonomy scans | Supported exactly with two direct rows under taxon ID `2895399`, for `DSM 104831` and type-strain deposit `DSM 104830`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:2895399`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2895399`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2895399`. |

NCBI records the `CBS 142205` culture and `IBRC-M 30265` holotype accessions as type material. Native GOLD instead points at `SARA-138H`, and native StrainInfo points at two DSM accessions; none of those native rows produce a generated local strain entry because no BacDive-derived strain or generated StrainInfo overlay row is filed under this target.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aureobasidium` parent, one related synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one joined project and no joined analysis rows.
- The local native StrainInfo snapshot supplies two exact rows, but the generated StrainInfo overlay surface is empty for this target.
- BacDive does not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Aureobasidium mangrovei` as `SPECIES`, and the generated record follows the source rank exactly.
