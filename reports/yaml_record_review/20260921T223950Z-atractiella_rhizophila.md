# YAML Record Review: Atractiella rhizophila

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/atractiella_rhizophila.yaml
- Started UTC: 2026-09-21T22:38:46Z
- Finished UTC: 2026-09-21T22:39:50Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1938712 |
| label | Atractiella rhizophila |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5228 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/atractiella_rhizophila.yaml`. It carries one exact NCBI synonym, one related NCBI synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*atractiella_rhizophila.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/atractiella_rhizophila.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/atractiella_rhizophila.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 497702 has `NCBITaxon:1938712`, label `Atractiella rhizophila`, rank `SPECIES`, direct parent `NCBITaxon:5228`, genetic code `1`, one exact synonym, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 61684 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Atractiella` under `Hoehnelomycetaceae`.

`data/raw/ncbi_merged_ids.tsv` line 10134 maps old ID `NCBITaxon:1264971` into `NCBITaxon:1938712`, but there is no retained retired row for that old ID in `data/raw/ncbitaxon_taxa.tsv`; the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 497702 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61684 | Supported exactly: `attested rule: Atractiella rhizophila, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 17823 | Supported exactly with one aggregate KG-Microbe GOLD row asserting two organisms for `NCBITaxon:1938712`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 73384-73390 | Supported exactly with seven `typematerial.dmp` designations for the PMI 95 holotype and related CBS and DUKE accessions. |
| Historical NCBI merge | `data/raw/ncbi_merged_ids.tsv` line 10134 plus exact retained-old-ID scan | Supported; one old ID merges into this target but does not generate `replaces` without a retained retired NCBI inventory row. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with `Go0019329` for strain `PMI 95` on line 16352. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with transcriptome project `Gp0019329` and standard-draft project `Gp0019383` on lines 15760 and 15777. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with one analysis row joining through project `Gp0019383`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1938712`. |
| Empty native StrainInfo surface | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has no direct records or deposit-taxonomy hits under `1938712`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1938712`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1938712`. |

The local native GOLD snapshot has one exact organism for the holotype strain token `PMI 95` and two projects for that organism. The KG-Microbe aggregate GOLD row still supplies the generated source-attestation count of two, and the generated record appropriately leaves `strain_count` at zero because no BacDive-derived or StrainInfo overlay row provides an eligible local strain for this target.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Atractiella` parent, one exact synonym, one related synonym, the visible merged-ID context, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot supplies one exact organism with two joined projects and one joined analysis row.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Atractiella rhizophila` as `SPECIES`, and the generated record follows the source rank exactly.
