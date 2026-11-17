# YAML Record Review: Cenococcum geophilum 1.58

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cenococcum_geophilum_1_58.yaml
- Started UTC: 2026-09-22T07:30:26Z
- Finished UTC: 2026-09-22T07:30:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:794803 |
| label | Cenococcum geophilum 1.58 |
| rank | STRAIN |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5570 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal strain at `data/taxa/eukaryota/cenococcum_geophilum_1_58.yaml`. It carries no NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cenococcum_geophilum_1_58.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cenococcum_geophilum_1_58.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cenococcum_geophilum_1_58.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 179087 has `NCBITaxon:794803`, label `Cenococcum geophilum 1.58`, rank `STRAIN`, direct parent `NCBITaxon:5570`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 56703 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent species `Cenococcum geophilum`.

`data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:1395199` into this taxon, but the retained retired rows are empty; the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, and genetic code | `data/raw/ncbitaxon_taxa.tsv` line 179087 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 56703 | Supported exactly: `attested rule: Cenococcum geophilum 1.58, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation count | `data/raw/gold_organisms.tsv` line 42786 | Mechanically supported with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:794803`, but the native GOLD row behind that taxon ID has the organism name `Postia placenta MAD-698-R-SB12`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Mismatched; the only exact native row is `Go0017842`, named `Postia placenta MAD-698-R-SB12`, not `Cenococcum geophilum 1.58`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Mismatched in the same way; project `Gp0017842` is also named `Postia placenta MAD-698-R-SB12`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Mismatched in the same way; two analysis rows join through `Gp0017842` and are both named `Postia placenta MAD-698-R-SB12`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material rows mention `NCBITaxon:794803`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `794803`. |
| Empty StrainInfo surface | Exact scans of native StrainInfo rows plus generated StrainInfo TSVs | Supported; no native or generated StrainInfo rows mention `NCBITaxon:794803`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:794803`. |
| Omitted `replaces` | Exact scan of retained retired rows plus side inventory for merged NCBI IDs | Supported; only the side inventory maps `NCBITaxon:1395199` into `NCBITaxon:794803`, so no retained retired row is available for generated `replaces`. |

The NCBI strain identity, parentage, and lineage are internally consistent. The GOLD side is suspicious: all exact native GOLD rows joined from the aggregate taxon ID are labeled as `Postia placenta MAD-698-R-SB12`, an unrelated organism name for a record that is otherwise `Cenococcum geophilum 1.58`.

## Completeness

The NCBI-derived portions are complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cenococcum geophilum` parent, no synonyms, and no type-material rows.
- NCBI has one side-inventory old ID for this taxon, but no retained retired rows to generate `replaces`.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

The GOLD attestation is incomplete until the `Go0017842` source mapping is audited, because its organism, project, and analysis names all describe `Postia placenta MAD-698-R-SB12` while the GOLD row is filed under `NCBITaxon:794803`.

## Findings

| Severity | Finding | Owner |
|---|---|---|
| major | The GOLD organism assertion for `NCBITaxon:794803` appears to be a cross-taxon source mapping. `data/raw/gold_organisms.tsv` line 42786 counts one GOLD organism for `Cenococcum geophilum 1.58`, but the native exact row is `Go0017842` named `Postia placenta MAD-698-R-SB12`, and its joined project plus two analyses carry the same `Postia placenta` name. | GOLD extraction/upstream mapping that produces `data/raw/gold_organisms.tsv` |

## Recommended Edits

Audit native GOLD organism `Go0017842` before using it as support for `NCBITaxon:794803`. If GOLD has the wrong NCBI taxon ID, correct the GOLD extraction or add a guard so `data/raw/gold_organisms.tsv` stops counting it for `Cenococcum geophilum 1.58`, then regenerate `data/raw/gold_organisms.tsv` and the generated taxon record.

## Follow-up Checks

- Re-run the exact native GOLD organism, project, and analysis scans for `NCBITaxon:794803` to confirm that no `Postia placenta MAD-698-R-SB12` rows remain joined to this strain.
- Re-run `just validate data/taxa/eukaryota/cenococcum_geophilum_1_58.yaml` and `just validate-strict data/taxa/eukaryota/cenococcum_geophilum_1_58.yaml`.
- Re-run `just verify-corpus` after regenerating the source aggregate and YAML corpus.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Cenococcum geophilum 1.58` as `STRAIN`, and the generated record follows the source rank exactly.
