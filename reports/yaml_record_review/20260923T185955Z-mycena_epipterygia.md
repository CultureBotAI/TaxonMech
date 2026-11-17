# YAML Record Review

- Target: `data/taxa/eukaryota/mycena_epipterygia.yaml`
- Taxon: `NCBITaxon:230806` (`Mycena epipterygia`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:230806`, label `Mycena epipterygia`.
- It is grounded exactly under `NCBITaxon:41247` (`Mycena`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Mycena`.

## Validation

- `just validate data/taxa/eukaryota/mycena_epipterygia.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycena_epipterygia.yaml data/taxa/eukaryota/mycena_filopes.yaml data/taxa/eukaryota/mycena_floridula.yaml data/taxa/eukaryota/mycena_galericulata.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54646` contains the seeded identifier with reason `attested rule: Mycena epipterygia, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:45353` matches the YAML identity: parent `NCBITaxon:41247`, rank `SPECIES`, one exact synonym, and three related synonyms.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:45353` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:21648`, where `NCBITaxon:230806` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0367697` / `Mycena epipterygia CBHHK145m`, linked to native projects `Gp0207998` and `Gp0251459` and one native analysis for `Gp0207998`.

## Completeness

- Exact StrainInfo has 9 direct records and 9 deposit rows for `NCBITaxon:230806`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, exact type-material rows, and all checked auxiliary source rows were empty for `NCBITaxon:230806`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found the current-ID side-inventory row `NCBITaxon:1263286 -> NCBITaxon:230806`.
- The record has no `replaces` entries, which is consistent with the absence of local retained retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
