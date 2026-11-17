# YAML Record Review: Aspergillus puulaauensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_puulaauensis.yaml
- Started UTC: 2026-09-21T20:25:26Z
- Finished UTC: 2026-09-21T20:26:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1220207 |
| label | Aspergillus puulaauensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5052 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_puulaauensis.yaml`. It carries two NCBI related synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_puulaauensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_puulaauensis.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_puulaauensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 276602 has `NCBITaxon:1220207`, label `Aspergillus puulaauensis`, rank `SPECIES`, direct parent `NCBITaxon:5052`, genetic code `1`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 58470 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, with `Aspergillus` as the immediate parent and no intervening subgenus node in the committed inventory.

`data/raw/ncbi_merged_ids.tsv` line 18202 redirects old ID `NCBITaxon:1507527` into `NCBITaxon:1220207`. That old ID is not retained in `data/raw/ncbitaxon_taxa.tsv` as a retired row pointing at this species, so the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 276602 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58470 | Supported exactly: `attested rule: Aspergillus puulaauensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 5296 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1220207`. |
| NCBI merged-ID handling | `data/raw/ncbi_merged_ids.tsv` line 18202; retained-old-ID scan of `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; the source row redirects `NCBITaxon:1507527` into this species, with no retained retired row. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 14796-14799 | Supported exactly with four culture-from-holotype designations for `Aspergillus puulaauensis`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with two exact organism rows, three linked sequencing projects, and one project-linked genome-analysis row under NCBI taxon `1220207`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1220207`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1220207`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1220207`. |

The native GOLD snapshot has exact organism rows for `Aspergillus puulaauensis IBT 32284` on line 304929 and `Aspergillus puulaauensis MK2` on line 462439. They join to minimal-draft and transcriptome projects `Gp0312235` and `Gp0317267` for `IBT 32284` plus `Gp0645773` for `MK2`; `Gp0645773` then links through `AP PROJECT GOLD IDS` to the analysis on line 362309.

Native StrainInfo has one direct strain row and one deposit-taxonomy hit under taxon `1220207`; the generated StrainInfo overlay files contain no rows for `NCBITaxon:1220207` because the overlay is limited to BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, two related synonyms, merged-ID provenance, and the culture-from-holotype designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot has two exact organisms with three linked sequencing projects, one linked genome analysis, and no matched BacDive-derived local strain identifier to join through.
- BacDive does not supply exact local strain records for this taxon, and the native StrainInfo record does not produce generated overlay rows.
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
