# YAML Record Review: Attheya septentrionalis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/attheya_septentrionalis.yaml
- Started UTC: 2026-09-21T22:41:05Z
- Finished UTC: 2026-09-21T22:42:01Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:420275 |
| label | Attheya septentrionalis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:265578 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic diatom species at `data/taxa/eukaryota/attheya_septentrionalis.yaml`. It carries two exact NCBI synonyms, two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*attheya_septentrionalis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/attheya_septentrionalis.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/attheya_septentrionalis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 92167 has `NCBITaxon:420275`, label `Attheya septentrionalis`, rank `SPECIES`, direct parent `NCBITaxon:265578`, genetic code `1`, two exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 55598 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Attheya` under `Attheyaceae`.

`data/raw/ncbi_merged_ids.tsv` line 47226 maps old ID `NCBITaxon:265593` into `NCBITaxon:420275`, but there is no retained retired row for that old ID in `data/raw/ncbitaxon_taxa.tsv`; the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 92167 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55598 | Supported exactly: `attested rule: Attheya septentrionalis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 35041 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:420275`. |
| Historical NCBI merge | `data/raw/ncbi_merged_ids.tsv` line 47226 plus exact retained-old-ID scan | Supported; one old ID merges into this target but does not generate `replaces` without a retained retired NCBI inventory row. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with `Go0368578` for strain `CCMP 2084` on line 273302. |
| Empty native GOLD project and analysis evidence | Exact native GOLD sequencing-project and analysis scans | Supported; no native GOLD project or analysis row joins back to this organism in the local snapshot. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows mention `NCBITaxon:420275`. |
| Native StrainInfo evidence | Exact native StrainInfo direct and deposit-taxonomy scans | Supported exactly with two direct rows under taxon ID `420275`, for `CCMP2083` and `CCMP2084`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:420275`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `420275`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:420275`. |

The local native GOLD row references `CCMP 2084`, one of the two native StrainInfo designations. Those native rows do not produce local strain entries here because no BacDive-derived strain or generated StrainInfo overlay row is filed under this target.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Attheya` parent, two exact synonyms, two related synonyms, and the visible merged-ID context.
- NCBI does not supply type-material rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with no joined project or analysis rows.
- The local native StrainInfo snapshot supplies two exact rows, but the generated StrainInfo overlay surface is empty for this target.
- BacDive does not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Attheya septentrionalis` as `SPECIES`, and the generated record follows the source rank exactly.
