# YAML Record Review: Calonectria leucothoes

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/calonectria_leucothoes.yaml
- Started UTC: 2026-09-22T03:48:34Z
- Finished UTC: 2026-09-22T03:48:34Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:149392 |
| label | Calonectria leucothoes |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2779502 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/calonectria_leucothoes.yaml`. It carries two NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*calonectria_leucothoes.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/calonectria_leucothoes.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/calonectria_leucothoes.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 30576 has `NCBITaxon:149392`, label `Calonectria leucothoes`, rank `SPECIES`, direct parent `NCBITaxon:2779502`, genetic code `1`, two exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 54061 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Calonectria mexicana species complex` under genus `Calonectria`.

The NCBI merged-ID side inventory maps old ID `NCBITaxon:149393` to `NCBITaxon:149392`, but the retained retired-row inventory is empty for this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 30576 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54061 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 11629 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:149392`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0384621` for `Calonectria leucothoes CBS 109166` at line 280027. |
| Native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported exactly by project `Gp0235732` for `Go0384621`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly by one analysis row joined through project `Gp0235732`. |
| NCBI merged-ID side inventory | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported exactly with old ID `NCBITaxon:149393` pointing at `NCBITaxon:149392`. |
| Empty retained retired-row inventory | Exact retained retired-row scan | Supported; no retained retired row points at `NCBITaxon:149392`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with six type-material rows for `Calonectria leucothoes`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `149392`. |
| Native StrainInfo exact taxon evidence | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has two deposit-taxonomy hits and two direct records under `149392`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:149392`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:149392`. |

The committed aggregate GOLD row is mirrored by one exact native GOLD organism, one native project row, and one analysis row joined through that project.

Native StrainInfo has exact taxon rows under `149392`, but the generated StrainInfo overlay correctly remains empty because no BacDive-derived local strain inventory entry joins those rows.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Calonectria mexicana species complex` parent, two exact synonyms, two related synonyms, and six type-material rows.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, one project row, and one joined analysis row.
- Native StrainInfo has exact rows under this taxon, but no BacDive-derived local strain inventory entry turns them into generated `data/straininfo/` overlay rows.
- BacDive does not supply exact local strain evidence for this taxon.
- The NCBI merged-ID side inventory has one old ID, but no retained retired row contributes a generated `replaces` value.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The NCBI type-material count exceeded the bounded scan sample, so this review also used an exact `rg -n '^NCBITaxon:149392\t' data/raw/ncbi_type_material.tsv` scan to recover all six rows.
- Exact local native GOLD scans recovered one organism row, one project row, and one analysis row for `NCBITaxon:149392`.
- GOLD analysis evidence joins through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- StrainInfo exact taxon rows do not generate overlay rows unless they join to the BacDive-derived local strain inventory.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Calonectria leucothoes` as `SPECIES`, and the generated record follows the source rank exactly.
