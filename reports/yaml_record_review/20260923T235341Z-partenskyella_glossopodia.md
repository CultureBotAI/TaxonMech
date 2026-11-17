# YAML Record Review

- Target: `data/taxa/eukaryota/partenskyella_glossopodia.yaml`
- Taxon: `NCBITaxon:552666` (`Partenskyella glossopodia`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:552666`, label `Partenskyella glossopodia`.
- It is grounded exactly under `NCBITaxon:647365` (`Partenskyella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 8 lineage entries from `root` through `Partenskyella`.

## Validation

- `just validate data/taxa/eukaryota/partenskyella_glossopodia.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/partenskyella_glossopodia.yaml data/taxa/eukaryota/parvodontia_relampaga.yaml data/taxa/eukaryota/pascua_guehoae.yaml data/taxa/eukaryota/paucimyces_polynucleatus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55983` contains the seeded identifier with reason `attested rule: Partenskyella glossopodia, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:129383` matches the YAML identity: parent `NCBITaxon:647365`, rank `SPECIES`, one exact synonym, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 8 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:129383` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38611`, where `NCBITaxon:552666` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0368779`, and no project or analysis rows for `NCBITaxon:552666`.

## Completeness

- BacDive, exact StrainInfo side evidence, NCBI type material, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:552666`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains old ID `NCBITaxon:629694`, which now points at `NCBITaxon:552666`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
