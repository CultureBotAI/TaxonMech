# YAML Record Review: Chionosphaera apobasidialis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/chionosphaera_apobasidialis.yaml
- Started UTC: 2026-09-22T08:48:35Z
- Finished UTC: 2026-09-22T08:48:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:54742 |
| label | Chionosphaera apobasidialis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:54741 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/chionosphaera_apobasidialis.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*chionosphaera_apobasidialis.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/chionosphaera_apobasidialis.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/chionosphaera_apobasidialis.yaml` exited successfully and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 6952 has `NCBITaxon:54742`, label `Chionosphaera apobasidialis`, rank `SPECIES`, direct parent `NCBITaxon:54741`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 52936 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Chionosphaera` under family `Chionosphaeraceae`.

The merged-ID scan found no old IDs pointing into this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 6952 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52936 | Supported exactly: `attested rule: Chionosphaera apobasidialis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 38477 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:54742`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has one exact organism row, `Go0111499` for `Chionosphaera apobasidialis 52639`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact projects `Gp0113487` and `Gp0113488` join to `Go0111499`. |
| Empty native GOLD analysis surface | Exact native GOLD analysis scan by project IDs | Supported; no native GOLD analysis rows join to exact projects `Gp0113487` or `Gp0113488`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with four CBS 7430 and IGC 5538 type-material rows on lines 232710-232713. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `54742`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:54742`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:54742`. |
| Omitted `replaces` | Exact scan of merged NCBI IDs | Supported; no old ID maps into this current taxon. |

The native StrainInfo snapshot has three exact direct rows and five exact deposit links under `NCBITaxon:54742`, but none overlays onto a BacDive-derived local strain inventory entry.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Chionosphaera` parent, one related synonym, and four type-material rows.
- The NCBI merged-ID side inventory has no old ID for this taxon, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, two joined projects, and no joined analysis rows for this taxon.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Chionosphaera apobasidialis` as `SPECIES`, and the generated record follows the source rank exactly.
