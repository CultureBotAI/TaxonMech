# YAML Record Review: Aalborgiella aggregata (SeqCode)

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/aalborgiella_aggregata_seqcode.yaml
- Started UTC: 2026-09-22T04:24:51Z
- Finished UTC: 2026-09-22T04:25:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:3386178 |
| label | Aalborgiella aggregata (SeqCode) |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:3386153 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/aalborgiella_aggregata_seqcode.yaml`. It carries NCBITaxon and GTDB support, a GTDB `skos:closeMatch` mapping with 12 genomes, five synonym assertions, a GTDB xref, five NCBI type-material inventory rows, no LPSN nomenclature, no BacDive-derived local strain entries, no generated AllTheBacteria or StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GTDB.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 451985 maps `NCBITaxon:3386178` to slug `aalborgiella_aggregata_seqcode`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*aalborgiella_aggregata_seqcode.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/aalborgiella_aggregata_seqcode.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/aalborgiella_aggregata_seqcode.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; the latest neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 624917 has `NCBITaxon:3386178`, label `Aalborgiella aggregata (SeqCode)`, rank `SPECIES`, direct parent `NCBITaxon:3386153`, genetic code `11`, exact synonyms `"Candidatus Hagefella amepia" Pallen et al. 2022`, `Aalborgiella aggregata`, `Rhodoferax midas_s_33`, and `s__JAAFJR01 sp016705065`, related synonym `"Aalborgiella aggregata" Petersen et al. 2025`, source set `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:1224` Pseudomonadota, `PHYLUM` | line 945 |
| `NCBITaxon:28216` Betaproteobacteria, `CLASS` | line 2916 |
| `NCBITaxon:80840` Burkholderiales, `ORDER` | line 12115 |
| `NCBITaxon:80864` Comamonadaceae, `FAMILY` | line 12133 |
| `NCBITaxon:3386153` Aalborgiella (SeqCode), `GENUS` | line 624911 |

`curation/seed_scope.tsv` line 131367 keeps this taxon in scope through the attested-source rule.

`data/raw/gtdb_mappings.tsv` line 275946 maps `GTDB:s__Aalborgiella_aggregata` to `NCBITaxon:3386178` with `skos:closeMatch` and 12 genomes; `data/raw/gtdb_species.tsv` line 2774 carries the same GTDB species ID under genus `GTDB:g__Aalborgiella` with genome count `12`.

`data/raw/ncbi_type_material.tsv` lines 182632-182636 preserve five `typematerial.dmp` rows for isolates `AalE_18-Q3-R2-46_MAXAC.018`, `AalE_MAXAC.018`, `GCA_016705065.1`, `personal::AalE_18-Q3-R2-46_MAXAC.018`, and `personal::GCA_016705065.1`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, exact synonyms, related synonym, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 624917 | Supported exactly. |
| GTDB close mapping, xref, and genome count | `data/raw/gtdb_mappings.tsv` line 275946; `data/raw/gtdb_species.tsv` line 2774 | Supported exactly with 12 genomes. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 451985 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 131367 | Supported exactly by a single seed-scope row. |
| NCBITAXON and GTDB attestations | NCBI and GTDB rows above | Supported exactly with one NCBI name assertion and 12 GTDB genome assertions. |
| NCBI type-material side inventory | `data/raw/ncbi_type_material.tsv` lines 182632-182636 | Supported exactly with five isolate designations. |
| Empty LPSN, BacDive-derived raw, MediaDive, GOLD, Madin et al., BactoTraits, ATB, and StrainInfo TSV surfaces | Exact gitignore-independent scans for `NCBITaxon:3386178` across the auxiliary raw/source TSV families | Supported; no non-NCBI-type-material auxiliary TSV row names this NCBI taxon. |
| Empty StrainInfo generated overlay | Exact generated overlay TSV scans | Supported; no `data/straininfo/*.tsv` row names `NCBITaxon:3386178`. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the identity, direct parent, root-first bacterial lineage, genetic code `11`, five name assertions, the sole related synonym, and five type-material inventory rows.
- GTDB supplies a `skos:closeMatch` species mapping, the `GTDB:s__Aalborgiella_aggregata` xref, and 12 genome assertions.
- The committed seed scope includes the taxon through the attested-source rule with NCBI plus GTDB support.
- NCBI `typematerial.dmp` rows are captured in `data/raw/ncbi_type_material.tsv`; TaxonMech currently generates `nomenclature` from LPSN rather than from this NCBI side inventory.
- No exact auxiliary source row in the committed TSV inventories supplies LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:3386178`.
- With `strain_count: 0`, no BacDive-derived or overlay strain rows, and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
