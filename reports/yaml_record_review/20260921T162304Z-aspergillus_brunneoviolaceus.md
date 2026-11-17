# YAML Record Review: Aspergillus brunneoviolaceus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_brunneoviolaceus.yaml
- Started UTC: 2026-09-21T16:22:00Z
- Finished UTC: 2026-09-21T16:23:04Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1191711 |
| label | Aspergillus brunneoviolaceus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_brunneoviolaceus.yaml`. It carries three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_brunneoviolaceus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_brunneoviolaceus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_brunneoviolaceus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 267394 has `NCBITaxon:1191711`, label `Aspergillus brunneoviolaceus`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, related synonyms `Aspergillus brunneoviolaceus Bat. & H. Maia 1955`, `Aspergillus brunneoviolaceus Batista & H. Maia, 1955`, and `Aspergillus sp. CCF 108`, and source `gold`. `curation/seed_scope.tsv` line 58255 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720871` subgenus `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` records `NCBITaxon:1107532` as merged into `NCBITaxon:1191711`, but that old ID is not a retained row in `data/raw/ncbitaxon_taxa.tsv`. The record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 267394 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58255 | Supported exactly: `attested rule: Aspergillus brunneoviolaceus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 4244 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1191711`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 12510-12520 | Supported exactly with 11 `type material` designation rows from `typematerial.dmp`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1191711`. |
| Empty generated StrainInfo overlay | Exact scans of `data/straininfo/exclusions.tsv`, `data/straininfo/assemblies.tsv`, and `data/straininfo/related_records.tsv.gz` for the matching StrainInfo IDs | Supported; all 12 exact StrainInfo rows for this taxon have `no_eligible_own_deposit_match` exclusions and produced no generated assembly or related-record rows. |

Native GOLD contains one exact organism row, `Go0047202` for `CBS 621.78`, and two sequencing-project rows, `Gp0047202` and `Gp0047203`, for that organism. It has no analysis row linked through either `AP ORGANISM GOLD ID` or `AP PROJECT GOLD IDS`, and no `CBS 621.78` row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

The type-material labels `CBS 621.78`, `IMI 312981`, `NRRL 4912`, and `WB 4912` appear in two StrainInfo rows filed under `Aspergillus japonicus` / NCBITaxon:34381, so they are not exact StrainInfo overlays for this taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, three related synonyms, the old-ID merge context reviewed above, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism and two sequencing-project rows for `CBS 621.78`; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- StrainInfo supplies exact rows for this taxon, but each was excluded from the generated overlay because it had no eligible own-deposit match to the BacDive-derived local strain inventory.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive, StrainInfo overlay, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
