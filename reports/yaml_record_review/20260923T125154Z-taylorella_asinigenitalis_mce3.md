# YAML Record Review: Taylorella asinigenitalis MCE3

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/taylorella_asinigenitalis_mce3.yaml
- Started UTC: 2026-09-23T12:48:06Z
- Finished UTC: 2026-09-23T12:51:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1008459` |
| Label | `Taylorella asinigenitalis MCE3` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:84590` `Taylorella asinigenitalis` |
| Status | `grounding_status: EXACT`; `mapping_status: SEEDED` |
| Maintained? | Generated under `data/taxa/`; future fixes belong in `data/raw/gtdb_mappings.tsv` generation and in `src/taxonmech/seed.py`, not in this YAML |

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*taylorella_asinigenitalis_mce3.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/myroides_injenensis_m09_0166.yaml data/taxa/bacteria/taylorella_asinigenitalis_mce3.yaml data/taxa/archaea/pyrococcus_yayanosii.yaml data/taxa/bacteria/shinella_sp_agr1.yaml` | Passed: 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate data/taxa/bacteria/taylorella_asinigenitalis_mce3.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: this record has no `causal_graphs`, and the product id/label gate is only for curator-added graph nodes |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

The NCBI row in `data/raw/ncbitaxon_taxa.tsv:211407` supports the record identifier, label, `STRAIN` rank, `NCBITaxon:84590` parent, genetic code `11`, both NCBI exact synonyms, the `ncbitaxon|gtdb|madin_etal` source flags, and the `2026-09-13` NCBI snapshot note. `curation/seed_scope.tsv:36074` carries the matching attested-scope row for this exact identifier and label.

The lineage is internally consistent with a bacterial strain under `Taylorella asinigenitalis`, and `taxon_domain: BACTERIA` matches the `NCBITaxon:2` domain ancestor at `data/taxa/bacteria/taylorella_asinigenitalis_mce3.yaml:13`.

`data/raw/madin_taxa.tsv:395` supports the one-count `MADIN` source attestation. Exact gitignore-independent searches across `data/atb/`, `data/straininfo/`, `data/raw/gold_organisms.tsv`, `data/raw/mediadive_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no same-taxon rows for `NCBITaxon:1008459`; no AllTheBacteria, StrainInfo, GOLD, MediaDive, BactoTraits, merged-id, or dropped-source block is expected on this record.

## Evidence

The seeded NCBI synonyms at `data/taxa/bacteria/taylorella_asinigenitalis_mce3.yaml:50` are exactly the synonym pipe from `data/raw/ncbitaxon_taxa.tsv:211407`. The NCBI and MADIN source attestations at `data/taxa/bacteria/taylorella_asinigenitalis_mce3.yaml:61` agree with their pinned inventory rows.

The GTDB species cluster is over-projected to a single strain. `data/raw/gtdb_species.tsv:174571` reports `GTDB:s__Taylorella_asinigenitalis` as a three-genome species cluster; `data/raw/gtdb_mappings.tsv:1105`, `data/raw/gtdb_mappings.tsv:3248`, and `data/raw/gtdb_mappings.tsv:24455` map that same cluster as `skos:closeMatch` to three different NCBI strain taxa: `MCE3`, `14/45`, and `ATCC 700933`. The record nevertheless emits `Taylorella asinigenitalis` as a GTDB-backed `EXACT_SYNONYM` for `MCE3` and keeps the GTDB species as an `xref`.

## Completeness

The record has no `nomenclature`, `strains`, `evidence`, `definition`, `discussions`, or `causal_graphs`; the exact source searches found no LPSN, BacDive, GOLD, ATB, StrainInfo, MediaDive, or BactoTraits rows for `NCBITaxon:1008459`, so those omissions are expected for this seeded strain record.

The only consequential completeness problem is that the emitted GTDB identity fields are too broad for the strain and should be removed or downgraded by the maintained mapping projection.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `GTDB:s__Taylorella_asinigenitalis` is emitted as a strain-level xref, exact synonym, mapping, and source attestation even though the same three-genome GTDB species cluster maps to several NCBI strain records. | `data/taxa/bacteria/taylorella_asinigenitalis_mce3.yaml:39-57` publishes the species cluster as exact-looking strain identity; `data/raw/gtdb_mappings.tsv:1105`, `:3248`, and `:24455` map that same source cluster to `NCBITaxon:1008459`, `NCBITaxon:1091495`, and `NCBITaxon:1408475`; `src/taxonmech/seed.py:447-468` promotes every `skos:closeMatch` GTDB row to an `xref` and `EXACT_SYNONYM`. | `data/raw/gtdb_mappings.tsv` generation plus the GTDB identity test in `src/taxonmech/seed.py` |

## Recommended Edits

1. Stop treating every GTDB `skos:closeMatch` as infraspecific identity in `src/taxonmech/seed.py`; a same-named GTDB species cluster should not become a strain-level `EXACT_SYNONYM` or `xref`.
2. Revisit the kg-microbe GTDB mapping transform that emitted one species cluster as close matches to `NCBITaxon:1008459`, `NCBITaxon:1091495`, and `NCBITaxon:1408475`. The regenerated `data/raw/gtdb_mappings.tsv` should not invite exact strain-level projection from a three-genome species cluster.
3. Re-run the seeder and verify the `MCE3` record carries NCBI and MADIN support without a GTDB exact synonym unless a source explicitly identifies the GTDB cluster with this strain.

## Follow-up Checks

Run `just seed-canary NCBITaxon:1008459`, `just validate data/taxa/bacteria/taylorella_asinigenitalis_mce3.yaml`, `just validate-strict data/taxa/bacteria/taylorella_asinigenitalis_mce3.yaml`, and `just verify-corpus`. Manually confirm that `Taylorella asinigenitalis` from GTDB is not reintroduced as a strain-level exact synonym.

## Additional Notes

Live NCBI and GTDB pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
