# YAML Record Review

- Target: `data/taxa/eukaryota/parvodontia_relampaga.yaml`
- Taxon: `NCBITaxon:3035422` (`Parvodontia relampaga`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:3035422`, label `Parvodontia relampaga`.
- It is grounded exactly under `NCBITaxon:2961514` (`Parvodontia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Parvodontia`.

## Validation

- `just validate data/taxa/eukaryota/parvodontia_relampaga.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/partenskyella_glossopodia.yaml data/taxa/eukaryota/parvodontia_relampaga.yaml data/taxa/eukaryota/pascua_guehoae.yaml data/taxa/eukaryota/paucimyces_polynucleatus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63493` contains the seeded identifier with reason `attested rule: Parvodontia relampaga, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:588158` matches the YAML identity: parent `NCBITaxon:2961514`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:588158` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:30399`, where `NCBITaxon:3035422` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:3035422`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found five holotype spellings centered on `FLAS F-71006` for `NCBITaxon:3035422`.

## Completeness

- BacDive, exact StrainInfo side evidence, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:3035422`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
