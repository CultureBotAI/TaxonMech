# YAML Record Review: Halobacteriales archaeon YIM 93697

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/halobacteriales_archaeon_yim_93697.yaml
- Started UTC: 2026-09-23T11:00:49Z
- Finished UTC: 2026-09-23T11:02:04Z
- Verdict: pass

## Target

Reviewed generated TaxonRecord `data/taxa/archaea/halobacteriales_archaeon_yim_93697.yaml` for `NCBITaxon:1008178`, `Halobacteriales archaeon YIM 93697`, an archaeal `SPECIES` child of `NCBITaxon:38063` / `unclassified Halobacteriales`.

## Validation

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-halobacteriales_archaeon_yim_93697.md'`: passed with no prior report; the check covered ignored report files.
- `just validate-strict data/taxa/archaea/halobacteriales_archaeon_yim_93694.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93696.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93697.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93699.yaml`: passed, 4 files scanned, 0 files with errors, 0 total error rows.
- `just validate data/taxa/archaea/halobacteriales_archaeon_yim_93697.yaml`: passed, no LinkML issues.
- Skipped: product validation, because there are no `causal_graphs`; history validation, because this read-only review did not add a history decision; full `just verify-corpus`, because no generated YAML was edited.

## Identity and Grounding

The record matches the pinned NCBI Taxonomy row exactly: identifier `NCBITaxon:1008178`, label `Halobacteriales archaeon YIM 93697`, rank `SPECIES`, parent `NCBITaxon:38063`, genetic code `11`, source `ncbitaxon`, snapshot `2026-09-13`. The lineage ends at the same parent, `grounding_status: EXACT` is appropriate for an NCBI-keyed record, and `mapping_status: SEEDED` matches the generated provenance.

## Evidence

Exact `rg --no-ignore --hidden` searches for `NCBITaxon:1008178` and `Halobacteriales archaeon YIM 93697` over `data/raw/`, `data/atb/`, and `data/straininfo/` found only the `PATHS.tsv` entry and the `data/raw/ncbitaxon_taxa.tsv` source row. The pinned NCBI row is the reviewed source of truth; no live source page was used.

## Completeness

No consequential gaps were found. The empty synonym, xref, nomenclature, taxonomy mapping, strain, and causal-graph sections are consistent with the absence of exact same-taxon LPSN, GTDB, BacDive, GOLD, ATB, NCBI Assembly, and StrainInfo rows.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If the NCBI snapshot changes, rerun source seeding and `just validate-strict` on the regenerated record.

## Additional Notes

This review was read-only; future generated-field changes belong in source inputs or `src/taxonmech/seed.py`.
