# YAML Record Review: Babjevia anomala

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/babjevia_anomala.yaml
- Started UTC: 2026-09-21T23:30:41Z
- Finished UTC: 2026-09-21T23:32:01Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1337061 |
| label | Babjevia anomala |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:54598 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic yeast species at `data/taxa/eukaryota/babjevia_anomala.yaml`. It carries two exact NCBI synonyms, two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*babjevia_anomala.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/babjevia_anomala.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/babjevia_anomala.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 320404 has `NCBITaxon:1337061`, label `Babjevia anomala`, rank `SPECIES`, direct parent `NCBITaxon:54598`, genetic code `1`, two exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 59534 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Babjevia` under family `Lipomycetaceae`.

`data/raw/ncbi_merged_ids.tsv` lines 5615 and 85536 map old identifiers `NCBITaxon:1156967` and `NCBITaxon:54599` into `NCBITaxon:1337061`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at this current taxon. The generated record therefore correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 320404 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 59534 | Supported exactly: `attested rule: Babjevia anomala, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 8174 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1337061`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with `Go0705658` for strain `NRRL Y-7931` on line 526104. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with project `Gp0831708` on line 610263. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis row joins to organism `Go0705658` or project `Gp0831708` in the local snapshot. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 16 `type material` rows on lines 23849-23864, all under synonym name `Lipomyces anomalus`. |
| NCBI merged-ID evidence | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported; two old identifiers map into `NCBITaxon:1337061` but are not retained as retired taxon rows, so they are not emitted as `replaces`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1337061`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1337061`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1337061`. |

The NCBI type-material inventory contributes 16 spelling variants across ATCC 32435, CBS 6740, IFO 10400, JCM 5988, MUCL 39785, NRRL Y-7931, and VKM Y-1969. The local native GOLD snapshot has the matching NRRL Y-7931 organism and one project, without a joined analysis row.

The native StrainInfo snapshot has four exact direct rows and 15 exact deposit rows under `NCBITaxon:1337061`, with deposits overlapping the NCBI type-material designations. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Babjevia` parent, two exact synonyms, two related synonyms, and 16 type-material rows.
- NCBI supplies two merged-ID rows, but no retained retired row that should become `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one project and no joined analysis row.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Babjevia anomala` as `SPECIES`, and the generated record follows the source rank exactly.
