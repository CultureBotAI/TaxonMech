# YAML Record Review

- Target: `data/taxa/eukaryota/parastagonospora_nodorum.yaml`
- Taxon: `NCBITaxon:13684` (`Parastagonospora nodorum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:13684`, label `Parastagonospora nodorum`.
- It is grounded exactly under `NCBITaxon:1351751` (`Parastagonospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Parastagonospora`.

## Validation

- `just validate data/taxa/eukaryota/parastagonospora_nodorum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/parapyrenis_maritima.yaml data/taxa/eukaryota/parasitella_parasitica.yaml data/taxa/eukaryota/parastagonospora_nodorum.yaml data/taxa/eukaryota/parastagonospora_nodorum_sn4.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52127` contains the seeded identifier with reason `attested rule: Parastagonospora nodorum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2690` matches the YAML identity: parent `NCBITaxon:1351751`, rank `SPECIES`, five exact synonyms, six related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2690` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:8834`, where `NCBITaxon:13684` has `organism_count` 157.
- The native GOLD exact current-taxid scan found 157 organism rows, 157 project rows, and 156 analysis rows for `NCBITaxon:13684`.
- Exact StrainInfo side evidence has 88 direct `NCBITaxon:13684` records and 90 deposits across those records.

## Completeness

- BacDive, NCBI type material, retained retired old-ID, checked auxiliary source rows, `data/straininfo/assemblies.tsv`, and `data/straininfo/related_records.tsv.gz` were empty for `NCBITaxon:13684`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains old ID `NCBITaxon:54791`, which now points at `NCBITaxon:13684`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
