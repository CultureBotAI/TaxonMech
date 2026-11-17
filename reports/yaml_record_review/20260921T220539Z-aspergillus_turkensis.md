# YAML Record Review: Aspergillus turkensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_turkensis.yaml
- Started UTC: 2026-09-21T22:05:03Z
- Finished UTC: 2026-09-21T22:05:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:660492 |
| label | Aspergillus turkensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_turkensis.yaml`. It carries three related NCBI synonyms, no exact NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_turkensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_turkensis.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_turkensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 152898 has `NCBITaxon:660492`, label `Aspergillus turkensis`, rank `SPECIES`, direct parent `NCBITaxon:2720870`, genetic code `1`, three related synonyms, no exact synonyms, and source `gold`. `curation/seed_scope.tsv` line 56300 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Nidulantes`.

`data/raw/ncbi_merged_ids.tsv` redirects old ID `NCBITaxon:469267` into `NCBITaxon:660492`. `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 152898 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 56300 | Supported exactly: `attested rule: Aspergillus turkensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 40659 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:660492`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 16 culture-from-holotype rows: four variants each for ATCC 16799, CBS 504.65, IMI 135420, and NRRL 4993. |
| Empty native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported; no exact native GOLD organism, sequencing-project, or analysis row was filed under taxon ID `660492`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `660492`. |
| Empty native and generated StrainInfo surfaces | Exact scans of native and generated StrainInfo snapshots | Supported; no native or generated StrainInfo row mentions `NCBITaxon:660492`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:660492`. |

The checked-in native GOLD organism, sequencing-project, and analysis snapshots have no exact rows under NCBI taxon `660492`. The generated `source_attestations` GOLD count follows the aggregate `data/raw/gold_organisms.tsv` row instead.

Native StrainInfo has no direct strain rows or deposit-taxonomy hits under taxon `660492`, and the generated StrainInfo overlay files contain no rows for `NCBITaxon:660492`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus subgen. Nidulantes` parent, and the three related synonyms.
- NCBI has 16 type-material rows for this taxon; these rows are inventory evidence and do not by themselves imply a generated local strain entry.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has no exact organisms, sequencing projects, or genome analyses.
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
- NCBI ranks `Aspergillus turkensis` as `SPECIES`, and the generated record follows the source rank exactly.
