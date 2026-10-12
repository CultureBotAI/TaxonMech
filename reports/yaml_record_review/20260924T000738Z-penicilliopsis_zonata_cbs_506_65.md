# YAML Record Review

- Target: `data/taxa/eukaryota/penicilliopsis_zonata_cbs_506_65.yaml`
- Taxon: `NCBITaxon:1073090` (`Penicilliopsis zonata CBS 506.65`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:1073090`, label `Penicilliopsis zonata CBS 506.65`.
- It is grounded exactly under `NCBITaxon:41063` (`Penicilliopsis zonata`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Penicilliopsis zonata`.

## Validation

- `just validate data/taxa/eukaryota/penicilliopsis_zonata_cbs_506_65.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/peltaster_fructicola.yaml data/taxa/eukaryota/penicilliopsis_zonata.yaml data/taxa/eukaryota/penicilliopsis_zonata_cbs_506_65.yaml data/taxa/eukaryota/penicillium_adametzioides.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57486` contains the seeded identifier with reason `attested rule: Penicilliopsis zonata CBS 506.65, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:229931` matches the YAML identity: parent `NCBITaxon:41063`, rank `STRAIN`, one exact synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:229931` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1271`, where `NCBITaxon:1073090` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0009751`, one project row, `Gp0009569`, and one analysis row for `NCBITaxon:1073090`.

## Completeness

- BacDive, exact StrainInfo side evidence, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:1073090`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
