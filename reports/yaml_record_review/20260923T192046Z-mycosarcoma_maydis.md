# YAML Record Review

- Target: `data/taxa/eukaryota/mycosarcoma_maydis.yaml`
- Taxon: `NCBITaxon:5270` (`Mycosarcoma maydis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5270`, label `Mycosarcoma maydis`.
- It is grounded exactly under `NCBITaxon:2689624` (`Mycosarcoma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mycosarcoma`.

## Validation

- `just validate data/taxa/eukaryota/mycosarcoma_maydis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycogone_sp.yaml data/taxa/eukaryota/myconymphaea_yatsukahoi.yaml data/taxa/eukaryota/mycosarcoma_maydis.yaml data/taxa/eukaryota/mycosphaerella_arachidis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51957` contains the seeded identifier with reason `attested rule: Mycosarcoma maydis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2324` matches the YAML identity: parent `NCBITaxon:2689624`, rank `SPECIES`, exact synonyms `Uredo maydis` and `Ustilago maydis`, and seven related synonyms.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2324` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37953`, where `NCBITaxon:5270` has `organism_count` 8.
- Native GOLD has 7 exact current-taxid organism rows, 7 linked projects, and 6 native analyses; the organism rows cover `FB1`, `JCM 2005`, `ATCC bA22899`, `AB33P5deltaR`, `ATCC 22904`, `ATCC 22901`, and `RK818`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 8 neotype rows for `NCBITaxon:5270`, all for `Uredo maydis` designations of `DSM 14603` or `FGSC 9021`.
- Exact StrainInfo has 176 direct records and 191 deposit rows for `NCBITaxon:5270`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:5270`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found 3 side-inventory old IDs merged into `NCBITaxon:5270`: `NCBITaxon:237631`, `NCBITaxon:2986375`, and `NCBITaxon:559306`.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows for those old IDs in `data/raw/ncbitaxon_taxa.tsv`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- The transformed GOLD aggregate has one more organism assertion than the 7 exact local native GOLD organism rows for this current taxid.
