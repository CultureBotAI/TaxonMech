# YAML Record Review: Accumulibacter sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/accumulibacter_sp.yaml
- Started UTC: 2026-09-22T07:17:37Z
- Finished UTC: 2026-09-22T07:18:38Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2053492 |
| label | Accumulibacter sp. |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2619054 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated species-level placeholder at `data/taxa/bacteria/accumulibacter_sp.yaml`. It is seeded from NCBITaxon, a pooled GTDB broadMatch bundle, and GOLD, sits under the NCBI `unclassified Candidatus Accumulibacter` bucket, carries one NCBITaxon exact synonym, 42 GTDB `skos:broadMatch` taxonomy mappings, no GTDB xrefs, no generated local strain entries, and no causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 323646 maps `NCBITaxon:2053492` to slug `accumulibacter_sp`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; the exact `find reports/yaml_record_review -maxdepth 1 ... -name "*-accumulibacter_sp.md"` probe returned no prior report. `find` includes ignored files, and the probe was scoped to `reports/yaml_record_review/`. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/accumulibacter_sp.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acaryochloris_thomasi.yaml data/taxa/bacteria/acaryochloris_thomasi_rcc1774.yaml data/taxa/bacteria/accumulibacter_sp.yaml data/taxa/bacteria/acer_campestre_aster_yellows_phytoplasma.yaml` scanned this file with zero ERROR rows in a four-file batch and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 514106 has `NCBITaxon:2053492`, label `Accumulibacter sp.`, rank `SPECIES`, direct parent `NCBITaxon:2619054`, genetic code `11`, exact synonym `Candidatus Accumulibacter sp.`, source set `ncbitaxon|gtdb|gold`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI parent chain exactly: root line 2, cellular organisms line 25334, Bacteria line 3, `Pseudomonadati` line 622851, `Pseudomonadota` line 945, `Betaproteobacteria` line 2916, `Betaproteobacteria incertae sedis` line 22328, `Candidatus Accumulibacter` line 66866, and `unclassified Candidatus Accumulibacter` line 537580.

The GTDB overlay is a generated pooled broadMatch bundle. The exact crosswalk scan found 42 `data/raw/gtdb_mappings.tsv` rows for `NCBITaxon:2053492`, from line 158868 through line 158909 inclusive; every row uses `skos:broadMatch`, and the YAML has the same 42 GTDB `taxonomy_mappings` with the source IDs, labels, predicates, genome counts, and pooled broadMatch note preserved. The top-level `source_attestations` entry summarizes the leading `GTDB:s__Accumulibacter_sp029255125` mapping with `assertion_count: 21` and notes the 41 further pooled species represented under `taxonomy_mappings`.

## Evidence

All three YAML source attestations match pinned source rows. The NCBITaxon attestation points back to `NCBITaxon:2053492` and the NCBI raw row on line 514106; the GTDB attestation summarizes the row-158890 broadMatch to `GTDB:s__Accumulibacter_sp029255125`; and the GOLD attestation matches `data/raw/gold_organisms.tsv` line 19579 with three organism assertions for `NCBITaxon:2053492`.

The seed scope and history are internally consistent with a generated pooled record. `curation/seed_scope.tsv` line 62212 keeps `NCBITaxon:2053492` in scope as `Accumulibacter sp.` by a source-count rule including NCBI, while the generated `curation_history` lists the three emitted attesting sources: GOLD, GTDB, and NCBITAXON.

## Completeness

For a generated species placeholder with pooled GTDB support, the record is complete. It has the required identity, rank, domain, direct parent, lineage, genetic code, seed status, NCBITaxon synonym, all GTDB broadMatch overlays from the committed crosswalk, the GOLD count, source attestations, and the generated seeding event.

The record correctly leaves `xrefs` absent because none of the GTDB mappings is an exact or close match, and it correctly leaves `strain_count: 0` because no generated children are currently in scope beneath this taxon.

## Findings

No required edits.

## Recommended Edits

None.

## Follow-up Checks

None specific to this record. Future changes to this generated YAML should be made through source extraction, seed-scope changes, or upstream mapping changes and then regenerated with the corpus.

## Additional Notes

NCBI, GTDB, and GOLD live fetches were unavailable during this review, so the authoritative primary evidence was the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot and committed auxiliary source tables.
