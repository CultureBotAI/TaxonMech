# YAML Record Review: Australozyma saccharicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/australozyma_saccharicola.yaml
- Started UTC: 2026-09-21T23:13:54Z
- Finished UTC: 2026-09-21T23:15:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1217583 |
| label | Australozyma saccharicola |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:3300567 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic yeast species at `data/taxa/eukaryota/australozyma_saccharicola.yaml`. It carries one exact NCBI synonym, six related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*australozyma_saccharicola.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/australozyma_saccharicola.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/australozyma_saccharicola.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 275532 has `NCBITaxon:1217583`, label `Australozyma saccharicola`, rank `SPECIES`, direct parent `NCBITaxon:3300567`, genetic code `12`, one exact synonym, six related synonyms, and source `gold`. `curation/seed_scope.tsv` line 58441 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Australozyma` under family `Metschnikowiaceae`.

`data/raw/ncbi_merged_ids.tsv` lines 5269-5272 map old identifiers `NCBITaxon:1146894`, `NCBITaxon:1146895`, `NCBITaxon:1146896`, and `NCBITaxon:1146897` into `NCBITaxon:1217583`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at this current taxon. The generated record therefore correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 275532 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58441 | Supported exactly: `attested rule: Australozyma saccharicola, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 5175 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1217583`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with `Go0705051` for strain `CBS 12575` on line 525497. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with project `Gp0831071` on line 609626. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis row joins to organism `Go0705051` or project `Gp0831071` in the local snapshot. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with nine rows on lines 14539-14547. |
| NCBI merged-ID evidence | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported; four old identifiers map into `NCBITaxon:1217583` but are not retained as retired taxon rows, so they are not emitted as `replaces`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1217583`. |
| Empty native StrainInfo surface | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has no direct records or deposit-taxonomy hits under `1217583`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1217583`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1217583`. |

The NCBI type-material inventory contributes five `culture from holotype` rows for CBS 12575 and four `holotype` rows for NBRC 108904. The local native GOLD snapshot has the matching CBS 12575 organism and one project, without a joined analysis row; those GOLD source rows do not create a local `strains` entry in this generated eukaryotic taxon record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Australozyma` parent, one exact synonym, six related synonyms, and nine type-material rows.
- NCBI supplies four merged-ID rows, but no retained retired row that should become `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one project and no joined analysis row.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Australozyma saccharicola` as `SPECIES`, and the generated record follows the source rank exactly.
