# YAML Record Review: Aspergillus brunneus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_brunneus.yaml
- Started UTC: 2026-09-21T16:23:05Z
- Finished UTC: 2026-09-21T16:24:15Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41418 |
| label | Aspergillus brunneus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720874 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_brunneus.yaml`. It carries two NCBI exact synonyms, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_brunneus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_brunneus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_brunneus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4838 has `NCBITaxon:41418`, label `Aspergillus brunneus`, rank `SPECIES`, direct parent `NCBITaxon:2720874`, genetic code `1`, exact synonyms `Aspergillus echinulatus` and `Eurotium echinulatum`, related synonym `Aspergillus brunneus Delacroix, 1893`, and source `gold`. `curation/seed_scope.tsv` line 52473 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720874` subgenus `Aspergillus subgen. Aspergillus`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4838 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52473 | Supported exactly: `attested rule: Aspergillus brunneus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34834 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:41418`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 206360-206365 | Supported exactly with six holotype or type-material designation rows from `typematerial.dmp`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `41418`. |
| Empty generated StrainInfo overlay | Exact scans of `data/straininfo/exclusions.tsv`, `data/straininfo/assemblies.tsv`, and `data/straininfo/related_records.tsv.gz` for the matching StrainInfo IDs | Supported; all 31 exact or deposit-only StrainInfo rows for this taxon have `no_eligible_own_deposit_match` exclusions and produced no generated assembly or related-record rows. |

Native GOLD contains one exact organism row, `Go0647336` for `CBS 112.26`, one sequencing-project row, `Gp0683403`, and one linked genome analysis, `Ga0663025`, with GenBank assembly `GCA_020284055.1`. No `CBS 112.26` row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, two exact synonyms, one related synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism, one sequencing-project row, and one analysis row for `CBS 112.26`; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- StrainInfo supplies exact or deposit-level rows for this taxon, but each was excluded from the generated overlay because it had no eligible own-deposit match to the BacDive-derived local strain inventory.
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
