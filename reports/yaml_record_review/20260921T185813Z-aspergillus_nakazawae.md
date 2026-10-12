# YAML Record Review: Aspergillus nakazawae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_nakazawae.yaml
- Started UTC: 2026-09-21T18:57:17Z
- Finished UTC: 2026-09-21T18:58:13Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1883082 |
| label | Aspergillus nakazawae |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5052 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_nakazawae.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no NCBI type-material designations, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_nakazawae.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_nakazawae.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_nakazawae.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 490334 has `NCBITaxon:1883082`, label `Aspergillus nakazawae`, rank `SPECIES`, direct parent `NCBITaxon:5052`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 61438 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:1883082`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 490334 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61438 | Supported exactly: `attested rule: Aspergillus nakazawae, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 16926 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1883082`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported as empty; no committed NCBI type-material row targets `NCBITaxon:1883082`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with organism `Go0108214`, strain `CBS 640.78`, and three linked sequencing projects; no local native analysis row targeted this organism or its projects. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1883082` or the reviewed native GOLD designation. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/records.jsonl.gz`, `data/straininfo/assemblies.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; StrainInfo has no direct strain record, deposit-taxonomy record, assembly overlay, or related-record overlay for `NCBITaxon:1883082`. |

The native GOLD `Aspergillus nakazawae CBS 640.78` organism links to three BioProjects, but that GOLD evidence does not emit `strain_assemblies`, `strain_genome_records`, or `strain_related_records` rows because `CBS 640.78` is absent from the BacDive-derived local strain inventory.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and a related synonym.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism row and three sequencing projects for this taxon, with no matched BacDive-derived local strain identifier to join through.
- StrainInfo and BacDive do not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, curated-evidence, and type-material sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The exact `CBS 640.78` quoted-token scan found a StrainInfo deposit under `Aspergillus petrakii`, NCBI taxon `138280`; it is not exact taxonomic support for `NCBITaxon:1883082`.
- No NCBI type-material rows were available for review.
