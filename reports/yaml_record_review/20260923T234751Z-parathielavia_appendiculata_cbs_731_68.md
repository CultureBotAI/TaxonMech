# YAML Record Review

- Target: `data/taxa/eukaryota/parathielavia_appendiculata_cbs_731_68.yaml`
- Taxon: `NCBITaxon:1384585` (`Parathielavia appendiculata CBS 731.68`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:1384585`, label `Parathielavia appendiculata CBS 731.68`.
- It is grounded exactly under `NCBITaxon:2587402` (`Parathielavia appendiculata`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Parathielavia appendiculata`.

## Validation

- `just validate data/taxa/eukaryota/parathielavia_appendiculata_cbs_731_68.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/parastagonospora_nodorum_sn79.yaml data/taxa/eukaryota/parastagonospora_sp.yaml data/taxa/eukaryota/parathielavia_appendiculata_cbs_731_68.yaml data/taxa/eukaryota/parathielavia_hyrcaniae_cbs_757_83.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59781` contains the seeded identifier with reason `attested rule: Parathielavia appendiculata CBS 731.68, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:338327` matches the YAML identity: parent `NCBITaxon:2587402`, rank `STRAIN`, no synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:338327` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:9069`, where `NCBITaxon:1384585` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0036450`, two project rows, and one analysis row for `NCBITaxon:1384585`.

## Completeness

- BacDive, exact StrainInfo side evidence, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:1384585`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
