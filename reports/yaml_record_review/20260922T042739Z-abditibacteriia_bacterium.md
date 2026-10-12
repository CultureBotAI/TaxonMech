# YAML Record Review: Abditibacteriia bacterium

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abditibacteriia_bacterium.yaml
- Started UTC: 2026-09-22T04:26:41Z
- Finished UTC: 2026-09-22T04:27:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:3050466 |
| label | Abditibacteriia bacterium |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:3050465 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abditibacteriia_bacterium.yaml`. It carries one GTDB `skos:closeMatch` mapping, one GTDB exact synonym, a GTDB xref, no NCBI synonyms, no retained retired NCBI predecessor, no LPSN nomenclature, no BacDive-derived local strain entries, no generated AllTheBacteria or StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GTDB.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 412645 maps `NCBITaxon:3050466` to slug `abditibacteriia_bacterium`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*abditibacteriia_bacterium.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abditibacteriia_bacterium.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abditibacteriia_bacterium.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; the latest neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 590395 has `NCBITaxon:3050466`, label `Abditibacteriia bacterium`, rank `SPECIES`, direct parent `NCBITaxon:3050465`, genetic code `11`, no NCBI exact synonyms, no NCBI related synonyms, source set `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:2109258` Abditibacteriota, `PHYLUM` | line 518358 |
| `NCBITaxon:2109259` Abditibacteriia, `CLASS` | line 518359 |
| `NCBITaxon:3050465` unclassified Abditibacteriia, `NO_RANK` | line 590394 |

`curation/seed_scope.tsv` line 117622 keeps this taxon in scope through the attested-source rule.

`data/raw/gtdb_mappings.tsv` line 253297 maps `GTDB:s__DAITOV01_sp036833945` to `NCBITaxon:3050466` with `skos:closeMatch` and one genome; `data/raw/gtdb_species.tsv` line 48586 carries the same GTDB species ID under genus `GTDB:g__DAITOV01` with genome count `1`.

`data/raw/ncbi_merged_ids.tsv` line 58552 redirects old ID `NCBITaxon:2953059` into `NCBITaxon:3050466`, but an exact gitignore-independent scan of `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and `curation/seed_scope.tsv` found no retained old row or generated path for `NCBITaxon:2953059`; the record therefore has no generated predecessor to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, source set, empty NCBI synonym slots, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 590395 | Supported exactly. |
| GTDB close mapping, xref, exact synonym, and genome count | `data/raw/gtdb_mappings.tsv` line 253297; `data/raw/gtdb_species.tsv` line 48586 | Supported exactly with one genome. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 412645 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 117622 | Supported exactly by a single seed-scope row. |
| NCBI merged-ID side inventory | `data/raw/ncbi_merged_ids.tsv` line 58552 plus exact retained-old-ID scans | Supported; one old ID redirects into this taxon but does not generate `replaces` without a retained retired NCBI inventory row. |
| NCBITAXON and GTDB attestations | NCBI and GTDB rows above | Supported exactly with one NCBI name assertion and one GTDB genome assertion. |
| Empty NCBI type-material, LPSN, BacDive-derived raw, MediaDive, GOLD, Madin et al., BactoTraits, ATB, and StrainInfo TSV surfaces | Exact gitignore-independent scans for `NCBITaxon:3050466` across the auxiliary raw/source TSV families | Supported; no non-merged auxiliary TSV row names this NCBI taxon. |
| Empty StrainInfo generated overlay | Exact generated overlay TSV scans | Supported; no `data/straininfo/*.tsv` row names `NCBITaxon:3050466`. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the identity, direct parent, root-first bacterial lineage, genetic code `11`, the NCBITAXON source attestation, and one non-retained merged-ID side row.
- GTDB supplies a `skos:closeMatch` species mapping, the `GTDB:s__DAITOV01_sp036833945` xref, the `DAITOV01 sp036833945` exact synonym, and one genome assertion.
- The committed seed scope includes the taxon through the attested-source rule with NCBI plus GTDB support.
- No exact auxiliary source row in the committed TSV inventories, outside the merged-ID side inventory, supplies NCBI type material, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:3050466`.
- With `strain_count: 0`, no retained retired predecessor, no BacDive-derived or overlay strain rows, and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, `replaces`, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
