# YAML Record Review: Halobacteriales archaeon YIM 93796

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/halobacteriales_archaeon_yim_93796.yaml
- Started UTC: 2026-09-23T11:09:29Z
- Finished UTC: 2026-09-23T11:10:36Z
- Verdict: pass

## Target

Reviewed generated TaxonRecord `data/taxa/archaea/halobacteriales_archaeon_yim_93796.yaml` for `NCBITaxon:1008192`, `Halobacteriales archaeon YIM 93796`, an archaeal `SPECIES` child of `NCBITaxon:38063` / `unclassified Halobacteriales`.

## Validation

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-halobacteriales_archaeon_yim_93796.md'`: passed with no prior report; ignored reports were included.
- `just validate-strict data/taxa/archaea/halobacteriales_archaeon_yim_93796.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93797.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93798.yaml data/taxa/archaea/halopelagius_sp_yim_93592.yaml`: passed; exited 0 for 4 files with no strict errors emitted.
- `just validate data/taxa/archaea/halobacteriales_archaeon_yim_93796.yaml`: passed, no LinkML issues.
- Skipped: product validation because there are no `causal_graphs`; history validation because this read-only review did not add a history decision; full `just verify-corpus` because no generated YAML was edited.

## Identity and Grounding

The YAML matches its pinned NCBI row exactly: `NCBITaxon:1008192`, `Halobacteriales archaeon YIM 93796`, rank `SPECIES`, parent `NCBITaxon:38063`, genetic code `11`, source `ncbitaxon`, snapshot `2026-09-13`.

## Evidence

Exact `rg --no-ignore --hidden` searches for `NCBITaxon:1008192` and `Halobacteriales archaeon YIM 93796` over `data/raw/`, `data/atb/`, and `data/straininfo/` found only `PATHS.tsv` plus the NCBI source row, which supports the identifier, label, lineage, genetic code, and NCBI source attestation.

## Completeness

No consequential gaps were found. Optional synonym, xref, nomenclature, taxonomy mapping, strain, and causal graph sections are empty because no exact same-taxon LPSN, GTDB, BacDive, GOLD, ATB, NCBI Assembly, or StrainInfo rows were present locally.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Rerun source seeding and `just validate-strict` for this YAML if the NCBI snapshot changes.

## Additional Notes

This review used the pinned 2026-09-13 NCBI row as source of truth and made no curation edits.
