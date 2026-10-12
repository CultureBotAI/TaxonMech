# YAML Record Review: Cladophialophora carrionii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cladophialophora_carrionii.yaml
- Started UTC: 2026-09-22T10:05:05Z
- Finished UTC: 2026-09-22T10:05:05Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:86049 |
| label | Cladophialophora carrionii |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:82105 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/cladophialophora_carrionii.yaml`. It carries one NCBI exact synonym, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cladophialophora_carrionii.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cladophialophora_carrionii.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cladophialophora_carrionii.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already passed on the current checkout. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 13310 has `NCBITaxon:86049`, label `Cladophialophora carrionii`, rank `SPECIES`, direct parent `NCBITaxon:82105`, genetic code `1`, exact synonym `Cladosporium carrionii`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53434 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Cladophialophora` under family `Herpotrichiellaceae`.

The side-inventory merged-ID scan found `NCBITaxon:470696` and `NCBITaxon:91944` pointing into this taxon, but no retained retired rows map to this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 13310 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53434 | Supported exactly: `attested rule: Cladophialophora carrionii, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 43358 | Supported exactly with one aggregate GOLD organism assertion for `NCBITaxon:86049`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has one exact organism row, `Go0355339` for `Cladophialophora carrionii KSF`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact project `Gp0189602` joins to `Go0355339`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by joined project IDs | Supported; one native GOLD analysis row joins through project `Gp0189602` and names `Cladophialophora carrionii KSF`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with two `CBS 160.54` culture-from-type-material spelling variants on lines 268565-268566, both under the synonym `Cladosporium carrionii`. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported with 51 exact direct StrainInfo records and 64 exact deposit-taxonomy matches under taxon ID `86049`. |
| Empty final BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz`, `data/raw/bacdive_strains.tsv`, and raw generated-strain inputs | Supported; no BacDive record, raw BacDive-derived strain row, or final raw generated-strain row was filed under taxon ID `86049`. |
| Intermediate StrainInfo overlay surface | Exact scans of `data/straininfo/strain_links.tsv` and `data/straininfo/related_records.tsv.gz` | Partially problematic; line 59550 links `straininfo.deposit:236459` to `kgmicrobe.strain:bacdive_16034` under `NCBITaxon:86049`, while the exact raw BacDive-derived row for `kgmicrobe.strain:bacdive_16034` is `Streptomyces tanashiensis` under `NCBITaxon:67367`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:86049`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; side-inventory old IDs `NCBITaxon:470696` and `NCBITaxon:91944` point into this taxon, but no retained retired row exists for the generator to carry into `replaces`. |

## Completeness

The record is complete for the committed source evidence that reaches final `data/raw/` strain inventories:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cladophialophora` parent, one exact synonym, two related synonyms, and two type-material rows.
- The NCBI merged-ID side inventory has two old IDs that are not present as retained retired rows, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, one joined project, and one joined analysis row for this taxon.
- Native StrainInfo has exact rows for this taxon, but there are no final local BacDive-derived strain records or final raw StrainInfo rows under `NCBITaxon:86049`.
- BacDive, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current final inventories.

## Findings

| Severity | Finding | Owner |
|---|---|---|
| minor | `data/straininfo/strain_links.tsv` line 59550 links fungal deposit `CBS 165.54` under `NCBITaxon:86049` to bacterial `kgmicrobe.strain:bacdive_16034`. That produces four intermediate `NCBITaxon:86049` rows in `data/straininfo/related_records.tsv.gz` even though `data/raw/bacdive_strains.tsv` line 15858 assigns `kgmicrobe.strain:bacdive_16034` to `NCBITaxon:67367`; final raw strain tables filter those rows away, so the reviewed YAML has no incorrect strain or related-record claim. | `scripts/straininfo.py` / the generated StrainInfo overlay in `data/straininfo/` |

## Recommended Edits

1. Add a StrainInfo matching guard or source exclusion so `straininfo.deposit:236459` / `CBS 165.54` is not linked to `bacdive:16034`, then rerun `just straininfo-index --apply`.

## Follow-up Checks

- Rerun exact `rg --no-ignore --hidden` or `gzip -dc ... | rg` scans for `NCBITaxon:86049` and `straininfo.deposit:236459` in `data/straininfo/strain_links.tsv` and `data/straininfo/related_records.tsv.gz`; the false `kgmicrobe.strain:bacdive_16034` rows should be gone.
- Rerun `just seed-canary NCBITaxon:86049` and confirm `data/taxa/eukaryota/cladophialophora_carrionii.yaml` remains free of BacDive-derived strains unless a valid fungal local strain is introduced.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- An `rg --no-ignore --hidden` check over `data/raw`, `data/straininfo`, `data/bacdive`, and `curation/seed_scope.tsv` included ignored files while tracing the intermediate StrainInfo rows and the exact final raw strain rows for `kgmicrobe.strain:bacdive_16034`.
- NCBI ranks `Cladophialophora carrionii` as `SPECIES`, and the generated record follows the source rank exactly.
