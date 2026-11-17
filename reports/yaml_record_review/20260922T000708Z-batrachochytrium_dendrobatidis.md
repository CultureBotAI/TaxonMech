# YAML Record Review: Batrachochytrium dendrobatidis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/batrachochytrium_dendrobatidis.yaml
- Started UTC: 2026-09-22T00:03:59Z
- Finished UTC: 2026-09-22T00:07:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:109871 |
| label | Batrachochytrium dendrobatidis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:100474 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/batrachochytrium_dendrobatidis.yaml`. It carries four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*batrachochytrium_dendrobatidis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/batrachochytrium_dendrobatidis.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/batrachochytrium_dendrobatidis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 19728 has `NCBITaxon:109871`, label `Batrachochytrium dendrobatidis`, rank `SPECIES`, direct parent `NCBITaxon:100474`, genetic code `1`, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53747 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Batrachochytrium` under `Rhizophydiales incertae sedis`.

`data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:81068` to this taxon, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at it with `retired_into`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 19728 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53747 | Supported exactly: `attested rule: Batrachochytrium dendrobatidis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 1834 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:109871`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with five native organisms: `Go0022118`, `Go0038582`, `Go0038583`, `Go0076103`, and `Go0113790`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with four projects, `Gp0038582`, `Gp0038583`, `Gp0076103`, and `Gp0117451`, for exact local organism IDs. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no local native GOLD analysis row joins to this taxon. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with four reference-material rows on lines 6277-6280. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `109871`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:109871`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:109871`. |

The NCBI type-material inventory contributes four `reference material` rows for AFTOL-ID 21 and JEL 197. The local native GOLD snapshot has five exact organisms and four exact joined projects, but no exact joined analysis rows for this taxon.

The native StrainInfo snapshot has two exact direct rows and two exact deposit rows under `NCBITaxon:109871`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Batrachochytrium` parent, four related synonyms, and four type-material rows.
- NCBI supplies one raw merged-ID row, but does not supply a retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies five exact organisms with four projects and no joined analyses.
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
- NCBI ranks `Batrachochytrium dendrobatidis` as `SPECIES`, and the generated record follows the source rank exactly.
