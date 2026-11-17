# YAML Record Review

- Target: `data/taxa/eukaryota/paracoccidioides_lutzii_pb01.yaml`
- Taxon: `NCBITaxon:502779` (`Paracoccidioides lutzii Pb01`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:502779`, label `Paracoccidioides lutzii Pb01`.
- It is grounded exactly under `NCBITaxon:1048829` (`Paracoccidioides lutzii`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Paracoccidioides lutzii`.

## Validation

- `just validate data/taxa/eukaryota/paracoccidioides_lutzii_pb01.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/parachaetomium_inaequale.yaml data/taxa/eukaryota/paracoccidioides_brasiliensis.yaml data/taxa/eukaryota/paracoccidioides_lutzii_pb01.yaml data/taxa/eukaryota/paraconiothyrium_cyclothyrioides.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55855` contains the seeded identifier with reason `attested rule: Paracoccidioides lutzii Pb01, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:114239` matches the YAML identity: parent `NCBITaxon:1048829`, rank `STRAIN`, one exact synonym, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:114239` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37359`, where `NCBITaxon:502779` has `organism_count` 2.
- The native GOLD exact current-taxid scan found one organism row, two project rows, and one analysis row for `Paracoccidioides brasiliensis Pb01`.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:502779`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future source refresh adds non-GOLD strain evidence for this identifier.

## Additional Notes

- None.
