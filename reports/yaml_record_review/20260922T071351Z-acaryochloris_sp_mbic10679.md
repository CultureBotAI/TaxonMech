# YAML Record Review: Acaryochloris sp. MBIC10679

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acaryochloris_sp_mbic10679.yaml
- Started UTC: 2026-09-22T07:13:23Z
- Finished UTC: 2026-09-22T07:13:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:155979 |
| label | Acaryochloris sp. MBIC10679 |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2631661 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/acaryochloris_sp_mbic10679.yaml`. It is seeded from NCBITaxon only, sits under the NCBI `unclassified Acaryochloris` bucket, carries one NCBITaxon exact synonym, no GTDB mappings, no xrefs, no LPSN nomenclature, no generated local strain entries, and no causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 205604 maps `NCBITaxon:155979` to slug `acaryochloris_sp_mbic10679`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; the exact `find reports/yaml_record_review -maxdepth 1 ... -name "*-acaryochloris_sp_mbic10679.md"` probe returned no prior report. `find` includes ignored files, and the probe was scoped to `reports/yaml_record_review/`. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acaryochloris_sp_mbic10679.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acaryochloris_sp_mbic10679.yaml data/taxa/bacteria/acaryochloris_sp_mbic10683.yaml data/taxa/bacteria/acaryochloris_sp_mbic10690.yaml data/taxa/bacteria/acaryochloris_sp_mbic10696.yaml` scanned this file with zero ERROR rows in a four-file batch and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 32350 has `NCBITaxon:155979`, label `Acaryochloris sp. MBIC10679`, rank `SPECIES`, direct parent `NCBITaxon:2631661`, genetic code `11`, exact synonym `Acaryochloris sp. PS-19`, source set `ncbitaxon`, and snapshot date `2026-09-13`.

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

The taxon remains correctly scoped as an exact NCBITaxon seed rather than a GTDB merge: an ignored-inclusive `rg --no-ignore --hidden` scan for the first-column ID found this taxon only in `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`, and the exact GTDB crosswalk scan of `data/raw/gtdb_mappings.tsv` found no row for `NCBITaxon:155979`.

## Evidence

The single YAML source attestation is consistent with the raw NCBI row and the seed scope. `source: NCBITAXON`, `source_id: NCBITaxon:155979`, `source_label: Acaryochloris sp. MBIC10679`, `assertion_count: 1`, and `assertion_unit: NAME` line up with the NCBI-only source set and synonym on `data/raw/ncbitaxon_taxa.tsv` line 32350 and the one-source scope rationale in `curation/seed_scope.tsv` line 155957.

The seed history is internally consistent: the only `curation_history` event is from `seed_from_sources` at `2026-09-13T17:54:04Z`, uses `SEEDED_FROM_SOURCES`, and repeats the `Acaryochloris sp. MBIC10679` NCBI attestation rationale from the scope file.

## Completeness

For a generated NCBITaxon-only species placeholder with one NCBI synonym, the record is complete. It has the required identity, rank, domain, direct parent, lineage, genetic code, seed status, source attestation, NCBI synonym, and provenance; no optional xref, GTDB, LPSN, local strain, or causal-graph blocks are implied by the pinned source rows.

The record correctly leaves `strain_count: 0`: no generated children are currently in scope beneath this taxon, and no first-column auxiliary rows for `NCBITaxon:155979` were present in `data/atb/` or `data/straininfo/` during the ignored-inclusive scan.

## Findings

No required edits.

## Recommended Edits

None.

## Follow-up Checks

None specific to this record. Future changes to this generated YAML should be made through source extraction, seed-scope changes, or upstream mapping changes and then regenerated with the corpus.

## Additional Notes

NCBI live fetches were unavailable during this review, so the authoritative primary evidence was the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot from `2026-09-13`.
