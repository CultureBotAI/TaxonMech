# YAML Record Review: Aspergillus asperescens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_asperescens.yaml
- Started UTC: 2026-09-21T15:58:12Z
- Finished UTC: 2026-09-21T15:59:12Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:176163 |
| label | Aspergillus asperescens |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_asperescens.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and NCBITAXON plus GOLD source attestations.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_asperescens.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Ignored report search | Pass; `rg --no-ignore --hidden -n "aspergillus_asperescens\|NCBITaxon:176163" reports/yaml_record_review -g '*'` returned no prior report references. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_asperescens.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_asperescens.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 35682 has `NCBITaxon:176163`, label `Aspergillus asperescens`, rank `SPECIES`, parent `NCBITaxon:2720870`, genetic code `1`, source `gold`, and NCBI related synonym `Aspergillus asperescens Stolk, 1954`. `curation/seed_scope.tsv` line 54291 keeps the taxon in scope through the attested-source rule, consistent with the `SEEDED` status and the `seed_from_sources` history event.

The YAML lineage matches the NCBI inventory parent chain exactly, from `root` through `Eukaryota`, `Fungi`, `Ascomycota`, `Eurotiales`, `Aspergillaceae`, `Aspergillus`, and `Aspergillus subgen. Nidulantes` to `Aspergillus asperescens`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the current record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 35682 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54291 | Supported exactly: `attested rule: Aspergillus asperescens, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 15328 and native `data/gold/organisms.jsonl.gz` rows 455337-455344 | Supported; the aggregate count is eight and the pinned native GOLD projection has eight matching organism rows for `NCBITaxon:176163`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `176163` and `NCBITaxon:176163` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` and `data/straininfo/exclusions.tsv` | Supported; eleven direct NCBI-taxonomy StrainInfo records exist, and every one is excluded with `no_eligible_own_deposit_match`. |

`data/raw/ncbi_type_material.tsv` has twelve NCBI type-material rows for `CBS 110.51`, `ATCC 11079`, `DSM 871`, `IMI 046813`, `NRRL 4770`, `QM 1946`, and their colon-separated variants. Exact quoted-token scans found no BacDive hits and one StrainInfo hit, `straininfo.strain:264542`, which is excluded with `no_eligible_own_deposit_match`. The absence of generated `nomenclature` is expected because TaxonMech only generates that section from LPSN rows.

## Completeness

The record is complete for the committed inventory evidence now available:

- NCBI supplies the identity, lineage, genetic code, and related synonym.
- GOLD supplies a taxon-level organism count of eight.
- Native GOLD has eight organism rows but no sequencing-project or analysis-project rows linked to those organisms, so it does not supply strain-level related records or genomes.
- BacDive has no exact records for this taxon.
- StrainInfo rows for this NCBI taxon are intentionally absent from the YAML because none reached the eligible own-deposit join.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The StrainInfo and BacDive absence checks above exhaustively scanned the relevant committed gzip JSONL snapshots by exact NCBI taxon ID and exact quoted type-material tokens.
- The native GOLD organism rows are organism-only in the local snapshot; there is no linked native GOLD project or analysis evidence to evaluate.
