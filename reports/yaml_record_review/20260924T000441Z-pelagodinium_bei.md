# YAML Record Review

- Target: `data/taxa/eukaryota/pelagodinium_bei.yaml`
- Taxon: `NCBITaxon:43686` (`Pelagodinium bei`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:43686`, label `Pelagodinium bei`.
- It is grounded exactly under `NCBITaxon:766107` (`Pelagodinium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 9 lineage entries from `root` through `Pelagodinium`.

## Validation

- `just validate data/taxa/eukaryota/pelagodinium_bei.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/pelagodinium_bei.yaml data/taxa/eukaryota/pelagomonas_calceolata.yaml data/taxa/eukaryota/pelagophyceae_sp_ccmp2097.yaml data/taxa/eukaryota/pelomyxa_schiedti.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52543` contains the seeded identifier with reason `attested rule: Pelagodinium bei, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:5253` matches the YAML identity: parent `NCBITaxon:766107`, rank `SPECIES`, one exact synonym, four related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 9 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:5253` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:35455`, where `NCBITaxon:43686` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0368784`, and no project or analysis rows for `NCBITaxon:43686`.

## Completeness

- BacDive, exact StrainInfo side evidence, NCBI type material, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:43686`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains old ID `NCBITaxon:3111326`, which now points at `NCBITaxon:43686`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
