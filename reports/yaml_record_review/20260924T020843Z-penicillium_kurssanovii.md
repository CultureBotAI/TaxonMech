# YAML Record Review: Penicillium kurssanovii

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/penicillium_kurssanovii.yaml`
- Started UTC: 2026-09-24T02:08:43Z
- Finished UTC: 2026-09-24T02:08:43Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:446509` |
| Label | `Penicillium kurssanovii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5073` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |
| Strain count | 0 |
| Maintained status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit `data/taxa/eukaryota/penicillium_kurssanovii.yaml`. |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/eukaryota/penicillium_kurssanovii.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/penicillium_kongii.yaml data/taxa/eukaryota/penicillium_kurssanovii.yaml data/taxa/eukaryota/penicillium_laevigatum.yaml data/taxa/eukaryota/penicillium_lanosocoeruleum.yaml` | Passed in the review worktree; 4 files scanned, 0 files with errors, 0 total errors. |
| Bounded source scan over the committed NCBI, GOLD, BacDive, GTDB, LPSN, Madin, MediaDive, BactoTraits, and StrainInfo inputs | Passed; the generated record matched its source rows and no seeded target rows were missed. |
| Exact tab-anchored scan of `data/raw/ncbi_type_material.tsv` | Passed; found all 15 rows for `NCBITaxon:446509`. |
| `just verify-corpus` | Not rerun for this generated record; the full-corpus reproducibility gate had already passed on this checkout. |
| `just validate-history` | Not rerun for this generated record; the history gate had already passed on this checkout. |
| `just validate-products` | Not applicable; this seeded record has no `causal_graphs` or curator-added ontology nodes. |

## Identity and Grounding

The record identity is internally consistent and exactly grounded:

- `data/raw/ncbitaxon_taxa.tsv` line 99387 has `taxon_id` `NCBITaxon:446509`, label `Penicillium kurssanovii`, rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, `attested_by` `gold`, no `retired_into`, and taxonomy snapshot `2026-09-13`.
- `curation/seed_scope.tsv` line 55677 retains the same identifier with reason `attested rule: Penicillium kurssanovii, 2 sources incl. NCBI`.
- The 15-entry root-first lineage in the YAML matched the source lineage exactly; no ancestor was missing or mismatched.
- No `data/raw/ncbi_merged_ids.tsv` or retained retired-taxon row maps this target into another identifier, so the empty `replaces` surface is correct.

## Evidence

All seeded assertions checked against the committed source inventories are supported:

- The `NCBITAXON` attestation is supported by `data/raw/ncbitaxon_taxa.tsv` line 99387 and correctly reports one name assertion from the 2026-09-13 NCBI taxonomy snapshot.
- The related synonym `Penicillium kurssanovii Chalab., 1950` matches the `related_synonyms` value in the NCBI row.
- The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv` line 35739, whose `NCBITaxon:446509` aggregate row reports `organism_count` `1`.
- NCBI type-material evidence is present in `data/raw/ncbi_type_material.tsv` lines 212764-212778 for ATCC 18387, CBS 625.67, FRR 3381, IJFM 5045, IMI 129965, NRRL 3381, and VKM F-1244 in the supplied space and colon formats. Those rows are not emitted as `strains` without a matching local BacDive-derived strain row.

## Completeness

- `strain_count: 0` is consistent with zero target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The scanner found zero exact BacDive rows, zero direct or deposit StrainInfo exact rows, and zero generated StrainInfo overlay rows for this taxon.
- The optional `nomenclature`, `taxonomy_mappings`, and trait-derived slots are correctly absent: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/mediadive_taxa.tsv`, and `data/raw/bactotraits_taxa.tsv` had zero rows for this target.
- The single aggregate GOLD row supplies the one GOLD source attestation in the YAML; no additional GOLD-derived strain or genome link was eligible for emission because no classified local strain row joins to it.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:446509`, inspect the regenerated `data/taxa/eukaryota/penicillium_kurssanovii.yaml`, then run `just validate data/taxa/eukaryota/penicillium_kurssanovii.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_kurssanovii.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_kurssanovii.md`, so the absence check included gitignored reports.
