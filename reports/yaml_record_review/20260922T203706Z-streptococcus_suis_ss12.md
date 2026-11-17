# YAML Record Review: Streptococcus suis SS12
- Repository: TaxonMech
- Record: `data/taxa/bacteria/streptococcus_suis_ss12.yaml`
- Started UTC: 2026-09-22T20:33:22Z
- Finished UTC: 2026-09-22T20:37:08Z
- Verdict: needs curation

## Target
- Reviewed `NCBITaxon:1005041` / `streptococcus_suis_ss12`.
- The record is a generated `STRAIN`-rank `BACTERIA` record for `Streptococcus suis SS12` under species parent `NCBITaxon:1307` (`Streptococcus suis`).
- The record is seeded from the pinned NCBITAXON, GTDB, and MADIN source inventories.

## Validation
- `just validate data/taxa/bacteria/streptococcus_suis_ss12.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/flexibacter_sp.yaml data/taxa/bacteria/fimbriimonas_ginsengisoli.yaml data/taxa/bacteria/streptococcus_suis_ss12.yaml data/taxa/bacteria/streptococcus_suis_d9.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005041`, `label: Streptococcus suis SS12`, `rank: STRAIN`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:1307`, and `genetic_code: 11` match the exact NCBI source row.
- The root-first lineage lands on the `Streptococcus suis` parent species, which is the right NCBI placement for this strain taxon.
- NCBI exact synonyms `Streptococcus suis str. SS12` and `Streptococcus suis strain SS12` preserve same-strain aliases from the NCBI row.
- The GTDB species cluster `GTDB:s__Streptococcus_suis` denotes the broader `Streptococcus suis` species cluster, not the SS12 strain.

## Evidence
- Exact-ID gitignore-independent `rg --no-ignore --hidden` searches across `data/raw`, `data/atb`, and `data/straininfo` found only the same-taxon NCBI row, the same-taxon Madin row, and the GTDB mapping row that projects `GTDB:s__Streptococcus_suis` onto `NCBITaxon:1005041`.
- `data/raw/gtdb_mappings.tsv` maps the 2,003-genome `GTDB:s__Streptococcus_suis` species cluster to the SS12 strain with `skos:closeMatch`; that local row is the source of the record's GTDB taxonomy mapping, xref, exact synonym, and GTDB source attestation.
- No exact-ID BacDive, MediaDive, LPSN, ATB, StrainInfo, or culture-collection rows were found for `NCBITaxon:1005041`, and `strain_count: 0` is therefore expected.

## Completeness
- The NCBI identity, parentage, two NCBI strain synonyms, and the one Madin trait-assertion count are present.
- There are no strain-level BacDive entries, culture-collection IDs, genome assemblies, or genome records for SS12 in the pinned local source rows searched with `rg --no-ignore --hidden`.
- The record is incomplete only through the over-scoped GTDB projection described below; it should not claim a species-cluster mapping as direct SS12 strain evidence.

## Findings
- **Major - GTDB species mapping is projected onto a strain.** `data/raw/gtdb_mappings.tsv` row 850 maps `GTDB:s__Streptococcus_suis` with 2,003 genomes to the strain-level `NCBITaxon:1005041` using `skos:closeMatch`. The generated YAML then emits a `taxonomy_mappings` entry, `xrefs: GTDB:s__Streptococcus_suis`, an exact synonym `Streptococcus suis`, and a GTDB source attestation on `Streptococcus suis SS12`. The species cluster is broader than one SS12 strain, so this mapping should not be represented as an exact strain synonym or same-taxon attestation. Future curation belongs in the `data/raw/gtdb_mappings.tsv` generation path and the GTDB taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`.

## Recommended Edits
- Regenerate or filter `data/raw/gtdb_mappings.tsv` so `GTDB:s__Streptococcus_suis` does not map as `skos:closeMatch` to `NCBITaxon:1005041`, then adjust `src/taxonmech/seed.py` as needed so GTDB species mappings are not projected into `taxonomy_mappings`, exact GTDB synonyms, GTDB `xrefs`, or GTDB source attestations on NCBI strain records.

## Follow-up Checks
- Re-run `just seed-canary NCBITaxon:1005041` and confirm the SS12 record still carries its NCBI and MADIN evidence but no direct `GTDB:s__Streptococcus_suis` mapping.
- Re-run `just validate data/taxa/bacteria/streptococcus_suis_ss12.yaml` and a focused `just validate-strict data/taxa/bacteria/streptococcus_suis_ss12.yaml` after re-seeding.
- Re-run a gitignore-independent exact-ID search for `NCBITaxon:1005041` across `data/raw`, `data/atb`, and `data/straininfo` to confirm no new same-taxon BacDive, LPSN, or culture-collection rows have become available.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-streptococcus_suis_ss12.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI, GTDB, and Madin lookups were not used; the pinned rows in `data/raw/` were treated as the local source of truth.
