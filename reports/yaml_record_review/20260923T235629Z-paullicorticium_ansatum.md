# YAML Record Review

- Target: `data/taxa/eukaryota/paullicorticium_ansatum.yaml`
- Taxon: `NCBITaxon:264205` (`Paullicorticium ansatum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:264205`, label `Paullicorticium ansatum`.
- It is grounded exactly under `NCBITaxon:139124` (`Paullicorticium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Paullicorticium`.

## Validation

- `just validate data/taxa/eukaryota/paullicorticium_ansatum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/paullicorticium_ansatum.yaml data/taxa/eukaryota/pavlomulina_ranunculiformis.yaml data/taxa/eukaryota/pavlova_gyrans.yaml data/taxa/eukaryota/pavlova_pinguis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54866` contains the seeded identifier with reason `attested rule: Paullicorticium ansatum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:54024` matches the YAML identity: parent `NCBITaxon:139124`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:54024` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:24237`, where `NCBITaxon:264205` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0609065`, two project rows, and no analysis rows for `NCBITaxon:264205`.

## Completeness

- BacDive, exact StrainInfo side evidence, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:264205`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
