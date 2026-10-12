# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_heterospora.yaml`
- Taxon: `NCBITaxon:2075006` (`Neurospora heterospora`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2075006`, label `Neurospora heterospora`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_heterospora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_heterospora.yaml data/taxa/eukaryota/neurospora_hispaniola.yaml data/taxa/eukaryota/neurospora_indica.yaml data/taxa/eukaryota/neurospora_intermedia.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62260` contains the seeded identifier with reason `attested rule: Neurospora heterospora, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:515745` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, three synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:515745` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:19815`, where `NCBITaxon:2075006` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0651474` / `Neurospora heterospora MNHN RF-02378`, linked to two native projects and no native analyses.

## Completeness

- A structured exact scan found no rows for `NCBITaxon:2075006` in `data/raw/ncbi_type_material.tsv`.
- Exact StrainInfo side inventory found 6 direct records and 7 exact deposit assertions, including sampled designations `MUCL 18446`, `IFO 30233`, `NBRC 30233`, `MUCL 18445`, `CBS 559.72`, and `CBS 407.82`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:2075006`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact StrainInfo side inventory did not materialize local strain rows; StrainInfo only joins through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
