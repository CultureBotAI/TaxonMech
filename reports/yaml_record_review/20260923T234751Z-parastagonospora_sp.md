# YAML Record Review

- Target: `data/taxa/eukaryota/parastagonospora_sp.yaml`
- Taxon: `NCBITaxon:2107949` (`Parastagonospora sp.`)
- Verdict: pass

## Target

- The record is the seeded species-level placeholder `NCBITaxon:2107949`, label `Parastagonospora sp.`.
- It is grounded exactly under `NCBITaxon:2619424` (`unclassified Parastagonospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 18 lineage entries from `root` through `unclassified Parastagonospora`.

## Validation

- `just validate data/taxa/eukaryota/parastagonospora_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/parastagonospora_nodorum_sn79.yaml data/taxa/eukaryota/parastagonospora_sp.yaml data/taxa/eukaryota/parathielavia_appendiculata_cbs_731_68.yaml data/taxa/eukaryota/parathielavia_hyrcaniae_cbs_757_83.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62358` contains the seeded identifier with reason `attested rule: Parastagonospora sp., 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:518313` matches the YAML identity: parent `NCBITaxon:2619424`, rank `SPECIES`, no synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 18 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:518313` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:20148`, where `NCBITaxon:2107949` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:2107949`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.

## Completeness

- BacDive, exact StrainInfo side evidence, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:2107949`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
