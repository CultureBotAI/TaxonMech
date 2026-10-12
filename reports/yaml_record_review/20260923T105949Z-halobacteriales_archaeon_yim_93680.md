# YAML Record Review: Halobacteriales archaeon YIM 93680

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/halobacteriales_archaeon_yim_93680.yaml
- Started UTC: 2026-09-23T10:58:35Z
- Finished UTC: 2026-09-23T10:59:49Z
- Verdict: pass

## Target

Reviewed `data/taxa/archaea/halobacteriales_archaeon_yim_93680.yaml`: `NCBITaxon:1008173`, label `Halobacteriales archaeon YIM 93680`, rank `SPECIES`, domain `ARCHAEA`, generated from the pinned inventories under `data/raw/`, `data/atb/`, and `data/straininfo/`.

## Validation

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-halobacteriales_archaeon_yim_93680.md'`: passed; no prior report for this stem, with ignored reports included.
- `just validate-strict data/taxa/archaea/halobacteriales_archaeon_yim_93671.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93680.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93683.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93689.yaml`: passed; 4 files scanned, 0 files with errors, 0 total error rows.
- `just validate data/taxa/archaea/halobacteriales_archaeon_yim_93680.yaml`: passed; LinkML validation reported no issues.
- Skipped: `just validate-products` because the taxon has no `causal_graphs`; `just validate-history` because this read-only review did not add a history decision; full-corpus `just verify-corpus` because no generated taxon YAML was edited.

## Identity and Grounding

The record is grounded exactly to its NCBI species placeholder. The pinned `data/raw/ncbitaxon_taxa.tsv` row has `NCBITaxon:1008173`, `Halobacteriales archaeon YIM 93680`, rank `SPECIES`, parent `NCBITaxon:38063`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`, matching the YAML identifier, label, rank, `parent_taxon`, lineage terminus `unclassified Halobacteriales`, `genetic_code`, and NCBI source attestation.

## Evidence

Exact `rg --no-ignore --hidden` searches for `NCBITaxon:1008173` and `Halobacteriales archaeon YIM 93680` over `data/raw/`, `data/atb/`, and `data/straininfo/` found only the expected `PATHS.tsv` and NCBI rows. No live source pages were used; the pinned 2026-09-13 NCBI row is the reviewed source of truth.

## Completeness

No consequential gaps were found. `strain_count: 0` and the empty synonym, xref, nomenclature, taxonomy-mapping, strain, and causal-graph sections are consistent with the absence of exact same-taxon BacDive, GOLD, ATB, NCBI Assembly, GTDB genome, LPSN, and StrainInfo rows.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No record-specific follow-up is needed. Rerun source seeding and the same narrow validators if the pinned NCBI snapshot changes.

## Additional Notes

This review was read-only. Future generated-field changes should be made in the source seed inputs or `src/taxonmech/seed.py`, not by hand-editing this YAML.
