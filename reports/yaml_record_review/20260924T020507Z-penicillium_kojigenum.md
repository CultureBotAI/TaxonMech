# YAML Record Review: Penicillium kojigenum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/penicillium_kojigenum.yaml`
- Started UTC: 2026-09-24T02:05:07Z
- Finished UTC: 2026-09-24T02:05:07Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:70098` |
| Label | `Penicillium kojigenum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5073` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |
| Strain count | 0 |
| Maintained status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit `data/taxa/eukaryota/penicillium_kojigenum.yaml`. |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/eukaryota/penicillium_kojigenum.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/penicillium_jugoslavicum.yaml data/taxa/eukaryota/penicillium_kewense.yaml data/taxa/eukaryota/penicillium_kiamaense.yaml data/taxa/eukaryota/penicillium_kojigenum.yaml` | Passed in the review worktree; 4 files scanned, 0 files with errors, 0 total errors. |
| Bounded source scan over the committed NCBI, GOLD, BacDive, GTDB, LPSN, Madin, MediaDive, BactoTraits, and StrainInfo inputs | Passed; the generated record matched its source rows and no seeded target rows were missed. |
| Exact tab-anchored scan of `data/raw/ncbi_type_material.tsv` | Passed; found all 20 rows for `NCBITaxon:70098`. |
| `just verify-corpus` | Not rerun for this generated record; the full-corpus reproducibility gate had already passed on this checkout. |
| `just validate-history` | Not rerun for this generated record; the history gate had already passed on this checkout. |
| `just validate-products` | Not applicable; this seeded record has no `causal_graphs` or curator-added ontology nodes. |

## Identity and Grounding

The record identity is internally consistent and exactly grounded:

- `data/raw/ncbitaxon_taxa.tsv` line 9771 has `taxon_id` `NCBITaxon:70098`, label `Penicillium kojigenum`, rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, `attested_by` `gold`, no `retired_into`, and taxonomy snapshot `2026-09-13`.
- `curation/seed_scope.tsv` line 53201 retains the same identifier with reason `attested rule: Penicillium kojigenum, 2 sources incl. NCBI`.
- The 15-entry root-first lineage in the YAML matched the source lineage exactly; no ancestor was missing or mismatched.
- No `data/raw/ncbi_merged_ids.tsv` or retained retired-taxon row maps this target into another identifier, so the empty `replaces` surface is correct.

## Evidence

All seeded assertions checked against the committed source inventories are supported:

- The `NCBITAXON` attestation is supported by `data/raw/ncbitaxon_taxa.tsv` line 9771 and correctly reports one name assertion from the 2026-09-13 NCBI taxonomy snapshot.
- The related synonym `Penicillium kojigenum G. Sm., 1961` matches the `related_synonyms` value in the NCBI row.
- The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv` line 41618, whose `NCBITaxon:70098` aggregate row reports `organism_count` `1`.
- NCBI type-material evidence is present in `data/raw/ncbi_type_material.tsv` lines 258658-258677 for ATCC 18227, BCRC 31515, CBS 345.61, CCRC 31515, FRR 3442, IFO 9581, IMI 086562, LSHB BB394, MUCL 2457, NRRL 3442, and QM 7957 in the supplied space and colon formats. Those rows are not emitted as `strains` without a matching local BacDive-derived strain row.
- Deposit-level StrainInfo exact hits exist for this taxon, but the three generated StrainInfo target tables had zero rows for `NCBITaxon:70098`; the generated record therefore correctly leaves StrainInfo genome and related-record links empty.

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

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:70098`, inspect the regenerated `data/taxa/eukaryota/penicillium_kojigenum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_kojigenum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_kojigenum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_kojigenum.md`, so the absence check included gitignored reports.
