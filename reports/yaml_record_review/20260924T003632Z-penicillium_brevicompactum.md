# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_brevicompactum.yaml`
- Taxon: `NCBITaxon:5074` (`Penicillium brevicompactum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5074`, label `Penicillium brevicompactum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_brevicompactum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_bilaiae.yaml data/taxa/eukaryota/penicillium_boreae.yaml data/taxa/eukaryota/penicillium_brasilianum.yaml data/taxa/eukaryota/penicillium_brevicompactum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51926` contains the seeded identifier with reason `attested rule: Penicillium brevicompactum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2217` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2217` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37443`, where `NCBITaxon:5074` has `organism_count` 10.
- The native GOLD exact current-taxid scan found seven organism rows, 29 project rows, and four analysis rows linked by `AP PROJECT GOLD IDS` for `NCBITaxon:5074`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 12 culture-from-neotype spellings centered on `ATCC 9056`, `CBS 257.29`, and `NRRL 2011`, plus four neotype spellings centered on `IMI 40225`.
- Exact StrainInfo side evidence has 165 direct `NCBITaxon:5074` records and 264 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:5074`.
- The sole merged-ID side row maps old `NCBITaxon:116980` to current `NCBITaxon:5074`, and the YAML correctly uses the current identifier.
- Exact StrainInfo evidence generated two related-record rows linking `straininfo.strain:64415` and `straininfo.deposit:181030` through `NRRL 3575`; there were no target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/raw/strain_*`, and the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
