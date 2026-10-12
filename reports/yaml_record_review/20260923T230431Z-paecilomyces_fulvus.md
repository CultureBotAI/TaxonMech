# YAML Record Review

- Target: `data/taxa/eukaryota/paecilomyces_fulvus.yaml`
- Taxon: `NCBITaxon:89137` (`Paecilomyces fulvus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:89137`, label `Paecilomyces fulvus`.
- It is grounded exactly under `NCBITaxon:33202` (`Paecilomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Paecilomyces`.

## Validation

- `just validate data/taxa/eukaryota/paecilomyces_fulvus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pachysolen_tannophilus.yaml data/taxa/eukaryota/paecilomyces_fulvus.yaml data/taxa/eukaryota/paecilomyces_sp.yaml data/taxa/eukaryota/paecilomyces_sp_m2901.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53471` contains the seeded identifier with reason `attested rule: Paecilomyces fulvus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:14223` matches the YAML identity: parent `NCBITaxon:33202`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:14223` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:44028`, where `NCBITaxon:89137` has `organism_count` 2.
- Native GOLD has one exact current-taxid organism row, `Go0384684` / `Byssochlamys fulva BYSS01`, linked to project `Gp0235800` and one analysis row via that project.
- Exact StrainInfo side evidence has 34 direct `NCBITaxon:89137` records and 77 deposits across those records.

## Completeness

- Exact NCBI type material has two culture-from-neotype rows for `NCBITaxon:89137`, covering `CBS 146.48` and `CBS:146.48`.
- Exact BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:89137`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, native GOLD, or StrainInfo side inventories.

## Additional Notes

- None.
