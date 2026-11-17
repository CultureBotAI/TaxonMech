# YAML Record Review: Balamuthia mandrillaris

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/balamuthia_mandrillaris.yaml
- Started UTC: 2026-09-21T23:43:28Z
- Finished UTC: 2026-09-21T23:44:31Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:66527 |
| label | Balamuthia mandrillaris |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:66526 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic amoebozoan species at `data/taxa/eukaryota/balamuthia_mandrillaris.yaml`. It carries no NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*balamuthia_mandrillaris.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/balamuthia_mandrillaris.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/balamuthia_mandrillaris.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 8698 has `NCBITaxon:66527`, label `Balamuthia mandrillaris`, rank `SPECIES`, direct parent `NCBITaxon:66526`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 53137 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Balamuthia` under family `Balamuthiidae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 8698 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53137 | Supported exactly: `attested rule: Balamuthia mandrillaris, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 40782 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:66527`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with two native organisms: `Go0117369` and `Go0117437`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with two projects, `Gp0122306` and `Gp0122376`, across the two organism IDs above. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with two analysis rows joining through the two project IDs above. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no exact type-material row was filed under `NCBITaxon:66527`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `66527`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:66527`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:66527`. |

The local native GOLD snapshot has two exact organisms, strains CDC-V039 and 2046, with two joined projects and two joined analyses.

The native StrainInfo snapshot has one exact direct row under `NCBITaxon:66527` with one type deposit, ATCC 50209. It does not overlay onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and the direct `Balamuthia` parent.
- NCBI does not supply synonyms, merged-ID rows, or type-material rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot supplies two exact organisms with two projects and two joined analyses.
- BacDive does not supply exact local strain evidence for this taxon, and the one exact native StrainInfo row correctly has no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Balamuthia mandrillaris` as `SPECIES`, and the generated record follows the source rank exactly.
