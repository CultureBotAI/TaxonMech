# YAML Record Review: Blastomyces percursus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/blastomyces_percursus.yaml
- Started UTC: 2026-09-22T02:21:39Z
- Finished UTC: 2026-09-22T02:21:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1658174 |
| label | Blastomyces percursus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:229219 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/blastomyces_percursus.yaml`. It carries no NCBI exact synonyms, five NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*blastomyces_percursus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/blastomyces_percursus.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/blastomyces_percursus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 433265 has `NCBITaxon:1658174`, label `Blastomyces percursus`, rank `SPECIES`, direct parent `NCBITaxon:229219`, genetic code `1`, no exact synonyms, five related synonyms, and source `gold`. `curation/seed_scope.tsv` line 60992 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Blastomyces` under family `Ajellomycetaceae`.

The exact NCBI merged-ID side scan maps old `NCBITaxon:1664002` and `NCBITaxon:1664003` to this taxon, but no retained retired-row evidence points at the record, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 433265 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 60992 | Supported exactly: `attested rule: Blastomyces percursus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| NCBI merged old IDs | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported with two side-inventory old IDs, `NCBITaxon:1664002` and `NCBITaxon:1664003`, remapped to `NCBITaxon:1658174`; no retained retired row generates a YAML `replaces` value. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 14278 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1658174`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0373177`, for strain EI222. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with one project, `Gp0219978`, joined through `Go0373177`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with one analysis row, `Blastomyces sp. CAC-2015b EI222`, joined through project `Gp0219978`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with eight rows on lines 50388-50395. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1658174`. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported with four exact direct StrainInfo records and four exact deposit-taxonomy matches. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1658174`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1658174`. |

The local native GOLD snapshot has one exact EI222 organism with one joined project and one joined native analysis row.

The NCBI type-material inventory contributes six `culture from holotype` rows and two `holotype` rows for CBS 139878, UAMH 7425, UAMH 7426, and Kemna 408-93 aliases.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Blastomyces` parent, five related synonyms, and eight type-material rows.
- NCBI also supplies two merged side-inventory old IDs, but no retained retired row that would generate `replaces`.
- NCBI does not supply exact synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one joined project and one joined analysis.
- Native StrainInfo has four exact direct records and four exact deposit-taxonomy hits, but the local StrainInfo overlay does not emit generated rows for this taxon.
- BacDive does not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The GOLD source attestation explicitly counts records filed directly under this taxon, not descendant taxa, and the exact native GOLD scan used direct `ORGANISM NCBI TAX ID` matches for `1658174`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Blastomyces percursus` as `SPECIES`, and the generated record follows the source rank exactly.
