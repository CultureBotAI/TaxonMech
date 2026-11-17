# YAML Record Review: Penicillium jugoslavicum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/penicillium_jugoslavicum.yaml`
- Started UTC: 2026-09-24T02:05:07Z
- Finished UTC: 2026-09-24T02:05:07Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1167491` |
| Label | `Penicillium jugoslavicum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5073` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |
| Strain count | 0 |
| Maintained status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit `data/taxa/eukaryota/penicillium_jugoslavicum.yaml`. |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/eukaryota/penicillium_jugoslavicum.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/penicillium_jugoslavicum.yaml data/taxa/eukaryota/penicillium_kewense.yaml data/taxa/eukaryota/penicillium_kiamaense.yaml data/taxa/eukaryota/penicillium_kojigenum.yaml` | Passed in the review worktree; 4 files scanned, 0 files with errors, 0 total errors. |
| Bounded source scan over the committed NCBI, GOLD, BacDive, GTDB, LPSN, Madin, MediaDive, BactoTraits, and StrainInfo inputs | Passed; the generated record matched its source rows and no seeded target rows were missed. |
| Exact tab-anchored scan of `data/raw/ncbi_type_material.tsv` | Passed; found all 4 rows for `NCBITaxon:1167491`. |
| `just verify-corpus` | Not rerun for this generated record; the full-corpus reproducibility gate had already passed on this checkout. |
| `just validate-history` | Not rerun for this generated record; the history gate had already passed on this checkout. |
| `just validate-products` | Not applicable; this seeded record has no `causal_graphs` or curator-added ontology nodes. |

## Identity and Grounding

The record identity is internally consistent and exactly grounded:

- `data/raw/ncbitaxon_taxa.tsv` line 257891 has `taxon_id` `NCBITaxon:1167491`, label `Penicillium jugoslavicum`, rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, `attested_by` `gold`, no `retired_into`, and taxonomy snapshot `2026-09-13`.
- `curation/seed_scope.tsv` line 58094 retains the same identifier with reason `attested rule: Penicillium jugoslavicum, 2 sources incl. NCBI`.
- The 15-entry root-first lineage in the YAML matched the source lineage exactly; no ancestor was missing or mismatched.
- No `data/raw/ncbi_merged_ids.tsv` or retained retired-taxon row maps this target into another identifier, so the empty `replaces` surface is correct.

## Evidence

All seeded assertions checked against the committed source inventories are supported:

- The `NCBITAXON` attestation is supported by `data/raw/ncbitaxon_taxa.tsv` line 257891 and correctly reports one name assertion from the 2026-09-13 NCBI taxonomy snapshot.
- The two related `Penicillium jugoslavicum` authority synonyms match the pipe-separated `related_synonyms` value in the NCBI row.
- The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv` line 3562, whose `NCBITaxon:1167491` aggregate row reports `organism_count` `1`.
- Native GOLD rows also contain one exact organism, `Go0583238` for ITEM 17442, plus projects `Gp0586822` and `Gp0589693`.
- NCBI type-material evidence is present in `data/raw/ncbi_type_material.tsv` lines 10867-10870 for CBS 192.87 and IMI 314508 in the supplied space and colon formats. Those rows are not emitted as `strains` without a matching local BacDive-derived strain row.
- Exact StrainInfo hits exist for this taxon, but the three generated StrainInfo target tables had zero rows for `NCBITaxon:1167491`; the generated record therefore correctly leaves StrainInfo genome and related-record links empty.

## Completeness

- `strain_count: 0` is consistent with zero target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The scanner found zero exact BacDive rows and zero generated StrainInfo overlay rows for this taxon.
- The optional `nomenclature`, `taxonomy_mappings`, and trait-derived slots are correctly absent: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/mediadive_taxa.tsv`, and `data/raw/bactotraits_taxa.tsv` had zero rows for this target.
- The single aggregate GOLD row supplies the one GOLD source attestation in the YAML; the native GOLD projects do not emit related records because no classified local strain row joins to `Go0583238`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:1167491`, inspect the regenerated `data/taxa/eukaryota/penicillium_jugoslavicum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_jugoslavicum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_jugoslavicum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_jugoslavicum.md`, so the absence check included gitignored reports.
