# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_ehrlichii.yaml`
- Taxon: `NCBITaxon:69796` (`Penicillium ehrlichii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:69796`, label `Penicillium ehrlichii`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_ehrlichii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_ehrlichii.yaml data/taxa/eukaryota/penicillium_eickeri.yaml data/taxa/eukaryota/penicillium_elizabethiae.yaml data/taxa/eukaryota/penicillium_euglaucum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53194` contains the seeded identifier with reason `attested rule: Penicillium ehrlichii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:9681` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Eupenicillium ehrlichii`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:9681` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41553`, where `NCBITaxon:69796` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:69796`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 15 `type-material` rows on lines 258245-258259, centered on ATCC 10442, CBS 324.48, IMI 039737, IMI 039737ii, NRRL 708, QM 1874, and VKM F-273.
- Exact StrainInfo side evidence has 4 direct `NCBITaxon:69796` records and 10 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:69796`.
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
