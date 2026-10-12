# YAML Record Review: Abyssiniarchaeum dallolvicinus (SeqCode)

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/abyssiniarchaeum_dallolvicinus_seqcode.yaml
- Started UTC: 2026-09-22T06:29:20Z
- Finished UTC: 2026-09-22T06:30:40Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:3879924 |
| label | Abyssiniarchaeum dallolvicinus (SeqCode) |
| rank | SPECIES |
| taxon_domain | ARCHAEA |
| parent_taxon | NCBITaxon:3879921 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a compact generated archaeal species record at `data/taxa/archaea/abyssiniarchaeum_dallolvicinus_seqcode.yaml`. It is seeded from NCBITaxon only, carries the SeqCode-specific NCBI name and two NCBI synonyms, and has no GTDB mappings, xrefs, LPSN nomenclature, generated local strain entries, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 489213 maps `NCBITaxon:3879924` to slug `abyssiniarchaeum_dallolvicinus_seqcode`, and the target file exists under `data/taxa/archaea/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abyssiniarchaeum_dallolvicinus_seqcode.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/archaea/abyssiniarchaeum_dallolvicinus_seqcode.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/archaea/abyssiniarchaeum_dallolvicinus_seqcode.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 650615 has `NCBITaxon:3879924`, label `Abyssiniarchaeum dallolvicinus (SeqCode)`, rank `SPECIES`, direct parent `NCBITaxon:3879921`, genetic code `11`, exact synonym `Abyssiniarchaeum dallolvicinus`, related synonym `"Abyssiniarchaeum dallolvicinus" Gutierrez-Preciado et al. 2024`, source set `ncbitaxon`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2157` Archaea, `DOMAIN` | line 1698 |
| `NCBITaxon:3366610` Methanobacteriati, `KINGDOM` | line 621140 |
| `NCBITaxon:28890` Methanobacteriota, `PHYLUM` | line 2981 |
| `NCBITaxon:2290931` Stenosarchaea group, `CLADE` | line 523053 |
| `NCBITaxon:183963` Halobacteria, `CLASS` | line 36616 |
| `NCBITaxon:2235` Halobacteriales, `ORDER` | line 1759 |
| `NCBITaxon:3879917` Abyssiniarchaeaceae (SeqCode), `FAMILY` | line 650608 |
| `NCBITaxon:3879921` Abyssiniarchaeum (SeqCode), `GENUS` | line 650612 |

`curation/seed_scope.tsv` line 625816 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 650615 | Supported exactly. |
| NCBI type-material evidence | `data/raw/ncbi_type_material.tsv` lines 201135-201136 | Supported by the committed `DAL-8mg-83m_91C4R` isolate rows. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 489213 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 625816 | Supported exactly by a single seed-scope row. |
| Empty GTDB, LPSN, MediaDive, GOLD, Madin et al., BactoTraits, BacDive-derived strain, ATB, and StrainInfo surfaces | Exact gitignore-independent scans for `NCBITaxon:3879924` across the auxiliary raw/source TSV families | Supported; no same-taxon auxiliary row names this NCBI taxon outside NCBI. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the archaeal species identity, direct SeqCode Abyssiniarchaeum parent, root-first archaeal lineage, genetic code `11`, one exact synonym, one related synonym, and the NCBITAXON source attestation.
- NCBI also supplies isolate type-material rows for `DAL-8mg-83m_91C4R`; those rows do not by themselves mint a generated local strain record.
- The committed seed scope includes the taxon through the attested-source rule with one source including NCBI.
- No exact same-taxon auxiliary source row in the committed TSV inventories supplies GTDB mappings, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:3879924`.
- With no same-taxon BacDive-derived or overlay strain rows and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
