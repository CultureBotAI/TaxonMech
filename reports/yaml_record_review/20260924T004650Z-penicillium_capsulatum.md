# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_capsulatum.yaml`
- Taxon: `NCBITaxon:69766` (`Penicillium capsulatum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:69766`, label `Penicillium capsulatum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_capsulatum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/penicillium_caperatum.yaml data/taxa/eukaryota/penicillium_caprifimosum.yaml data/taxa/eukaryota/penicillium_capsulatum.yaml data/taxa/eukaryota/penicillium_carneum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53179` contains the seeded identifier with reason `attested rule: Penicillium capsulatum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:9666` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:9666` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41537`, where `NCBITaxon:69766` has `organism_count` 11.
- The native GOLD exact current-taxid scan found 11 organism rows, four project rows, and four analysis rows linked through `AP PROJECT GOLD IDS` for `NCBITaxon:69766`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two culture-from-type-material spellings centered on `NRRL 2056` and two neotype spellings centered on `CBS 301.48`.
- Exact StrainInfo side evidence has 30 direct `NCBITaxon:69766` records and 45 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:69766`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
