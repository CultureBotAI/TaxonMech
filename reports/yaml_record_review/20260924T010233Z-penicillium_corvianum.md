# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_corvianum.yaml`
- Taxon: `NCBITaxon:1850974` (`Penicillium corvianum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1850974`, label `Penicillium corvianum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_corvianum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_copticola.yaml data/taxa/eukaryota/penicillium_coralligerum.yaml data/taxa/eukaryota/penicillium_corvianum.yaml data/taxa/eukaryota/penicillium_cravenianum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61358` contains the seeded identifier with reason `attested rule: Penicillium corvianum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:483102` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:483102` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:16459`, where `NCBITaxon:1850974` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:1850974`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found four culture-from-holotype spellings centered on `CBS 141000` and `KAS 3618`, plus two holotype spellings centered on `DAOM 695764`.
- Exact StrainInfo side evidence has one direct `NCBITaxon:1850974` record and one deposit across that record.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1850974`.
- Two merged-ID side rows map old `NCBITaxon:1853514` and `NCBITaxon:1853515` to current `NCBITaxon:1850974`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
