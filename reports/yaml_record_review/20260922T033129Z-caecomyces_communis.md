# YAML Record Review: Caecomyces communis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/caecomyces_communis.yaml
- Started UTC: 2026-09-22T03:31:29Z
- Finished UTC: 2026-09-22T03:31:29Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:4824 |
| label | Caecomyces communis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:4823 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/caecomyces_communis.yaml`. It carries one NCBI exact synonym, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*caecomyces_communis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/caecomyces_communis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/caecomyces_communis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2080 has `NCBITaxon:4824`, label `Caecomyces communis`, rank `SPECIES`, direct parent `NCBITaxon:4823`, genetic code `1`, exact synonym `Sphaeromonas communis`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 51852 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Caecomyces` under family `Neocallimastigaceae`.

`data/raw/ncbi_merged_ids.tsv` line 32082 records side-inventory old ID `NCBITaxon:191552` merged into `NCBITaxon:4824`, but the retained NCBI row for this generated record is current and has no `retired_into` value. The record correctly omits `replaces`, which is generated only from retained retired rows.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2080 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 51852 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 36786 | Supported exactly with four aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:4824`. |
| Empty native GOLD organism evidence | Exact native GOLD organism scan | Supported; no native GOLD organism row currently carries NCBI taxon `4824`. |
| Empty native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported; with no exact organism IDs, no native GOLD project joins to this taxon. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis joins to this taxon by exact organism ID or project ID. |
| NCBI merged-ID side inventory | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported exactly with old ID `NCBITaxon:191552` pointing to the current taxon. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material row mentions `NCBITaxon:4824`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `4824`. |
| Empty StrainInfo taxon surface | Exact native StrainInfo taxon scans plus generated overlay scans | Supported; no native direct/deposit hit or generated StrainInfo overlay row mentions `NCBITaxon:4824`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:4824`. |

The committed aggregate GOLD row gives this fungal species its second source attestation, but the local native GOLD organism/project/analysis snapshots do not contain an exact row for taxon ID `4824`.

The side-inventory old NCBI taxon ID does not require a `replaces` entry because no retained retired row points at the current ID.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Caecomyces` parent, one exact synonym, and one related synonym.
- The aggregate GOLD transform supplies a taxon-level organism count of four.
- The local native GOLD snapshot supplies no exact organism, project, or analysis rows for this taxon.
- BacDive and StrainInfo do not supply exact local strain or overlay evidence for this taxon.
- NCBI type-material, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The side-inventory NCBI merge row for `NCBITaxon:191552` does not require a YAML `replaces` entry without a retained retired source row.
- The GOLD aggregate row is present even though no exact local native GOLD row remains for `NCBITaxon:4824`; this review treats both committed surfaces separately.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Caecomyces communis` as `SPECIES`, and the generated record follows the source rank exactly.
