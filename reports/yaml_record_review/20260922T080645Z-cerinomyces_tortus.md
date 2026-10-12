# YAML Record Review: Cerinomyces tortus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cerinomyces_tortus.yaml
- Started UTC: 2026-09-22T08:06:45Z
- Finished UTC: 2026-09-22T08:06:45Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2780975 |
| label | Cerinomyces tortus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:139293 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/cerinomyces_tortus.yaml`. It carries two NCBI exact synonyms, four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, two NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 \( -name '*cercospora_zeina.md' -o -name '*cerinomyces_crustulinus.md' -o -name '*cerinomyces_tortus.md' -o -name '*cerioporus_squamosus.md' \) -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cerinomyces_tortus.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cerinomyces_tortus.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 554582 has `NCBITaxon:2780975`, label `Cerinomyces tortus`, rank `SPECIES`, direct parent `NCBITaxon:139293`, genetic code `1`, two exact synonyms, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 63229 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Cerinomyces` under family `Cerinomycetaceae`.

The side-inventory merged-ID scan found `NCBITaxon:2079947` pointing into this taxon, but no retained retired row maps to this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 554582 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 63229 | Supported exactly: `attested rule: Cerinomyces tortus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 26486 | Supported exactly with three aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:2780975`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has three exact organism rows: `Go0401818` for `OMC1656`, and `Go0515938` and `Go0516834` for `OMC 1693`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; four projects join to those three exact GOLD organisms. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; one exact native analysis, `Cerinomyces tortus OMC1656`, joins to project `Gp0272388`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with isoneotype `H:7009710` and neotype `UPS:F-946515` rows on lines 121230-121231. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2780975`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:2780975`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2780975`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; side-inventory old ID `NCBITaxon:2079947` points into this taxon, but no retained retired row exists for the generator to carry into `replaces`. |

The aggregate GOLD row used for generation contributes three organism assertions. The local native GOLD snapshot supplies the same three exact organism IDs, four joined sequencing projects, and one joined native GOLD analysis row.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cerinomyces` parent, two exact synonyms, four related synonyms, and two type-material rows.
- The NCBI merged-ID side inventory has one old ID that is not present as a retained retired row, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of three.
- The local native GOLD snapshot supplies three exact organisms, four joined projects, and one joined analysis for this taxon.
- BacDive and StrainInfo do not supply exact local strain or overlay evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Cerinomyces tortus` as `SPECIES`, and the generated record follows the source rank exactly.

