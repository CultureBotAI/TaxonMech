# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_tetraspora.yaml`
- Taxon: `NCBITaxon:94610` (`Neurospora tetraspora`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:94610`, label `Neurospora tetraspora`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_tetraspora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_tetrasperma.yaml data/taxa/eukaryota/neurospora_tetraspora.yaml data/taxa/eukaryota/nia_vibrissa.yaml data/taxa/eukaryota/nidula_niveotomentosa.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53553` contains the seeded identifier with reason `attested rule: Neurospora tetraspora, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:15660` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, exact synonym `Gelasinospora tetrasperma`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:15660` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45016`, where `NCBITaxon:94610` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0358438` / `Neurospora tetraspora CBS 560.94`, linked to projects `Gp0197115` and `Gp0251463`; one native analysis links through `Gp0197115`.

## Completeness

- `data/raw/ncbi_type_material.tsv:274923-274924` has duplicate culture-from-type-material spellings for `CBS 178.33` and `CBS:178.33` under `Gelasinospora tetrasperma`.
- Exact StrainInfo side inventory found 16 direct records and 24 deposit entries, including sampled designations `IFO 6888`, `NBRC 6888`, `IFO 8522`, `NBRC 8522`, `IFO 8805`, `NBRC 8805`, `CBS 178.33`, and `CBS 592.69`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:94610`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact NCBI type-material, StrainInfo side-inventory, and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, StrainInfo, or native GOLD side inventories.

## Additional Notes

- None.
