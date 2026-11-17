# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_antarctica.yaml`
- Taxon: `NCBITaxon:979670` (`Mortierella antarctica`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:979670`, label `Mortierella antarctica`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_antarctica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_alliacea.yaml ... mortierella_antarctica.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57038` contains the seeded identifier with reason `attested rule: Mortierella antarctica, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:204243` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella antarctica Linnem., 1969`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:204243` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45177`, where `NCBITaxon:979670` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0145919` / `Mortierella antarctica KOD1030` and `Go0145920` / `Mortierella antarctica KOD1229`, linked to projects `Gp0154280` and `Gp0154281`; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:275835-275838` has `SZMC 11217` culture-from-type-material aliases and `CBS 609.70` type-material aliases.

## Completeness

- Exact StrainInfo has six direct records and six deposit rows for `NCBITaxon:979670`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:979670`.
- `data/raw/ncbi_merged_ids.tsv:39270` maps retired `NCBITaxon:2217658` into this target; a complete ignored-file-inclusive retained-old-ID scan found no matching `data/raw/ncbitaxon_taxa.tsv` row, so the retired ID is side inventory only.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The `CBS 609.70` type-material alias also appears as the native GOLD culture collection ID for the KOD1229 organism row.
