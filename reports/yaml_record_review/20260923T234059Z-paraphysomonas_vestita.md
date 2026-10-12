# YAML Record Review

- Target: `data/taxa/eukaryota/paraphysomonas_vestita.yaml`
- Taxon: `NCBITaxon:36770` (`Paraphysomonas vestita`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:36770`, label `Paraphysomonas vestita`.
- It is grounded exactly under `NCBITaxon:36769` (`Paraphysomonas`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Paraphysomonas`.

## Validation

- `just validate data/taxa/eukaryota/paraphysomonas_vestita.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paraphysoderma_sedebokerense.yaml data/taxa/eukaryota/paraphysomonas_bandaiensis.yaml data/taxa/eukaryota/paraphysomonas_imperforata.yaml data/taxa/eukaryota/paraphysomonas_vestita.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52353` contains the seeded identifier with reason `attested rule: Paraphysomonas vestita, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4113` matches the YAML identity: parent `NCBITaxon:36769`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4113` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33470`, where `NCBITaxon:36770` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row for `NCBITaxon:36770`, GOLD organism `Go0368778`, and no native GOLD project or analysis rows.
- Exact StrainInfo side evidence has two direct `NCBITaxon:36770` records, `siID` 346771 and `siID` 357990, with non-type deposits `CCAP 935/14` and `NIES-1377`.

## Completeness

- BacDive, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:36770`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
