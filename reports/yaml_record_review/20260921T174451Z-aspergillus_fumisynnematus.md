# YAML Record Review: Aspergillus fumisynnematus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_fumisynnematus.yaml
- Started UTC: 2026-09-21T17:44:00Z
- Finished UTC: 2026-09-21T17:44:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:286432 |
| label | Aspergillus fumisynnematus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_fumisynnematus.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_fumisynnematus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_fumisynnematus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_fumisynnematus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 58519 has `NCBITaxon:286432`, label `Aspergillus fumisynnematus`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, related synonym `Aspergillus fumisynnematus Y. Horie, Miyaji, Nishim., Taguchi & Udagawa, 1993`, and source `gold`. `curation/seed_scope.tsv` line 55002 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:286432`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 58519 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55002 | Supported exactly: `attested rule: Aspergillus fumisynnematus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 27823 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:286432`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 133614-133615 | Supported exactly with two `typematerial.dmp` culture-from-holotype designations for `IFM 42277` under taxon name `Aspergillus fumisynnematus`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `286432` or the reviewed NCBI type-material designations. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/assemblies.tsv` and `data/straininfo/related_records.tsv.gz` | Supported; `data/straininfo/records.jsonl.gz` has two direct strain records and two deposit-taxonomy records for taxon ID `286432`, but none produce StrainInfo assembly or related-record overlay rows for `NCBITaxon:286432`. |

The local native GOLD snapshot has no exact organism, project, or analysis row for `NCBITaxon:286432`, so there are no committed native GOLD rows that should have generated strain, assembly, genome, or related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot does not have an exact organism row for this taxon.
- StrainInfo has direct records for this taxon, but no assembly or related-record exports for it and no BacDive-derived strain to overlay.
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
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
