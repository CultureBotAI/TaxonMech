# YAML Record Review: Pseudomonas sp. SR5
- Repository: TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_sr5.yaml
- Started UTC: 2026-09-23T12:18:30Z
- Finished UTC: 2026-09-23T12:18:30Z
- Verdict: pass

## Target

Reviewed `NCBITaxon:1008356`, the NCBI-sourced species placeholder `Pseudomonas sp. SR5`, encoded at `data/taxa/bacteria/pseudomonas_sp_sr5.yaml`.

## Validation

`just validate-strict data/taxa/bacteria/pseudomonas_sp_sr5.yaml data/taxa/eukaryota/starmerella_kuoi.yaml data/taxa/bacteria/marinimicrobium_sp_acht5_2.yaml data/taxa/bacteria/bacteroidetes_bacterium_acht4.yaml` scanned the batch and returned 0 errors on rerun.

`just validate data/taxa/bacteria/pseudomonas_sp_sr5.yaml` returned `No issues found`.

## Identity and Grounding

The record is grounded to `NCBITaxon:1008356` with label `Pseudomonas sp. SR5`. Its parent is `NCBITaxon:196821`, `unclassified Pseudomonas`, matching an NCBI placeholder species under genus `Pseudomonas`.

`data/taxa/PATHS.tsv` maps the identifier to `pseudomonas_sp_sr5`, matching the reviewed YAML path.

## Evidence

The local NCBI source row in `data/raw/ncbitaxon_taxa.tsv` is the source of truth for the accepted identifier, label, rank, parentage, genetic code, and NCBI-only source attribution. An exact `rg --no-ignore --hidden` ID search over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS entry and the expected `ncbitaxon_taxa.tsv` row for `NCBITaxon:1008356`.

A tab-bounded gitignore-independent search for the full label found only the exact `ncbitaxon_taxa.tsv` source row among `data/raw`, `data/atb`, and `data/straininfo`; no BacDive, GTDB, LPSN, GOLD, ATB, or StrainInfo rows are available for this placeholder.

## Completeness

The YAML is intentionally minimal: it captures a placeholder species asserted by NCBI and does not invent strain, type-material, assembly, synonym, or culture-collection data that are absent from the pinned local inputs.

The `strain_count: 0`, NCBITAXON-only `source_attestations`, and seed-only curation history are complete for the local evidence available.

## Findings

No curation findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

A gitignore-independent `find` of `reports/yaml_record_review` found no pre-existing report for `pseudomonas_sp_sr5` before this report was written. Live external lookups were unavailable during this review; the pinned rows under `data/raw`, `data/atb`, and `data/straininfo` were treated as authoritative.
