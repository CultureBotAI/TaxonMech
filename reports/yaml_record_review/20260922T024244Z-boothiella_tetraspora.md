# YAML Record Review: Boothiella tetraspora

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/boothiella_tetraspora.yaml
- Started UTC: 2026-09-22T02:42:44Z
- Finished UTC: 2026-09-22T02:42:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2081573 |
| label | Boothiella tetraspora |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2081572 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/boothiella_tetraspora.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*boothiella_tetraspora.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/boothiella_tetraspora.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/boothiella_tetraspora.yaml` exited successfully. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 517664 has `NCBITaxon:2081573`, label `Boothiella tetraspora`, rank `SPECIES`, direct parent `NCBITaxon:2081572`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 62280 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Boothiella` under family `Sordariaceae`.

No committed NCBI merged-ID or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 517664 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 62280 | Supported exactly: `attested rule: Boothiella tetraspora, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 19916 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:2081573`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0651396`, for strain CBS 334.67. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with two joined projects, `Gp0688300` and `Gp0699281`, for strain CBS 334.67. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis row joins through exact `NCBITaxon:2081573` organism or project IDs. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported exactly with six direct records and 13 deposit-taxonomy hits under `2081573`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:2081573`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material row mentions `NCBITaxon:2081573`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2081573`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2081573`. |

The local native GOLD snapshot has one exact CBS 334.67 organism and two joined projects with no joined analyses.

The native StrainInfo snapshot has exact rows for this taxon, but the generated StrainInfo overlay surface is empty because this taxon has no BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Boothiella` parent, and one related synonym.
- NCBI does not supply merged-ID rows, type-material rows, or a retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism and two joined projects, with no joined analyses.
- StrainInfo supplies native exact rows, but no generated overlay rows, and BacDive does not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- StrainInfo only overlays local BacDive-derived strains, so native StrainInfo rows alone are not expected to create `assemblies.tsv` or `related_records.tsv.gz` rows.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Boothiella tetraspora` as `SPECIES`, and the generated record follows the source rank exactly.
