# YAML Record Review: Halobacteriales archaeon YIM 93756

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/halobacteriales_archaeon_yim_93756.yaml
- Started UTC: 2026-09-23T11:03:07Z
- Finished UTC: 2026-09-23T11:04:14Z
- Verdict: pass

## Target

Reviewed generated TaxonRecord `data/taxa/archaea/halobacteriales_archaeon_yim_93756.yaml` for `NCBITaxon:1008182`, `Halobacteriales archaeon YIM 93756`, an archaeal `SPECIES` child of `NCBITaxon:38063` / `unclassified Halobacteriales`.

## Validation

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-halobacteriales_archaeon_yim_93756.md'`: passed with no prior report; ignored reports were included.
- `just validate-strict data/taxa/archaea/halobacteriales_archaeon_yim_93737.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93755.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93756.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93762.yaml`: passed, 4 files scanned, 0 files with errors, 0 total error rows.
- `just validate data/taxa/archaea/halobacteriales_archaeon_yim_93756.yaml`: passed, no LinkML issues.
- Skipped: product validation because there are no `causal_graphs`; history validation because this read-only review did not add a history decision; full `just verify-corpus` because no generated YAML was edited.

## Identity and Grounding

The record matches the pinned `data/raw/ncbitaxon_taxa.tsv` row exactly: `NCBITaxon:1008182`, `Halobacteriales archaeon YIM 93756`, rank `SPECIES`, parent `NCBITaxon:38063`, genetic code `11`, source `ncbitaxon`, snapshot `2026-09-13`. The lineage, `grounding_status: EXACT`, `mapping_status: SEEDED`, and NCBI source attestation are consistent with that source row.

## Evidence

Exact `rg --no-ignore --hidden` searches for `NCBITaxon:1008182` and `Halobacteriales archaeon YIM 93756` over `data/raw/`, `data/atb/`, and `data/straininfo/` found only the `PATHS.tsv` entry and the NCBI source row. No live source page was used.

## Completeness

No consequential gaps were found. The empty synonym, xref, nomenclature, taxonomy mapping, strain, and causal-graph sections are consistent with the absence of exact same-taxon LPSN, GTDB, BacDive, GOLD, ATB, NCBI Assembly, and StrainInfo rows.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Rerun source seeding and `just validate-strict` for this YAML if the NCBI snapshot changes.

## Additional Notes

This review was read-only. Future generated-field changes belong in source inputs or `src/taxonmech/seed.py`.
