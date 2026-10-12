# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_commune.yaml`
- Taxon: `NCBITaxon:36653` (`Penicillium commune`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:36653`, label `Penicillium commune`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_commune.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_coccotrypicola.yaml data/taxa/eukaryota/penicillium_coffeae.yaml data/taxa/eukaryota/penicillium_commune.yaml data/taxa/eukaryota/penicillium_compactum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52348` contains the seeded identifier with reason `attested rule: Penicillium commune, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4091` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4091` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33434`, where `NCBITaxon:36653` has `organism_count` 12.
- The native GOLD exact current-taxid scan found 12 organism rows, four project rows, and no analysis rows for `NCBITaxon:36653`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two isotype spellings centered on `CBS 311.48` and 20 type-material spellings centered on `ATCC 10460`, `ATCC 18232`, `CBS 216.30`, `CBS 343.51`, `IFO 7727`, `IMI 089312`, `LSHB BB264`, `LSHB Sm85`, `NRRL 894`, `QM 7589`, and `QM 8148`.
- Exact StrainInfo side evidence has 85 direct `NCBITaxon:36653` records and 166 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:36653`.
- The sole merged-ID side row maps old `NCBITaxon:1009001` to current `NCBITaxon:36653`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
