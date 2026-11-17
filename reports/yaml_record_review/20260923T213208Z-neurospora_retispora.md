# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_retispora.yaml`
- Taxon: `NCBITaxon:241054` (`Neurospora retispora`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:241054`, label `Neurospora retispora`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_retispora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_retispora.yaml data/taxa/eukaryota/neurospora_santi_florii.yaml data/taxa/eukaryota/neurospora_seminuda.yaml data/taxa/eukaryota/neurospora_stellata.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54703` contains the seeded identifier with reason `attested rule: Neurospora retispora, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:47343` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, three exact synonyms, four related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:47343` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:21997`, where `NCBITaxon:241054` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0651437` / `Neurospora retispora FGSC 960`, linked to projects `Gp0688341` and `Gp0699253`; no native analysis rows linked to those projects.

## Completeness

- `data/raw/ncbi_type_material.tsv:94188-94189` has duplicate culture-from-type-material spellings for `CBS 275.50` and `CBS:275.50` under `Gelasinospora retispora`.
- Exact StrainInfo side inventory found 20 direct records and 27 deposit entries, including sampled designations `CBS 212.58`, `IFO 8367`, `NBRC 8367`, `IFO 32009`, `NBRC 32009`, `IFO 32010`, `NBRC 32010`, `IFO 32844`, and `NBRC 32844`.
- `data/raw/ncbi_merged_ids.tsv:37019` maps side-inventory old ID `NCBITaxon:2075012` into `NCBITaxon:241054`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:241054`; the record correctly has `strain_count: 0`.
- The exact NCBI type-material, StrainInfo side-inventory, and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, StrainInfo, or native GOLD side inventories.

## Additional Notes

- None.
