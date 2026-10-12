# YAML Record Review: Canariomyces arenarius CBS 508.74

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/canariomyces_arenarius_cbs_508_74.yaml
- Started UTC: 2026-09-22T03:58:12Z
- Finished UTC: 2026-09-22T03:58:12Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1384583 |
| label | Canariomyces arenarius CBS 508.74 |
| rank | STRAIN |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2609790 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal strain at `data/taxa/eukaryota/canariomyces_arenarius_cbs_508_74.yaml`. It carries no NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*canariomyces_arenarius_cbs_508_74.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/canariomyces_arenarius_cbs_508_74.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/canariomyces_arenarius_cbs_508_74.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 338325 has `NCBITaxon:1384583`, label `Canariomyces arenarius CBS 508.74`, rank `STRAIN`, direct parent `NCBITaxon:2609790`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 59779 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate species parent `Canariomyces arenarius` under genus `Canariomyces`.

No committed NCBI merged-ID row or retained retired row points at `NCBITaxon:1384583`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 338325 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 59779 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 9067 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1384583`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0036388` for `Canariomyces arenarius CBS 508.74` at line 30852. |
| Native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported exactly by projects `Gp0036388` and `Gp0036389` for `Go0036388`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly by one analysis row joined through project `Gp0036388`. |
| Empty NCBI merged-ID inventories | Exact scans of `data/raw/ncbi_merged_ids.tsv` and retained retired rows | Supported; neither side old-ID inventory nor retained retired-row evidence points at `NCBITaxon:1384583`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material row is filed under `NCBITaxon:1384583`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1384583`. |
| Empty StrainInfo taxon surface | Exact native StrainInfo taxon scans plus generated overlay scans | Supported; no native direct/deposit hit or generated StrainInfo overlay row mentions `NCBITaxon:1384583`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1384583`. |

The committed aggregate GOLD row is mirrored by one exact native GOLD organism, two native project rows, and one analysis row joined through one of those projects.

The record is strain-rank in NCBI and remains strain-rank in the generated YAML.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, and the direct `Canariomyces arenarius` species parent.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, two project rows, and one joined analysis row.
- BacDive and StrainInfo do not supply exact local strain or overlay evidence for this taxon.
- NCBI merged-ID, NCBI type-material, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- Exact local native GOLD scans recovered one organism row, two project rows, and one analysis row for `NCBITaxon:1384583`.
- GOLD analysis evidence joins through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Canariomyces arenarius CBS 508.74` as `STRAIN`, and the generated record follows the source rank exactly.
