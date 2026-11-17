# YAML Record Review

- Target: `data/taxa/eukaryota/paraphysomonas_imperforata.yaml`
- Taxon: `NCBITaxon:37642` (`Paraphysomonas imperforata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:37642`, label `Paraphysomonas imperforata`.
- It is grounded exactly under `NCBITaxon:36769` (`Paraphysomonas`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Paraphysomonas`.

## Validation

- `just validate data/taxa/eukaryota/paraphysomonas_imperforata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paraphysoderma_sedebokerense.yaml data/taxa/eukaryota/paraphysomonas_bandaiensis.yaml data/taxa/eukaryota/paraphysomonas_imperforata.yaml data/taxa/eukaryota/paraphysomonas_vestita.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52373` contains the seeded identifier with reason `attested rule: Paraphysomonas imperforata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4267` matches the YAML identity: parent `NCBITaxon:36769`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4267` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33752`, where `NCBITaxon:37642` has `organism_count` 2.
- The native GOLD exact current-taxid scan found three organism rows, four project rows, and one analysis row for `NCBITaxon:37642`; the project-backed rows include GOLD organism `Go0008515` and project `Gp0003947`.
- Exact StrainInfo side evidence has one direct `NCBITaxon:37642` record, `siID` 346770 with DOI `10.60712/SI-ID346770.1`, and one non-type deposit, `CCAP 935/13`.

## Completeness

- BacDive, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:37642`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
