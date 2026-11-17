# YAML Record Review: Capniomyces stellatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/capniomyces_stellatus.yaml
- Started UTC: 2026-09-22T07:16:23Z
- Finished UTC: 2026-09-22T07:16:23Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:4885 |
| label | Capniomyces stellatus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:4884 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/capniomyces_stellatus.yaml`. It carries no NCBI exact synonyms, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*capniomyces_stellatus.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/capniomyces_stellatus.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/capniomyces_stellatus.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2123 has `NCBITaxon:4885`, label `Capniomyces stellatus`, rank `SPECIES`, direct parent `NCBITaxon:4884`, genetic code `1`, no exact synonyms, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 51869 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Capniomyces` under family `Legeriomycetaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2123 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 51869 | Supported exactly: `attested rule: Capniomyces stellatus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37018 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:4885`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0384449`, strain MIS-10-108 under the source name `Capniomyces stellatus MIS-10-108`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with one project, `Gp0235554`, for `Go0384449`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported exactly with one analysis row for MIS-10-108. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material rows mention `NCBITaxon:4885`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `4885`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:4885`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:4885`. |

The local native GOLD snapshot has one exact organism, MIS-10-108, with one joined project and one joined analysis row. The native StrainInfo snapshot has one exact direct row and one exact deposit link under `NCBITaxon:4885`, but no generated StrainInfo overlay rows because no BacDive-derived local strain row exists for this taxon.

The exact NCBI type-material, BacDive, raw strain, and auxiliary-source scans are all empty for this taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Capniomyces` parent, and one related synonym.
- NCBI does not supply merged-ID or type-material rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one project and one joined analysis.
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
- NCBI ranks `Capniomyces stellatus` as `SPECIES`, and the generated record follows the source rank exactly.
