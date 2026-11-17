# YAML Record Review: Chroomonas dispersa

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/chroomonas_dispersa.yaml
- Started UTC: 2026-09-22T09:04:20Z
- Finished UTC: 2026-09-22T09:04:20Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:356657 |
| label | Chroomonas dispersa |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:3028 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic cryptomonad species at `data/taxa/eukaryota/chroomonas_dispersa.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*chroomonas_dispersa.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/chroomonas_dispersa.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/chroomonas_dispersa.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 73551 has `NCBITaxon:356657`, label `Chroomonas dispersa`, rank `SPECIES`, direct parent `NCBITaxon:3028`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 55336 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Chroomonas` under family `Chroomonadaceae`.

The merged-ID scan found no old IDs pointing into this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 73551 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55336 | Supported exactly: `attested rule: Chroomonas dispersa, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 33099 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:356657`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has one exact organism row, `Go0583109` for `Chroomonas dispersa NIES 704`. |
| Empty native GOLD project and analysis surfaces | Exact native GOLD scans by organism ID and empty project-ID set | Supported; no native GOLD project rows join to `Go0583109`, so no analysis rows can join through exact project IDs. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported with one exact direct StrainInfo record and two exact deposit-taxonomy matches under taxon ID `356657`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz`, `data/raw/bacdive_strains.tsv`, and raw generated-strain inputs | Supported; no BacDive record, raw BacDive-derived strain row, or raw generated-strain row was filed under taxon ID `356657`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:356657`. |
| Empty type-material and auxiliary source surfaces | Exact scans of `data/raw/ncbi_type_material.tsv` plus the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no type-material or auxiliary source row mentions `NCBITaxon:356657`. |
| Omitted `replaces` | Exact scan of merged NCBI IDs | Supported; no old ID maps into this current taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Chroomonas` parent, and one related synonym.
- The NCBI merged-ID side inventory has no old ID for this taxon, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism and no joined project or analysis rows for this taxon.
- Native StrainInfo has exact rows for this taxon, but there are no local BacDive-derived strain records or generated StrainInfo overlay rows under `NCBITaxon:356657`.
- BacDive, type-material, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Chroomonas dispersa` as `SPECIES`, and the generated record follows the source rank exactly.
- Native StrainInfo has one exact direct entry, `siID` 357153, with `NIES-704` and `CCAP 978/10` deposits; no local generated StrainInfo assembly, exclusion, or related-record row is derived from it in the current maintained overlay tables.
