# YAML Record Review

- Target: `data/taxa/eukaryota/pavlomulina_ranunculiformis.yaml`
- Taxon: `NCBITaxon:2904541` (`Pavlomulina ranunculiformis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2904541`, label `Pavlomulina ranunculiformis`.
- It is grounded exactly under `NCBITaxon:2904540` (`Pavlomulina`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 9 lineage entries from `root` through `Pavlomulina`.

## Validation

- `just validate data/taxa/eukaryota/pavlomulina_ranunculiformis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paullicorticium_ansatum.yaml data/taxa/eukaryota/pavlomulina_ranunculiformis.yaml data/taxa/eukaryota/pavlova_gyrans.yaml data/taxa/eukaryota/pavlova_pinguis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63371` contains the seeded identifier with reason `attested rule: Pavlomulina ranunculiformis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:569882` matches the YAML identity: parent `NCBITaxon:2904540`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 9 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:569882` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:28360`, where `NCBITaxon:2904541` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:2904541`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two holotype spellings centered on `TNS AC-58979`, two `NIES 3900` type-material spellings, and two `RCC 3430` type-material spellings.

## Completeness

- BacDive, exact StrainInfo side evidence, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:2904541`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
