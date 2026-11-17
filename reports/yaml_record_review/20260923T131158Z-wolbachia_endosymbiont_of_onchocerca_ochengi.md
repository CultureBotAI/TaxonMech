# YAML Record Review: Wolbachia endosymbiont of Onchocerca ochengi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/wolbachia_endosymbiont_of_onchocerca_ochengi.yaml
- Started UTC: 2026-09-23T13:10:52Z
- Finished UTC: 2026-09-23T13:11:58Z
- Verdict: pass

## Target

`data/taxa/bacteria/wolbachia_endosymbiont_of_onchocerca_ochengi.yaml` is the generated `TaxonRecord` for `NCBITaxon:100901`, label `Wolbachia endosymbiont of Onchocerca ochengi`, rank `SPECIES`, `taxon_domain: BACTERIA`, and parent `NCBITaxon:2640676` `unclassified Wolbachia`.

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*wolbachia_endosymbiont_of_onchocerca_ochengi.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/brevundimonas_sp_te4.yaml data/taxa/bacteria/flavobacterium_sp_te15.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_onchocerca_ochengi.yaml data/taxa/bacteria/beta_proteobacterium_in3.yaml` | Passed for the 4-file batch |
| `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_onchocerca_ochengi.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: no `causal_graphs` are present |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:17341` supports the identifier, label, `SPECIES` rank, `NCBITaxon:2640676` parent, genetic code `11`, and NCBI synonym `Wolbachia sp. wOo`. `data/raw/gtdb_mappings.tsv:1118` supports the `GTDB:s__Wolbachia_sp000306885` `skos:closeMatch` with 17 genomes, `data/raw/gold_organisms.tsv:205` supports the direct GOLD organism count, and `data/raw/madin_taxa.tsv:400` supports the two direct Madin trait assertions. `curation/seed_scope.tsv:23609` carries the matching four-source inclusion row, and `data/taxa/PATHS.tsv:2821` resolves the identifier to this YAML path.

## Evidence

The `source_attestations` summarize the expected local evidence mix: one `NCBITAXON` `NAME` assertion, a 17-genome `GTDB` species-cluster mapping, one direct `GOLD` `ORGANISM` assertion, and two direct `MADIN` `TRAIT_ASSERTION` rows. The GTDB synonym and xref preserve the mapped species-cluster label `Wolbachia sp000306885` / `GTDB:s__Wolbachia_sp000306885`.

## Completeness

Exact gitignore-independent searches over the pinned auxiliary sources found no same-taxon AllTheBacteria or StrainInfo rows and no LPSN, BacDive, MediaDive, BactoTraits, or curator-added rows beyond the direct NCBI, GTDB, GOLD, and Madin support above. The known child strain `NCBITaxon:1141110`, `Wolbachia endosymbiont of Onchocerca ochengi str. Adamawa_Cameroon`, remains a separate generated strain record with its own GOLD row, so this parent record is not incorrectly absorbing descendant GOLD evidence.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. After any source refresh that changes the GTDB species-cluster mapping or moves GOLD/Madin rows between this species and `NCBITaxon:1141110`, rerun `just seed-canary NCBITaxon:100901`, `just validate`, `just validate-strict`, and `just verify-corpus`.

## Additional Notes

Live NCBI pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
