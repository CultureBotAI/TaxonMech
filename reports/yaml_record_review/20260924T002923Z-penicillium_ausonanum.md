# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_ausonanum.yaml`
- Taxon: `NCBITaxon:2595039` (`Penicillium ausonanum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2595039`, label `Penicillium ausonanum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_ausonanum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_aurantiacobrunneum.yaml data/taxa/eukaryota/penicillium_ausonanum.yaml data/taxa/eukaryota/penicillium_austroafricanum.yaml data/taxa/eukaryota/penicillium_baarnense.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62882` contains the seeded identifier with reason `attested rule: Penicillium ausonanum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:535053` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:535053` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:23825`, where `NCBITaxon:2595039` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:2595039`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found eight culture-from-holotype spellings centered on `CBS 148237` and `FMR 16948`, plus four holotype spellings centered on `CBS H-24781`.
- Exact StrainInfo side evidence has two direct `NCBITaxon:2595039` records and two deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:2595039`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.
