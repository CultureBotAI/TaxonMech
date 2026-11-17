# YAML Record Review: Abyssibacter sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abyssibacter_sp.yaml
- Started UTC: 2026-09-22T06:23:00Z
- Finished UTC: 2026-09-22T06:25:07Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2320200 |
| label | Abyssibacter sp. |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2624364 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abyssibacter_sp.yaml`. It combines NCBITaxon identity with three pooled GTDB `skos:broadMatch` species mappings and carries no LPSN nomenclature, generated local strain entries, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 338742 maps `NCBITaxon:2320200` to slug `abyssibacter_sp`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abyssibacter_sp.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abyssibacter_sp.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abyssibacter_sp.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 524945 has `NCBITaxon:2320200`, label `Abyssibacter sp.`, rank `SPECIES`, direct parent `NCBITaxon:2624364`, genetic code `11`, empty NCBI synonym slots, source set `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:1224` Pseudomonadota, `PHYLUM` | line 945 |
| `NCBITaxon:1236` Gammaproteobacteria, `CLASS` | line 952 |
| `NCBITaxon:135613` Chromatiales, `ORDER` | line 27091 |
| `NCBITaxon:3103149` Oceanococcaceae, `FAMILY` | line 598809 |
| `NCBITaxon:2320199` Abyssibacter, `GENUS` | line 524944 |
| `NCBITaxon:2624364` unclassified Abyssibacter, `NO_RANK` | line 538054 |

`curation/seed_scope.tsv` line 94388 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, empty synonym slots, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 524945 | Supported exactly. |
| Primary pooled GTDB mapping | `data/raw/gtdb_mappings.tsv` line 183466 and `data/raw/gtdb_species.tsv` line 2823 | Supported exactly: `GTDB:s__Abyssibacter_sp023146115` maps to `NCBITaxon:2320200` by `skos:broadMatch` with 10 genomes. |
| Additional pooled GTDB mappings | `data/raw/gtdb_mappings.tsv` lines 183467-183468, `data/raw/gtdb_species.tsv` line 2824, and `data/raw/gtdb_species.tsv` line 41226 | Supported exactly for `GTDB:s__Abyssibacter_sp036156195` with two genomes and `GTDB:s__Celeribacter_sp964220165` with six genomes. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 94388 | Supported exactly by a single seed-scope row. |
| Empty NCBI type-material, LPSN, MediaDive, GOLD, Madin et al., BactoTraits, BacDive-derived strain, ATB, and StrainInfo surfaces | Exact gitignore-independent scans for `NCBITaxon:2320200` across the auxiliary raw/source TSV families | Supported; no same-taxon auxiliary row names this NCBI taxon outside NCBI and GTDB. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct unclassified Abyssibacter parent, root-first bacterial lineage, genetic code `11`, and the NCBITAXON source attestation.
- GTDB supplies three pooled `skos:broadMatch` species mappings to this NCBI bin, with 10, two, and six genomes respectively; the YAML records all three under `taxonomy_mappings` and summarizes the first plus a "2 further GTDB species" note under `source_attestations`.
- The committed seed scope includes the taxon through the attested-source rule with two sources including NCBI.
- No exact same-taxon auxiliary source row in the committed TSV inventories supplies NCBI type material, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:2320200`.
- With no same-taxon BacDive-derived or overlay strain rows and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
