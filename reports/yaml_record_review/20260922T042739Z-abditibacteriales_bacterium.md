# YAML Record Review: Abditibacteriales bacterium

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abditibacteriales_bacterium.yaml
- Started UTC: 2026-09-22T04:26:41Z
- Finished UTC: 2026-09-22T04:27:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2972663 |
| label | Abditibacteriales bacterium |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2972662 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abditibacteriales_bacterium.yaml`. It carries two pooled GTDB `skos:broadMatch` mappings, no synonyms, no GTDB xrefs, no LPSN nomenclature, no BacDive-derived local strain entries, no generated AllTheBacteria or StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GTDB.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 401924 maps `NCBITaxon:2972663` to slug `abditibacteriales_bacterium`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*abditibacteriales_bacterium.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abditibacteriales_bacterium.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abditibacteriales_bacterium.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; the latest neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 580360 has `NCBITaxon:2972663`, label `Abditibacteriales bacterium`, rank `SPECIES`, direct parent `NCBITaxon:2972662`, genetic code `11`, no exact synonyms, no related synonyms, source set `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

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
| `NCBITaxon:2972662` unclassified Abditibacteriales, `NO_RANK` | line 580359 |

`curation/seed_scope.tsv` line 113296 keeps this taxon in scope through the attested-source rule.

`data/raw/gtdb_mappings.tsv` line 242122 maps `GTDB:s__JANWYM01_sp025055355` to `NCBITaxon:2972663` with `skos:broadMatch` and two genomes, and line 242121 maps `GTDB:s__Abditibacterium_sp038236075` with one genome; the corresponding `data/raw/gtdb_species.tsv` rows are lines 97159 and 2798.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, source set, empty synonym slots, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 580360 | Supported exactly. |
| Two GTDB broad mappings | `data/raw/gtdb_mappings.tsv` lines 242121-242122 and `data/raw/gtdb_species.tsv` lines 2798 and 97159 | Supported exactly with three total GTDB genomes. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 401924 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 113296 | Supported exactly by a single seed-scope row. |
| NCBITAXON and GTDB attestations | NCBI row plus the two GTDB rows above | Supported; the generated GTDB attestation records the two-genome `JANWYM01` broad mapping and notes one further pooled GTDB species. |
| Empty NCBI type-material, LPSN, BacDive-derived raw, MediaDive, GOLD, Madin et al., BactoTraits, ATB, and StrainInfo TSV surfaces | Exact gitignore-independent scans for `NCBITaxon:2972663` across the auxiliary raw/source TSV families | Supported; no auxiliary TSV row names this NCBI taxon. |
| Empty StrainInfo generated overlay | Exact generated overlay TSV scans | Supported; no `data/straininfo/*.tsv` row names `NCBITaxon:2972663`. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the identity, direct parent, root-first bacterial lineage, genetic code `11`, and the NCBITAXON source attestation.
- GTDB supplies one two-genome and one one-genome `skos:broadMatch` species mapping that are intentionally pooled onto this placeholder taxon and therefore do not generate close-match xrefs or exact GTDB synonyms.
- The committed seed scope includes the taxon through the attested-source rule with NCBI plus GTDB support.
- No exact auxiliary source row in the committed TSV inventories supplies NCBI type material, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:2972663`.
- With `strain_count: 0`, no BacDive-derived or overlay strain rows, and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
