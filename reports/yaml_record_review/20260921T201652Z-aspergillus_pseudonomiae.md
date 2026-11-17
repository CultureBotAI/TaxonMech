# YAML Record Review: Aspergillus pseudonomiae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_pseudonomiae.yaml
- Started UTC: 2026-09-21T20:15:41Z
- Finished UTC: 2026-09-21T20:16:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1506151 |
| label | Aspergillus pseudonomiae |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_pseudonomiae.yaml`. It carries one NCBI exact synonym, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_pseudonomiae.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_pseudonomiae.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_pseudonomiae.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 386763 has `NCBITaxon:1506151`, label `Aspergillus pseudonomiae`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, one exact synonym, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 60354 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` line 90717 redirects old ID `NCBITaxon:656919` into `NCBITaxon:1506151`. That old ID is not retained in `data/raw/ncbitaxon_taxa.tsv` as a retired row pointing at this species, so the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 386763 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 60354 | Supported exactly: `attested rule: Aspergillus pseudonomiae, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 11828 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1506151`. |
| NCBI merged-ID handling | `data/raw/ncbi_merged_ids.tsv` line 90717; retained-old-ID scan of `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; the source row redirects `NCBITaxon:656919` into this species, with no retained retired row. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 37617-37626 | Supported exactly with ten culture-from-holotype and culture-from-type-material designations for `Aspergillus pseudonomiae`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one exact organism row, two linked sequencing projects, and one project-linked genome-analysis row under NCBI taxon `1506151`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1506151`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1506151`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1506151`. |

The native GOLD snapshot has one exact organism row, `Go0108191` for `Aspergillus pseudonomiae CBS 119388` on line 59841. It joins to standard-draft project `Gp0108191` and transcriptome project `Gp0108192` on lines 61565-61566; `Gp0108191` then links through `AP PROJECT GOLD IDS` to the standard-draft analysis on line 134002.

Native BacDive and StrainInfo have no exact entries under taxon `1506151`, and the generated StrainInfo overlay files contain no rows for `NCBITaxon:1506151`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one exact synonym, one related synonym, merged-ID provenance, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism with two linked sequencing projects, one linked genome analysis, and no matched BacDive-derived local strain identifier to join through.
- BacDive and StrainInfo do not supply exact strain records for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- Native GOLD genome analyses may be linked by `AP PROJECT GOLD IDS`; the exact scan checked those project IDs as well as direct AP organism IDs.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
