# YAML Record Review: Candidatus Thiomargarita nelsonii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/candidatus_thiomargarita_nelsonii.yaml
- Started UTC: 2026-09-22T16:35:21Z
- Finished UTC: 2026-09-22T16:35:21Z
- Verdict: pass with minor issues

## Target

Reviewed `data/taxa/bacteria/candidatus_thiomargarita_nelsonii.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003181` / `Candidatus Thiomargarita nelsonii`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003181`
- Label: `Candidatus Thiomargarita nelsonii`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:90372` / `Thiomargarita`
- Maintained owner: source rows under `data/raw/`, `curation/seed_scope.tsv`, and the seed-generation code; do not patch `data/taxa/bacteria/candidatus_thiomargarita_nelsonii.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/candidatus_thiomargarita_nelsonii.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/bacterium_ktt_14.yaml data/taxa/bacteria/candidatus_thiomargarita_nelsonii.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_1.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_agona_str_sa_2.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The identity row in `data/raw/ncbitaxon_taxa.tsv` maps `NCBITaxon:1003181` to label `Candidatus Thiomargarita nelsonii`, rank `SPECIES`, parent `NCBITaxon:90372`, genetic code `11`, exact synonym `Thiomargarita nelsonii`, a set of NCBI related `Thiomargarita sp.` isolate synonyms, source bundle `ncbitaxon|gtdb|gold|madin_etal`, and snapshot date `2026-09-13`; the YAML carries those same identity fields.
- The root-first lineage is internally consistent and reaches `NCBITaxon:90372` through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, `Thiotrichales`, and `Thiotrichaceae`. Each checked ancestor had an exact local NCBI source row.
- The two GTDB mappings to `GTDB:s__Thiomargarita_nelsonii_A` and `GTDB:s__Thiomargarita_nelsonii_B` are correctly scoped as `skos:broadMatch`; both have one genome in `data/raw/gtdb_mappings.tsv` and `data/raw/gtdb_species.tsv`.

## Evidence

- The GOLD count of `11` organisms and the MADIN count of `3` trait assertions match `data/raw/gold_organisms.tsv` and `data/raw/madin_taxa.tsv`.
- Source attestations for NCBI, GTDB, GOLD, and MADIN all have supporting local rows.
- No unsupported biological claim or mismatched source identifier was found in the record body.

## Completeness

- The record correctly leaves causal-graph and strain slots absent; no causal graph or same-taxon BacDive strain was attested in the reviewed raw rows.
- Optional GTDB, GOLD, and MADIN surfaces that have same-taxon evidence are represented.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found no LPSN, BacDive, StrainInfo, medium, or strain-genome evidence that would require additional blocks for this record.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| minor | The generated `curation_history` says `attested by GOLD, GTDB, MADIN, NCBITAXON` but its scope reason from `curation/seed_scope.tsv` says `3 sources incl. NCBI`. The record body has four source-attestation groups, so the history prose undercounts by one source even though the biological assertions are supported. | `curation/seed_scope.tsv` row for `NCBITaxon:1003181`, produced by `scripts/propose_scope.py` and copied into generated records by `src/taxonmech/seed.py`. |

## Recommended Edits

- Make the scope-reason source count in `scripts/propose_scope.py` consistent with `src/taxonmech/seed.py`'s attestation grouping for broad GTDB mappings, or stop embedding a frozen source count in `curation/seed_scope.tsv`; then regenerate the `NCBITaxon:1003181` record from maintained inputs.

## Follow-up Checks

- Rerun the taxon generation step that owns `data/taxa/bacteria/candidatus_thiomargarita_nelsonii.yaml`.
- Rerun `just validate data/taxa/bacteria/candidatus_thiomargarita_nelsonii.yaml` and a strict validation over the regenerated file.
- Manually confirm that the regenerated `curation_history` count agrees with the regenerated `source_attestations`.

## Additional Notes

- A live authority audit beyond the pinned `2026-09-13` source snapshots was not run.
