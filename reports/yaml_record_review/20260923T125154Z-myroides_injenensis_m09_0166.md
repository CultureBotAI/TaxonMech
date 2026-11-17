# YAML Record Review: Myroides injenensis M09-0166

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/myroides_injenensis_m09_0166.yaml
- Started UTC: 2026-09-23T12:48:06Z
- Finished UTC: 2026-09-23T12:51:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1008457` |
| Label | `Myroides injenensis M09-0166` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1183151` `Myroides injenensis` |
| Status | `grounding_status: EXACT`; `mapping_status: SEEDED` |
| Maintained? | Generated under `data/taxa/`; future fixes belong in `data/raw/gtdb_mappings.tsv` generation and in `src/taxonmech/seed.py`, not in this YAML |

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*myroides_injenensis_m09_0166.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/myroides_injenensis_m09_0166.yaml data/taxa/bacteria/taylorella_asinigenitalis_mce3.yaml data/taxa/archaea/pyrococcus_yayanosii.yaml data/taxa/bacteria/shinella_sp_agr1.yaml` | Passed: 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate data/taxa/bacteria/myroides_injenensis_m09_0166.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: this record has no `causal_graphs`, and the product id/label gate is only for curator-added graph nodes |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

The NCBI row in `data/raw/ncbitaxon_taxa.tsv:211406` supports the record identifier, label, `STRAIN` rank, `NCBITaxon:1183151` parent, genetic code `11`, three NCBI exact synonyms, the `ncbitaxon|gtdb|madin_etal` source flags, and the `2026-09-13` NCBI snapshot note. `curation/seed_scope.tsv:36073` carries the matching attested-scope row for this exact identifier and label.

The root-to-species lineage in `data/taxa/bacteria/myroides_injenensis_m09_0166.yaml:6` is internally consistent with a bacterial strain under `Myroides injenensis`, and `taxon_domain: BACTERIA` matches the `NCBITaxon:2` domain ancestor.

`data/raw/madin_taxa.tsv:394` supports the `MADIN` source attestation with one `TRAIT_ASSERTION`. Exact gitignore-independent searches across `data/atb/`, `data/straininfo/`, `data/raw/gold_organisms.tsv`, `data/raw/mediadive_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no same-taxon rows for `NCBITaxon:1008457`; no AllTheBacteria, StrainInfo, GOLD, MediaDive, BactoTraits, merged-id, or dropped-source block is therefore expected on this record.

## Evidence

The seeded NCBI synonyms at `data/taxa/bacteria/myroides_injenensis_m09_0166.yaml:56` are exactly the synonym pipe from `data/raw/ncbitaxon_taxa.tsv:211406`. The `source_attestations` block at `data/taxa/bacteria/myroides_injenensis_m09_0166.yaml:70` agrees with the exact NCBI and MADIN rows.

The pinned BacDive strain and genome rows for `M09-0166` are classed through `kgmicrobe.strain:bacdive_162021`, which `data/raw/bacdive_strains.tsv:84258` files under the parent species `NCBITaxon:1183151`. The BacDive assembly, IMG, and PATRIC rows in `data/raw/strain_assemblies.tsv:73228` and `data/raw/strain_genome_records.tsv:57137-57138` also keep `NCBITaxon:1008457` as the genome taxon metadata, and those rows are published on `data/taxa/bacteria/myroides_injenensis.yaml` as a child strain gathered under the species. They do not require a BacDive strain block on this strain-level NCBI record.

The GTDB block is over-projected. `data/raw/gtdb_mappings.tsv:1104` maps the two-genome cluster `GTDB:s__Flavobacterium_injenense` to this strain as `skos:closeMatch`, while `data/raw/gtdb_mappings.tsv:10299` maps the same two-genome species cluster to the parent species `NCBITaxon:1183151`. That cluster is broader than a single `M09-0166` strain, but `data/taxa/bacteria/myroides_injenensis_m09_0166.yaml:45` emits it as this strain's `taxonomy_mappings`, `xrefs`, `GTDB` source attestation, and `EXACT_SYNONYM`.

## Completeness

The strain has no `nomenclature`, `strains`, `evidence`, `definition`, `discussions`, or `causal_graphs`, which is consistent with the pinned rows for this exact NCBI taxon. `strain_count: 0` is consistent because the known BacDive row is classed to the parent `Myroides injenensis` species, not directly to `NCBITaxon:1008457`.

Exact gitignore-independent raw searches covered the identifier, slug, and label in the same-taxon source locations under `data/raw/`, `data/atb/`, and `data/straininfo/`. The only consequential completeness problem is the over-specific GTDB projection described above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `GTDB:s__Flavobacterium_injenense` is emitted as a strain-level xref, exact synonym, mapping, and source attestation even though that GTDB species cluster spans two genomes and is also mapped to the parent `Myroides injenensis` species. | `data/taxa/bacteria/myroides_injenensis_m09_0166.yaml:45-66` publishes the cluster as exact-looking strain identity; `data/raw/gtdb_mappings.tsv:1104` and `data/raw/gtdb_mappings.tsv:10299` show the same cluster mapped to both the strain and the species; `src/taxonmech/seed.py:447-468` promotes every `skos:closeMatch` GTDB row to an `xref` and `EXACT_SYNONYM`. | `data/raw/gtdb_mappings.tsv` generation plus the GTDB identity test in `src/taxonmech/seed.py` |

## Recommended Edits

1. Stop treating every GTDB `skos:closeMatch` as strain identity in `src/taxonmech/seed.py`. A GTDB species cluster should not become a strain-level `xref` or `EXACT_SYNONYM` unless the mapping is independently known to denote the same infraspecific taxon.
2. Review the kg-microbe `GTDB:s__Flavobacterium_injenense` mapping generation that produced close-match rows for both `NCBITaxon:1008457` and `NCBITaxon:1183151`. Re-extract `data/raw/gtdb_mappings.tsv` after that upstream predicate logic is corrected.
3. Re-run the seeder so `data/taxa/bacteria/myroides_injenensis_m09_0166.yaml` retains only source claims scoped to the `M09-0166` NCBI strain.

## Follow-up Checks

Run `just seed-canary NCBITaxon:1008457`, `just validate data/taxa/bacteria/myroides_injenensis_m09_0166.yaml`, `just validate-strict data/taxa/bacteria/myroides_injenensis_m09_0166.yaml`, and `just verify-corpus`. Manually confirm that `GTDB:s__Flavobacterium_injenense` no longer appears as this strain's exact synonym or xref while remaining available on the appropriate species-level record if the upstream mapping still supports it.

## Additional Notes

Live NCBI, GTDB, BacDive, and literature pages were not used in this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
