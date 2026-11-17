# YAML Record Review: Caloboletus calopus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/caloboletus_calopus.yaml
- Started UTC: 2026-09-22T03:38:35Z
- Finished UTC: 2026-09-22T03:38:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:141855 |
| label | Caloboletus calopus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:1573176 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/caloboletus_calopus.yaml`. It carries two NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*caloboletus_calopus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/caloboletus_calopus.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/caloboletus_calopus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 28673 has `NCBITaxon:141855`, label `Caloboletus calopus`, rank `SPECIES`, direct parent `NCBITaxon:1573176`, genetic code `1`, exact synonyms `Boletaceae sp. KZ-2014a` and `Boletus calopus`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 54015 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Caloboletus` under subfamily `Boletoideae`.

`data/raw/ncbi_merged_ids.tsv` line 19448 records side-inventory old ID `NCBITaxon:1542316` merged into `NCBITaxon:141855`, but the retained NCBI row for this generated record is current and has no `retired_into` value. The record correctly omits `replaces`, which is generated only from retained retired rows.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 28673 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54015 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 10082 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:141855`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0518042` for `Caloboletus calopus MG23` at line 364066. |
| Native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported exactly by project `Gp0442111` for `Go0518042`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly by one analysis row joined through project `Gp0442111`. |
| NCBI merged-ID side inventory | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported exactly with old ID `NCBITaxon:1542316` pointing to the current taxon. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material row mentions `NCBITaxon:141855`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `141855`. |
| Empty StrainInfo taxon surface | Exact native StrainInfo taxon scans plus generated overlay scans | Supported; no native direct/deposit hit or generated StrainInfo overlay row mentions `NCBITaxon:141855`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:141855`. |

The committed aggregate GOLD row is mirrored by one exact native GOLD organism, one native project row, and one analysis row joined through that project.

The side-inventory old NCBI taxon ID does not require a `replaces` entry because no retained retired row points at the current ID.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Caloboletus` parent, two exact synonyms, and two related synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, one project row, and one joined analysis row.
- BacDive and StrainInfo do not supply exact local strain or overlay evidence for this taxon.
- NCBI type-material, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The side-inventory NCBI merge row for `NCBITaxon:1542316` does not require a YAML `replaces` entry without a retained retired source row.
- Exact local native GOLD scans recovered one organism row, one project row, and one analysis row for `NCBITaxon:141855`.
- GOLD analysis evidence joins through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Caloboletus calopus` as `SPECIES`, and the generated record follows the source rank exactly.
