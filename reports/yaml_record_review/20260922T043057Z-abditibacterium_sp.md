# YAML Record Review: Abditibacterium sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abditibacterium_sp.yaml
- Started UTC: 2026-09-22T04:28:00Z
- Finished UTC: 2026-09-22T04:30:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2109264 |
| label | Abditibacterium sp. |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2633457 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abditibacterium_sp.yaml`. It carries eight pooled GTDB `skos:broadMatch` mappings, no synonyms, no xrefs, no LPSN nomenclature, no generated local strain entries, no causal graphs, and source attestations from NCBITAXON and GTDB.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 328704 maps `NCBITaxon:2109264` to slug `abditibacterium_sp`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abditibacterium_sp.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abditibacterium_sp.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abditibacterium_sp.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 518363 has `NCBITaxon:2109264`, label `Abditibacterium sp.`, rank `SPECIES`, direct parent `NCBITaxon:2633457`, genetic code `11`, empty NCBI synonym slots, source set `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:2109258` Abditibacteriota, `PHYLUM` | line 518358 |
| `NCBITaxon:2109259` Abditibacteriia, `CLASS` | line 518359 |
| `NCBITaxon:2109260` Abditibacteriales, `ORDER` | line 518360 |
| `NCBITaxon:2109261` Abditibacteriaceae, `FAMILY` | line 518361 |
| `NCBITaxon:2109263` Abditibacterium, `GENUS` | line 518362 |
| `NCBITaxon:2633457` unclassified Abditibacterium, `NO_RANK` | line 538801 |

`curation/seed_scope.tsv` line 92335 keeps this taxon in scope through the attested-source rule.

`data/raw/gtdb_mappings.tsv` lines 168083-168090 map eight one-genome GTDB species to `NCBITaxon:2109264` with `skos:broadMatch`; the corresponding `data/raw/gtdb_species.tsv` rows are lines 2796, 2797, 2799, 2800, and 2802-2805.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, empty synonym slots, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 518363 | Supported exactly. |
| Eight GTDB broad mappings | `data/raw/gtdb_mappings.tsv` lines 168083-168090 and the matching `data/raw/gtdb_species.tsv` rows | Supported exactly with eight one-genome GTDB species. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 328704 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 92335 | Supported exactly by a single seed-scope row. |
| NCBITAXON and GTDB attestations | NCBI row plus the eight GTDB rows above | Supported; the generated GTDB attestation records the first one-genome broad mapping and notes the seven further pooled GTDB species. |
| Empty NCBI type-material, LPSN, MediaDive, GOLD, Madin et al., BactoTraits, BacDive-derived strain, ATB, and StrainInfo surfaces | Exact gitignore-independent scans for `NCBITaxon:2109264` across the auxiliary raw/source TSV families | Supported; no same-taxon auxiliary row names this NCBI taxon outside NCBI and GTDB mapping tables. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the identity, direct unclassified parent, root-first bacterial lineage, genetic code `11`, and the NCBITAXON source attestation.
- GTDB supplies eight one-genome `skos:broadMatch` species mappings that are intentionally pooled onto this placeholder species and therefore do not generate close-match xrefs or exact GTDB synonyms.
- The committed seed scope includes the taxon through the attested-source rule with NCBI plus GTDB support.
- No exact same-taxon auxiliary source row in the committed TSV inventories supplies NCBI type material, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:2109264`.
- With no same-taxon BacDive-derived or overlay strain rows and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
