# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_hiemalis_f_silvaticus.yaml`
- Taxon: `NCBITaxon:155724` (`Mucor hiemalis f. silvaticus`)
- Verdict: pass

## Target

- The record is the seeded forma `NCBITaxon:155724`, label `Mucor hiemalis f. silvaticus`.
- It is grounded exactly under `NCBITaxon:64493` (`Mucor hiemalis`) with rank `FORMA`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Mucor hiemalis`.

## Validation

- `just validate data/taxa/eukaryota/mucor_hiemalis_f_silvaticus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucor_hiemalis_f_silvaticus.yaml ... mucor_indicus_b7402.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54113` contains the seeded identifier with reason `attested rule: Mucor hiemalis f. silvaticus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:32254` matches the YAML identity: parent `NCBITaxon:64493`, rank `FORMA`, exact synonym `Mucor silvaticus`, and no related synonyms.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:32254` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12454`, where `NCBITaxon:155724` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0402567` / `Mucor silvaticus NRRL 1431`, linked to project `Gp0290192`; no native analysis row linked to that project.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:155724` type-material rows.

## Completeness

- Exact StrainInfo has 22 direct records and 28 deposit rows for `NCBITaxon:155724`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:155724`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:155724`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- Native GOLD uses the synonym-bearing organism name `Mucor silvaticus NRRL 1431`, which is compatible with the NCBI exact synonym `Mucor silvaticus`.
