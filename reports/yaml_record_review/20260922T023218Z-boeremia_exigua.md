# YAML Record Review: Boeremia exigua

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/boeremia_exigua.yaml
- Started UTC: 2026-09-22T02:32:18Z
- Finished UTC: 2026-09-22T02:32:18Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:749465 |
| label | Boeremia exigua |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:749461 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/boeremia_exigua.yaml`. It carries one NCBI exact synonym, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*boeremia_exigua.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/boeremia_exigua.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/boeremia_exigua.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 173218 has `NCBITaxon:749465`, label `Boeremia exigua`, rank `SPECIES`, direct parent `NCBITaxon:749461`, genetic code `1`, one exact synonym, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 56635 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Boeremia` under family `Didymellaceae`.

The side merged-ID inventory maps `NCBITaxon:73000` into this taxon, but no committed retained retired-row evidence points at it, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 173218 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 56635 | Supported exactly: `attested rule: Boeremia exigua, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 42276 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:749465`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with two native organisms, `Go0358419` and `Go0383100`, both for strain MPI-SDFR-AT-0100. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with two joined projects, `Gp0197087` and `Gp0224132`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with one analysis, `Boeremia exigua MPI-SDFR-AT-0100 Standard Draft`, joined through `Gp0224132`. |
| NCBI merged-ID side inventory | Exact `data/raw/ncbi_merged_ids.tsv` scan | Supported; old ID `NCBITaxon:73000` merges into `NCBITaxon:749465`, but it is not a retained retired row and therefore does not generate `replaces`. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported exactly with 133 direct records and 141 deposit-taxonomy hits under `749465`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:749465`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material row mentions `NCBITaxon:749465`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `749465`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:749465`. |

The local native GOLD snapshot has two exact organisms, two joined projects, and one analysis joined through a project ID.

The native StrainInfo snapshot has exact rows for this taxon, but the generated StrainInfo overlay surface is empty because this taxon has no BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Boeremia` parent, one exact synonym, and two related synonyms.
- NCBI supplies one side-inventory old ID in `data/raw/ncbi_merged_ids.tsv`, but no retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot supplies two exact organisms, two joined projects, and one project-joined analysis.
- StrainInfo supplies native exact rows, but no generated overlay rows, and BacDive does not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- Native GOLD analysis rows can join by project ID as well as organism ID; the MPI-SDFR-AT-0100 analysis is recovered through `AP PROJECT GOLD IDS`, so it does not require a direct `AP ORGANISM GOLD ID`.
- Native StrainInfo rows alone do not increase `strain_count`; only local BacDive-derived strain records participate in the generated strain surface.
- NCBI ranks `Boeremia exigua` as `SPECIES`, and the generated record follows the source rank exactly.
