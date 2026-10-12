# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_crassa_or74a.yaml`
- Taxon: `NCBITaxon:367110` (`Neurospora crassa OR74A`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:367110`, label `Neurospora crassa OR74A`.
- It is grounded exactly under `NCBITaxon:5141` (`Neurospora crassa`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Neurospora crassa`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_crassa_or74a.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_africana_fgsc_1740.yaml data/taxa/eukaryota/neurospora_calospora.yaml data/taxa/eukaryota/neurospora_crassa.yaml data/taxa/eukaryota/neurospora_crassa_or74a.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55372` contains the seeded identifier with reason `attested rule: Neurospora crassa OR74A, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:76790` matches the YAML identity: parent `NCBITaxon:5141`, rank `STRAIN`, five exact synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:76790` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33449`, where `NCBITaxon:367110` has `organism_count` 8.
- Native GOLD has eight exact current-taxid organism rows linked to 108 native project rows; no native analysis rows are linked to those projects in this snapshot.

## Completeness

- A structured exact scan found no rows for `NCBITaxon:367110` in `data/raw/ncbi_type_material.tsv`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:284814` and `NCBITaxon:948871` into `NCBITaxon:367110`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` point to the target, so the generated record correctly omits `replaces`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, exact StrainInfo side inventory, and checked auxiliary source rows were empty for `NCBITaxon:367110`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation adds local strain evidence for `Neurospora crassa OR74A`.

## Additional Notes

- None.
