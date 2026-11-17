# YAML Record Review

- Target: `data/taxa/eukaryota/paratrypanosoma_confusum.yaml`
- Taxon: `NCBITaxon:1470209` (`Paratrypanosoma confusum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1470209`, label `Paratrypanosoma confusum`.
- It is grounded exactly under `NCBITaxon:1470208` (`Paratrypanosoma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Paratrypanosoma`.

## Validation

- `just validate data/taxa/eukaryota/paratrypanosoma_confusum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paratrimastix_pyriformis.yaml data/taxa/eukaryota/paratrypanosoma_confusum.yaml data/taxa/eukaryota/parengyodontium_album.yaml data/taxa/eukaryota/parengyodontium_torokii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60241` contains the seeded identifier with reason `attested rule: Paratrypanosoma confusum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:375453` matches the YAML identity: parent `NCBITaxon:1470208`, rank `SPECIES`, two exact synonyms, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:375453` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:11331`, where `NCBITaxon:1470209` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0519928`, one project row, `Gp0444098`, and one analysis row for `NCBITaxon:1470209`.

## Completeness

- BacDive, exact StrainInfo side evidence, NCBI type material, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1470209`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains old ID `NCBITaxon:1296663`, which now points at `NCBITaxon:1470209`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
