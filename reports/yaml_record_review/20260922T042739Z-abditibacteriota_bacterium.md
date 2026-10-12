# YAML Record Review: Abditibacteriota bacterium

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abditibacteriota_bacterium.yaml
- Started UTC: 2026-09-22T04:26:41Z
- Finished UTC: 2026-09-22T04:27:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2783868 |
| label | Abditibacteriota bacterium |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2562436 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abditibacteriota_bacterium.yaml`. It carries seven pooled GTDB `skos:broadMatch` mappings, no synonyms, no GTDB xrefs, no LPSN nomenclature, no same-taxon BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GTDB.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 374827 maps `NCBITaxon:2783868` to slug `abditibacteriota_bacterium`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*abditibacteriota_bacterium.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abditibacteriota_bacterium.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abditibacteriota_bacterium.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; the latest neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 554926 has `NCBITaxon:2783868`, label `Abditibacteriota bacterium`, rank `SPECIES`, direct parent `NCBITaxon:2562436`, genetic code `11`, no exact synonyms, no related synonyms, source set `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:2109258` Abditibacteriota, `PHYLUM` | line 518358 |
| `NCBITaxon:2562436` unclassified Abditibacteriota, `NO_RANK` | line 530426 |

`curation/seed_scope.tsv` line 103034 keeps this taxon in scope through the attested-source rule.

`data/raw/gtdb_mappings.tsv` lines 216961-216967 map seven GTDB species to `NCBITaxon:2783868` with `skos:broadMatch`; the corresponding `data/raw/gtdb_species.tsv` rows are lines 2795, 65597, 98698, 149931, and 150971-150973.

BV-BRC/ATB genome evidence still mentions this placeholder taxon ID, but the linked local BacDive strain is filed under a different current taxon: `data/raw/bacdive_strains.tsv` line 86555 files `kgmicrobe.strain:bacdive_164319` under `NCBITaxon:2562437`, while `data/raw/strain_genome_records.tsv` line 60759, `data/raw/strain_assemblies.tsv` line 78167, `data/raw/strain_related_records.tsv` lines 239638-239639, `data/atb/strain_links.tsv` line 2499, and `data/atb/genome_links.tsv` lines 10557-10558 carry the `NCBITaxon:2783868` genome label through that cross-taxon strain.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, source set, empty synonym slots, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 554926 | Supported exactly. |
| Seven GTDB broad mappings | `data/raw/gtdb_mappings.tsv` lines 216961-216967 and `data/raw/gtdb_species.tsv` rows for the same species IDs | Supported exactly with eight total GTDB genomes. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 374827 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 103034 | Supported exactly by a single seed-scope row. |
| NCBITAXON and GTDB attestations | NCBI row plus the seven GTDB rows above | Supported; the generated GTDB attestation records the two-genome `RGIG10368` broad mapping and notes six further pooled GTDB species. |
| Cross-taxon BV-BRC and ATB genome rows | Exact scans for `kgmicrobe.strain:bacdive_164319` and `NCBITaxon:2783868` across `data/raw/strain_*` and `data/atb/*.tsv` | Supported; those rows are present but join to a BacDive local strain filed under `NCBITaxon:2562437`, not this taxon. |
| Empty NCBI type-material, LPSN, MediaDive, GOLD, Madin et al., BactoTraits, same-taxon ATB strain, and StrainInfo TSV surfaces | Exact gitignore-independent scans for `NCBITaxon:2783868` across the auxiliary raw/source TSV families | Supported; no same-taxon BacDive row or StrainInfo overlay row names this NCBI taxon. |
| Empty StrainInfo generated overlay | Exact generated overlay TSV scans | Supported; no `data/straininfo/*.tsv` row names `NCBITaxon:2783868`. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the identity, direct parent, root-first bacterial lineage, genetic code `11`, and the NCBITAXON source attestation.
- GTDB supplies one two-genome and six one-genome `skos:broadMatch` species mappings that are intentionally pooled onto this placeholder taxon and therefore do not generate close-match xrefs or exact GTDB synonyms.
- The committed seed scope includes the taxon through the attested-source rule with NCBI plus GTDB support.
- BV-BRC and ATB rows that still mention `NCBITaxon:2783868` are attached to BacDive strain `164319`, whose checked-in BacDive row is filed under `NCBITaxon:2562437`; the generated `strain_count: 0` is therefore consistent for this current placeholder taxon.
- No exact same-taxon auxiliary source row in the committed TSV inventories supplies NCBI type material, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:2783868`.
- With no same-taxon BacDive-derived or overlay strain rows and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
