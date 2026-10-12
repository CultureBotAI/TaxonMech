# YAML Record Review: Aspergillus askiburgiensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_askiburgiensis.yaml
- Started UTC: 2026-09-21T15:52:00Z
- Finished UTC: 2026-09-21T15:58:07Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1695225 |
| label | Aspergillus askiburgiensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one species record at `data/taxa/eukaryota/aspergillus_askiburgiensis.yaml`. The reviewed file is a compact seeded record with no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_askiburgiensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_askiburgiensis.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_askiburgiensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 441489 has `NCBITaxon:1695225`, label `Aspergillus askiburgiensis`, rank `SPECIES`, parent `NCBITaxon:2720870`, genetic code `1`, source `gold`, and the two NCBI related synonyms generated into the record. `curation/seed_scope.tsv` line 61031 keeps this identifier in scope through the attested-source rule, so the `SEEDED` mapping status and `seed_from_sources` history entry are consistent with a generated exact NCBI record.

The root-first lineage in the YAML matches the NCBI inventory parent chain exactly:

`root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Eurotiales` -> `Aspergillaceae` -> `Aspergillus` -> `Aspergillus subgen. Nidulantes` -> `Aspergillus askiburgiensis`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and related synonyms | `data/raw/ncbitaxon_taxa.tsv` line 441489 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61031 | Supported exactly: `attested rule: Aspergillus askiburgiensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 14634 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1695225`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `1695225` and `NCBITaxon:1695225` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` for strain and deposit taxon IDs `1695225` and `NCBITaxon:1695225` | Supported; no direct or deposit-only StrainInfo rows were found. |

`data/raw/ncbi_type_material.tsv` has eight NCBI type-material rows for holotype culture designations `CBS 134374`, `CBS:134374`, `CCF 4716`, `CCF:4716`, `IBT 33114`, `IBT:33114`, `NRRL 62818`, and `NRRL:62818`. Exact quoted-token scans for those values found no matching BacDive or StrainInfo snapshot records, so `strain_count: 0` is consistent with the current strain evidence. These type-material rows are NCBI inventory evidence only; eukaryotic type material does not generate LPSN `nomenclature`.

## Completeness

The record is complete for the evidence currently present in local source inventories:

- NCBI supplies identity, lineage, genetic code, and two related synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- BacDive and StrainInfo do not supply any exact strain rows or exact holotype-token rows for this species.
- LPSN and GTDB do not contribute to this eukaryotic record.
- There are no causal graphs or curated evidence overlays to validate.

The local native GOLD snapshot under `data/gold/*.jsonl.gz` has no inspectable organism, sequencing-project, or analysis-project row for taxon ID `1695225`. This does not contradict the YAML because the generated taxon-level GOLD count is sourced from `data/raw/gold_organisms.tsv`, TaxonMech's aggregate KG-Microbe GOLD inventory.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The absence checks above used source-specific exhaustive scans of the relevant committed TSV and gzip JSONL snapshots rather than ignored-aware repository search.
- No source-native GOLD organism row was available locally for manual drill-down beyond the aggregate transformed count.
