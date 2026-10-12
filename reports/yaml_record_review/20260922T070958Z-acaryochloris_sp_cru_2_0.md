# YAML Record Review: Acaryochloris sp. CRU_2_0

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acaryochloris_sp_cru_2_0.yaml
- Started UTC: 2026-09-22T07:09:26Z
- Finished UTC: 2026-09-22T07:09:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2720402 |
| label | Acaryochloris sp. CRU_2_0 |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2631661 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/acaryochloris_sp_cru_2_0.yaml`. It is seeded from NCBITaxon and a GTDB species mapping under the NCBI `unclassified Acaryochloris` bucket and carries one GTDB closeMatch, one GTDB exact synonym, one GTDB xref, no generated local strain entries, and no causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 366952 maps `NCBITaxon:2720402` to slug `acaryochloris_sp_cru_2_0`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; the exact `find reports/yaml_record_review -maxdepth 1 ... -name "*-acaryochloris_sp_cru_2_0.md"` probe returned no prior report. `find` includes ignored files, and the probe was scoped to `reports/yaml_record_review/`. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acaryochloris_sp_cru_2_0.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acaryochloris_sp_beach_rock_5.yaml data/taxa/bacteria/acaryochloris_sp_ccmee_5410.yaml data/taxa/bacteria/acaryochloris_sp_ccnum4.yaml data/taxa/bacteria/acaryochloris_sp_cru_2_0.yaml` scanned this file with zero ERROR rows in a four-file batch and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 547098 has `NCBITaxon:2720402`, label `Acaryochloris sp. CRU_2_0`, rank `SPECIES`, direct parent `NCBITaxon:2631661`, genetic code `11`, empty NCBI synonym slots, source set `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:1798711` Cyanobacteriota/Melainabacteria group, `CLADE` | line 469139 |
| `NCBITaxon:1117` Cyanobacteriota, `PHYLUM` | line 870 |
| `NCBITaxon:3028117` Cyanophyceae, `CLASS` | line 587019 |
| `NCBITaxon:3079744` Acaryochloridales, `ORDER` | line 595536 |
| `NCBITaxon:1890429` Acaryochloridaceae, `FAMILY` | line 490868 |
| `NCBITaxon:155977` Acaryochloris, `GENUS` | line 32348 |
| `NCBITaxon:2631661` unclassified Acaryochloris, `NO_RANK` | line 538637 |

The GTDB overlay is internally coherent for this target. `data/raw/gtdb_mappings.tsv` line 210160 maps `GTDB:s__Acaryochloris_sp012034865` / `s__Acaryochloris_sp012034865` under `GTDB:g__Acaryochloris` to `NCBITaxon:2720402` with `skos:closeMatch` and a genome count of `2`; the YAML repeats that source ID, label, predicate, and genome count in `taxonomy_mappings`, derives `Acaryochloris sp012034865` as the GTDB exact synonym, and mirrors the mapping as `GTDB:s__Acaryochloris_sp012034865` in `xrefs`.

## Evidence

The two YAML source attestations match the pinned source rows. The NCBITaxon attestation points back to `NCBITaxon:2720402` and the NCBI raw row on line 547098; the GTDB attestation points back to `GTDB:s__Acaryochloris_sp012034865`, uses `skos:closeMatch`, and preserves the GTDB genome count of `2`.

The seed scope agrees with those sources: `curation/seed_scope.tsv` line 99826 keeps `NCBITaxon:2720402` in scope as `Acaryochloris sp. CRU_2_0` with two sources including NCBI, and the only `curation_history` event records the same GTDB plus NCBITAXON seeding decision at `2026-09-13T17:54:04Z`.

## Completeness

For a generated species placeholder with one species-level GTDB mapping, the record is complete. It has the required identity, rank, domain, direct parent, lineage, genetic code, seed status, both source attestations, GTDB mapping provenance, the GTDB synonym/xref material, and the generated seeding event.

The record correctly leaves `strain_count: 0`: no generated children are currently in scope beneath this taxon, and no first-column auxiliary rows for `NCBITaxon:2720402` were present in `data/atb/` or `data/straininfo/` during the ignored-inclusive scan.

## Findings

No required edits.

## Recommended Edits

None.

## Follow-up Checks

When reviewing `acaryochloris_sp_ru_4_1`, cross-check that its shared `GTDB:s__Acaryochloris_sp012034865` mapping is still represented exactly from `data/raw/gtdb_mappings.tsv` line 210185.

## Additional Notes

The same GTDB species row also maps to `NCBITaxon:2720442` / `acaryochloris_sp_ru_4_1`; that neighbor row is not an issue for this target because the CRU_2_0 YAML exactly reflects the line 210160 crosswalk. NCBI and GTDB live fetches were unavailable during this review, so the authoritative primary evidence was the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot and committed `data/raw/gtdb_mappings.tsv` crosswalk.
