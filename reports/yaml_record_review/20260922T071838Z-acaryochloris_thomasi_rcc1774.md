# YAML Record Review: Acaryochloris thomasi RCC1774

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acaryochloris_thomasi_rcc1774.yaml
- Started UTC: 2026-09-22T07:17:37Z
- Finished UTC: 2026-09-22T07:18:38Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1764569 |
| label | Acaryochloris thomasi RCC1774 |
| rank | STRAIN |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2929456 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial strain record at `data/taxa/bacteria/acaryochloris_thomasi_rcc1774.yaml`. It is seeded from NCBITaxon and a GTDB species mapping, carries one NCBITaxon related synonym, one GTDB exact synonym, one GTDB xref, no generated local strain entries, and no causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 267714 maps `NCBITaxon:1764569` to slug `acaryochloris_thomasi_rcc1774`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; the exact `find reports/yaml_record_review -maxdepth 1 ... -name "*-acaryochloris_thomasi_rcc1774.md"` probe returned no prior report. `find` includes ignored files, and the probe was scoped to `reports/yaml_record_review/`. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acaryochloris_thomasi_rcc1774.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acaryochloris_thomasi.yaml data/taxa/bacteria/acaryochloris_thomasi_rcc1774.yaml data/taxa/bacteria/accumulibacter_sp.yaml data/taxa/bacteria/acer_campestre_aster_yellows_phytoplasma.yaml` scanned this file with zero ERROR rows in a four-file batch and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 461116 has `NCBITaxon:1764569`, label `Acaryochloris thomasi RCC1774`, rank `STRAIN`, direct parent `NCBITaxon:2929456`, genetic code `11`, related synonym `Acaryochloris sp. RCC1774`, source set `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

The YAML lineage follows the same Acaryochloris parent chain as `Acaryochloris thomasi` and adds that species as the final ancestor. All ancestor IDs and ranks match `data/raw/ncbitaxon_taxa.tsv`: root line 2, cellular organisms line 25334, Bacteria line 3, Bacillati line 464835, Cyanobacteriota/Melainabacteria group line 469139, Cyanobacteriota line 870, Cyanophyceae line 587019, Acaryochloridales line 595536, Acaryochloridaceae line 490868, Acaryochloris line 32348, and `NCBITaxon:2929456` on line 573005.

The GTDB overlay is internally coherent. `data/raw/gtdb_mappings.tsv` line 55606 maps `GTDB:s__RCC1774_sp003231495` / `s__RCC1774_sp003231495` under `GTDB:g__RCC1774` to `NCBITaxon:1764569` with `skos:closeMatch` and a genome count of `2`; the YAML repeats that source ID, label, predicate, and genome count in `taxonomy_mappings`, derives `RCC1774 sp003231495` as the GTDB exact synonym, and mirrors the mapping as `GTDB:s__RCC1774_sp003231495` in `xrefs`.

## Evidence

The two YAML source attestations match the pinned source rows. The NCBITaxon attestation points back to `NCBITaxon:1764569` and the NCBI raw row on line 461116; the GTDB attestation points back to `GTDB:s__RCC1774_sp003231495`, uses `skos:closeMatch`, and preserves the GTDB genome count of `2`.

The seed scope agrees with those sources: `curation/seed_scope.tsv` line 76722 keeps `NCBITaxon:1764569` in scope as `Acaryochloris thomasi RCC1774` with two sources including NCBI, and the only `curation_history` event records the same GTDB plus NCBITAXON seeding decision at `2026-09-13T17:54:04Z`.

## Completeness

For a generated NCBITaxon strain with one GTDB mapping, the record is complete. It has the required identity, rank, domain, direct parent, lineage, genetic code, seed status, both source attestations, the NCBITaxon related synonym, the GTDB synonym/xref material, GTDB mapping provenance, and the generated seeding event.

The record correctly leaves `strain_count: 0`: generated children are not expected beneath this strain-level taxon, and no first-column auxiliary rows for `NCBITaxon:1764569` were present in `data/atb/` or `data/straininfo/` during the ignored-inclusive scan.

## Findings

No required edits.

## Recommended Edits

None.

## Follow-up Checks

None specific to this record. Future changes to this generated YAML should be made through source extraction, seed-scope changes, or upstream mapping changes and then regenerated with the corpus.

## Additional Notes

NCBI and GTDB live fetches were unavailable during this review, so the authoritative primary evidence was the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot and committed `data/raw/gtdb_mappings.tsv` crosswalk.
