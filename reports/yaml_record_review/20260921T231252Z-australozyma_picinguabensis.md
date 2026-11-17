# YAML Record Review: Australozyma picinguabensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/australozyma_picinguabensis.yaml
- Started UTC: 2026-09-21T23:11:39Z
- Finished UTC: 2026-09-21T23:12:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:291308 |
| label | Australozyma picinguabensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:3300567 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic yeast species at `data/taxa/eukaryota/australozyma_picinguabensis.yaml`. It carries one exact NCBI synonym, two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*australozyma_picinguabensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/australozyma_picinguabensis.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/australozyma_picinguabensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 59436 has `NCBITaxon:291308`, label `Australozyma picinguabensis`, rank `SPECIES`, direct parent `NCBITaxon:3300567`, genetic code `12`, one exact synonym, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 55019 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Australozyma` under family `Metschnikowiaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 59436 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55019 | Supported exactly: `attested rule: Australozyma picinguabensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 28543 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:291308`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with `Go0705500` for strain `NRRL Y-27814` on line 525946. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with project `Gp0831543` on line 610098. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis row joins to organism `Go0705500` or project `Gp0831543` in the local snapshot. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with nine `culture from holotype` rows on lines 140434-140442, all under synonym name `Candida picinguabensis`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `291308`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:291308`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:291308`. |

The NCBI type-material inventory contributes spelling variants for CBS 9999, NRRL Y-27814, and UNESP 00-89. The local native GOLD snapshot has the matching NRRL Y-27814 organism and one project, without a joined analysis row.

The native StrainInfo snapshot has five exact direct rows and six exact deposit-taxonomy rows under `NCBITaxon:291308`, including CBS 9999 and NRRL Y-27814 deposits. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Australozyma` parent, one exact synonym, two related synonyms, and nine type-material rows.
- NCBI does not supply merged-ID rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one project and no joined analysis row.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Australozyma picinguabensis` as `SPECIES`, and the generated record follows the source rank exactly.
