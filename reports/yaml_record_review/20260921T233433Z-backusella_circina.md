# YAML Record Review: Backusella circina

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/backusella_circina.yaml
- Started UTC: 2026-09-21T23:33:16Z
- Finished UTC: 2026-09-21T23:34:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:64653 |
| label | Backusella circina |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:64649 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/backusella_circina.yaml`. It carries one related NCBI synonym, no exact NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*backusella_circina.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/backusella_circina.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/backusella_circina.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 8222 has `NCBITaxon:64653`, label `Backusella circina`, rank `SPECIES`, direct parent `NCBITaxon:64649`, genetic code `1`, one related synonym, no exact synonyms, and source `gold`. `curation/seed_scope.tsv` line 53115 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Backusella` under family `Backusellaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 8222 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53115 | Supported exactly: `attested rule: Backusella circina, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 40371 | Supported exactly with six aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:64653`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with six native organisms: `Go0032377`, `Go0452953`, `Go0452971`, `Go0527613`, `Go0535907`, and `Go0535922`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with seven projects across the six organism IDs above. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with one analysis row joining through project `Gp0032377`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with eight rows on lines 244658-244665. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `64653`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:64653`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:64653`. |

The NCBI type-material inventory contributes two `culture from type material` rows for CBS 128.70 and six `type material` rows for ATCC 18878, IMI 146484, and NRRL 2446. The local native GOLD snapshot has six exact organisms, including NRRL 2446, with seven joined projects and one joined analysis row; the second FSU 941 project and all five NRRL resequencing projects lack matching analysis rows in the local snapshot.

The native StrainInfo snapshot has 14 exact direct rows and 34 exact deposit rows under `NCBITaxon:64653`, with deposits overlapping the NCBI type-material designations. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Backusella` parent, one related synonym, and eight type-material rows.
- NCBI does not supply merged-ID rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of six.
- The local native GOLD snapshot supplies six exact organisms with seven projects and one joined analysis row.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Backusella circina` as `SPECIES`, and the generated record follows the source rank exactly.
