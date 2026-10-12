# YAML Record Review: Aspergillus sergii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_sergii.yaml
- Started UTC: 2026-09-21T20:50:00Z
- Finished UTC: 2026-09-21T20:50:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1034303 |
| label | Aspergillus sergii |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_sergii.yaml`. It carries no NCBI exact synonyms, seven NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_sergii.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_sergii.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_sergii.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 221571 has `NCBITaxon:1034303`, label `Aspergillus sergii`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, seven related synonyms, and source `gold`. `curation/seed_scope.tsv` line 57250 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` has five old IDs redirected into `NCBITaxon:1034303`; `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species, so the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 221571 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 57250 | Supported exactly: `attested rule: Aspergillus sergii, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 465 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1034303`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 1720-1726 | Supported exactly with CBS 130017 variants and holotype designations for `09AAsp494` and `MUM 10.219`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism, two sequencing projects, and one native GOLD analysis for `Aspergillus sergii CBS 130017`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1034303`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1034303`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1034303`. |

The native GOLD snapshot has one exact organism row on line 59843 for `Aspergillus sergii CBS 130017`. That organism joins to sequencing projects `Gp0108195` and `Gp0108196` on lines 61569-61570; the native GOLD analysis row on line 134004 joins through `AP PROJECT GOLD IDS` to `Gp0108195`.

Native StrainInfo has no direct strain rows or deposit-taxonomy hits under taxon `1034303`, and the generated StrainInfo overlay files contain no rows for `NCBITaxon:1034303`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, seven related synonyms, five non-retained merged IDs, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism, two linked sequencing projects, one linked genome analysis, and no matched BacDive-derived local strain identifier to join through.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, native GOLD, and complete NCBI type-material checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
