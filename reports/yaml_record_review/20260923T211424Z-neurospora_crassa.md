# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_crassa.yaml`
- Taxon: `NCBITaxon:5141` (`Neurospora crassa`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5141`, label `Neurospora crassa`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_crassa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_africana_fgsc_1740.yaml data/taxa/eukaryota/neurospora_calospora.yaml data/taxa/eukaryota/neurospora_crassa.yaml data/taxa/eukaryota/neurospora_crassa_or74a.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51945` contains the seeded identifier with reason `attested rule: Neurospora crassa, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2257` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, three synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2257` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37570`, where `NCBITaxon:5141` has `organism_count` 1781.
- Exact native GOLD expansion found 1734 current-taxid organism rows, 3635 project rows linked to those organisms, and 28 project-linked native analysis rows.

## Completeness

- A structured exact scan found no rows for `NCBITaxon:5141` in `data/raw/ncbi_type_material.tsv`.
- Exact StrainInfo side inventory found 12273 direct records and 12578 exact deposit assertions, including sampled designations `IHEM 18019`, `CBS 195.57`, `ATCC 10816`, `ATCC 12525`, `IMI 075722`, and `FGSC 627`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:5141`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact StrainInfo side inventory and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- The retained GOLD aggregate count is 1781, while the current local native GOLD JSONL snapshot exposes 1734 exact organism rows. The generated source attestation follows the retained aggregate row.
