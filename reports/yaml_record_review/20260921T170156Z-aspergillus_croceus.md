# YAML Record Review: Aspergillus croceus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_croceus.yaml
- Started UTC: 2026-09-21T17:00:48Z
- Finished UTC: 2026-09-21T17:01:56Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1695224 |
| label | Aspergillus croceus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_croceus.yaml`. It carries two NCBI related synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_croceus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_croceus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_croceus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 441488 has `NCBITaxon:1695224`, label `Aspergillus croceus`, rank `SPECIES`, direct parent `NCBITaxon:2720870`, genetic code `1`, related synonyms `Aspergillus croceus Hubka, A. Novakova , Frisvad, S.W. Peterson & M.Kolarik, 2016` and `Aspergillus sp. 3 VH-2015`, and source `gold`. `curation/seed_scope.tsv` line 61030 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the intervening `NCBITaxon:2720870` subgenus `Aspergillus subgen. Nidulantes`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:1695224`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 441488 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61030 | Supported exactly: `attested rule: Aspergillus croceus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 14633 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1695224`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 52990-52997 | Supported exactly with eight culture-from-holotype designations for `CBS 134396`, `CCF 4405`, `IBT 33602`, and `NRRL 62495`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1695224` or the reviewed NCBI type-material designations. |
| Empty StrainInfo overlay | Exact direct, deposit taxon, and exact quoted-designation scans of `data/straininfo/records.jsonl.gz` | Supported; no StrainInfo record asserted taxon ID `1695224` through its direct strain taxon or any deposit taxon. |

Native GOLD contains two exact organism rows for `CBS 134396` and `JS3-P1`; two linked sequencing-project rows; and one isolate genome analysis, `Ga0663005`, linked through `AP PROJECT GOLD IDS` for `JS3-P1`. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, two synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot has two organisms, two sequencing projects, and one project-linked analysis for this taxon; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- BacDive and StrainInfo do not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
