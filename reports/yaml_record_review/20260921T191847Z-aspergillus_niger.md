# YAML Record Review: Aspergillus niger

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_niger.yaml
- Started UTC: 2026-09-21T19:15:34Z
- Finished UTC: 2026-09-21T19:18:47Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5061 |
| label | Aspergillus niger |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_niger.yaml`. It carries two NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_niger.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_niger.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_niger.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2210 has `NCBITaxon:5061`, label `Aspergillus niger`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, two exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 51920 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` line 65833 redirects old ID `NCBITaxon:319628` into `NCBITaxon:5061`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2210 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 51920 | Supported exactly: `attested rule: Aspergillus niger, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37425 | Supported exactly with 194 aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:5061`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 225412-225419 | Supported exactly with `CBS 101883` culture-from-holotype variants for exact synonym `Aspergillus lacticoffeatus` and `ATCC 16888`, `CBS 554.65`, and `NRRL 326` culture-from-neotype variants for `Aspergillus niger`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with 188 organism rows, 1,924 linked sequencing projects, and 51 genome analyses linked through `AP PROJECT GOLD IDS`. |
| Empty BacDive strain surface | Exact taxon and exact raw-table scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5061`. |
| StrainInfo evidence | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; StrainInfo has 912 direct records and 926 deposit-taxonomy records under `NCBITaxon:5061`, four intermediate related-record overlay rows, and no assembly or exclusion rows for this target. |

The local native GOLD snapshot has exact `Aspergillus niger` organism rows beginning at lines 2220, 2221, 4359, 17808, and 17933 and project rows beginning at lines 2250, 2251, 4369, 17229, and 17362. Its first ten genome-analysis rows include `Ga0052390`, `Ga0052391`, `Ga0133622`, `Ga0136813`, `Ga0212313`, `Ga0212770`, `Ga0212807`, `Ga0212897`, `Ga0212931`, and `Ga0233286`; those rows link through `AP PROJECT GOLD IDS`.

The StrainInfo overlay rows at `data/straininfo/related_records.tsv.gz` lines 254932-254935 match deposits `KCTC 19375` and `JCM 16961` to `kgmicrobe.strain:bacdive_7785` through `straininfo.strain:75690`. The generated raw strain tables have no exact `NCBITaxon:5061` rows, so those intermediate overlay rows do not produce `data/raw/strain_related_records.tsv`, `data/raw/strain_assemblies.tsv`, or `data/raw/strain_genome_records.tsv` entries for this generated taxon record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of 194.
- The local native GOLD snapshot has 188 organism rows, 1,924 linked sequencing projects, and 51 genome analyses for this taxon, with no matched BacDive-derived local strain identifier to join through in the generated raw strain tables.
- StrainInfo has exact direct, deposit-taxonomy, and intermediate related-record rows for this taxon but no assembly or exclusion rows.
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
- Native GOLD has ten exact organism rows with non-empty `ORGANISM CULTURE COLLECTION ID` values, and StrainInfo has exact quoted-token hits for several NCBI and GOLD designations, but those rows do not join to a BacDive-derived local strain in the generated raw strain tables.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
