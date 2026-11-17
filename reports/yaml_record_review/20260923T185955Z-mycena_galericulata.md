# YAML Record Review

- Target: `data/taxa/eukaryota/mycena_galericulata.yaml`
- Taxon: `NCBITaxon:71905` (`Mycena galericulata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:71905`, label `Mycena galericulata`.
- It is grounded exactly under `NCBITaxon:41247` (`Mycena`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Mycena`.

## Validation

- `just validate data/taxa/eukaryota/mycena_galericulata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycena_epipterygia.yaml data/taxa/eukaryota/mycena_filopes.yaml data/taxa/eukaryota/mycena_floridula.yaml data/taxa/eukaryota/mycena_galericulata.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53225` contains the seeded identifier with reason `attested rule: Mycena galericulata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:10058` matches the YAML identity: parent `NCBITaxon:41247`, rank `SPECIES`, two exact synonyms, and three related synonyms.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:10058` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41949`, where `NCBITaxon:71905` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0302577` / `Mycena galericulata CBHHK162m`, linked to native projects `Gp0157069` and `Gp0197060` and one native analysis for `Gp0157069`.

## Completeness

- Exact StrainInfo has 9 direct records and 9 deposit rows for `NCBITaxon:71905`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:71905`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found the current-ID side-inventory row `NCBITaxon:2082139 -> NCBITaxon:71905`.
- The record has no `replaces` entries, which is consistent with the absence of local retained retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
