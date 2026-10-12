# YAML Record Review

- Target: `data/taxa/eukaryota/parengyodontium_album.yaml`
- Taxon: `NCBITaxon:37998` (`Parengyodontium album`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:37998`, label `Parengyodontium album`.
- It is grounded exactly under `NCBITaxon:1892809` (`Parengyodontium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Parengyodontium`.

## Validation

- `just validate data/taxa/eukaryota/parengyodontium_album.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/paratrimastix_pyriformis.yaml data/taxa/eukaryota/paratrypanosoma_confusum.yaml data/taxa/eukaryota/parengyodontium_album.yaml data/taxa/eukaryota/parengyodontium_torokii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52379` contains the seeded identifier with reason `attested rule: Parengyodontium album, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4313` matches the YAML identity: parent `NCBITaxon:1892809`, rank `SPECIES`, three exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4313` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33853`, where `NCBITaxon:37998` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:37998`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact StrainInfo side evidence has 41 direct `NCBITaxon:37998` records and 51 deposits across those records.

## Completeness

- BacDive, NCBI type material, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:37998`.
- The NCBI merged-ID side inventory contains old ID `NCBITaxon:5558`, which now points at `NCBITaxon:37998`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entries.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
