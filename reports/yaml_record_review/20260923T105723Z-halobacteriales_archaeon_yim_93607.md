# YAML Record Review: Halobacteriales archaeon YIM 93607

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/halobacteriales_archaeon_yim_93607.yaml
- Started UTC: 2026-09-23T10:55:42Z
- Finished UTC: 2026-09-23T10:57:23Z
- Verdict: pass

## Target

Reviewed `data/taxa/archaea/halobacteriales_archaeon_yim_93607.yaml`.

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1008169` |
| label | `Halobacteriales archaeon YIM 93607` |
| rank | `SPECIES` |
| domain | `ARCHAEA` |
| parent | `NCBITaxon:38063` / `unclassified Halobacteriales` |
| generated status | Seeded from pinned source inventories in `data/raw/`, `data/atb/`, and `data/straininfo/` |

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-halobacteriales_archaeon_yim_93607.md'` | Passed: no prior report for this stem; `find` inspected ignored report files. |
| `just validate-strict data/taxa/archaea/halobacteriales_archaeon_yim_93606.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93607.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93608.yaml data/taxa/archaea/halobacteriales_archaeon_yim_93615.yaml` | Passed: exited 0 for 4 files with no strict-validation errors emitted. |
| `just validate data/taxa/archaea/halobacteriales_archaeon_yim_93607.yaml` | Passed: LinkML validation reported no issues. |

`just validate-products` was skipped because this taxon has no `causal_graphs`. `just validate-history` was skipped because this read-only review did not add a history decision. The full-corpus `just verify-corpus` gate was skipped for this individual review batch because these reports do not edit generated taxon YAML.

## Identity and Grounding

The record consistently denotes the NCBI species-level placeholder `NCBITaxon:1008169`, `Halobacteriales archaeon YIM 93607`.

- The curated identifier, label, rank, `parent_taxon`, genetic code, and NCBI-only source attestation match the pinned row in `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1008169`, `Halobacteriales archaeon YIM 93607`, `SPECIES`, parent `NCBITaxon:38063`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.
- The lineage terminates at `NCBITaxon:38063` / `unclassified Halobacteriales`, matching the raw NCBI parent.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a record keyed to its source NCBI taxon.
- No synonyms, xrefs, nomenclature, taxonomy mappings, strains, or causal graph are expected for this NCBI-only row.

## Evidence

The only material biological assertion is the NCBI identity and placement. Exact `rg --no-ignore --hidden` searches for `NCBITaxon:1008169` and `Halobacteriales archaeon YIM 93607` over `data/raw/`, `data/atb/`, and `data/straininfo/` found the NCBI source row and no auxiliary same-taxon rows.

No external live source pages were used; the pinned 2026-09-13 NCBI row is the reviewed source of truth for this generated record.

## Completeness

No consequential gaps were found.

- `strain_count: 0` is consistent with the absence of exact BacDive, GOLD, ATB, NCBI Assembly, GTDB genome, and StrainInfo rows for this NCBI ID.
- Empty optional nomenclature, mapping, synonym, xref, strain, and causal-graph sections are expected.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No record-specific follow-up is needed. If the pinned NCBI snapshot changes, rerun source seeding and the narrow validators used above.

## Additional Notes

This review was read-only. Future generated-field changes should be made in the source seed inputs or `src/taxonmech/seed.py`, not by hand-editing this YAML.
