# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_atramentosum.yaml`
- Taxon: `NCBITaxon:36652` (`Penicillium atramentosum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:36652`, label `Penicillium atramentosum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_atramentosum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_arabicum.yaml data/taxa/eukaryota/penicillium_arizonense.yaml data/taxa/eukaryota/penicillium_athertonense.yaml data/taxa/eukaryota/penicillium_atramentosum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52347` contains the seeded identifier with reason `attested rule: Penicillium atramentosum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4090` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4090` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33432`, where `NCBITaxon:36652` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:36652`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two culture-from-neotype spellings centered on `NRRL 795` and two neotype spellings centered on `CBS 291.48`.
- Exact StrainInfo side evidence has 46 direct `NCBITaxon:36652` records and 73 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:36652`.
- The sole merged-ID side row maps old `NCBITaxon:1353554` to current `NCBITaxon:36652`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
