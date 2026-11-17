# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_bilaiae.yaml`
- Taxon: `NCBITaxon:69765` (`Penicillium bilaiae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:69765`, label `Penicillium bilaiae`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_bilaiae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_bilaiae.yaml data/taxa/eukaryota/penicillium_boreae.yaml data/taxa/eukaryota/penicillium_brasilianum.yaml data/taxa/eukaryota/penicillium_brevicompactum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53178` contains the seeded identifier with reason `attested rule: Penicillium bilaiae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:9665` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:9665` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41536`, where `NCBITaxon:69765` has `organism_count` 3.
- The native GOLD exact current-taxid scan found three organism rows, 16 project rows, and one analysis row linked by `AP PROJECT GOLD IDS` for `NCBITaxon:69765`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found eight neotype spellings centered on `ATCC 22348`, `CBS 221.66`, `IMI 113677`, and `NRRL 3391`.
- Exact StrainInfo side evidence has 19 direct `NCBITaxon:69765` records and 34 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:69765`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
