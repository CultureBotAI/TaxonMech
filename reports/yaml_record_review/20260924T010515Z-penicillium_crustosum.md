# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_crustosum.yaml`
- Taxon: `NCBITaxon:36656` (`Penicillium crustosum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:36656`, label `Penicillium crustosum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_crustosum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_cremeogriseum.yaml data/taxa/eukaryota/penicillium_crocicola.yaml data/taxa/eukaryota/penicillium_crustosum.yaml data/taxa/eukaryota/penicillium_cryptum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52350` contains the seeded identifier with reason `attested rule: Penicillium crustosum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4093` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Penicillium solitum var. crustosum`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4093` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33438`, where `NCBITaxon:36656` has `organism_count` 3.
- The native GOLD exact current-taxid scan found three organism rows, five project rows, and one analysis row linked through `AP PROJECT GOLD IDS` for `NCBITaxon:36656`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found four culture-from-neotype spellings centered on `CBS 115503` and `FRR 1669`, plus eight type-material spellings centered on `ATCC 52044`, `IMI 91917`, `NCTC 4002`, and `Thom 5034.16`.
- Exact StrainInfo side evidence has 143 direct `NCBITaxon:36656` records and 227 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:36656`.
- The sole merged-ID side row maps old `NCBITaxon:2478652` to current `NCBITaxon:36656`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
