# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_indica.yaml`
- Taxon: `NCBITaxon:241059` (`Neurospora indica`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:241059`, label `Neurospora indica`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_indica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_heterospora.yaml data/taxa/eukaryota/neurospora_hispaniola.yaml data/taxa/eukaryota/neurospora_indica.yaml data/taxa/eukaryota/neurospora_intermedia.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54704` contains the seeded identifier with reason `attested rule: Neurospora indica, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:47344` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, five synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:47344` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:21998`, where `NCBITaxon:241059` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0651420` / `Neurospora indica FGSC 7793`, linked to two native projects and no native analyses.

## Completeness

- A structured exact scan found no rows for `NCBITaxon:241059` in `data/raw/ncbi_type_material.tsv`.
- Exact StrainInfo side inventory found 8 direct records and 14 exact deposit assertions, including sampled designations `IFO 30246`, `NBRC 30246`, `IFO 30247`, `NBRC 30247`, `CBS 263.91`, `IMI 364322`, `UAMH 7727`, `ATCC 76346`, and `FGSC 7793`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old ID `NCBITaxon:2075007` into `NCBITaxon:241059`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points to the target, so the generated record correctly omits `replaces`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and checked auxiliary source rows were empty for `NCBITaxon:241059`; the record correctly has `strain_count: 0`.
- The exact StrainInfo side inventory did not materialize local strain rows; StrainInfo only joins through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
