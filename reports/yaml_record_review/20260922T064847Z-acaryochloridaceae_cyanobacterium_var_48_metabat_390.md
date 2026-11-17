# YAML Record Review: Acaryochloridaceae cyanobacterium VAR_48_metabat_390

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acaryochloridaceae_cyanobacterium_var_48_metabat_390.yaml
- Started UTC: 2026-09-22T06:47:08Z
- Finished UTC: 2026-09-22T06:48:47Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2964580 |
| label | Acaryochloridaceae cyanobacterium VAR_48_metabat_390 |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2720654 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/acaryochloridaceae_cyanobacterium_var_48_metabat_390.yaml`. It is seeded from NCBITaxon and GTDB, carries one GTDB `skos:closeMatch` taxonomy mapping, one GTDB exact synonym, one GTDB xref, no LPSN nomenclature, no generated local strain entries, and no causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 401156 maps `NCBITaxon:2964580` to slug `acaryochloridaceae_cyanobacterium_var_48_metabat_390`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -type f -name "*acaryochloridaceae_cyanobacterium_var_48_metabat_390.md" -print` returned no prior report. `find` includes ignored files, and the probe was scoped to `reports/yaml_record_review/`. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acaryochloridaceae_cyanobacterium_var_48_metabat_390.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acaryochloridaceae_cyanobacterium_su_2_1.yaml data/taxa/bacteria/acaryochloridaceae_cyanobacterium_var_48_metabat_390.yaml data/taxa/bacteria/acaryochloridales_cyanobacterium.yaml data/taxa/bacteria/acaryochloridales_cyanobacterium_e46.yaml` scanned this file with zero ERROR rows in a four-file batch and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 579711 has `NCBITaxon:2964580`, label `Acaryochloridaceae cyanobacterium VAR_48_metabat_390`, rank `SPECIES`, direct parent `NCBITaxon:2720654`, genetic code `11`, empty NCBI synonym slots, source set `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

The GTDB crosswalk is also exact: `data/raw/gtdb_species.tsv` line 77190 defines `GTDB:s__JAAURS01_sp031422435` as `s__JAAURS01_sp031422435` under `GTDB:g__JAAURS01` with genome count `1`, and `data/raw/gtdb_mappings.tsv` line 241577 maps that GTDB species to `NCBITaxon:2964580` with predicate `skos:closeMatch` and genome count `1`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:1798711` Cyanobacteriota/Melainabacteria group, `CLADE` | line 469139 |
| `NCBITaxon:1117` Cyanobacteriota, `PHYLUM` | line 870 |
| `NCBITaxon:3028117` Cyanophyceae, `CLASS` | line 587019 |
| `NCBITaxon:3079744` Acaryochloridales, `ORDER` | line 595536 |
| `NCBITaxon:1890429` Acaryochloridaceae, `FAMILY` | line 490868 |
| `NCBITaxon:2720654` unclassified Acaryochloridaceae, `NO_RANK` | line 547212 |

`curation/seed_scope.tsv` line 113017 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, empty synonym slots, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 579711 | Supported exactly. |
| GTDB cross-reference, exact synonym basis, mapping predicate, and genome count | `data/raw/gtdb_species.tsv` line 77190 and `data/raw/gtdb_mappings.tsv` line 241577 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 401156 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 113017 | Supported exactly by a single seed-scope row. |
| Empty NCBI type-material, LPSN, MediaDive, GOLD, Madin et al., BactoTraits, BacDive-derived strain, ATB, and StrainInfo surfaces | Exact gitignore-independent scans for `NCBITaxon:2964580` across `data/raw/`, `data/atb/`, and `data/straininfo/` TSV inventories | Supported; no same-taxon auxiliary row names this NCBI taxon outside the expected NCBI taxonomy row and GTDB crosswalk row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct unclassified Acaryochloridaceae parent, root-first bacterial lineage, genetic code `11`, and the NCBITAXON source attestation.
- GTDB supplies one species-level crosswalk, one derived exact synonym, one xref, and a GTDB source attestation with `GENOME` assertion count `1`.
- The committed seed scope includes the taxon through the attested-source rule with two sources including NCBI.
- No exact same-taxon auxiliary source row in the committed TSV inventories supplies NCBI type material, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:2964580`.
- With no same-taxon BacDive-derived or overlay strain rows and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
