# YAML Record Review: Candolleomyces aberdarensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/candolleomyces_aberdarensis.yaml
- Started UTC: 2026-09-22T07:10:35Z
- Finished UTC: 2026-09-22T07:10:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2316362 |
| label | Candolleomyces aberdarensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2791032 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/candolleomyces_aberdarensis.yaml`. It carries one NCBI exact synonym, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*candolleomyces_aberdarensis.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/candolleomyces_aberdarensis.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/candolleomyces_aberdarensis.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 524850 has `NCBITaxon:2316362`, label `Candolleomyces aberdarensis`, rank `SPECIES`, direct parent `NCBITaxon:2791032`, genetic code `1`, one exact synonym, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 62555 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Candolleomyces` under family `Psathyrellaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 524850 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 62555 | Supported exactly: `attested rule: Candolleomyces aberdarensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 21708 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:2316362`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0518878`, strain IHI B618 under the source name `Candolleomyces aberdarensis IHI B618`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with one project, `Gp0443006`, for `Go0518878`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported exactly with one analysis row for IHI B618. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with two rows on lines 92761-92762. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2316362`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:2316362`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2316362`. |

The NCBI type-material inventory contributes two `holotype` rows under the source taxon name `Psathyrella aberdarensis` for GLM-F116094 spelling variants. The local native GOLD snapshot has one exact organism, IHI B618, with one joined project and one joined analysis row.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Candolleomyces` parent, one exact synonym, three related synonyms, and two type-material rows.
- NCBI does not supply merged-ID rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one project and one joined analysis.
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
- NCBI ranks `Candolleomyces aberdarensis` as `SPECIES`, and the generated record follows the source rank exactly.
