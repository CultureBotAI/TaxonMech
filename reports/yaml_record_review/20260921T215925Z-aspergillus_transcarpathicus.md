# YAML Record Review: Aspergillus transcarpathicus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_transcarpathicus.yaml
- Started UTC: 2026-09-21T21:58:46Z
- Finished UTC: 2026-09-21T21:59:25Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1904041 |
| label | Aspergillus transcarpathicus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_transcarpathicus.yaml`. It carries two related NCBI synonyms, no exact NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_transcarpathicus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_transcarpathicus.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_transcarpathicus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 492348 has `NCBITaxon:1904041`, label `Aspergillus transcarpathicus`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, two related synonyms, no exact synonyms, and source `gold`. `curation/seed_scope.tsv` line 61513 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:1904041`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 492348 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61513 | Supported exactly: `attested rule: Aspergillus transcarpathicus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 17214 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1904041`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 11 culture-from-holotype rows for CBS 423.68, DTO 022-C7, IBT 22080, IMI 134108, and VKM F-1331 variants. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism, three sequencing projects, and no matching native GOLD analysis row. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1904041`. |
| Empty native and generated StrainInfo surfaces | Exact scans of native and generated StrainInfo snapshots | Supported; no native or generated StrainInfo row mentions `NCBITaxon:1904041`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1904041`. |

The native GOLD snapshot has one exact organism row on line 304896 for `Aspergillus transcarpathicus CBS 423.68` under NCBI taxon `1904041`, strain `CBS 423.68`, and GOLD organism `Go0446099`. That organism joins to sequencing projects `Gp0312196`, `Gp0317273`, and `Gp0397207` on lines 211432, 216448, and 283784; the bounded native GOLD analysis scan found no analysis row linked to that organism or project.

Native StrainInfo has no direct strain rows or deposit-taxonomy hits under taxon `1904041`, and the generated StrainInfo overlay files contain no rows for `NCBITaxon:1904041`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus subgen. Fumigati` parent, and the two related synonyms.
- NCBI has 11 type-material rows for this taxon; these rows are inventory evidence and do not by themselves imply a generated local strain entry.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism, three linked sequencing projects, and no linked genome analysis.
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
- NCBI ranks `Aspergillus transcarpathicus` as `SPECIES`, and the generated record follows the source rank exactly.
