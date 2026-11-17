# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_kobi.yaml`
- Taxon: `NCBITaxon:241062` (`Neurospora kobi`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:241062`, label `Neurospora kobi`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_kobi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_kobi.yaml data/taxa/eukaryota/neurospora_lineolata.yaml data/taxa/eukaryota/neurospora_macrospora.yaml data/taxa/eukaryota/neurospora_perkinsii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54706` contains the seeded identifier with reason `attested rule: Neurospora kobi, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:47346` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, exact synonym `Gelasinospora kobi`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:47346` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:22000`, where `NCBITaxon:241062` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0651467` / `Neurospora kobi MNHN RF-02382`, linked to projects `Gp0688371` and `Gp0699239`; no native analysis rows linked to those projects.

## Completeness

- `data/raw/ncbi_type_material.tsv:94194-94195` has duplicate culture-from-type-material spellings for `CBS 560.72` and `CBS:560.72` under `Gelasinospora kobi`.
- Exact StrainInfo side inventory found 7 direct records and 8 deposit entries, including sampled designations `MUCL 18447`, `IFO 30234`, `NBRC 30234`, `MUCL 18448`, `CBS 109.84`, and `CBS 560.72`.
- `data/raw/ncbi_merged_ids.tsv:37017` maps side-inventory old ID `NCBITaxon:2075009` into `NCBITaxon:241062`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:241062`; the record correctly has `strain_count: 0`.
- The exact NCBI type-material, StrainInfo side-inventory, and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, StrainInfo, or native GOLD side inventories.

## Additional Notes

- None.
