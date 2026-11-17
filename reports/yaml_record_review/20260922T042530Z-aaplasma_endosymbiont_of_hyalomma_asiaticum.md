# YAML Record Review: Aaplasma endosymbiont of Hyalomma asiaticum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/aaplasma_endosymbiont_of_hyalomma_asiaticum.yaml
- Started UTC: 2026-09-22T04:24:51Z
- Finished UTC: 2026-09-22T04:25:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:3236821 |
| label | Aaplasma endosymbiont of Hyalomma asiaticum |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2617684 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/aaplasma_endosymbiont_of_hyalomma_asiaticum.yaml`. It carries one GTDB exact synonym, a GTDB `skos:closeMatch` mapping with one genome, a GTDB xref, no NCBI synonyms, no LPSN nomenclature, no BacDive-derived local strain entries, no generated AllTheBacteria or StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GTDB.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 438567 maps `NCBITaxon:3236821` to slug `aaplasma_endosymbiont_of_hyalomma_asiaticum`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*aaplasma_endosymbiont_of_hyalomma_asiaticum.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/aaplasma_endosymbiont_of_hyalomma_asiaticum.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/aaplasma_endosymbiont_of_hyalomma_asiaticum.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; the latest neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 614377 has `NCBITaxon:3236821`, label `Aaplasma endosymbiont of Hyalomma asiaticum`, rank `SPECIES`, direct parent `NCBITaxon:2617684`, genetic code `11`, no NCBI exact synonyms, no NCBI related synonyms, source set `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:1224` Pseudomonadota, `PHYLUM` | line 945 |
| `NCBITaxon:28211` Alphaproteobacteria, `CLASS` | line 2912 |
| `NCBITaxon:766` Rickettsiales, `ORDER` | line 594 |
| `NCBITaxon:942` Anaplasmataceae, `FAMILY` | line 725 |
| `NCBITaxon:768` Anaplasma, `GENUS` | line 595 |
| `NCBITaxon:2617684` unclassified Anaplasma, `NO_RANK` | line 537468 |

`curation/seed_scope.tsv` line 125928 keeps this taxon in scope through the attested-source rule.

`data/raw/gtdb_mappings.tsv` line 268520 maps `GTDB:s__Anaplasma_sp048496795` to `NCBITaxon:3236821` with `skos:closeMatch` and one genome; `data/raw/gtdb_species.tsv` line 9925 carries the same GTDB species ID under genus `GTDB:g__Anaplasma` with genome count `1`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, source set, empty NCBI synonym slots, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 614377 | Supported exactly. |
| GTDB close mapping, xref, exact synonym, and genome count | `data/raw/gtdb_mappings.tsv` line 268520; `data/raw/gtdb_species.tsv` line 9925 | Supported exactly with one genome. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 438567 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 125928 | Supported exactly by a single seed-scope row. |
| NCBITAXON and GTDB attestations | NCBI and GTDB rows above | Supported exactly with one NCBI name assertion and one GTDB genome assertion. |
| Empty NCBI type-material, LPSN, BacDive-derived raw, MediaDive, GOLD, Madin et al., BactoTraits, ATB, and StrainInfo TSV surfaces | Exact gitignore-independent scans for `NCBITaxon:3236821` across the auxiliary raw/source TSV families | Supported; no auxiliary TSV row names this NCBI taxon. |
| Empty StrainInfo generated overlay | Exact generated overlay TSV scans | Supported; no `data/straininfo/*.tsv` row names `NCBITaxon:3236821`. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the identity, direct parent, root-first bacterial lineage, genetic code `11`, and the NCBITAXON source attestation.
- GTDB supplies a `skos:closeMatch` species mapping, the `GTDB:s__Anaplasma_sp048496795` xref, the `Anaplasma sp048496795` exact synonym, and one genome assertion.
- The committed seed scope includes the taxon through the attested-source rule with NCBI plus GTDB support.
- No exact auxiliary source row in the committed TSV inventories supplies NCBI type material, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:3236821`.
- With `strain_count: 0`, no BacDive-derived or overlay strain rows, and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
