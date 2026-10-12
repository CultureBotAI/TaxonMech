# YAML Record Review: Candidatus Regiella insecticola 5.15
- Repository: TaxonMech
- Record: `data/taxa/bacteria/candidatus_regiella_insecticola_5_15.yaml`
- Started UTC: 2026-09-22T20:38:22Z
- Finished UTC: 2026-09-22T20:39:27Z
- Verdict: needs curation

## Target
- Reviewed `NCBITaxon:1005043` / `candidatus_regiella_insecticola_5_15`.
- The record is a generated `STRAIN`-rank `BACTERIA` record for `Candidatus Regiella insecticola 5.15` under species parent `NCBITaxon:138073` (`Candidatus Regiella insecticola`).
- The record is seeded from the pinned NCBITAXON, GTDB, GOLD, and MADIN source inventories.

## Validation
- `just validate data/taxa/bacteria/candidatus_regiella_insecticola_5_15.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/candidatus_regiella_insecticola_5_15.yaml data/taxa/bacteria/haemophilus_ducreyi_025.yaml data/taxa/bacteria/haemophilus_ducreyi_511.yaml data/taxa/bacteria/haemophilus_ducreyi_atcc_33921.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005043`, `label: Candidatus Regiella insecticola 5.15`, `rank: STRAIN`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:138073`, and `genetic_code: 11` match the exact NCBI source row.
- The root-first lineage lands under `Candidatus Regiella insecticola`, matching the NCBI strain placement.
- NCBI exact synonyms `Candidatus Regiella insecticola str. 5.15` and `Candidatus Regiella insecticola strain 5.15` are same-strain aliases.
- GTDB species cluster `GTDB:s__Regiella_insecticola` denotes the broader `Regiella insecticola` species cluster, not just strain `5.15`.

## Evidence
- Exact-ID gitignore-independent `rg --no-ignore --hidden` searches across `data/raw`, `data/atb`, and `data/straininfo` found the same-taxon NCBI row, one Gold organism row, one Madin trait row, and the GTDB mapping row that projects `GTDB:s__Regiella_insecticola` onto `NCBITaxon:1005043`.
- `data/raw/gtdb_mappings.tsv` row 852 maps the seven-genome `GTDB:s__Regiella_insecticola` species cluster to strain `NCBITaxon:1005043` with `skos:closeMatch`; that raw row explains the generated GTDB taxonomy mapping, xref, exact synonym, and GTDB source attestation.
- No exact-ID BacDive, LPSN, MediaDive, ATB, StrainInfo, or culture-collection rows were found for `NCBITaxon:1005043`, so the empty strain and genome sections are expected.

## Completeness
- The NCBI identity, NCBI strain synonyms, Gold organism count, and Madin trait-assertion count are present.
- `strain_count: 0` is consistent with the absence of exact same-taxon BacDive rows in the pinned local inventory.
- The record is incomplete only because its GTDB mapping should not assert that a seven-genome species cluster is equivalent to the `5.15` strain.

## Findings
- **Major - GTDB species mapping is projected onto a strain.** The `GTDB:s__Regiella_insecticola` species cluster is broader than `NCBITaxon:1005043`, but `data/raw/gtdb_mappings.tsv` row 852 maps it to the strain with `skos:closeMatch`, producing a same-taxon GTDB `taxonomy_mappings` entry, GTDB xref, exact synonym `Regiella insecticola`, and seven-genome source attestation on this strain record. Future curation belongs in the `data/raw/gtdb_mappings.tsv` generation path and the GTDB taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`.

## Recommended Edits
- Regenerate or filter `data/raw/gtdb_mappings.tsv` so `GTDB:s__Regiella_insecticola` is not projected as a `skos:closeMatch` to `NCBITaxon:1005043`, then adjust `src/taxonmech/seed.py` as needed to keep GTDB species clusters from generating exact GTDB synonyms, xrefs, taxonomy mappings, or same-taxon GTDB attestations on strain records.

## Follow-up Checks
- Re-run `just seed-canary NCBITaxon:1005043` and confirm the `5.15` record keeps its NCBITAXON, GOLD, and MADIN attestations but no direct `GTDB:s__Regiella_insecticola` mapping.
- Re-run `just validate data/taxa/bacteria/candidatus_regiella_insecticola_5_15.yaml` and a focused `just validate-strict data/taxa/bacteria/candidatus_regiella_insecticola_5_15.yaml` after re-seeding.
- Re-run a gitignore-independent exact-ID source search for `NCBITaxon:1005043` across `data/raw`, `data/atb`, and `data/straininfo` to confirm no new same-taxon BacDive or culture-collection rows have become available.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-candidatus_regiella_insecticola_5_15.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI, GTDB, Gold, and Madin lookups were not used; the pinned rows in `data/raw/` were treated as the local source of truth.
