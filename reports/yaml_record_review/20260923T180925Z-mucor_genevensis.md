# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_genevensis.yaml`
- Taxon: `NCBITaxon:64492` (`Mucor genevensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:64492`, label `Mucor genevensis`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_genevensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_fuscus.yaml ... mucor_griseo_ochraceus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53077` contains the seeded identifier with reason `attested rule: Mucor genevensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8165` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor genevensis Lendn., 1907`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8165` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40304`, where `NCBITaxon:64492` has `organism_count` 8.
- Exact native GOLD expansion found eight exact current-taxid organism rows linked to eight projects; no native analysis row linked to those projects.
- `data/raw/ncbi_type_material.tsv:244322-244325` has the `CBS 114.08`, `CBS:114.08`, `MUCL 15442`, and `MUCL:15442` type-material aliases.

## Completeness

- Exact StrainInfo has 28 direct records and 43 deposit rows for `NCBITaxon:64492`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:64492`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:64492`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
