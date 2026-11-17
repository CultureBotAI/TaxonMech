# YAML Record Review: Penicillium janthinellum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/penicillium_janthinellum.yaml`
- Started UTC: 2026-09-24T02:01:26Z
- Finished UTC: 2026-09-24T02:01:26Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5079` |
| Label | `Penicillium janthinellum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5073` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |
| Strain count | 0 |
| Maintained status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit `data/taxa/eukaryota/penicillium_janthinellum.yaml`. |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/eukaryota/penicillium_janthinellum.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/penicillium_irregulare.yaml data/taxa/eukaryota/penicillium_isariiforme.yaml data/taxa/eukaryota/penicillium_italicum.yaml data/taxa/eukaryota/penicillium_janthinellum.yaml` | Passed in the review worktree; 4 files scanned, 0 files with errors, 0 total errors. |
| Bounded source scan over the committed NCBI, GOLD, BacDive, GTDB, LPSN, Madin, MediaDive, BactoTraits, and StrainInfo inputs | Passed; the generated record matched its source rows and no seeded target rows were missed. |
| Exact tab-anchored scan of `data/raw/ncbi_type_material.tsv` | Passed; found both rows for `NCBITaxon:5079`. |
| `just verify-corpus` | Not rerun for this generated record; the full-corpus reproducibility gate had already passed on this checkout. |
| `just validate-history` | Not rerun for this generated record; the history gate had already passed on this checkout. |
| `just validate-products` | Not applicable; this seeded record has no `causal_graphs` or curator-added ontology nodes. |

## Identity and Grounding

The record identity is internally consistent and exactly grounded:

- `data/raw/ncbitaxon_taxa.tsv` line 2221 has `taxon_id` `NCBITaxon:5079`, label `Penicillium janthinellum`, rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, `attested_by` `gold`, no `retired_into`, and taxonomy snapshot `2026-09-13`.
- `curation/seed_scope.tsv` line 51930 retains the same identifier with reason `attested rule: Penicillium janthinellum, 2 sources incl. NCBI`.
- The 15-entry root-first lineage in the YAML matched the source lineage exactly; no ancestor was missing or mismatched.
- `data/raw/ncbi_merged_ids.tsv` line 37206 maps old `NCBITaxon:2081968` into current `NCBITaxon:5079`, but an exact anchored search of `data/raw/ncbitaxon_taxa.tsv` found no retained retired row for `NCBITaxon:2081968`; the empty generated `replaces` surface is therefore expected.

## Evidence

All seeded assertions checked against the committed source inventories are supported:

- The `NCBITAXON` attestation is supported by `data/raw/ncbitaxon_taxa.tsv` line 2221 and correctly reports one name assertion from the 2026-09-13 NCBI taxonomy snapshot.
- The exact synonym `Penicillium vitale` and the related synonym `Penicillium janthinellum Biourge, 1923` match the NCBI row's synonym fields.
- The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv` line 37455, whose `NCBITaxon:5079` aggregate row reports `organism_count` `3`.
- Native GOLD rows also contain three exact organisms: `Go0039214` for ATCC 10455, `Go0657980` for PG2902, and `Go0657981` for PG2901; the native project rows are `Gp0039214`, `Gp0039215`, `Gp0312055`, `Gp0702248`, and `Gp0702249`, and three of those projects have analysis rows.
- NCBI type-material evidence is present in `data/raw/ncbi_type_material.tsv` lines 225706-225707 for `CBS 340.48` and `CBS:340.48`. Those rows are not emitted as `strains` without a matching local BacDive-derived strain row.
- Exact StrainInfo hits exist for this taxon, but the three generated StrainInfo target tables had zero rows for `NCBITaxon:5079`; the generated record therefore correctly leaves StrainInfo genome and related-record links empty.

## Completeness

- `strain_count: 0` is consistent with zero target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The scanner found zero exact BacDive rows and zero generated StrainInfo overlay rows for this taxon.
- The optional `nomenclature`, `taxonomy_mappings`, and trait-derived slots are correctly absent: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/mediadive_taxa.tsv`, and `data/raw/bactotraits_taxa.tsv` had zero rows for this target.
- The three aggregate GOLD organism assertions supply the GOLD source attestation in the YAML; no additional GOLD-derived strain or genome link was eligible for emission because no classified local strain row joins to those organisms.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:5079`, inspect the regenerated `data/taxa/eukaryota/penicillium_janthinellum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_janthinellum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_janthinellum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_janthinellum.md`, so the absence check included gitignored reports.
