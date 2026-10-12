# YAML Record Review: Cytophagales bacterium B6
- Repository: TaxonMech
- Record: `data/taxa/bacteria/cytophagales_bacterium_b6.yaml`
- Started UTC: 2026-09-22T20:14:00Z
- Finished UTC: 2026-09-22T20:15:42Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:100480` / `cytophagales_bacterium_b6`.
- The record is a `SPECIES`-rank `BACTERIA` record for `Cytophagales bacterium B6`.
- Parentage is the seeded NCBI placement under `NCBITaxon:37452` (`unclassified Bacteroidota`), with lineage through the `FCB group`, `Bacteroidota/Chlorobiota group`, and `Bacteroidota`.

## Validation
- `just validate data/taxa/bacteria/cytophagales_bacterium_b6.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/alteromonas_mediterranea_de1.yaml data/taxa/bacteria/alteromonas_macleodii_str_balearic_sea_ad45.yaml data/taxa/bacteria/alteromonas_macleodii_str_english_channel_673.yaml data/taxa/bacteria/cytophagales_bacterium_b6.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was not applicable because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `id: NCBITaxon:100480`, `label: Cytophagales bacterium B6`, `rank: SPECIES`, `domain: BACTERIA`, `parent: NCBITaxon:37452`, and `genetic_code: 11` match the pinned row in `data/raw/ncbitaxon_taxa.tsv`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon species record.
- The NCBI exact synonym `Cytophagales str. B6` is carried from the pinned NCBI row.

## Evidence
- Local same-taxon source rows for `NCBITaxon:100480` include `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`.
- `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Mucilaginibacter_oryzae` to this species with `skos:closeMatch` and `genome_count: 2`.
- `data/raw/gold_organisms.tsv` contributes one organism assertion.
- The BACDIVE-derived assembly evidence contains one NCBI assembly assertion plus IMG and BV-BRC genome-record links for `kgmicrobe.strain:bacdive_161515`, all keyed to `NCBITaxon:100480`.

## Completeness
- The record includes the expected NCBITAXON, GTDB, and GOLD source attestations from the pinned source rows.
- `strain_count: 0` is consistent with the absence of a same-taxon BacDive strain inventory row for `NCBITaxon:100480`; the BACDIVE assembly rows alone do not populate this taxon's strain list.
- The GTDB mapping, `Mucilaginibacter oryzae` GTDB synonym, and `GTDB:s__Mucilaginibacter_oryzae` xref are supported by exact same-taxon GTDB rows.

## Findings
- No findings.

## Recommended Edits
- None.

## Follow-up Checks
- None required for this record.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name *-cytophagales_bacterium_b6.md` returned no prior ignored report for this stem.
- Live NCBI and GTDB lookup were not used; local pinned source rows dated `2026-09-13` were treated as the source of truth.
