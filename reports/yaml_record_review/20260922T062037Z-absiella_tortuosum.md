# YAML Record Review: Absiella tortuosum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/absiella_tortuosum.yaml
- Started UTC: 2026-09-22T06:19:00Z
- Finished UTC: 2026-09-22T06:20:37Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:39494 |
| label | Absiella tortuosum |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2749267 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/absiella_tortuosum.yaml`. It carries six NCBI synonyms, one BacDive-derived local strain with GOLD and StrainInfo related records, no GTDB mappings, no LPSN nomenclature, no generated assembly or genome records, no causal graphs, and source attestations from NCBITAXON, BACDIVE, GOLD, and MADIN.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 491403 maps `NCBITaxon:39494` to slug `absiella_tortuosum`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-absiella_tortuosum.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/absiella_tortuosum.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/absiella_tortuosum.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4471 has `NCBITaxon:39494`, label `Absiella tortuosum`, rank `SPECIES`, direct parent `NCBITaxon:2749267`, genetic code `11`, three exact synonyms, three related synonyms, source set `ncbitaxon|bacdive|gold|madin_etal`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:1239` Bacillota, `PHYLUM` | line 955 |
| `NCBITaxon:526524` Erysipelotrichia, `CLASS` | line 120147 |
| `NCBITaxon:526525` Erysipelotrichales, `ORDER` | line 120148 |
| `NCBITaxon:128827` Erysipelotrichaceae, `FAMILY` | line 24654 |
| `NCBITaxon:2749267` Amedibacterium, `GENUS` | line 550631 |

`data/raw/bacdive_strains.tsv` line 5338 supports BacDive strain 5447 with taxon `NCBITaxon:39494` and ATCC 25548, DSM 3987, and VPI 1084B culture IDs.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 4471 | Supported exactly. |
| BacDive local strain | `data/raw/bacdive_strains.tsv` line 5338 | Supported exactly. |
| GOLD source attestation and related records | `data/raw/gold_organisms.tsv` line 34271 and `data/raw/strain_related_records.tsv` lines 381369-381370 | Supported by one same-taxon GOLD organism and the two GOLD organism related-record joins through ATCC 25548. |
| Madin source attestation | `data/raw/madin_taxa.tsv` line 23179 | Supported exactly with one direct trait assertion. |
| StrainInfo overlay | `data/straininfo/strain_links.tsv` lines 92831-92832 and an exact gzip scan of `data/straininfo/related_records.tsv.gz` for `kgmicrobe.strain:bacdive_5447` | Supported with the ATCC 25548 rRNA sequence, ATCC 25548 and DSM 3987 deposit rows, and the paired StrainInfo strain rows. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 491403 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 21829 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct Amedibacterium parent, root-first bacterial lineage, genetic code `11`, three exact synonyms, three related synonyms, and the NCBITAXON source attestation.
- BacDive supplies one local strain with its ATCC/DSM/VPI culture IDs.
- GOLD and StrainInfo source rows generate the expected GOLD organism, rRNA, deposit, and strain related records for that local strain.
- Madin et al. supplies one directly filed trait assertion represented in `source_attestations`.
- No exact same-taxon GTDB, LPSN, MediaDive, BactoTraits, ATB, or assembly/genome source rows appear in the committed inventories, and no curator-added `causal_graphs` are present.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
