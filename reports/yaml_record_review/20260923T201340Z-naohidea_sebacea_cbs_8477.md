# YAML Record Review

- Target: `data/taxa/eukaryota/naohidea_sebacea_cbs_8477.yaml`
- Taxon: `NCBITaxon:1397327` (`Naohidea sebacea CBS 8477`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:1397327`, label `Naohidea sebacea CBS 8477`.
- It is grounded exactly under `NCBITaxon:112072` (`Naohidea sebacea`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Naohidea sebacea`.

## Validation

- `just validate data/taxa/eukaryota/naohidea_sebacea_cbs_8477.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nanofrustulum_trainorii.yaml data/taxa/eukaryota/naohidea_sebacea.yaml data/taxa/eukaryota/naohidea_sebacea_cbs_8477.yaml data/taxa/eukaryota/naumovozyma_baii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59850` contains the seeded identifier with reason `attested rule: Naohidea sebacea CBS 8477, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:343833` matches the YAML identity: parent `NCBITaxon:112072`, rank `STRAIN`, and genetic code `1`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:343833` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:9371`, where `NCBITaxon:1397327` has `organism_count` 1.
- The current native GOLD catalogs have no exact organism, project, or analysis rows for `NCBITaxon:1397327`; the retained GOLD aggregate in `data/raw/gold_organisms.tsv` supplies the GOLD assertion.

## Completeness

- Exact ignored-file-inclusive scans of `data/raw/ncbi_type_material.tsv` and `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:1397327`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1397327`.
- The record has no generated local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains or retained retired-ID provenance for this strain.

## Additional Notes

- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv` and can differ from current native GOLD exact rows.
