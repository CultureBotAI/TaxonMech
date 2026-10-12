# YAML Record Review

- Target: `data/taxa/eukaryota/pelagophyceae_sp_ccmp2097.yaml`
- Taxon: `NCBITaxon:483370` (`Pelagophyceae sp. CCMP2097`)
- Verdict: pass

## Target

- The record is the seeded species-level placeholder `NCBITaxon:483370`, label `Pelagophyceae sp. CCMP2097`.
- It is grounded exactly under `NCBITaxon:114041` (`unclassified Pelagophyceae`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 8 lineage entries from `root` through `unclassified Pelagophyceae`.

## Validation

- `just validate data/taxa/eukaryota/pelagophyceae_sp_ccmp2097.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pelagodinium_bei.yaml data/taxa/eukaryota/pelagomonas_calceolata.yaml data/taxa/eukaryota/pelagophyceae_sp_ccmp2097.yaml data/taxa/eukaryota/pelomyxa_schiedti.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55801` contains the seeded identifier with reason `attested rule: Pelagophyceae sp. CCMP2097, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:107954` matches the YAML identity: parent `NCBITaxon:114041`, rank `SPECIES`, one exact synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 8 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:107954` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36819`, where `NCBITaxon:483370` has `organism_count` 2.
- The native GOLD exact current-taxid scan found one organism row, 77 project rows, and no analysis rows for `NCBITaxon:483370`.

## Completeness

- BacDive, exact StrainInfo side evidence, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:483370`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
