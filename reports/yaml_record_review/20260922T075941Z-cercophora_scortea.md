# YAML Record Review: Cercophora scortea

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cercophora_scortea.yaml
- Started UTC: 2026-09-22T07:59:41Z
- Finished UTC: 2026-09-22T07:59:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:314031 |
| label | Cercophora scortea |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:42303 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/cercophora_scortea.yaml`. It carries one NCBI exact synonym, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cercophora_scortea.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cercophora_scortea.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cercophora_scortea.yaml data/taxa/eukaryota/cercophora_squamulosa.yaml data/taxa/eukaryota/cercospora_apii.yaml data/taxa/eukaryota/cercospora_beticola.yaml` scanned four files with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 64227 has `NCBITaxon:314031`, label `Cercophora scortea`, rank `SPECIES`, direct parent `NCBITaxon:42303`, genetic code `1`, exact synonym `Bombardia scortea`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 55148 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Cercophora` under family `Lasiosphaeriaceae`.

The bounded merged-ID scan found no old NCBI IDs that point into this taxon and no retained retired rows, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 64227 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55148 | Supported exactly: `attested rule: Cercophora scortea, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 31712 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:314031`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has exact organism `Go0358428` for `Cercophora scortea SMH4131-1`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact projects `Gp0197096` and `Gp0251473` both join to `Go0358428`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; exact analysis `Cercophora scortea SMH4131-1 Standard Draft` joins to project `Gp0197096`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material rows mention `NCBITaxon:314031`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `314031`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:314031`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:314031`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; no retained retired row or side-inventory merged ID points into `NCBITaxon:314031`. |

The aggregate GOLD row used for generation contributes one organism assertion, matching the one exact organism row in the local native GOLD snapshot. That organism joins to one native GOLD genome project and one transcriptome project.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cercophora` parent, one exact synonym, two related synonyms, and no type-material rows.
- NCBI has no side-inventory old IDs or retained retired rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, two joined projects, and one joined analysis for this taxon.
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
- NCBI ranks `Cercophora scortea` as `SPECIES`, and the generated record follows the source rank exactly.
