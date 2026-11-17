# YAML Record Review: Bacteroidetes bacterium 6E
- Repository: TaxonMech
- Record: data/taxa/bacteria/bacteroidetes_bacterium_6e.yaml
- Started UTC: 2026-09-23T01:46:14Z
- Finished UTC: 2026-09-23T01:46:14Z
- Verdict: pass

## Target

- YAML record: `data/taxa/bacteria/bacteroidetes_bacterium_6e.yaml`
- Identifier: `NCBITaxon:1005738`
- Label: `Bacteroidetes bacterium 6E`
- Rank: `SPECIES`
- Parent: `NCBITaxon:37452`
- Registry row: `data/taxa/PATHS.tsv:1833`
- Scope row: `curation/seed_scope.tsv:57179`
- A pre-write `find reports/yaml_record_review ... -name '*-bacteroidetes_bacterium_6e.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/bacteroidetes_bacterium_6e.yaml data/taxa/bacteria/aminivibrio_pyruvatiphilus.yaml data/taxa/bacteria/saprospiraceae_bacterium_kmm_9006.yaml data/taxa/bacteria/bradyrhizobium_sp_semia_6002.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/bacteroidetes_bacterium_6e.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, genetic code, empty synonym set, and NCBI/GOLD source attestations agree with `data/raw/ncbitaxon_taxa.tsv:210496` and `data/raw/gold_organisms.tsv:149`.
- The stored lineage terminates at the asserted parent `NCBITaxon:37452` / `unclassified Bacteroidota`.
- `grounding_status: EXACT` is appropriate for the NCBI placeholder species taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210496` attests `NCBITaxon:1005738` as `Bacteroidetes bacterium 6E`, rank `SPECIES`, parent `NCBITaxon:37452`, genetic code `11`, no NCBI synonyms, and NCBI snapshot `2026-09-13`.
- `data/raw/gold_organisms.tsv:149` contributes one GOLD organism assertion for `NCBITaxon:1005738`.
- Exact, gitignore-independent scans of `data/raw/madin_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` found no same-taxon rows for `NCBITaxon:1005738`.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no same-taxon rows for `NCBITaxon:1005738`, `Bacteroidetes bacterium 6E`, or `bacteroidetes_bacterium_6e`.

## Completeness

- The generated NCBI identity, lineage, GOLD source attestation, and seed history are complete for the local source rows.
- The record has no synonyms, GTDB mapping, xref, Madin, ATB, or StrainInfo material, matching the pinned local rows.

## Findings

- No findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/bacteroidetes_bacterium_6e.yaml` if the record is regenerated from updated sources.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
