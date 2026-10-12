# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_discreta_fgsc_8579.yaml`
- Taxon: `NCBITaxon:510953` (`Neurospora discreta FGSC 8579`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:510953`, label `Neurospora discreta FGSC 8579`.
- It is grounded exactly under `NCBITaxon:29879` (`Neurospora discreta`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Neurospora discreta`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_discreta_fgsc_8579.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_cratophora.yaml data/taxa/eukaryota/neurospora_dictyophora.yaml data/taxa/eukaryota/neurospora_discreta.yaml data/taxa/eukaryota/neurospora_discreta_fgsc_8579.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55866` contains the seeded identifier with reason `attested rule: Neurospora discreta FGSC 8579, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:115941` matches the YAML identity: parent `NCBITaxon:29879`, rank `STRAIN`, no synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:115941` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37497`, where `NCBITaxon:510953` has `organism_count` 2.
- The current native GOLD snapshot has one exact current-taxid organism row, `Go0006341` / `Neurospora discreta FGSC 8579 mat A`, linked to one native project and no native analyses.

## Completeness

- Exact structured scans found no rows for `NCBITaxon:510953` in `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, retained retired NCBI old IDs, exact BacDive, generated raw strain rows, generated StrainInfo target rows, exact StrainInfo side inventory, or checked auxiliary source rows.
- The record correctly has `strain_count: 0` and no generated `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation adds local strain evidence for `Neurospora discreta FGSC 8579`.

## Additional Notes

- The retained GOLD aggregate count is two, while the current local native GOLD JSONL snapshot exposes one exact organism row. The generated source attestation follows the retained aggregate row.
