# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_santi_florii.yaml`
- Taxon: `NCBITaxon:176682` (`Neurospora santi-florii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:176682`, label `Neurospora santi-florii`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_santi_florii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_retispora.yaml data/taxa/eukaryota/neurospora_santi_florii.yaml data/taxa/eukaryota/neurospora_seminuda.yaml data/taxa/eukaryota/neurospora_stellata.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54307` contains the seeded identifier with reason `attested rule: Neurospora santi-florii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:35722` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, exact synonym `Gelasinospora santi-florii`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:35722` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:15396`, where `NCBITaxon:176682` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0651461` / `Neurospora santi-florii MNHN RF-02390`, linked to projects `Gp0688365` and `Gp0699240`; no native analysis rows linked to those projects.

## Completeness

- `data/raw/ncbi_type_material.tsv:57918-57921` has `type material` rows for `CBS 571.72`, `CBS:571.72`, `LCP 44a`, and `LCP:44a` under `Neurospora santi-florii`.
- Exact StrainInfo side inventory found 11 direct records and 18 deposit entries, including sampled designations `IFO 30236`, `NBRC 30236`, `IFO 32841`, `NBRC 32841`, `IFO 32890`, `NBRC 32890`, `CBS 101516`, `ATCC 204308`, `FGSC 8330`, `CBS 101517`, `ATCC 204310`, and `FGSC 8331`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:176682`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact NCBI type-material, StrainInfo side-inventory, and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, StrainInfo, or native GOLD side inventories.

## Additional Notes

- None.
