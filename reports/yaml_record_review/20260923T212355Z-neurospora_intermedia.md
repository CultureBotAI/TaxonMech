# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_intermedia.yaml`
- Taxon: `NCBITaxon:5142` (`Neurospora intermedia`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5142`, label `Neurospora intermedia`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_intermedia.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_heterospora.yaml data/taxa/eukaryota/neurospora_hispaniola.yaml data/taxa/eukaryota/neurospora_indica.yaml data/taxa/eukaryota/neurospora_intermedia.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51946` contains the seeded identifier with reason `attested rule: Neurospora intermedia, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2258` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2258` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37571`, where `NCBITaxon:5142` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0579797` / `Neurospora intermedia FGSC 2613`, linked to 49 native project rows and no native analyses.

## Completeness

- A structured exact scan found no rows for `NCBITaxon:5142` in `data/raw/ncbi_type_material.tsv`.
- Exact StrainInfo side inventory found 680 direct records and 692 exact deposit assertions, including sampled designations `DSM 1266`, `FGSC 1940`, `IMI 317527`, `BCRC 32682`, `DSM 1265`, `FGSC 2316`, `CBS 131.92`, `CBS 268.36`, and `FGSC 2540`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:5142`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact StrainInfo side inventory and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
