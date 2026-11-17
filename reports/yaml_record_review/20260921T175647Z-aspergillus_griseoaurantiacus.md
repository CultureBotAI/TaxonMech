# YAML Record Review: Aspergillus griseoaurantiacus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_griseoaurantiacus.yaml
- Started UTC: 2026-09-21T17:55:33Z
- Finished UTC: 2026-09-21T17:56:47Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1507545 |
| label | Aspergillus griseoaurantiacus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5052 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_griseoaurantiacus.yaml`. It carries two NCBI related synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_griseoaurantiacus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_griseoaurantiacus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_griseoaurantiacus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 387186 has `NCBITaxon:1507545`, label `Aspergillus griseoaurantiacus`, rank `SPECIES`, direct parent `NCBITaxon:5052`, genetic code `1`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 60366 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate genus parent `Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:1507545`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 387186 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 60366 | Supported exactly: `attested rule: Aspergillus griseoaurantiacus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 11855 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1507545`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 37797-37802 | Supported exactly with six `typematerial.dmp` holotype and culture-from-holotype designations for `CBS 138191`, `DTO 267D8`, `CBS H-21814`, and their colon-normalized variants under taxon name `Aspergillus griseoaurantiacus`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1507545` or the reviewed NCBI type-material designations. |
| Empty StrainInfo overlay | Exact taxon and exact quoted-designation scans of `data/straininfo/records.jsonl.gz`; exact scans of `data/straininfo/assemblies.tsv` and `data/straininfo/related_records.tsv.gz` | Supported; StrainInfo has no direct or deposit-taxonomy record for taxon ID `1507545`, and no assembly or related-record overlay rows for `NCBITaxon:1507545`. |

The local native GOLD snapshot has no organism row with `ORGANISM NCBI TAX ID` equal to `1507545`; consequently, it has no exact project rows and no analysis rows linked by `AP ORGANISM GOLD ID` or `AP PROJECT GOLD IDS`. Generated strain, assembly, genome, and related-record precursor tables likewise have no row for `NCBITaxon:1507545`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, two related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot does not include an exact organism row for this NCBI taxon, so there are no native GOLD strain-level assertions to emit.
- BacDive and StrainInfo do not supply exact records for this taxon.
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
