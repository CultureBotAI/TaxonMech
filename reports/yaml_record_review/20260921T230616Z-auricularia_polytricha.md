# YAML Record Review: Auricularia polytricha

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/auricularia_polytricha.yaml
- Started UTC: 2026-09-21T23:04:00Z
- Finished UTC: 2026-09-21T23:06:16Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:29893 |
| label | Auricularia polytricha |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5230 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/auricularia_polytricha.yaml`. It carries two exact NCBI synonyms, two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*auricularia_polytricha.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/auricularia_polytricha.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/auricularia_polytricha.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 3296 has `NCBITaxon:29893`, label `Auricularia polytricha`, rank `SPECIES`, direct parent `NCBITaxon:5230`, genetic code `1`, two exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52224 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Auricularia` under `Auriculariaceae`.

`data/raw/ncbi_merged_ids.tsv` line 12404 maps old identifier `NCBITaxon:1331289` into `NCBITaxon:29893`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at this current taxon. The generated record therefore correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 3296 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52224 | Supported exactly: `attested rule: Auricularia polytricha, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 29926 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:29893`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with `Go0518039` for strain `MG66` on line 364063. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with project `Gp0442108` on line 313748. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with one analysis row joining through project `Gp0442108`. |
| NCBI merged-ID evidence | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported; old identifier `NCBITaxon:1331289` maps into `NCBITaxon:29893` but is not retained as a retired taxon row, so it is not emitted as `replaces`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows mention `NCBITaxon:29893`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `29893`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:29893`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:29893`. |

The local native GOLD snapshot has one exact MG66 organism with one joined project and one joined analysis row. The analysis row links through `AP PROJECT GOLD IDS` rather than a populated `AP ORGANISM GOLD ID`, which still supports the GOLD evidence for this taxon.

The native StrainInfo snapshot has 45 exact direct rows and 76 exact deposit-taxonomy rows under `NCBITaxon:29893`, but none overlays onto a BacDive-derived local strain inventory entry. The generated StrainInfo assembly, exclusion, and related-record surfaces are therefore correctly empty for this generated taxon record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Auricularia` parent, and four synonyms.
- NCBI supplies one merged-ID row, but no retained retired row that should become `replaces`.
- NCBI does not supply type-material rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one joined project and one joined analysis row.
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
- NCBI ranks `Auricularia polytricha` as `SPECIES`, and the generated record follows the source rank exactly.
