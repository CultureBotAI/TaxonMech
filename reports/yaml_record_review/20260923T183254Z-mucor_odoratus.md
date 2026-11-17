# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_odoratus.yaml`
- Taxon: `NCBITaxon:1196544` (`Mucor odoratus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1196544`, label `Mucor odoratus`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_odoratus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_nidicola.yaml ... mucor_petropolitanus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58295` contains the seeded identifier with reason `attested rule: Mucor odoratus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:269151` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor odoratus Treschew, 1941`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:269151` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:4743`, where `NCBITaxon:1196544` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0402597` / `Mucor odoratus NRRL 3064`, linked to project `Gp0290222`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:12978-12985` has eight type-material aliases: `BCRC:32155`, `CBS 130.41`, `CBS:130.41`, `CCRC 32155`, `CCRC:32155`, `VKM F-1236`, `VKM:F-1236`, and `VKM:F:1236`.

## Completeness

- Exact StrainInfo has 8 direct records and 14 deposit rows for `NCBITaxon:1196544`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1196544`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1196544`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- None.
