# YAML Record Review

- Target: `data/taxa/eukaryota/paraphysoderma_sedebokerense.yaml`
- Taxon: `NCBITaxon:1500003` (`Paraphysoderma sedebokerense`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1500003`, label `Paraphysoderma sedebokerense`.
- It is grounded exactly under `NCBITaxon:1500004` (`Paraphysoderma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 11 lineage entries from `root` through `Paraphysoderma`.

## Validation

- `just validate data/taxa/eukaryota/paraphysoderma_sedebokerense.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paraphysoderma_sedebokerense.yaml data/taxa/eukaryota/paraphysomonas_bandaiensis.yaml data/taxa/eukaryota/paraphysomonas_imperforata.yaml data/taxa/eukaryota/paraphysomonas_vestita.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60322` contains the seeded identifier with reason `attested rule: Paraphysoderma sedebokerense, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:384932` matches the YAML identity: parent `NCBITaxon:1500004`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 11 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:384932` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:11704`, where `NCBITaxon:1500003` has `organism_count` 2.
- The native GOLD exact current-taxid scan found two organism rows, three project rows, and one analysis row for `NCBITaxon:1500003`, including GOLD organism IDs `Go0136950` and `Go0515114`.

## Completeness

- BacDive, exact StrainInfo side evidence, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:1500003`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
