# YAML Record Review

- Target: `data/taxa/eukaryota/pedinellales_sp_ccmp2098.yaml`
- Taxon: `NCBITaxon:483369` (`Pedinellales sp. CCMP2098`)
- Verdict: pass

## Target

- The record is the seeded species-level placeholder `NCBITaxon:483369`, label `Pedinellales sp. CCMP2098`.
- It is grounded exactly under `NCBITaxon:483368` (`unclassified Pedinellales`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 9 lineage entries from `root` through `unclassified Pedinellales`.

## Validation

- `just validate data/taxa/eukaryota/pedinellales_sp_ccmp2098.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/paxillus_rubicundulus.yaml data/taxa/eukaryota/pecoramyces_ruminantium.yaml data/taxa/eukaryota/pedinellales_sp_ccmp2098.yaml data/taxa/eukaryota/pelagococcus_subviridis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55800` contains the seeded identifier with reason `attested rule: Pedinellales sp. CCMP2098, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:107953` matches the YAML identity: parent `NCBITaxon:483368`, rank `SPECIES`, no synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 9 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:107953` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36818`, where `NCBITaxon:483369` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:483369`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.

## Completeness

- BacDive, exact StrainInfo side evidence, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:483369`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
