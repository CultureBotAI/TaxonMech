# YAML Record Review: Penicillium gravinicasei

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/penicillium_gravinicasei.yaml`
- Started UTC: 2026-09-24T01:46:40Z
- Finished UTC: 2026-09-24T01:46:40Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2055942` |
| Label | `Penicillium gravinicasei` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5073` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |
| Strain count | 0 |
| Maintained status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit `data/taxa/eukaryota/penicillium_gravinicasei.yaml`. |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/eukaryota/penicillium_gravinicasei.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/penicillium_granulatum.yaml data/taxa/eukaryota/penicillium_gravinicasei.yaml data/taxa/eukaryota/penicillium_griseoazureum.yaml data/taxa/eukaryota/penicillium_griseofulvum.yaml` | Passed in the review worktree; 4 files scanned, 0 files with errors, 0 total errors. |
| Bounded source scan over the committed NCBI, GOLD, BacDive, GTDB, LPSN, Madin, MediaDive, BactoTraits, and StrainInfo inputs | Passed; the generated record matched its source rows and no seeded target rows were missed. |
| Exact tab-anchored scan of `data/raw/ncbi_type_material.tsv` | Passed; found both rows for `NCBITaxon:2055942`. |
| `just verify-corpus` | Not rerun for this generated record; the full-corpus reproducibility gate had already passed on this checkout. |
| `just validate-history` | Not rerun for this generated record; the history gate had already passed on this checkout. |
| `just validate-products` | Not applicable; this seeded record has no `causal_graphs` or curator-added ontology nodes. |

## Identity and Grounding

The record identity is internally consistent and exactly grounded:

- `data/raw/ncbitaxon_taxa.tsv` line 514446 has `taxon_id` `NCBITaxon:2055942`, label `Penicillium gravinicasei`, rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, `attested_by` `gold`, no `retired_into`, and taxonomy snapshot `2026-09-13`.
- `curation/seed_scope.tsv` line 62232 retains the same identifier with reason `attested rule: Penicillium gravinicasei, 2 sources incl. NCBI`.
- The 15-entry root-first lineage in the YAML matched the source lineage exactly; no ancestor was missing or mismatched.
- No `data/raw/ncbi_merged_ids.tsv` or retained retired-taxon row maps this target into another identifier, so the empty `replaces` surface is correct.

## Evidence

All seeded assertions checked against the committed source inventories are supported:

- The `NCBITAXON` attestation is supported by `data/raw/ncbitaxon_taxa.tsv` line 514446 and correctly reports one name assertion from the 2026-09-13 NCBI taxonomy snapshot.
- The related synonyms `Penicillium gravinicasei S.W. Peterson, P. Anelli, Haidukowski & Susca, 2018` and `Penicillium sp. AS-2017` match the pipe-separated `related_synonyms` value in the NCBI row.
- The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv` line 19627, whose `NCBITaxon:2055942` aggregate row reports `organism_count` `1`.
- Native GOLD rows also contain one exact organism, `Go0583237` for `Penicillium gravinicasei ITEM 17411`, plus two projects, `Gp0586821` and `Gp0589692`, tied to that organism.
- NCBI type-material evidence is present in `data/raw/ncbi_type_material.tsv` lines 81668-81669 for `NRRL 66733` and `NRRL:66733`. Those rows are not emitted as `strains` without a matching local BacDive-derived strain row.

## Completeness

- `strain_count: 0` is consistent with zero target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The scanner found zero exact BacDive rows and zero direct or deposit StrainInfo exact rows for this taxon.
- The optional `nomenclature`, `taxonomy_mappings`, and trait-derived slots are correctly absent: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/mediadive_taxa.tsv`, and `data/raw/bactotraits_taxa.tsv` had zero rows for this target.
- The single aggregate GOLD row supplies the one GOLD source attestation in the YAML; the native GOLD projects do not emit related records because no classified local strain row joins to `Go0583237`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:2055942`, inspect the regenerated `data/taxa/eukaryota/penicillium_gravinicasei.yaml`, then run `just validate data/taxa/eukaryota/penicillium_gravinicasei.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_gravinicasei.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_gravinicasei.md`, so the absence check included gitignored reports.
