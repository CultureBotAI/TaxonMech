# YAML Record Review: Casaregolazyma patagonica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/casaregolazyma_patagonica.yaml
- Started UTC: 2026-09-22T07:26:01Z
- Finished UTC: 2026-09-22T07:26:01Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:399783 |
| label | Casaregolazyma patagonica |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:3712543 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/casaregolazyma_patagonica.yaml`. It carries one NCBI exact synonym, four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, four NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*casaregolazyma_patagonica.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/casaregolazyma_patagonica.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/casaregolazyma_patagonica.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 85562 has `NCBITaxon:399783`, label `Casaregolazyma patagonica`, rank `SPECIES`, direct parent `NCBITaxon:3712543`, genetic code `1`, exact synonym `Candida patagonica`, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 55521 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Casaregolazyma` under family `Trichomonascaceae`.

`data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:546103` into this taxon, but the retained retired rows are empty; the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 85562 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55521 | Supported exactly: `attested rule: Casaregolazyma patagonica, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34430 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:399783`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0704955`, strain CBS 10443 under the source name `Candida patagonica CBS 10443`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with project `Gp0830971` for `Go0704955`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; no native analysis rows join to that project ID in the local snapshot. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with four holotype rows for CBS 10443 spelling variants. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `399783`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:399783`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:399783`. |
| Omitted `replaces` | Exact scan of retained retired rows plus side inventory for merged NCBI IDs | Supported; only the side inventory maps `NCBITaxon:546103` into `NCBITaxon:399783`, so no retained retired row is available for generated `replaces`. |

The local native GOLD snapshot has one exact organism, CBS 10443, with one joined project and no joined analysis rows. NCBI lists the CBS 10443 spelling variants as holotype material for this taxon.

The native StrainInfo snapshot has seven exact direct rows and nine exact deposit links under `NCBITaxon:399783`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Casaregolazyma` parent, one exact synonym, four related synonyms, and four type-material rows.
- NCBI has one side-inventory old ID for this taxon, but no retained retired rows to generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
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
- NCBI ranks `Casaregolazyma patagonica` as `SPECIES`, and the generated record follows the source rank exactly.
