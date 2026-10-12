# YAML Record Review: Buchnera aphidicola str. Ua (Uroleucon ambrosiae)
- Repository: TaxonMech
- Record: `data/taxa/bacteria/buchnera_aphidicola_str_ua_uroleucon_ambrosiae.yaml`
- Started UTC: 2026-09-22T20:40:28Z
- Finished UTC: 2026-09-22T20:41:32Z
- Verdict: needs curation

## Target
- Reviewed `NCBITaxon:1005057` / `buchnera_aphidicola_str_ua_uroleucon_ambrosiae`.
- The record is a generated `STRAIN`-rank `BACTERIA` record for `Buchnera aphidicola str. Ua (Uroleucon ambrosiae)` under forma-specialis parent `NCBITaxon:118117` (`Buchnera aphidicola (Uroleucon ambrosiae)`).
- The record is seeded from the pinned NCBITAXON, GTDB, GOLD, and MADIN source inventories.

## Validation
- `just validate data/taxa/bacteria/buchnera_aphidicola_str_ua_uroleucon_ambrosiae.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/haemophilus_ducreyi_hmc112.yaml data/taxa/bacteria/collimonas_fungivorans_ter331.yaml data/taxa/bacteria/buchnera_aphidicola_str_ua_uroleucon_ambrosiae.yaml data/taxa/bacteria/gallibacterium_anatis_umn179.yaml` completed successfully for the four-file batch.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005057`, `label: Buchnera aphidicola str. Ua (Uroleucon ambrosiae)`, `rank: STRAIN`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:118117`, and `genetic_code: 11` match the exact NCBI source row.
- The lineage's `FORMA_SPECIALIS` parent below `Buchnera aphidicola` is the pinned NCBI placement for this strain.
- The NCBI synonym `Buchnera aphidicola strain Ua (Uroleucon ambrosiae)` is a same-strain alias from the NCBI row.
- GTDB species cluster `GTDB:s__Buchnera_aphidicola_B` is still a GTDB species-level cluster even though the local species row has only one genome.

## Evidence
- Exact-ID gitignore-independent `rg --no-ignore --hidden` searches across `data/raw`, `data/atb`, and `data/straininfo` found the same-taxon NCBI row, one Gold organism row, one Madin trait row, and the GTDB mapping row that projects `GTDB:s__Buchnera_aphidicola_B` onto `NCBITaxon:1005057`.
- `data/raw/gtdb_mappings.tsv` row 854 maps `GTDB:s__Buchnera_aphidicola_B` directly to strain `NCBITaxon:1005057` with `skos:closeMatch`.
- No exact-ID BacDive, LPSN, MediaDive, ATB, StrainInfo, or culture-collection rows were found for `NCBITaxon:1005057`, so the empty strain and genome sections are expected.

## Completeness
- The NCBI identity, one NCBI strain synonym, Gold organism count, and Madin trait-assertion count are present.
- `strain_count: 0` is consistent with the absence of exact same-taxon BacDive rows in the pinned local inventory.
- The record is incomplete only through the GTDB species cluster being treated as a direct strain-level mapping.

## Findings
- **Major - GTDB species mapping is projected onto a strain.** `GTDB:s__Buchnera_aphidicola_B` is a GTDB species cluster, but `data/raw/gtdb_mappings.tsv` row 854 maps it to the strain-level `NCBITaxon:1005057` with `skos:closeMatch`, producing a same-taxon GTDB `taxonomy_mappings` entry, GTDB xref, exact synonym `Buchnera aphidicola B`, and GTDB source attestation on this strain record. Future curation belongs in the `data/raw/gtdb_mappings.tsv` generation path and the GTDB taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`.

## Recommended Edits
- Regenerate or filter `data/raw/gtdb_mappings.tsv` so `GTDB:s__Buchnera_aphidicola_B` is not projected as a `skos:closeMatch` to `NCBITaxon:1005057`, then adjust `src/taxonmech/seed.py` as needed to avoid species-cluster taxonomy mappings, exact GTDB synonyms, xrefs, and same-taxon GTDB attestations on strain records.

## Follow-up Checks
- Re-run `just seed-canary NCBITaxon:1005057` and confirm the Ua record keeps its NCBITAXON, GOLD, and MADIN attestations but no direct `GTDB:s__Buchnera_aphidicola_B` mapping.
- Re-run `just validate data/taxa/bacteria/buchnera_aphidicola_str_ua_uroleucon_ambrosiae.yaml` and a focused `just validate-strict data/taxa/bacteria/buchnera_aphidicola_str_ua_uroleucon_ambrosiae.yaml` after re-seeding.
- Re-run a gitignore-independent exact-ID source search for `NCBITaxon:1005057` across `data/raw`, `data/atb`, and `data/straininfo` to confirm no new same-taxon BacDive or culture-collection rows have become available.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-buchnera_aphidicola_str_ua_uroleucon_ambrosiae.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI, GTDB, Gold, and Madin lookups were not used; the pinned rows in `data/raw/` were treated as the local source of truth.
