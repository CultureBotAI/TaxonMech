# YAML Record Review: Aspergillus ruber

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_ruber.yaml
- Started UTC: 2026-09-21T20:34:38Z
- Finished UTC: 2026-09-21T20:35:50Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:396024 |
| label | Aspergillus ruber |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720874 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_ruber.yaml`. It carries three NCBI exact synonyms, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_ruber.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_ruber.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_ruber.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 84287 has `NCBITaxon:396024`, label `Aspergillus ruber`, rank `SPECIES`, direct parent `NCBITaxon:2720874`, genetic code `1`, three exact synonyms, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 55502 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` redirects old IDs `NCBITaxon:28570` and `NCBITaxon:469279` into `NCBITaxon:396024` on lines 55058 and 80066. Neither old ID is retained in `data/raw/ncbitaxon_taxa.tsv` as a retired row pointing at this species, so the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 84287 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55502 | Supported exactly: `attested rule: Aspergillus ruber, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34308 | Supported exactly with four aggregate KG-Microbe GOLD organism assertions filed directly under `NCBITaxon:396024`. |
| NCBI merged-ID handling | `data/raw/ncbi_merged_ids.tsv` lines 55058 and 80066; retained-old-ID scan of `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; both old IDs redirect into this species, with no retained retired rows. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 202791-202802 | Supported exactly with 12 culture-from-holotype, culture-from-neotype, and neotype designations for `Aspergillus ruber`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with four exact organism rows, six linked sequencing projects, and three project-linked genome-analysis rows under NCBI taxon `396024`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `396024`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:396024`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:396024`. |

The native GOLD snapshot has exact organism rows for `Aspergillus ruber CBS 135680`, `Aspergillus rubrobrunneus CBS 530.65`, `Aspergillus ruber S3811C`, and `Aspergillus ruber S1907`. Those rows join to six sequencing projects and to three genome analyses through `AP PROJECT GOLD IDS`: CBS 135680 on line 138979, S3811C on line 445129, and S1907 on line 445130.

Native StrainInfo has 111 direct strain rows and 160 deposit-taxonomy hits under taxon `396024`; the generated StrainInfo overlay files contain no rows for `NCBITaxon:396024` because the overlay is limited to BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, three exact synonyms, one related synonym, merged-ID provenance, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of four filed directly under this taxon, matching the YAML note that descendant taxa are not gathered.
- The local native GOLD snapshot has four exact organisms with six linked sequencing projects, three linked genome analyses, and no matched BacDive-derived local strain identifier to join through.
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
- Native GOLD genome analyses may be linked by `AP PROJECT GOLD IDS`; the exact scan checked those project IDs as well as direct AP organism IDs.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
