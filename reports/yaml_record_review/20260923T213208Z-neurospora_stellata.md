# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_stellata.yaml`
- Taxon: `NCBITaxon:241061` (`Neurospora stellata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:241061`, label `Neurospora stellata`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_stellata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_retispora.yaml data/taxa/eukaryota/neurospora_santi_florii.yaml data/taxa/eukaryota/neurospora_seminuda.yaml data/taxa/eukaryota/neurospora_stellata.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54705` contains the seeded identifier with reason `attested rule: Neurospora stellata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:47345` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:47345` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:21999`, where `NCBITaxon:241061` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0651459` / `Neurospora stellata MNHN RF-02395`, linked to projects `Gp0688363` and `Gp0699241`; no native analysis rows linked to those projects.

## Completeness

- `data/raw/ncbi_type_material.tsv:94190-94193` has culture-from-type-material rows for `CBS 561.72`, `CBS:561.72`, `IFO 30242`, and `IFO:30242` under `Gelasinospora stellata`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:241061`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact NCBI type-material and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
