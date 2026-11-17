# YAML Record Review: Byssothecium circinans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/byssothecium_circinans.yaml
- Started UTC: 2026-09-22T03:28:11Z
- Finished UTC: 2026-09-22T03:28:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:147558 |
| label | Byssothecium circinans |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:147557 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/byssothecium_circinans.yaml`. It carries one NCBI related synonym, no exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*byssothecium_circinans.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/byssothecium_circinans.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/byssothecium_circinans.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 30114 has `NCBITaxon:147558`, label `Byssothecium circinans`, rank `SPECIES`, direct parent `NCBITaxon:147557`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 54047 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Byssothecium` under family `Massarinaceae`.

No committed NCBI merged-ID row or retained retired row points at `NCBITaxon:147558`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 30114 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54047 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 11404 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:147558`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0036418` for `Byssothecium circinans CBS 675.92` at line 30870. |
| Native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported exactly by projects `Gp0036418` and `Gp0036419` for `Go0036418`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly by one analysis row, `Byssothecium circinans CBS 675.92`, joined through project `Gp0036418`. |
| Empty NCBI merged-ID inventories | Exact scans of `data/raw/ncbi_merged_ids.tsv` and retained retired rows | Supported; neither side old-ID inventory nor retained retired-row evidence points at `NCBITaxon:147558`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material row mentions `NCBITaxon:147558`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `147558`. |
| Native StrainInfo exact taxon evidence | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has five deposit-taxonomy hits and two direct records under `147558`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:147558`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:147558`. |

The committed aggregate GOLD row supplies two taxon-level organism assertions; the local native GOLD snapshot currently has one exact organism, two project rows for that organism, and one joined analysis row.

Native StrainInfo has exact taxon rows under `147558`, but the generated StrainInfo overlay correctly remains empty because no BacDive-derived local strain inventory entry joins those rows.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Byssothecium` parent, and one related synonym.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot supplies one exact organism, two project rows, and one joined analysis row.
- Native StrainInfo has exact rows under this taxon, but no BacDive-derived local strain inventory entry turns them into generated `data/straininfo/` overlay rows.
- BacDive does not supply exact local strain evidence for this taxon.
- NCBI type-material, NCBI merged-ID, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The GOLD aggregate row's organism count differs from the exact local native GOLD organism count; this review treats both committed surfaces separately.
- Exact local native GOLD scans recovered one organism row, two project rows, and one analysis row for `NCBITaxon:147558`.
- GOLD analysis evidence joins through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- StrainInfo exact taxon rows do not generate overlay rows unless they join to the BacDive-derived local strain inventory.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Byssothecium circinans` as `SPECIES`, and the generated record follows the source rank exactly.
