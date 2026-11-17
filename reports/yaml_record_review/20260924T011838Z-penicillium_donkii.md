# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_donkii.yaml`
- Taxon: `NCBITaxon:69772` (`Penicillium donkii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:69772`, label `Penicillium donkii`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_donkii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_dipodomyus.yaml data/taxa/eukaryota/penicillium_discolor.yaml data/taxa/eukaryota/penicillium_doidgeae.yaml data/taxa/eukaryota/penicillium_donkii.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53182` contains the seeded identifier with reason `attested rule: Penicillium donkii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:9669` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:9669` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41540`, where `NCBITaxon:69772` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:69772`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 17 rows on lines 258095-258111: 2 `culture-from-type-material` spellings centered on NRRL 5562 and 15 `type-material` spellings centered on ATCC 48439, BCRC or CCRC 31694, CBS 188.72, FRR 1738, IFO 31746, IMI 197489, and MUCL 31188.
- Exact StrainInfo side evidence has 6 direct `NCBITaxon:69772` records and 17 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:69772`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.
- NCBI type-material rows are available side evidence only and do not imply generated strain inventory rows for this record.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
