# YAML Record Review: Buwchfawromyces eastonii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/buwchfawromyces_eastonii.yaml
- Started UTC: 2026-09-22T03:24:12Z
- Finished UTC: 2026-09-22T03:24:12Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:512029 |
| label | Buwchfawromyces eastonii |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:1623672 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/buwchfawromyces_eastonii.yaml`. It carries two NCBI related synonyms, no exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*buwchfawromyces_eastonii.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/buwchfawromyces_eastonii.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/buwchfawromyces_eastonii.yaml` exited successfully and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 116193 has `NCBITaxon:512029`, label `Buwchfawromyces eastonii`, rank `SPECIES`, direct parent `NCBITaxon:1623672`, genetic code `1`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 55867 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Buwchfawromyces` under family `Neocallimastigaceae`.

No committed NCBI merged-ID row or retained retired row points at `NCBITaxon:512029`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 116193 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55867 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37528 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:512029`. |
| Empty native GOLD organism evidence | Exact native GOLD organism scan | Supported; no native GOLD organism row currently carries NCBI taxon `512029`. |
| Empty native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported; with no exact organism IDs, no native GOLD project joins to this taxon. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis joins to this taxon by exact organism ID or project ID. |
| Empty NCBI merged-ID inventories | Exact scans of `data/raw/ncbi_merged_ids.tsv` and retained retired rows | Supported; neither side old-ID inventory nor retained retired-row evidence points at `NCBITaxon:512029`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with one holotype row and two type-material rows for `Buwchfawromyces eastonii`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `512029`. |
| Empty StrainInfo taxon surface | Exact native StrainInfo taxon scans plus generated overlay scans | Supported; no native direct/deposit hit or generated StrainInfo overlay row mentions `NCBITaxon:512029`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:512029`. |

The committed aggregate GOLD row gives this fungal species its second source attestation, but the local native GOLD organism/project/analysis snapshots do not contain an exact row for taxon ID `512029`.

The NCBI type-material inventory contributes three rows for `Buwchfawromyces eastonii`: holotype `ABS GE09` and type-material designations `GE09` and `GE:09`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Buwchfawromyces` parent, two related synonyms, and three type-material rows.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies no exact organism, project, or analysis rows for this taxon.
- BacDive and StrainInfo do not supply exact local strain or overlay evidence for this taxon.
- NCBI merged-ID, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The GOLD aggregate row is present even though no exact local native GOLD row remains for `NCBITaxon:512029`; this review treats both committed surfaces separately.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Buwchfawromyces eastonii` as `SPECIES`, and the generated record follows the source rank exactly.
