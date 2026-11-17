# YAML Record Review: Bjerkandera adusta

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/bjerkandera_adusta.yaml
- Started UTC: 2026-09-22T01:17:34Z
- Finished UTC: 2026-09-22T01:17:34Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5331 |
| label | Bjerkandera adusta |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5330 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/bjerkandera_adusta.yaml`. It carries four NCBI exact synonyms, four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*bjerkandera_adusta.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/bjerkandera_adusta.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/bjerkandera_adusta.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2355 has `NCBITaxon:5331`, label `Bjerkandera adusta`, rank `SPECIES`, direct parent `NCBITaxon:5330`, genetic code `1`, four exact synonyms, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 51971 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Bjerkandera` under family `Phanerochaetaceae`.

`data/raw/ncbi_merged_ids.tsv` maps two old IDs to this taxon: `NCBITaxon:2081288` and `NCBITaxon:798527`. No retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at this taxon with `retired_into`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2355 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 51971 | Supported exactly: `attested rule: Bjerkandera adusta, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 38051 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:5331`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0008855`, for strain HHB-12826-SP SB-22. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with three projects joined through `Go0008855`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with one analysis row joining through project `Gp0008855`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with two rows on lines 228970-228971. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5331`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:5331`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:5331`. |

The local native GOLD snapshot has one exact HHB-12826-SP SB-22 organism with a genome project, `Gp0008855`, and two gene-expression projects, `Gp0332784` and `Gp0332785`. The one native analysis row joins by `AP PROJECT GOLD IDS` to `Gp0008855`.

The NCBI type-material inventory contributes two `reference material` rows for CFMR HHB-12826-Sp. The native StrainInfo snapshot has 83 exact direct rows and 97 exact deposit rows under `NCBITaxon:5331`; none overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Bjerkandera` parent, four exact synonyms, four related synonyms, and two type-material rows.
- NCBI supplies two raw merged-ID rows, but does not supply a retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with three joined projects and one joined analysis.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The GOLD source attestation explicitly counts records filed directly under this taxon, not descendant taxa, and the exact native GOLD scan used direct `ORGANISM NCBI TAX ID` matches for `5331`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Bjerkandera adusta` as `SPECIES`, and the generated record follows the source rank exactly.
