# YAML Record Review

- Target: `data/taxa/eukaryota/parathielavia_hyrcaniae_cbs_757_83.yaml`
- Taxon: `NCBITaxon:1384584` (`Parathielavia hyrcaniae CBS 757.83`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:1384584`, label `Parathielavia hyrcaniae CBS 757.83`.
- It is grounded exactly under `NCBITaxon:113614` (`Parathielavia hyrcaniae`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Parathielavia hyrcaniae`.

## Validation

- `just validate data/taxa/eukaryota/parathielavia_hyrcaniae_cbs_757_83.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/parastagonospora_nodorum_sn79.yaml data/taxa/eukaryota/parastagonospora_sp.yaml data/taxa/eukaryota/parathielavia_appendiculata_cbs_731_68.yaml data/taxa/eukaryota/parathielavia_hyrcaniae_cbs_757_83.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59780` contains the seeded identifier with reason `attested rule: Parathielavia hyrcaniae CBS 757.83, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:338326` matches the YAML identity: parent `NCBITaxon:113614`, rank `STRAIN`, no synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:338326` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:9068`, where `NCBITaxon:1384584` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, `Go0036447`, two project rows, and one analysis row for `NCBITaxon:1384584`.

## Completeness

- BacDive, exact StrainInfo side evidence, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:1384584`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
