# YAML Record Review

- Target: `data/taxa/eukaryota/pavlova_pinguis.yaml`
- Taxon: `NCBITaxon:119481` (`Pavlova pinguis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:119481`, label `Pavlova pinguis`.
- It is grounded exactly under `NCBITaxon:2831` (`Pavlova`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 9 lineage entries from `root` through `Pavlova`.

## Validation

- `just validate data/taxa/eukaryota/pavlova_pinguis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paullicorticium_ansatum.yaml data/taxa/eukaryota/pavlomulina_ranunculiformis.yaml data/taxa/eukaryota/pavlova_gyrans.yaml data/taxa/eukaryota/pavlova_pinguis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53847` contains the seeded identifier with reason `attested rule: Pavlova pinguis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:22398` matches the YAML identity: parent `NCBITaxon:2831`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 9 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:22398` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:4638`, where `NCBITaxon:119481` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:119481`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact StrainInfo side evidence has five direct `NCBITaxon:119481` records and seven deposits across those records.

## Completeness

- BacDive, NCBI type material, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:119481`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
