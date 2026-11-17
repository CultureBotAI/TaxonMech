# YAML Record Review: Aspergillus violaceus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_violaceus.yaml
- Started UTC: 2026-09-21T22:18:22Z
- Finished UTC: 2026-09-21T22:19:25Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41738 |
| label | Aspergillus violaceus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_violaceus.yaml`. It carries two exact NCBI synonyms, one related NCBI synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_violaceus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_violaceus.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_violaceus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4872 has `NCBITaxon:41738`, label `Aspergillus violaceus`, rank `SPECIES`, direct parent `NCBITaxon:2720870`, genetic code `1`, two exact synonyms, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 52484 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Nidulantes`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4872 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52484 | Supported exactly: `attested rule: Aspergillus violaceus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34933 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:41738`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` lines 206982-206991 | Supported exactly with 10 rows: four culture-from-neotype rows, two culture-from-type-material rows, two lectotype rows, and two type-material rows. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism and three sequencing projects; no matching native GOLD analysis row is present in the local snapshot. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `41738`. |
| Native StrainInfo exact hits | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has five direct records and 24 deposit-taxonomy hits under `41738`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:41738`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:41738`. |

The local native GOLD snapshot has an exact organism row for `Aspergillus violaceus CBS 138.55` with `ORGANISM GOLD ID` `Go0446076` on line 304879. It joins to sequencing projects `Gp0312173`, `Gp0317280`, and `Gp0397222` on lines 211415, 216455, and 283797; no native analysis row joins back to those projects in the local snapshot.

Native StrainInfo has five direct strain rows and 24 deposit-taxonomy hits under taxon `41738`. Those native StrainInfo hits do not create generated overlay rows because StrainInfo overlays only BacDive-derived local strain entries, and there is no exact BacDive-derived local strain for this NCBI taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus subgen. Nidulantes` parent, two exact synonyms, and one related synonym.
- NCBI has 10 type-material rows for this taxon; these rows are inventory evidence and do not by themselves imply a generated local strain entry.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism and three linked sequencing projects.
- BacDive does not supply exact local strain evidence for this taxon, and the native StrainInfo exact hits have no BacDive-derived local strain to overlay.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Aspergillus violaceus` as `SPECIES`, and the generated record follows the source rank exactly.
