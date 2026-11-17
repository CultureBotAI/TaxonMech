# YAML Record Review: Auricularia auricula-judae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/auricularia_auricula_judae.yaml
- Started UTC: 2026-09-21T23:00:33Z
- Finished UTC: 2026-09-21T23:01:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:29892 |
| label | Auricularia auricula-judae |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5230 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/auricularia_auricula_judae.yaml`. It carries four exact NCBI synonyms, four related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*auricularia_auricula_judae.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/auricularia_auricula_judae.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/auricularia_auricula_judae.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 3295 has `NCBITaxon:29892`, label `Auricularia auricula-judae`, rank `SPECIES`, direct parent `NCBITaxon:5230`, genetic code `1`, four exact synonyms, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52223 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Auricularia` under `Auriculariaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 3295 | Supported exactly, including `jelly ear fungus` and `wood ear fungus` as related synonyms. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52223 | Supported exactly: `attested rule: Auricularia auricula-judae, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 29925 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:29892`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with `Go0384458` for strain `B14-8` on line 279864. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with project `Gp0235563` on line 156328. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with one analysis row joining through project `Gp0235563`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows mention `NCBITaxon:29892`. |
| Native StrainInfo evidence | Exact native StrainInfo direct and deposit-taxonomy scans | Supported with 36 direct native StrainInfo rows and 57 deposit-taxonomy hits under taxon ID `29892`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:29892`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `29892`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:29892`. |

The local native GOLD snapshot has one exact B14-8 organism with one joined project and one joined analysis row. Native StrainInfo contributes exact rows, but no BacDive-derived strain or generated StrainInfo overlay row is filed under this target.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Auricularia` parent, four exact synonyms, and four related synonyms.
- NCBI does not supply type-material or merged-ID rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one joined project and one joined analysis row.
- The local native StrainInfo snapshot supplies 36 exact direct rows and 57 deposit-taxonomy hits, but the generated StrainInfo overlay surface is empty for this target.
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
- NCBI ranks `Auricularia auricula-judae` as `SPECIES`, and the generated record follows the source rank exactly.
