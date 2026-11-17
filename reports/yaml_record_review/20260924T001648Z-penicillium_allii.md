# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_allii.yaml`
- Taxon: `NCBITaxon:1459053` (`Penicillium allii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1459053`, label `Penicillium allii`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_allii.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/penicillium_allii.yaml data/taxa/eukaryota/penicillium_allsoppiae.yaml data/taxa/eukaryota/penicillium_americanum.yaml data/taxa/eukaryota/penicillium_angulare.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60222` contains the seeded identifier with reason `attested rule: Penicillium allii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:370702` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one exact synonym, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:370702` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:11150`, where `NCBITaxon:1459053` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0685623`, two project rows, and no analysis rows for `NCBITaxon:1459053`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two culture-from-type-material spellings centered on `CBS 131.89`.
- Exact StrainInfo side evidence has 28 direct `NCBITaxon:1459053` records and 43 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1459053`.
- The sole merged-ID side row maps old `NCBITaxon:60177` to current `NCBITaxon:1459053`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
