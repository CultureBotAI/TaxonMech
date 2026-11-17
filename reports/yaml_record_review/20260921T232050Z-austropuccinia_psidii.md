# YAML Record Review: Austropuccinia psidii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/austropuccinia_psidii.yaml
- Started UTC: 2026-09-21T23:19:41Z
- Finished UTC: 2026-09-21T23:20:50Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:181123 |
| label | Austropuccinia psidii |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2234120 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic rust fungal species at `data/taxa/eukaryota/austropuccinia_psidii.yaml`. It carries one exact NCBI synonym, two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*austropuccinia_psidii.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/austropuccinia_psidii.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/austropuccinia_psidii.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 36362 has `NCBITaxon:181123`, label `Austropuccinia psidii`, rank `SPECIES`, direct parent `NCBITaxon:2234120`, genetic code `1`, one exact synonym, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 54350 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Austropuccinia` under family `Sphaerophragmiaceae`.

`data/raw/ncbi_merged_ids.tsv` line 79361 maps old identifier `NCBITaxon:462779` into `NCBITaxon:181123`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at this current taxon. The generated record therefore correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 36362 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54350 | Supported exactly: `attested rule: Austropuccinia psidii, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 16028 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:181123`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with `Go0139611` for strain `Aus_3` on line 79566 and `Go0678516` for strain `Au3-C622-A115012` on line 503147. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with projects `Gp0144693`, `Gp0460953`, and `Gp0780475` on lines 90836, 328937, and 579512. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with two analysis rows joining through projects `Gp0144693` and `Gp0780475`. |
| NCBI merged-ID evidence | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported; old identifier `NCBITaxon:462779` maps into `NCBITaxon:181123` but is not retained as a retired taxon row, so it is not emitted as `replaces`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows mention `NCBITaxon:181123`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `181123`. |
| Empty native StrainInfo surface | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has no direct records or deposit-taxonomy hits under `181123`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:181123`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:181123`. |

The local native GOLD snapshot has two exact organisms with three joined projects and two joined analysis rows. Project `Gp0460953` is present for `Go0139611` without a matching analysis row in the local snapshot, and none of the GOLD rows create a local `strains` entry in this generated eukaryotic taxon record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Austropuccinia` parent, one exact synonym, and two related synonyms.
- NCBI supplies one merged-ID row, but no retained retired row that should become `replaces`.
- NCBI does not supply type-material rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot supplies two exact organisms with three projects and two joined analysis rows.
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
- NCBI ranks `Austropuccinia psidii` as `SPECIES`, and the generated record follows the source rank exactly.
