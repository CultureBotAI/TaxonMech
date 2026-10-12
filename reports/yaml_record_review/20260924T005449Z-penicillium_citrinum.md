# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_citrinum.yaml`
- Taxon: `NCBITaxon:5077` (`Penicillium citrinum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5077`, label `Penicillium citrinum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_citrinum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_citrinum.yaml data/taxa/eukaryota/penicillium_claroviride.yaml data/taxa/eukaryota/penicillium_clavigerum.yaml data/taxa/eukaryota/penicillium_clavistipitatum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51928` contains the seeded identifier with reason `attested rule: Penicillium citrinum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2219` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2219` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37450`, where `NCBITaxon:5077` has `organism_count` 26.
- The native GOLD exact current-taxid scan found 25 organism rows, 25 project rows, and 22 analysis rows linked through `AP PROJECT GOLD IDS` for `NCBITaxon:5077`; the generated GOLD aggregate count matches the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 10 culture-from-neotype spellings centered on `ATCC 1109`, `CBS 139.45`, `IMI 091961`, `MUCL 29781`, and `NRRL 1841`.
- Exact StrainInfo side evidence has 182 direct `NCBITaxon:5077` records and 301 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:5077`.
- Two merged-ID side rows map old `NCBITaxon:2211329` and `NCBITaxon:60176` to current `NCBITaxon:5077`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
