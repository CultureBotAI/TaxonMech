# YAML Record Review: Penicillium hirsutum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/penicillium_hirsutum.yaml`
- Started UTC: 2026-09-24T01:54:29Z
- Finished UTC: 2026-09-24T01:54:29Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:36648` |
| Label | `Penicillium hirsutum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5073` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |
| Strain count | 0 |
| Maintained status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit `data/taxa/eukaryota/penicillium_hirsutum.yaml`. |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/eukaryota/penicillium_hirsutum.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/penicillium_hetheringtonii.yaml data/taxa/eukaryota/penicillium_hirayamae.yaml data/taxa/eukaryota/penicillium_hirsutum.yaml data/taxa/eukaryota/penicillium_hispanicum.yaml` | Passed in the review worktree; the strict validator exited successfully for this 4-record batch. |
| Bounded source scan over the committed NCBI, GOLD, BacDive, GTDB, LPSN, Madin, MediaDive, BactoTraits, and StrainInfo inputs | Passed; the generated record matched its source rows and no seeded target rows were missed. |
| Exact tab-anchored scan of `data/raw/ncbi_type_material.tsv` | Passed; found all 6 rows for `NCBITaxon:36648`. |
| `just verify-corpus` | Not rerun for this generated record; the full-corpus reproducibility gate had already passed on this checkout. |
| `just validate-history` | Not rerun for this generated record; the history gate had already passed on this checkout. |
| `just validate-products` | Not applicable; this seeded record has no `causal_graphs` or curator-added ontology nodes. |

## Identity and Grounding

The record identity is internally consistent and exactly grounded:

- `data/raw/ncbitaxon_taxa.tsv` line 4086 has `taxon_id` `NCBITaxon:36648`, label `Penicillium hirsutum`, rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, `attested_by` `gold`, no `retired_into`, and taxonomy snapshot `2026-09-13`.
- `curation/seed_scope.tsv` line 52343 retains the same identifier with reason `attested rule: Penicillium hirsutum, 2 sources incl. NCBI`.
- The 15-entry root-first lineage in the YAML matched the source lineage exactly; no ancestor was missing or mismatched.
- `data/raw/ncbi_merged_ids.tsv` line 88403 maps old `NCBITaxon:60179` into current `NCBITaxon:36648`, but an exact anchored search of `data/raw/ncbitaxon_taxa.tsv` found no retained retired row for `NCBITaxon:60179`; the empty generated `replaces` surface is therefore expected.

## Evidence

All seeded assertions checked against the committed source inventories are supported:

- The `NCBITAXON` attestation is supported by `data/raw/ncbitaxon_taxa.tsv` line 4086 and correctly reports one name assertion from the 2026-09-13 NCBI taxonomy snapshot.
- The exact synonyms `Penicillium corymbiferum` and `Penicillium hirsutum var. hirsutum` and the related synonym `Penicillium hirsutum Dierckx, 1901` match the NCBI row's synonym fields.
- The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv` line 33428, whose `NCBITaxon:36648` aggregate row reports `organism_count` `1`.
- NCBI type-material evidence is present in `data/raw/ncbi_type_material.tsv` lines 194874-194879 for ATCC 10429, CBS 135.41, and NRRL 2032 in the supplied space and colon formats. Those rows are not emitted as `strains` without a matching local BacDive-derived strain row.
- Exact StrainInfo hits exist for this taxon, but the three generated StrainInfo target tables had zero rows for `NCBITaxon:36648`; the generated record therefore correctly leaves StrainInfo genome and related-record links empty.

## Completeness

- `strain_count: 0` is consistent with zero target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The scanner found zero exact BacDive rows and zero generated StrainInfo overlay rows for this taxon.
- The optional `nomenclature`, `taxonomy_mappings`, and trait-derived slots are correctly absent: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/mediadive_taxa.tsv`, and `data/raw/bactotraits_taxa.tsv` had zero rows for this target.
- The single aggregate GOLD row supplies the one GOLD source attestation in the YAML; no additional GOLD-derived strain or genome link was eligible for emission because no classified local strain row joins to it.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:36648`, inspect the regenerated `data/taxa/eukaryota/penicillium_hirsutum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_hirsutum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_hirsutum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_hirsutum.md`, so the absence check included gitignored reports.
