# YAML Record Review: Aspergillus parasiticus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_parasiticus.yaml
- Started UTC: 2026-09-21T19:50:35Z
- Finished UTC: 2026-09-21T19:51:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5067 |
| label | Aspergillus parasiticus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_parasiticus.yaml`. It carries ten NCBI related synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_parasiticus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_parasiticus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_parasiticus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2214 has `NCBITaxon:5067`, label `Aspergillus parasiticus`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, ten related synonyms, and source `gold`. `curation/seed_scope.tsv` line 51924 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` lines 18697-18705 redirect nine old IDs, `NCBITaxon:1521359` through `NCBITaxon:1521367`, into `NCBITaxon:5067`; none of those old IDs is retained in `data/raw/ncbitaxon_taxa.tsv`, so the record has no retired predecessor records to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2214 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 51924 | Supported exactly: `attested rule: Aspergillus parasiticus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37432 | Supported exactly with seven aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:5067`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 225495-225500 | Supported exactly with `ATCC 1018`, `CBS 100926`, and `NRRL 502` culture-from-neotype variants for `Aspergillus parasiticus`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with seven exact organism rows, seven linked sequencing projects, and two linked analyses under NCBI taxon `5067`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5067`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:5067`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:5067`. |

The native GOLD snapshot has seven exact organism rows for NCBI taxon `5067`, including `Go0046685` for `FRR 2744`, `Go0046686` for `FRR 3282`, and `Go0098895` for `NRRL 2999`. They join to seven sequencing projects; analyses for `Aspergillus parasiticus 68-5` and `Aspergillus parasiticus CBS 117618 Standard Draft` are linked through `AP PROJECT GOLD IDS`.

Native StrainInfo has 150 direct strain rows and 274 deposit-taxonomy hits under taxon `5067`, including type-strain deposits on line 51126; the generated StrainInfo overlay files contain no rows for `NCBITaxon:5067` because the overlay is limited to BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, ten related synonyms, the nine merged old IDs, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of seven.
- The local native GOLD snapshot has seven exact organism rows, seven linked sequencing projects, and two linked analyses, with no matched BacDive-derived local strain identifiers to join through.
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
- GOLD analyses for this taxon are linked through project IDs, so the native scan checked `AP PROJECT GOLD IDS` as well as direct `AP ORGANISM GOLD ID` values.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
