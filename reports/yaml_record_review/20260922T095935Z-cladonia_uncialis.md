# YAML Record Review: Cladonia uncialis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cladonia_uncialis.yaml
- Started UTC: 2026-09-22T09:59:35Z
- Finished UTC: 2026-09-22T09:59:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:174080 |
| label | Cladonia uncialis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5199 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic lichen-forming fungal species at `data/taxa/eukaryota/cladonia_uncialis.yaml`. It carries one NCBI exact synonym, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cladonia_uncialis.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cladonia_uncialis.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cladonia_uncialis.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already passed on the current checkout. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 35364 has `NCBITaxon:174080`, label `Cladonia uncialis`, rank `SPECIES`, direct parent `NCBITaxon:5199`, genetic code `1`, exact synonym `Lichen uncialis`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 54277 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Cladonia` under family `Cladoniaceae`.

Exact scans found no retained retired row or exact `data/raw/ncbi_merged_ids.tsv` old ID for this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 35364 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54277 | Supported exactly: `attested rule: Cladonia uncialis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 15127 | Supported exactly with one aggregate GOLD organism assertion for `NCBITaxon:174080`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has one exact organism row, `Go0455075` for `Cladonia uncialis Normore 8774`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact project `Gp0323401` joins to `Go0455075`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by joined project IDs | Supported; one native GOLD analysis row joins through project `Gp0323401` and names `Cladonia uncialis Normore 8774`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material row exists for `NCBITaxon:174080`. |
| Empty native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported; no exact direct StrainInfo record or deposit-taxonomy match exists under taxon ID `174080`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz`, `data/raw/bacdive_strains.tsv`, and raw generated-strain inputs | Supported; no BacDive record, raw BacDive-derived strain row, or raw generated-strain row was filed under taxon ID `174080`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:174080`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:174080`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; no retained retired row or exact merged-ID row points into this taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cladonia` parent, one exact synonym, and two related synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, one joined project, and one joined analysis row for this taxon.
- BacDive, NCBI type-material, native StrainInfo, generated StrainInfo overlay, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- An `rg --no-ignore --hidden` check over `data/raw`, `data/straininfo`, and `curation/seed_scope.tsv` included ignored files while confirming there were no additional maintained rows for this taxon beyond the expected NCBI, GOLD aggregate, seed-scope, and native GOLD evidence.
- NCBI ranks `Cladonia uncialis` as `SPECIES`, and the generated record follows the source rank exactly.
