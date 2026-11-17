# YAML Record Review: Buchnera aphidicola str. Ak (Acyrthosiphon kondoi)
- Repository: TaxonMech
- Record: `data/taxa/bacteria/buchnera_aphidicola_str_ak_acyrthosiphon_kondoi.yaml`
- Started UTC: 2026-09-22T20:42:32Z
- Finished UTC: 2026-09-22T20:43:24Z
- Verdict: needs curation

## Target
- Reviewed `NCBITaxon:1005090` / `buchnera_aphidicola_str_ak_acyrthosiphon_kondoi`.
- The record is a generated `STRAIN`-rank `BACTERIA` record for `Buchnera aphidicola str. Ak (Acyrthosiphon kondoi)` under forma-specialis parent `NCBITaxon:668607` (`Buchnera aphidicola (Acyrthosiphon kondoi)`).
- The record is seeded from the pinned NCBITAXON, GTDB, GOLD, and MADIN source inventories.

## Validation
- `just validate data/taxa/bacteria/buchnera_aphidicola_str_ak_acyrthosiphon_kondoi.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/buchnera_aphidicola_str_ak_acyrthosiphon_kondoi.yaml data/taxa/bacteria/clostridium_sp_bj1.yaml data/taxa/bacteria/clostridium_sp_bj2.yaml data/taxa/bacteria/streptomyces_sp_udsc1.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005090`, `label: Buchnera aphidicola str. Ak (Acyrthosiphon kondoi)`, `rank: STRAIN`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:668607`, and `genetic_code: 11` match the exact NCBI source row.
- The `FORMA_SPECIALIS` parent below `Buchnera aphidicola` is carried from the pinned NCBI lineage.
- The NCBI synonym `Buchnera aphidicola strain Ak (Acyrthosiphon kondoi)` is a same-strain alias from the NCBI row.
- GTDB species cluster `GTDB:s__Buchnera_aphidicola_A` is a two-genome GTDB species-level cluster, not a one-to-one identity for the `Ak` strain.

## Evidence
- Exact-ID gitignore-independent `rg --no-ignore --hidden` searches across `data/raw`, `data/atb`, and `data/straininfo` found the same-taxon NCBI row, one Gold organism row, one Madin trait row, and the GTDB mapping row that projects `GTDB:s__Buchnera_aphidicola_A` onto `NCBITaxon:1005090`.
- `data/raw/gtdb_mappings.tsv` row 856 maps `GTDB:s__Buchnera_aphidicola_A` directly to strain `NCBITaxon:1005090` with `skos:closeMatch`.
- No exact-ID BacDive, LPSN, MediaDive, ATB, StrainInfo, or culture-collection rows were found for `NCBITaxon:1005090`, so the empty strain and genome sections are expected.

## Completeness
- The NCBI identity, one NCBI strain synonym, Gold organism count, and Madin trait-assertion count are present.
- `strain_count: 0` is consistent with the absence of exact same-taxon BacDive rows in the pinned local inventory.
- The record is incomplete only through the GTDB species cluster being treated as a direct strain-level mapping.

## Findings
- **Major - GTDB species mapping is projected onto a strain.** The two-genome `GTDB:s__Buchnera_aphidicola_A` species cluster is broader than `NCBITaxon:1005090`, but `data/raw/gtdb_mappings.tsv` row 856 maps it to the strain with `skos:closeMatch`, producing a same-taxon GTDB `taxonomy_mappings` entry, GTDB xref, exact synonym `Buchnera aphidicola A`, and GTDB source attestation on this strain record. Future curation belongs in the `data/raw/gtdb_mappings.tsv` generation path and the GTDB taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`.

## Recommended Edits
- Regenerate or filter `data/raw/gtdb_mappings.tsv` so `GTDB:s__Buchnera_aphidicola_A` is not projected as a `skos:closeMatch` to `NCBITaxon:1005090`, then adjust `src/taxonmech/seed.py` as needed to avoid species-cluster taxonomy mappings, exact GTDB synonyms, xrefs, and same-taxon GTDB attestations on strain records.

## Follow-up Checks
- Re-run `just seed-canary NCBITaxon:1005090` and confirm the Ak record keeps its NCBITAXON, GOLD, and MADIN attestations but no direct `GTDB:s__Buchnera_aphidicola_A` mapping.
- Re-run `just validate data/taxa/bacteria/buchnera_aphidicola_str_ak_acyrthosiphon_kondoi.yaml` and a focused `just validate-strict data/taxa/bacteria/buchnera_aphidicola_str_ak_acyrthosiphon_kondoi.yaml` after re-seeding.
- Re-run a gitignore-independent exact-ID source search for `NCBITaxon:1005090` across `data/raw`, `data/atb`, and `data/straininfo` to confirm no new same-taxon BacDive or culture-collection rows have become available.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-buchnera_aphidicola_str_ak_acyrthosiphon_kondoi.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI, GTDB, Gold, and Madin lookups were not used; the pinned rows in `data/raw/` were treated as the local source of truth.
