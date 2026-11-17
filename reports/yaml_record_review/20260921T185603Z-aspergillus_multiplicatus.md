# YAML Record Review: Aspergillus multiplicatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_multiplicatus.yaml
- Started UTC: 2026-09-21T18:54:56Z
- Finished UTC: 2026-09-21T18:56:03Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1806848 |
| label | Aspergillus multiplicatus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_multiplicatus.yaml`. It carries one NCBI exact synonym, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_multiplicatus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_multiplicatus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_multiplicatus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 472306 has `NCBITaxon:1806848`, label `Aspergillus multiplicatus`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, one exact synonym, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 61290 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` line 98832 redirects old ID `NCBITaxon:91490` into `NCBITaxon:1806848`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 472306 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61290 | Supported exactly: `attested rule: Aspergillus multiplicatus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 15909 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1806848`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 61147-61150 | Supported exactly with the `CBS 646.95` and `IBT 17517` type-material designations plus colon-normalized variants under taxon name `Aspergillus multiplicatus`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with organism `Go0125784`, strain text `CBS 646958`, and one linked sequencing project; no local native analysis row targeted this organism or its project. |
| BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported as empty; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1806848` or the reviewed NCBI/native GOLD designations. |
| StrainInfo evidence | Exact direct, deposit-taxonomy, assembly, exclusion, and related-record scans | Supported; StrainInfo has two direct records under `NCBITaxon:1806848`, including one with `CBS 646.95` and `IBT 17517`, and no assembly or related-record overlay rows for this target. |

The native GOLD `Aspergillus multiplicatus CBS 646958` organism links to one BioProject, but that GOLD evidence does not emit `strain_assemblies`, `strain_genome_records`, or `strain_related_records` rows because `CBS 646958` is absent from the BacDive-derived local strain inventory. StrainInfo contains a direct record for the related `CBS 646.95` deposit, but GOLD joins are mediated through BacDive-derived local strain IDs.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism row and one sequencing project for this taxon, with no matched BacDive-derived local strain identifier to join through.
- StrainInfo has exact direct records for this taxon but no assembly, exclusion, or related-record overlay rows.
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
- The exact quoted-token scan found StrainInfo `siID` 174275 under `NCBITaxon:1806848`, consistent with the direct StrainInfo taxon scan.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
