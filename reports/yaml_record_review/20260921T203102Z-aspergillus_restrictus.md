# YAML Record Review: Aspergillus restrictus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_restrictus.yaml
- Started UTC: 2026-09-21T20:29:55Z
- Finished UTC: 2026-09-21T20:31:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5064 |
| label | Aspergillus restrictus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720874 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_restrictus.yaml`. It carries two NCBI related synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_restrictus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_restrictus.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_restrictus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2213 has `NCBITaxon:5064`, label `Aspergillus restrictus`, rank `SPECIES`, direct parent `NCBITaxon:2720874`, genetic code `1`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 51923 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` line 72661 redirects old ID `NCBITaxon:361780` into `NCBITaxon:5064`. That old ID is not retained in `data/raw/ncbitaxon_taxa.tsv` as a retired row pointing at this species, so the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2213 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 51923 | Supported exactly: `attested rule: Aspergillus restrictus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37428 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:5064`. |
| NCBI merged-ID handling | `data/raw/ncbi_merged_ids.tsv` line 72661; retained-old-ID scan of `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; the source row redirects `NCBITaxon:361780` into this species, with no retained retired row. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 225434-225479 | Supported exactly with 46 culture-from-lectotype, culture-from-type-material, and type-material designations for `Aspergillus restrictus`. |
| Native GOLD evidence | Exact native GOLD organism and sequencing-project scans | Supported exactly with one exact organism row and two linked sequencing projects under NCBI taxon `5064`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5064`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:5064`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:5064`. |

The native GOLD snapshot has one exact organism row, `Go0108086` for `Aspergillus restrictus CBS 118.33` on line 59790. It joins to standard-draft project `Gp0108085` and transcriptome project `Gp0108086` on lines 61465-61466, with no linked genome-analysis rows.

Native StrainInfo has 57 direct strain rows and 107 deposit-taxonomy hits under taxon `5064`; the generated StrainInfo overlay files contain no rows for `NCBITaxon:5064` because the overlay is limited to BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, two related synonyms, merged-ID provenance, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism with two linked sequencing projects, no linked genome analyses, and no matched BacDive-derived local strain identifier to join through.
- BacDive does not supply exact local strain records for this taxon, and the native StrainInfo records do not produce generated overlay rows.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
