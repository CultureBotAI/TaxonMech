# YAML Record Review: Brunneochlamydosporium cibotii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/brunneochlamydosporium_cibotii.yaml
- Started UTC: 2026-09-22T03:15:04Z
- Finished UTC: 2026-09-22T03:15:04Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:66309 |
| label | Brunneochlamydosporium cibotii |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2716904 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/brunneochlamydosporium_cibotii.yaml`. It carries one NCBI exact synonym, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*brunneochlamydosporium_cibotii.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/brunneochlamydosporium_cibotii.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/brunneochlamydosporium_cibotii.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 8668 has `NCBITaxon:66309`, label `Brunneochlamydosporium cibotii`, rank `SPECIES`, direct parent `NCBITaxon:2716904`, genetic code `1`, one exact synonym, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53133 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Brunneochlamydosporium` under family `Plectosphaerellaceae`.

No committed NCBI merged-ID row or retained retired row points at `NCBITaxon:66309`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 8668 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53133 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 40710 | Supported exactly with four aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:66309`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with four native organisms: `Go0608023`, `Go0608024`, `Go0608025`, and `Go0608026`. |
| Empty native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported; none of the exact native organisms has a joined project in the local snapshot. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis joins to this taxon by exact organism ID or project ID. |
| Empty NCBI merged-ID inventories | Exact scans of `data/raw/ncbi_merged_ids.tsv` and retained retired rows | Supported; neither side old-ID inventory nor retained retired-row evidence points at `NCBITaxon:66309`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with six culture-from-neotype spellings and four isotype spellings for `Gliocladium cibotii`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `66309`. |
| Native StrainInfo exact taxon evidence | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 10 deposit-taxonomy hits and seven direct records under `66309`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:66309`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:66309`. |

The local native GOLD snapshot has four exact organism rows but no joined projects or analyses.

The NCBI type-material inventory contributes 10 rows under the `Gliocladium cibotii` synonym.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Brunneochlamydosporium` parent, one exact synonym, two related synonyms, and 10 type-material rows.
- The aggregate GOLD transform supplies a taxon-level organism count of four.
- The local native GOLD snapshot supplies four exact organisms, no joined projects, and no joined analyses.
- Native StrainInfo has exact rows under this taxon, but no BacDive-derived local strain inventory entry turns them into generated `data/straininfo/` overlay rows.
- BacDive does not supply exact local strain evidence for this taxon.
- NCBI merged-ID, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The NCBI type-material count exceeded the bounded scan sample, so this review also used an exact `rg -n '^NCBITaxon:66309\t' data/raw/ncbi_type_material.tsv` scan to recover all 10 rows.
- StrainInfo exact taxon rows do not generate overlay rows unless they join to the BacDive-derived local strain inventory.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Brunneochlamydosporium cibotii` as `SPECIES`, and the generated record follows the source rank exactly.
