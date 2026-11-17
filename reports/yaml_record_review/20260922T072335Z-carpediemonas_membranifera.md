# YAML Record Review: Carpediemonas membranifera

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/carpediemonas_membranifera.yaml
- Started UTC: 2026-09-22T07:23:35Z
- Finished UTC: 2026-09-22T07:23:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:201153 |
| label | Carpediemonas membranifera |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:201152 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic metamonad species at `data/taxa/eukaryota/carpediemonas_membranifera.yaml`. It carries no NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*carpediemonas_membranifera.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/carpediemonas_membranifera.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/carpediemonas_membranifera.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 39748 has `NCBITaxon:201153`, label `Carpediemonas membranifera`, rank `SPECIES`, direct parent `NCBITaxon:201152`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 54451 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Carpediemonas` under `Carpediemonas-like organisms`.

The bounded merged-ID scan found no old NCBI IDs that point into this taxon and no retained retired rows, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 39748 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54451 | Supported exactly: `attested rule: Carpediemonas membranifera, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 18570 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:201153`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with two native organisms, `Go0002362` with no named strain and `Go0598305` strain BICM. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with projects `Gp0002362` and `Gp0616734`, one for each exact native GOLD organism. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported exactly with one analysis row, `Carpediemonas membranifera BICM`, linked by `AP PROJECT GOLD IDS` to `Gp0616734`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material rows mention `NCBITaxon:201153`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `201153`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:201153`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:201153`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; no retained retired row or side-inventory merged ID points into `NCBITaxon:201153`. |

The aggregate GOLD row used for generation contributes one organism assertion. The local native GOLD snapshot currently has two exact organism rows, two joined projects, and one joined analysis row; the generated record is still faithful to the committed aggregate row that drives `source_attestations`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Carpediemonas` parent, no synonyms, and no type-material rows.
- NCBI has no side-inventory old IDs or retained retired rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies two exact organisms with two projects and one joined analysis.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Carpediemonas membranifera` as `SPECIES`, and the generated record follows the source rank exactly.
