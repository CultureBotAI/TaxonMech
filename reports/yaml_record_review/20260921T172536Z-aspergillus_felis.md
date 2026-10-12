# YAML Record Review: Aspergillus felis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_felis.yaml
- Started UTC: 2026-09-21T17:24:22Z
- Finished UTC: 2026-09-21T17:25:36Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1287682 |
| label | Aspergillus felis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_felis.yaml`. It carries four NCBI related synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_felis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_felis.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_felis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 301712 has `NCBITaxon:1287682`, label `Aspergillus felis`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, related synonyms `Aspergillus felis Barrs, van Doorn, Varga & Samson, 2013`, `Aspergillus sp. DTO 155G2`, `Aspergillus sp. IFM 60053`, and `Aspergillus sp. JV-2013`, and source `gold`. `curation/seed_scope.tsv` line 58927 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720872` subgenus `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` redirects `NCBITaxon:1287684` and `NCBITaxon:1323497` into `NCBITaxon:1287682`, but an exact first-column scan of `data/raw/ncbitaxon_taxa.tsv` found no retained row for either old ID. The generated YAML therefore has no `replaces` value to add.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 301712 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58927 | Supported exactly: `attested rule: Aspergillus felis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 6671 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1287682`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 19438-19444 | Supported exactly with seven `typematerial.dmp` designations spanning culture-from-holotype `CBS 130245`, culture-from-type-material `DTO 155G2`, holotype `CBS H-21125`, and type-material `131F4`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact `CNM-CM7691` and `CNM-CM5623` quoted-token scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1287682`, the reviewed NCBI type-material designations, or the native GOLD strain tokens. |
| Empty StrainInfo assembly and related-record surface | Exact direct, deposit taxon, and exact quoted-designation scans of `data/straininfo/records.jsonl.gz`, `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, and generated raw strain tables | Supported; StrainInfo has four direct taxon matches for `1287682`, but it emits no assembly, related-record, or generated strain rows for this taxon. |

Native GOLD contains two exact organism rows, `CNM-CM7691` and `CNM-CM5623`, plus two linked isolate analyses. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, four synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local StrainInfo snapshot has four direct strain records for this taxon, but they have no local assembly or related-record export rows.
- The local native GOLD snapshot has two organisms, two sequencing projects, and two linked isolate analyses for this taxon; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- BacDive does not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, native GOLD, and retained-retired-ID checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
