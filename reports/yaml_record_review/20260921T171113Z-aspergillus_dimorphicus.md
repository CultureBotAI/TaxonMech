# YAML Record Review: Aspergillus dimorphicus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_dimorphicus.yaml
- Started UTC: 2026-09-21T17:10:09Z
- Finished UTC: 2026-09-21T17:11:13Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:36641 |
| label | Aspergillus dimorphicus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720873 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_dimorphicus.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_dimorphicus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_dimorphicus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_dimorphicus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4081 has `NCBITaxon:36641`, label `Aspergillus dimorphicus`, rank `SPECIES`, direct parent `NCBITaxon:2720873`, genetic code `1`, related synonym `Aspergillus dimorphicus B.S. Mehrotra & R. Prasad, 1969`, and source `gold`. `curation/seed_scope.tsv` line 52339 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720873` subgenus `Aspergillus subgen. Cremei`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:36641`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 4081 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52339 | Supported exactly: `attested rule: Aspergillus dimorphicus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 33424 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:36641`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 194843-194852 | Supported exactly with ten `typematerial.dmp` designations spanning culture-from-lectotype `NRRL 3650`, culture-from-neotype `CBS 649.74`, and culture-from-type-material `IMI 131553` and `QM 9190` aliases. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `36641` or the reviewed NCBI type-material designations. |
| Empty StrainInfo assembly and related-record surface | Exact direct, deposit taxon, and exact quoted-designation scans of `data/straininfo/records.jsonl.gz`, `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, and generated raw strain tables | Supported; StrainInfo has five direct taxon matches for `36641`, including exact type-token deposits for `CBS 649.74`, `IMI 131553`, `NRRL 3650`, and `QM 9190`, but it emits no assembly, related-record, or generated strain rows for this taxon. |

Native GOLD contains one exact organism row for `CBS 649.79` and three linked sequencing-project rows. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local StrainInfo snapshot has five direct strain records for this taxon, but they have no local assembly or related-record export rows.
- The local native GOLD snapshot has one organism and three sequencing projects for this taxon; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
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
