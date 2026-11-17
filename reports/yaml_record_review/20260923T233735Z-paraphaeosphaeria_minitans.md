# YAML Record Review

- Target: `data/taxa/eukaryota/paraphaeosphaeria_minitans.yaml`
- Taxon: `NCBITaxon:565426` (`Paraphaeosphaeria minitans`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:565426`, label `Paraphaeosphaeria minitans`.
- It is grounded exactly under `NCBITaxon:125369` (`Paraphaeosphaeria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Paraphaeosphaeria`.

## Validation

- `just validate data/taxa/eukaryota/paraphaeosphaeria_minitans.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paranamyces_uniporus.yaml data/taxa/eukaryota/paraphaeosphaeria_minitans.yaml data/taxa/eukaryota/paraphaeosphaeria_sporulosa.yaml data/taxa/eukaryota/paraphoma_chrysanthemicola.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56056` contains the seeded identifier with reason `attested rule: Paraphaeosphaeria minitans, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:133396` matches the YAML identity: parent `NCBITaxon:125369`, rank `SPECIES`, two exact synonyms, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:133396` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38980`, where `NCBITaxon:565426` has `organism_count` 3.
- The native GOLD exact current-taxid scan found two organism rows, two project rows, and one analysis row for `NCBITaxon:565426`.
- Exact StrainInfo side evidence has 24 direct `NCBITaxon:565426` records and 26 deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:565426`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains two old IDs that now point at `NCBITaxon:565426`: `NCBITaxon:565416` and `NCBITaxon:78389`; neither is retained as a retired taxon, so the YAML correctly has no `replaces` entries.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
