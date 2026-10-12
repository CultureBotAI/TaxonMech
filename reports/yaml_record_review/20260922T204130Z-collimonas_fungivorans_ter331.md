# YAML Record Review: Collimonas fungivorans Ter331
- Repository: TaxonMech
- Record: `data/taxa/bacteria/collimonas_fungivorans_ter331.yaml`
- Started UTC: 2026-09-22T20:40:28Z
- Finished UTC: 2026-09-22T20:41:32Z
- Verdict: needs curation

## Target
- Reviewed `NCBITaxon:1005048` / `collimonas_fungivorans_ter331`.
- The record is a generated `STRAIN`-rank `BACTERIA` record for `Collimonas fungivorans Ter331` under species parent `NCBITaxon:158899` (`Collimonas fungivorans`).
- The record is seeded from the pinned NCBITAXON, GTDB, and MADIN source inventories.

## Validation
- `just validate data/taxa/bacteria/collimonas_fungivorans_ter331.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/haemophilus_ducreyi_hmc112.yaml data/taxa/bacteria/collimonas_fungivorans_ter331.yaml data/taxa/bacteria/buchnera_aphidicola_str_ua_uroleucon_ambrosiae.yaml data/taxa/bacteria/gallibacterium_anatis_umn179.yaml` completed successfully for the four-file batch.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005048`, `label: Collimonas fungivorans Ter331`, `rank: STRAIN`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:158899`, and `genetic_code: 11` match the exact NCBI source row.
- The NCBI aliases `Collimonas fungivorans str. Ter331`, `Collimonas fungivorans strain Ter331`, and `beta proteobacterium Ter331` are same-strain synonyms from the same NCBI row.
- GTDB species cluster `GTDB:s__Collimonas_fungivorans_A` denotes a broader two-genome species cluster, not just strain `Ter331`.

## Evidence
- Exact-ID gitignore-independent `rg --no-ignore --hidden` searches across `data/raw`, `data/atb`, and `data/straininfo` found the same-taxon NCBI row, one Madin trait row with six trait assertions, and the GTDB mapping row that projects `GTDB:s__Collimonas_fungivorans_A` onto `NCBITaxon:1005048`.
- `data/raw/gtdb_mappings.tsv` row 853 maps the two-genome `GTDB:s__Collimonas_fungivorans_A` species cluster directly to strain `NCBITaxon:1005048` with `skos:closeMatch`.
- No exact-ID BacDive, LPSN, MediaDive, ATB, StrainInfo, or culture-collection rows were found for `NCBITaxon:1005048`, so the empty strain and genome sections are expected.

## Completeness
- The NCBI identity, NCBI strain synonyms, and Madin trait-assertion count are present.
- `strain_count: 0` is consistent with the absence of exact same-taxon BacDive rows in the pinned local inventory.
- The record is incomplete only through the over-scoped GTDB projection described below.

## Findings
- **Major - GTDB species mapping is projected onto a strain.** The two-genome `GTDB:s__Collimonas_fungivorans_A` species cluster is broader than `NCBITaxon:1005048`, but `data/raw/gtdb_mappings.tsv` row 853 maps it to the strain with `skos:closeMatch`, producing a same-taxon GTDB `taxonomy_mappings` entry, GTDB xref, exact synonym `Collimonas fungivorans A`, and GTDB source attestation on this strain record. Future curation belongs in the `data/raw/gtdb_mappings.tsv` generation path and the GTDB taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`.

## Recommended Edits
- Regenerate or filter `data/raw/gtdb_mappings.tsv` so `GTDB:s__Collimonas_fungivorans_A` is not projected as a `skos:closeMatch` to `NCBITaxon:1005048`, then adjust `src/taxonmech/seed.py` as needed to avoid species-cluster taxonomy mappings, exact GTDB synonyms, xrefs, and same-taxon GTDB attestations on strain records.

## Follow-up Checks
- Re-run `just seed-canary NCBITaxon:1005048` and confirm the `Ter331` record keeps its NCBITAXON and MADIN attestations but no direct `GTDB:s__Collimonas_fungivorans_A` mapping.
- Re-run `just validate data/taxa/bacteria/collimonas_fungivorans_ter331.yaml` and a focused `just validate-strict data/taxa/bacteria/collimonas_fungivorans_ter331.yaml` after re-seeding.
- Re-run a gitignore-independent exact-ID source search for `NCBITaxon:1005048` across `data/raw`, `data/atb`, and `data/straininfo` to confirm no new same-taxon BacDive or culture-collection rows have become available.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-collimonas_fungivorans_ter331.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI, GTDB, and Madin lookups were not used; the pinned rows in `data/raw/` were treated as the local source of truth.
