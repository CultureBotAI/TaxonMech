# YAML Record Review: Bacteroidetes bacterium Acht4
- Repository: TaxonMech
- Record: data/taxa/bacteria/bacteroidetes_bacterium_acht4.yaml
- Started UTC: 2026-09-23T12:18:30Z
- Finished UTC: 2026-09-23T12:18:30Z
- Verdict: pass

## Target

Reviewed `NCBITaxon:1008390`, the NCBI-sourced species placeholder `Bacteroidetes bacterium Acht4`, encoded at `data/taxa/bacteria/bacteroidetes_bacterium_acht4.yaml`.

## Validation

`just validate-strict data/taxa/bacteria/pseudomonas_sp_sr5.yaml data/taxa/eukaryota/starmerella_kuoi.yaml data/taxa/bacteria/marinimicrobium_sp_acht5_2.yaml data/taxa/bacteria/bacteroidetes_bacterium_acht4.yaml` scanned the batch and returned 0 errors on rerun.

`just validate data/taxa/bacteria/bacteroidetes_bacterium_acht4.yaml` returned `No issues found`.

## Identity and Grounding

The record is grounded to `NCBITaxon:1008390` with label `Bacteroidetes bacterium Acht4`. Its parent is `NCBITaxon:37452`, `unclassified Bacteroidota`, matching an NCBI phylum-level bacterial placeholder rather than a formally named genus species.

`data/taxa/PATHS.tsv` maps the identifier to `bacteroidetes_bacterium_acht4`, matching the reviewed YAML path.

## Evidence

The local NCBI source row in `data/raw/ncbitaxon_taxa.tsv` is the source of truth for the accepted identifier, NCBI-preserved label casing, rank, parentage, genetic code, and NCBI-only source attribution. An exact `rg --no-ignore --hidden` ID search over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS entry and the expected `ncbitaxon_taxa.tsv` row for `NCBITaxon:1008390`.

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

A gitignore-independent `find` of `reports/yaml_record_review` found no pre-existing report for `bacteroidetes_bacterium_acht4` before this report was written. Live external lookups were unavailable during this review; the pinned rows under `data/raw`, `data/atb`, and `data/straininfo` were treated as authoritative.
