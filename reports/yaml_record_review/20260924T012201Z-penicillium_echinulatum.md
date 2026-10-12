# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_echinulatum.yaml`
- Taxon: `NCBITaxon:60174` (`Penicillium echinulatum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:60174`, label `Penicillium echinulatum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_echinulatum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_dunedinense.yaml data/taxa/eukaryota/penicillium_echinulatum.yaml data/taxa/eukaryota/penicillium_echinulonalgiovense.yaml data/taxa/eukaryota/penicillium_egyptiacum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53017` contains the seeded identifier with reason `attested rule: Penicillium echinulatum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:7585` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:7585` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:39775`, where `NCBITaxon:60174` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:60174`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found no rows for `NCBITaxon:60174`.
- Exact StrainInfo side evidence has 38 direct `NCBITaxon:60174` records and 61 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:60174`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
