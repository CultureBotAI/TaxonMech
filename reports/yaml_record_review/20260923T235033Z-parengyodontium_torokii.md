# YAML Record Review

- Target: `data/taxa/eukaryota/parengyodontium_torokii.yaml`
- Taxon: `NCBITaxon:3039824` (`Parengyodontium torokii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:3039824`, label `Parengyodontium torokii`.
- It is grounded exactly under `NCBITaxon:1892809` (`Parengyodontium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Parengyodontium`.

## Validation

- `just validate data/taxa/eukaryota/parengyodontium_torokii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paratrimastix_pyriformis.yaml data/taxa/eukaryota/paratrypanosoma_confusum.yaml data/taxa/eukaryota/parengyodontium_album.yaml data/taxa/eukaryota/parengyodontium_torokii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63494` contains the seeded identifier with reason `attested rule: Parengyodontium torokii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:588723` matches the YAML identity: parent `NCBITaxon:1892809`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:588723` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:30448`, where `NCBITaxon:3039824` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0647367`, one project row, `Gp0683434`, and one analysis row for `NCBITaxon:3039824`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found eight culture-from-holotype spellings centered on `NRRL 64203` and `NRRL FJII-L10-SW-P1`.
- Exact StrainInfo side evidence has three direct `NCBITaxon:3039824` records and three deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:3039824`.
- The NCBI merged-ID side inventory contains old ID `NCBITaxon:2778099`, which now points at `NCBITaxon:3039824`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entries.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
