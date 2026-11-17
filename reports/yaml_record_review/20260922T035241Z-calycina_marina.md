# YAML Record Review: Calycina marina

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/calycina_marina.yaml
- Started UTC: 2026-09-22T03:52:41Z
- Finished UTC: 2026-09-22T03:52:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1763456 |
| label | Calycina marina |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:186310 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/calycina_marina.yaml`. It carries one NCBI exact synonym, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*calycina_marina.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/calycina_marina.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/calycina_marina.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 460988 has `NCBITaxon:1763456`, label `Calycina marina`, rank `SPECIES`, direct parent `NCBITaxon:186310`, genetic code `1`, one exact synonym, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 61229 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent genus `Calycina` under family `Pezizellaceae`.

No committed NCBI merged-ID row or retained retired row points at `NCBITaxon:1763456`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 460988 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61229 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 15355 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1763456`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0115657` for `Calycina marina TRa3180A` at line 65327. |
| Native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported exactly by projects `Gp0119912` and `Gp0119913` for `Go0115657`. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no analysis row joins through the exact organism or project IDs for `NCBITaxon:1763456`. |
| Empty NCBI merged-ID inventories | Exact scans of `data/raw/ncbi_merged_ids.tsv` and retained retired rows | Supported; neither side old-ID inventory nor retained retired-row evidence points at `NCBITaxon:1763456`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material row is filed under `NCBITaxon:1763456`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1763456`. |
| Empty StrainInfo taxon surface | Exact native StrainInfo taxon scans plus generated overlay scans | Supported; no native direct/deposit hit or generated StrainInfo overlay row mentions `NCBITaxon:1763456`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1763456`. |

The committed aggregate GOLD row is mirrored by one exact native GOLD organism and two native project rows. The local native GOLD analysis snapshot has no row joined through those exact project IDs.

The NCBI type-material inventory is empty for `Calycina marina`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Calycina` genus parent, one exact synonym, and two related synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism and two project rows, but no joined analysis row.
- BacDive and StrainInfo do not supply exact local strain or overlay evidence for this taxon.
- NCBI merged-ID, NCBI type-material, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- Exact local native GOLD scans recovered one organism row, two project rows, and zero analysis rows for `NCBITaxon:1763456`.
- GOLD analysis evidence joins through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Calycina marina` as `SPECIES`, and the generated record follows the source rank exactly.
