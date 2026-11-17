# YAML Record Review: Acaryochloris marina MU04

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acaryochloris_marina_mu04.yaml
- Started UTC: 2026-09-22T06:59:02Z
- Finished UTC: 2026-09-22T06:59:38Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2762542 |
| label | Acaryochloris marina MU04 |
| rank | STRAIN |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:155978 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a compact generated bacterial strain record at `data/taxa/bacteria/acaryochloris_marina_mu04.yaml`. It is seeded from NCBITaxon only, carries no GTDB mappings, no synonyms, no xrefs, no LPSN nomenclature, no generated local strain entries, and no causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 371968 maps `NCBITaxon:2762542` to slug `acaryochloris_marina_mu04`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -type f -name "*acaryochloris_marina_mu04.md" -print` returned no prior report. `find` includes ignored files, and the probe was scoped to `reports/yaml_record_review/`. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acaryochloris_marina_mu04.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acaryochloris_marina_mu03.yaml data/taxa/bacteria/acaryochloris_marina_mu04.yaml data/taxa/bacteria/acaryochloris_marina_mu05.yaml data/taxa/bacteria/acaryochloris_marina_mu06.yaml` scanned this file with zero ERROR rows in a four-file batch and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 551920 has `NCBITaxon:2762542`, label `Acaryochloris marina MU04`, rank `STRAIN`, direct parent `NCBITaxon:155978`, genetic code `11`, empty NCBI synonym slots, source set `ncbitaxon`, and snapshot date `2026-09-13`.

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
| `NCBITaxon:155977` Acaryochloris, `GENUS` | line 32348 |
| `NCBITaxon:155978` Acaryochloris marina, `SPECIES` | line 32349 |

`curation/seed_scope.tsv` line 573506 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, empty synonym slots, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 551920 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 371968 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 573506 | Supported exactly by a single seed-scope row. |
| Empty GTDB, NCBI type-material, LPSN, MediaDive, GOLD, Madin et al., BactoTraits, BacDive-derived strain, ATB, and StrainInfo surfaces | Exact gitignore-independent source-row scans for `NCBITaxon:2762542` across `data/raw/`, `data/atb/`, and `data/straininfo/` TSV inventories, plus an exact GTDB crosswalk scan | Supported; no same-taxon auxiliary row names this NCBI taxon outside `data/raw/ncbitaxon_taxa.tsv`. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the strain identity, direct Acaryochloris marina parent, root-first bacterial lineage, genetic code `11`, and the NCBITAXON source attestation.
- The committed seed scope includes the taxon through the attested-source rule with one source including NCBI.
- No exact same-taxon auxiliary source row in the committed TSV inventories supplies GTDB mappings, NCBI type material, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:2762542`.
- With no same-taxon BacDive-derived or overlay strain rows and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
