# YAML Record Review: Bacteroidetes bacterium 4F6B
- Repository: TaxonMech
- Record: data/taxa/bacteria/bacteroidetes_bacterium_4f6b.yaml
- Started UTC: 2026-09-23T01:42:09Z
- Finished UTC: 2026-09-23T01:42:09Z
- Verdict: pass

## Target

- YAML record: `data/taxa/bacteria/bacteroidetes_bacterium_4f6b.yaml`
- Identifier: `NCBITaxon:1005737`
- Label: `Bacteroidetes bacterium 4F6B`
- Rank: `SPECIES`
- Parent: `NCBITaxon:37452`
- Registry row: `data/taxa/PATHS.tsv:1832`
- Scope row: `curation/seed_scope.tsv:311214`
- A pre-write `find reports/yaml_record_review ... -name '*-bacteroidetes_bacterium_4f6b.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/phormidium_pseudo_okenii.yaml data/taxa/bacteria/geitlerinema_serpens.yaml data/taxa/bacteria/schizothrix_tenebrosa.yaml data/taxa/bacteria/bacteroidetes_bacterium_4f6b.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/bacteroidetes_bacterium_4f6b.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, genetic code, empty synonym set, and NCBI-only source attestation agree with `data/raw/ncbitaxon_taxa.tsv:210495`.
- The stored lineage terminates at the asserted parent `NCBITaxon:37452` / `unclassified Bacteroidota`.
- `grounding_status: EXACT` is appropriate for the NCBI placeholder species taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210495` attests `NCBITaxon:1005737` as `Bacteroidetes bacterium 4F6B`, rank `SPECIES`, parent `NCBITaxon:37452`, genetic code `11`, no NCBI synonyms, and NCBI snapshot `2026-09-13`.
- Exact, gitignore-independent scans of `data/raw/madin_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` found no same-taxon rows for `NCBITaxon:1005737`.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no same-taxon rows for `NCBITaxon:1005737`, `Bacteroidetes bacterium 4F6B`, or `bacteroidetes_bacterium_4f6b`.

## Completeness

- The generated NCBI identity, lineage, source attestation, and seed history are complete for the local source row.
- The record has no synonyms, GTDB mapping, xref, Madin, GOLD, ATB, or StrainInfo material, matching the pinned local rows.

## Findings

- No findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/bacteroidetes_bacterium_4f6b.yaml` if the record is regenerated from updated sources.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.
