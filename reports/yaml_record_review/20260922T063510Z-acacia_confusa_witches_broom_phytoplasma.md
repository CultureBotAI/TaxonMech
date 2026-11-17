# YAML Record Review: 'Acacia confusa' witches'-broom phytoplasma

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acacia_confusa_witches_broom_phytoplasma.yaml
- Started UTC: 2026-09-22T06:33:55Z
- Finished UTC: 2026-09-22T06:35:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2940219 |
| label | 'Acacia confusa' witches'-broom phytoplasma |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:3098986 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a compact generated bacterial species record at `data/taxa/bacteria/acacia_confusa_witches_broom_phytoplasma.yaml`. It is seeded from NCBITaxon only, carries no GTDB mappings, no synonyms, no xrefs, no LPSN nomenclature, no generated local strain entries, and no causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 395653 maps `NCBITaxon:2940219` to slug `acacia_confusa_witches_broom_phytoplasma`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-acacia_confusa_witches_broom_phytoplasma.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acacia_confusa_witches_broom_phytoplasma.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acacia_confusa_witches_broom_phytoplasma.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 574509 has `NCBITaxon:2940219`, label `'Acacia confusa' witches'-broom phytoplasma`, rank `SPECIES`, direct parent `NCBITaxon:3098986`, genetic code `11`, empty NCBI synonym slots, source set `ncbitaxon`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:544448` Mycoplasmatota, `PHYLUM` | line 126468 |
| `NCBITaxon:31969` Mollicutes, `CLASS` | line 3369 |
| `NCBITaxon:186329` Acholeplasmatales, `ORDER` | line 36985 |
| `NCBITaxon:2146` Acholeplasmataceae, `FAMILY` | line 1689 |
| `NCBITaxon:33926` Candidatus Phytoplasma, `GENUS` | line 3660 |
| `NCBITaxon:3098986` unclassified Candidatus Phytoplasma, `NO_RANK` | line 598049 |

`curation/seed_scope.tsv` line 582300 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, empty synonym slots, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 574509 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 395653 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 582300 | Supported exactly by a single seed-scope row. |
| Empty GTDB, NCBI type-material, LPSN, MediaDive, GOLD, Madin et al., BactoTraits, BacDive-derived strain, ATB, and StrainInfo surfaces | Exact gitignore-independent scans for `NCBITaxon:2940219` across the auxiliary raw/source TSV families | Supported; no same-taxon auxiliary row names this NCBI taxon outside NCBI. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct unclassified Candidatus Phytoplasma parent, root-first bacterial lineage, genetic code `11`, and the NCBITAXON source attestation.
- The committed seed scope includes the taxon through the attested-source rule with one source including NCBI.
- No exact same-taxon auxiliary source row in the committed TSV inventories supplies GTDB mappings, NCBI type material, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:2940219`.
- With no same-taxon BacDive-derived or overlay strain rows and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
