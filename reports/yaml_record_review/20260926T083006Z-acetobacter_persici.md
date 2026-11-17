# YAML Record Review: Acetobacter persici

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_persici.yaml`
- Reviewed UTC: 2026-09-26T08:30:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1076596` |
| label | `Acetobacter persici` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated species record under `Acetobacter`. It has source attestations from NCBITAXON, LPSN, GTDB, BACDIVE, GOLD, and MADIN; one LPSN nomenclature row; one GTDB `skos:closeMatch`; six synonyms; two BacDive strain rows with the type strain filed under descendant `NCBITaxon:1236503`; 10 generated genome assemblies; 6 generated genome records; 29 generated related records; and no definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 24159 maps `NCBITaxon:1076596` to `acetobacter_persici`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_persici.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_persici.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_peroxydans.yaml data/taxa/bacteria/acetobacter_peroxydans_nbrc_13755.yaml data/taxa/bacteria/acetobacter_persici.yaml data/taxa/bacteria/acetobacter_persici_jcm_25330.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 230856 has `NCBITaxon:1076596`, label `Acetobacter persici`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`, one exact synonym, four NCBITaxon related synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 10851 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, species rank, parent, genetic code, source set, snapshot date, exact synonym, and related synonyms | `data/raw/ncbitaxon_taxa.tsv` line 230856 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 24159 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 10851 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type strains | `data/raw/lpsn_names.tsv` line 27330 | Supported; LPSN carries this name as the correct name, links synonym `lpsn:790361`, lists JCM-25330 and LMG-26458 as type-strain deposits, and supplies accession `INSDC:AB665070`. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 2870 | Supported exactly by one 16-genome `skos:closeMatch` to `GTDB:s__Acetobacter_persici`. |
| BacDive direct and descendant strains | Native BacDive taxon assignments plus `data/raw/bacdive_strains.tsv` line 85574 and culture-collection rows for BacDive 163337 and 163338 | Supported; BacDive 163338 is direct to the species, and BacDive 163337 is retained as the type-strain row classified at child `NCBITaxon:1236503`. |
| GOLD and Madin et al. source attestations | `data/raw/gold_organisms.tsv` line 1387, `data/raw/madin_taxa.tsv` line 1769, and native GOLD organism/project rows | Supported; GOLD has eight direct organisms and seven direct native projects, and Madin et al. has one direct assertion keyed to this species. |
| Empty auxiliary evidence | Exact scans of MediaDive, BactoTraits, and same-taxon StrainInfo surfaces for `NCBITaxon:1076596` | Supported; no committed row directly keys those auxiliary sources to this NCBI species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, the direct `Acetobacter` parent, the exact 9-ancestor lineage, one exact synonym, and four related synonyms.
- LPSN supplies the sixth synonym through its nomenclature row.
- GTDB supplies the only taxonomy mapping as `skos:closeMatch`.
- BacDive direct and descendant accounting explains `strain_count: 2`: BacDive 163338 is filed directly here with `JCM 25332`, and BacDive 163337 is filed under child strain `NCBITaxon:1236503`.
- GOLD and Madin et al. have committed rows keyed directly to this species.
- StrainInfo contributes one assembly and seven related rows through matched deposits, but no exact direct target row exists for this species.
- NCBI merged old IDs `NCBITaxon:1076597` and `NCBITaxon:1514892` redirect to this taxon in the raw merge map; the generated YAML does not carry a `retained_old_ids` block for them.
- No exact same-taxon MediaDive or BactoTraits row exists in the committed inventories, and no curator-added `causal_graphs` or definitions are expected.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The type strain is correctly represented in the descendant `Acetobacter persici JCM 25330` record, while the species record retains both the descendant BacDive type-strain row and the direct species BacDive row for JCM 25332.
