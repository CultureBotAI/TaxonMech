# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_seminuda.yaml`
- Taxon: `NCBITaxon:303338` (`Neurospora seminuda`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:303338`, label `Neurospora seminuda`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_seminuda.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_retispora.yaml data/taxa/eukaryota/neurospora_santi_florii.yaml data/taxa/eukaryota/neurospora_seminuda.yaml data/taxa/eukaryota/neurospora_stellata.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55083` contains the seeded identifier with reason `attested rule: Neurospora seminuda, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:62088` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, exact synonym `Gelasinospora seminuda`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:62088` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:30351`, where `NCBITaxon:303338` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0651465` / `Neurospora seminuda MNHN RF-02393`, linked to projects `Gp0688369` and `Gp0699312`; no native analysis rows linked to those projects.

## Completeness

- `data/raw/ncbi_type_material.tsv:157468-157469` has duplicate `isotype` spellings for `CBS 572.72` and `CBS:572.72` under `Gelasinospora seminuda`.
- Exact StrainInfo side inventory found 7 direct records and 9 deposit entries, including sampled designations `IFO 31374`, `NBRC 31374`, `IFO 32891`, `NBRC 32891`, `CBS 572.72`, `CBS 702.96`, and `IMI 364324`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:303338`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact NCBI type-material, StrainInfo side-inventory, and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, StrainInfo, or native GOLD side inventories.

## Additional Notes

- None.
