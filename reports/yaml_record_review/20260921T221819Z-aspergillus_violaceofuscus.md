# YAML Record Review: Aspergillus violaceofuscus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_violaceofuscus.yaml
- Started UTC: 2026-09-21T22:17:18Z
- Finished UTC: 2026-09-21T22:18:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:657443 |
| label | Aspergillus violaceofuscus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5052 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_violaceofuscus.yaml`. It carries one related NCBI synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_violaceofuscus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_violaceofuscus.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_violaceofuscus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 152104 has `NCBITaxon:657443`, label `Aspergillus violaceofuscus`, rank `SPECIES`, direct parent `NCBITaxon:5052`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 56286 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus`. NCBI does not place this taxon under an `Aspergillus` subgenus in the committed inventory, and the generated 15-node lineage correctly follows the direct genus parent.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 152104 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 56286 | Supported exactly: `attested rule: Aspergillus violaceofuscus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 40597 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:657443`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` lines 246081-246082 | Supported exactly with two neotype rows for CBS `123.27`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism and two sequencing projects; no matching native GOLD analysis row is present in the local snapshot. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `657443`. |
| Native StrainInfo exact hits | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has four direct records and eight deposit-taxonomy hits under `657443`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:657443`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:657443`. |

The local native GOLD snapshot has an exact organism row for `Aspergillus violaceofuscus CBS 115571` with `ORGANISM GOLD ID` `Go0047313` on line 38664. It joins to sequencing projects `Gp0047313` and `Gp0047314` on lines 32500-32501; no native analysis row joins back to those projects in the local snapshot.

Native StrainInfo has four direct strain rows and eight deposit-taxonomy hits under taxon `657443`. Those native StrainInfo hits do not create generated overlay rows because StrainInfo overlays only BacDive-derived local strain entries, and there is no exact BacDive-derived local strain for this NCBI taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus` parent, and one related synonym.
- NCBI has two type-material rows for this taxon; these rows are inventory evidence and do not by themselves imply a generated local strain entry.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism and two linked sequencing projects.
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
- NCBI ranks `Aspergillus violaceofuscus` as `SPECIES`, and the generated record follows the source rank exactly.
