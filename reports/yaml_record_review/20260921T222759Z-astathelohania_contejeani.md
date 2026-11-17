# YAML Record Review: Astathelohania contejeani

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/astathelohania_contejeani.yaml
- Started UTC: 2026-09-21T22:26:51Z
- Finished UTC: 2026-09-21T22:27:59Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:164912 |
| label | Astathelohania contejeani |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2932330 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/astathelohania_contejeani.yaml`. It carries one exact NCBI synonym, two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*astathelohania_contejeani.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/astathelohania_contejeani.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/astathelohania_contejeani.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 33833 has `NCBITaxon:164912`, label `Astathelohania contejeani`, rank `SPECIES`, direct parent `NCBITaxon:2932330`, genetic code `1`, one exact synonym, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 54210 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Astathelohania` under `Microsporidia`. NCBI carries this taxon in a 10-node lineage through `Fungi incertae sedis`, and the generated record follows that source lineage exactly.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 33833 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54210 | Supported exactly: `attested rule: Astathelohania contejeani, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 14150 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:164912`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows mention `NCBITaxon:164912`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism, one sequencing project, and one matching native GOLD analysis row. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `164912`. |
| Empty native StrainInfo surface | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has no direct records or deposit-taxonomy hits under `164912`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:164912`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:164912`. |

The local native GOLD snapshot has an exact organism row for `Thelohania contejeani T1` with `ORGANISM GOLD ID` `Go0631949` on line 462435. It joins to sequencing project `Gp0645769` on line 482498, and native GOLD analysis line 362513 joins to that project through `AP PROJECT GOLD IDS`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Astathelohania` parent, one exact synonym, and two related synonyms.
- NCBI does not supply type-material rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism, one linked sequencing project, and one linked genome analysis.
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
- NCBI ranks `Astathelohania contejeani` as `SPECIES`, and the generated record follows the source rank exactly.
