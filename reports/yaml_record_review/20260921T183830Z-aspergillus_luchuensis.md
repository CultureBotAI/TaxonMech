# YAML Record Review: Aspergillus luchuensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_luchuensis.yaml
- Started UTC: 2026-09-21T18:37:12Z
- Finished UTC: 2026-09-21T18:38:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1069201 |
| label | Aspergillus luchuensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_luchuensis.yaml`. It carries six NCBI exact synonyms, five NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and direct source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_luchuensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_luchuensis.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_luchuensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 228731 has `NCBITaxon:1069201`, label `Aspergillus luchuensis`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, six exact synonyms, five related synonyms, and source `gold`. `curation/seed_scope.tsv` line 57452 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` lines 56229, 76025, and 99083 redirect old IDs `NCBITaxon:288671`, `NCBITaxon:40384`, and `NCBITaxon:929029` into `NCBITaxon:1069201`, but none of those old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 228731 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 57452 | Supported exactly: `attested rule: Aspergillus luchuensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 1162 | Supported exactly with eleven aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1069201`; the generated note correctly states that these are records filed directly under this taxon, with descendant taxa not gathered. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 4324-4333 | Supported exactly with ten `typematerial.dmp` culture-from-type-material designations for `CBS 205.80`, `IFM 47726`, `KACC 46772`, `NBRC 4281`, `RIB 2642`, and their colon-normalized variants under taxon name `Aspergillus luchuensis`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1069201` or the reviewed NCBI type-material and GOLD culture designations. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/assemblies.tsv` and `data/straininfo/related_records.tsv.gz` | Supported; `data/straininfo/records.jsonl.gz` has sixteen direct strain records and seventeen matching deposit-taxonomy records for taxon ID `1069201`, including one entry with exact `IFO 4308`, but none produce StrainInfo assembly or related-record overlay rows for `NCBITaxon:1069201`. |

Native GOLD contains eleven exact organism rows, eleven linked sequencing-project rows, and eleven linked analysis rows through `AP PROJECT GOLD IDS`. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a direct taxon-level organism count of eleven.
- The local native GOLD snapshot has eleven organisms, eleven sequencing projects, and eleven analyses filed directly under this taxon; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- StrainInfo has exact taxon records, but no assembly or related-record exports for them and no BacDive-derived strains to overlay.
- BacDive does not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The native GOLD analysis lookup checked both `AP ORGANISM GOLD ID` and exact IDs in `AP PROJECT GOLD IDS`.
- Some NCBI type-material strings occur in StrainInfo under other taxa, for example `CBS 205.80` under `Aspergillus niger var. intermedius`; those text hits are not exact taxonomic support for `NCBITaxon:1069201`.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
