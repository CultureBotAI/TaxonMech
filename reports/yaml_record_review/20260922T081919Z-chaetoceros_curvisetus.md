# YAML Record Review: Chaetoceros curvisetus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/chaetoceros_curvisetus.yaml
- Started UTC: 2026-09-22T08:19:19Z
- Finished UTC: 2026-09-22T08:19:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:230516 |
| label | Chaetoceros curvisetus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:49237 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic diatom species at `data/taxa/eukaryota/chaetoceros_curvisetus.yaml`. It carries one NCBI related synonym, no exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 \( -name '*chaetoceros_curvisetus.md' -o -name '*chaetoceros_debilis.md' -o -name '*chaetoceros_decipiens.md' -o -name '*chaetoceros_dichaeta.md' \) -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/chaetoceros_curvisetus.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/chaetoceros_curvisetus.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 45275 has `NCBITaxon:230516`, label `Chaetoceros curvisetus`, rank `SPECIES`, direct parent `NCBITaxon:49237`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 54642 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Chaetoceros` under family `Chaetocerotaceae`.

The bounded merged-ID scan found no old NCBI IDs that point into this taxon and no retained retired rows, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 45275 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54642 | Supported exactly: `attested rule: Chaetoceros curvisetus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 21606 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:230516`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has one exact organism row, `Go0368603` for `Chaetoceros curvisetus`. |
| Empty native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; no native project row joins to `Go0368603` in the local snapshot. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; with no joined native projects, no native analyses join to this taxon in the local snapshot. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material rows mention `NCBITaxon:230516`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `230516`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:230516`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:230516`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; no retained retired row or side-inventory merged ID points into `NCBITaxon:230516`. |

The aggregate GOLD row used for generation contributes one organism assertion. The native StrainInfo snapshot has one exact direct row and one exact deposit link under `NCBITaxon:230516`, but none overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Chaetoceros` parent, one related synonym, no exact synonyms, and no type-material rows.
- NCBI has no side-inventory old IDs or retained retired rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, no joined projects, and no joined analyses for this taxon.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Chaetoceros curvisetus` as `SPECIES`, and the generated record follows the source rank exactly.

