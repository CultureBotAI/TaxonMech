# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_sp.yaml`
- Taxon: `NCBITaxon:1715235` (`Mortierella sp.`)
- Verdict: pass

## Target

- The record is the seeded species-rank NCBI placeholder `NCBITaxon:1715235`, label `Mortierella sp.`.
- It is grounded exactly under `NCBITaxon:2604474` (`unclassified Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `unclassified Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_sp.yaml ... mortierella_turficola.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61155` contains the seeded identifier with reason `attested rule: Mortierella sp., 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:447641` matches the YAML identity: parent `NCBITaxon:2604474`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella sp`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:447641` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:14880`, where `NCBITaxon:1715235` has `organism_count` 31.
- Native GOLD has seven exact current-taxid organism rows for strains `KOD 989`, `JL 126`, `NB1`, `FSU 13910`, `JL 128`, `MGC 100`, and `BESC-360`, linked to seven projects; a full project-ID join found no linked native analysis rows.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:1715235` type-material rows.

## Completeness

- Exact StrainInfo had no direct records or deposit rows for `NCBITaxon:1715235`.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1715235`.
- `data/raw/ncbi_merged_ids.tsv:32976` carries side-inventory old ID `NCBITaxon:1941413 -> NCBITaxon:1715235`, but the bounded scan found no retained retired row in `data/raw/ncbitaxon_taxa.tsv`; generated `replaces` omission is consistent with local retained-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation materializes local strain rows for one of the exact native GOLD organism strains.

## Additional Notes

- The transformed GOLD aggregate asserts 31 organisms, while the complete local native exact current-taxid scan currently exposes seven organism JSONL rows and seven project JSONL rows.
