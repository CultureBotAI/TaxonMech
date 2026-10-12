# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_aethiopicum.yaml`
- Taxon: `NCBITaxon:36650` (`Penicillium aethiopicum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:36650`, label `Penicillium aethiopicum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_aethiopicum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_aethiopicum.yaml data/taxa/eukaryota/penicillium_albocoremium.yaml data/taxa/eukaryota/penicillium_alexiae.yaml data/taxa/eukaryota/penicillium_allaniae.yaml` exited successfully for the four-file batch.

## Identity and Grounding

- `curation/seed_scope.tsv:52345` contains the seeded identifier with reason `attested rule: Penicillium aethiopicum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4088` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4088` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33430`, where `NCBITaxon:36650` has `organism_count` 3.
- The native GOLD exact current-taxid scan found one organism row, `Go0098805`, three project rows, and no analysis rows for `NCBITaxon:36650`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 12 type-material rows centered on `CBS 484.84`, `ETH 11`, `FRR 2942`, `IBT 21501`, `IBT 5903`, and `IMI 285524`.
- Exact StrainInfo side evidence has 14 direct `NCBITaxon:36650` records and 19 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:36650`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
