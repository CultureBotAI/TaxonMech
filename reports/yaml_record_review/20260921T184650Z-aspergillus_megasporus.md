# YAML Record Review: Aspergillus megasporus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_megasporus.yaml
- Started UTC: 2026-09-21T18:45:24Z
- Finished UTC: 2026-09-21T18:46:50Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2814297 |
| label | Aspergillus megasporus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720874 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_megasporus.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_megasporus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_megasporus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_megasporus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 558816 has `NCBITaxon:2814297`, label `Aspergillus megasporus`, rank `SPECIES`, direct parent `NCBITaxon:2720874`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 63280 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:2814297`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 558816 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 63280 | Supported exactly: `attested rule: Aspergillus megasporus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 27080 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:2814297`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 126603-126612 | Supported exactly with six culture-from-holotype designations and two colon-normalized variants, plus the `DAOM 741781` holotype and colon-normalized variant under taxon name `Aspergillus megasporus`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with organism `Go0446110`, strain `DTO 048-I3`, and three linked sequencing projects; no local native analysis row targeted this organism or its projects. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2814297` or the reviewed NCBI/native GOLD designations. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/records.jsonl.gz`, `data/straininfo/assemblies.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; StrainInfo has no direct strain record, deposit-taxonomy record, assembly overlay, or related-record overlay for `NCBITaxon:2814297`. |

The native GOLD `Aspergillus megasporus DTO 048-I3` organism links to three BioProjects, but that GOLD evidence does not emit `strain_assemblies`, `strain_genome_records`, or `strain_related_records` rows because `DTO 048-I3` is absent from the BacDive-derived local strain inventory.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, a related synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism row and three sequencing projects for this taxon, with no matched BacDive-derived local strain identifier to join through.
- StrainInfo and BacDive do not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The native GOLD rows for `DTO 048-I3` are useful GOLD support, but the type material is represented by `DTO 356-H7`, `CBS 141929`, and the `DAOM` designations in NCBI.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
