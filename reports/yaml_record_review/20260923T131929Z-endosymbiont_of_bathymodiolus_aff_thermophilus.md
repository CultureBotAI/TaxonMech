# YAML Record Review: endosymbiont of Bathymodiolus aff. thermophilus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/endosymbiont_of_bathymodiolus_aff_thermophilus.yaml
- Started UTC: 2026-09-23T13:17:48Z
- Finished UTC: 2026-09-23T13:19:32Z
- Verdict: pass

## Target

`data/taxa/bacteria/endosymbiont_of_bathymodiolus_aff_thermophilus.yaml` is the generated `TaxonRecord` for `NCBITaxon:1009020`, label `endosymbiont of Bathymodiolus aff. thermophilus`, rank `SPECIES`, `taxon_domain: BACTERIA`, and parent `NCBITaxon:49928` `unclassified Bacteria`.

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*endosymbiont_of_bathymodiolus_aff_thermophilus.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/endosymbiont_of_bathymodiolus_puteoserpentis.yaml data/taxa/bacteria/endosymbiont_of_bathymodiolus_aff_thermophilus.yaml data/taxa/bacteria/ectosymbiont_of_rimicaris_exoculata.yaml data/taxa/bacteria/agrobacterium_sp_ch11.yaml` | Passed for the 4-file batch |
| `just validate data/taxa/bacteria/endosymbiont_of_bathymodiolus_aff_thermophilus.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: no `causal_graphs` are present |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:211443` supports the identifier, label, `SPECIES` rank, `NCBITaxon:49928` parent, genetic code `11`, and the NCBI-only source flag. `curation/seed_scope.tsv:312069` carries the matching one-source inclusion row, and `data/taxa/PATHS.tsv:2833` resolves the identifier to this YAML path.

## Evidence

The only `source_attestations` entry is a one-count `NCBITAXON` `NAME` assertion from the pinned 2026-09-13 NCBI snapshot.

## Completeness

Exact gitignore-independent searches over the full `data/raw/`, `data/atb/`, and `data/straininfo/` auxiliary source trees found no same-taxon rows for `NCBITaxon:1009020`. The longer Bathymodiolus Logatchev symbiont hits from label search are different NCBI taxa under `NCBITaxon:33811`, so their GTDB support is correctly absent from this generic `NCBITaxon:1009020` record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. After any source refresh that adds non-NCBI support for `NCBITaxon:1009020`, rerun `just seed-canary NCBITaxon:1009020`, `just validate`, `just validate-strict`, and `just verify-corpus`.

## Additional Notes

Live NCBI pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
