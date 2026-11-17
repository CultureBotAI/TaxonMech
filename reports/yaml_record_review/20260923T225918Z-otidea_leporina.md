# YAML Record Review

- Target: `data/taxa/eukaryota/otidea_leporina.yaml`
- Taxon: `NCBITaxon:47199` (`Otidea leporina`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:47199`, label `Otidea leporina`.
- It is grounded exactly under `NCBITaxon:47198` (`Otidea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Otidea`.

## Validation

- `just validate data/taxa/eukaryota/otidea_leporina.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/osmozyma_mogii.yaml data/taxa/eukaryota/osmozyma_tolerans.yaml data/taxa/eukaryota/ostropella_albocincta.yaml data/taxa/eukaryota/otidea_leporina.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52718` contains the seeded identifier with reason `attested rule: Otidea leporina, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:5937` matches the YAML identity: parent `NCBITaxon:47198`, rank `SPECIES`, three exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:5937` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36462`, where `NCBITaxon:47199` has `organism_count` 1.
- The native GOLD exact current-taxid scan found no local organism, project, or analysis rows for `NCBITaxon:47199`.

## Completeness

- Exact NCBI type material has two holotype rows for `NCBITaxon:47199`, covering `H 6003548` and `H:6003548`.
- Exact StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:47199`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
