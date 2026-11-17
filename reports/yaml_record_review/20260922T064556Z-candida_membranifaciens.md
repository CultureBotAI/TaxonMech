# YAML Record Review: Yamadazyma membranifaciens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/candida_membranifaciens.yaml
- Started UTC: 2026-09-22T06:45:56Z
- Finished UTC: 2026-09-22T06:45:56Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:45567 |
| label | Yamadazyma membranifaciens |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:766765 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/candida_membranifaciens.yaml`. It carries two NCBI exact synonyms, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*candida_membranifaciens.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/candida_membranifaciens.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/candida_membranifaciens.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 5616 has `NCBITaxon:45567`, label `Yamadazyma membranifaciens`, rank `SPECIES`, direct parent `NCBITaxon:766765`, genetic code `12`, two exact synonyms, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52662 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Yamadazyma` under family `Debaryomycetaceae`.

`data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:297796` into this taxon, but the retained retired rows are empty; the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 5616 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52662 | Supported exactly: `attested rule: [Candida] membranifaciens, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 36071 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:45567`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0705371`, strain NRRL Y-2089 under the source name `Candida membranifaciens NRRL Y-2089`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with one project, `Gp0831412`, for `Go0705371`. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no local native GOLD analysis row joins to this taxon. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 24 rows on lines 215378-215401. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `45567`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:45567`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:45567`. |
| Omitted `replaces` | Exact scan of retained retired rows plus side inventory for merged NCBI IDs | Supported; only the side inventory maps `NCBITaxon:297796` into `NCBITaxon:45567`, so no retained retired row is available for generated `replaces`. |

The NCBI type-material inventory contributes two `culture from type material` rows for MUCL 29859 and 22 `type material` rows under the source taxon name `Candida melibiosi var. membranifaciens` for AS 2.2499, ATCC 42267, BCRC 22398, CBS 1952, CCRC 22398, CGMCC 2.2499, DBVPG 6145, IFO 1246, JCM 9450, NRRL Y-2089, and VKM Y-1510 spelling variants. The local native GOLD snapshot has one exact organism, NRRL Y-2089, with one joined project and no joined analysis rows.

The native StrainInfo snapshot has 26 exact direct rows and 49 exact deposit links under `NCBITaxon:45567`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `12`, the direct `Yamadazyma` parent, two exact synonyms, three related synonyms, and 24 type-material rows.
- NCBI has one side-inventory old ID for this taxon, but no retained retired rows to generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot supplies one exact organism with one project and no joined analyses.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Yamadazyma membranifaciens` as `SPECIES`, and the generated record follows the source rank exactly.
