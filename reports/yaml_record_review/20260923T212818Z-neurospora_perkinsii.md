# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_perkinsii.yaml`
- Taxon: `NCBITaxon:588810` (`Neurospora perkinsii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:588810`, label `Neurospora perkinsii`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_perkinsii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_kobi.yaml data/taxa/eukaryota/neurospora_lineolata.yaml data/taxa/eukaryota/neurospora_macrospora.yaml data/taxa/eukaryota/neurospora_perkinsii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56117` contains the seeded identifier with reason `attested rule: Neurospora perkinsii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:139300` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:139300` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:39562`, where `NCBITaxon:588810` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0516850` / `Neurospora perkinsii FGSC 10406`, linked to projects `Gp0440452` and `Gp0534297`; no native analysis rows linked to those projects.

## Completeness

- The bounded exact scan found no NCBI type-material rows, no exact StrainInfo rows, and no NCBI merged-ID side rows for `NCBITaxon:588810`; no retained retired old-ID rows were present either.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and checked auxiliary source rows were empty for `NCBITaxon:588810`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact native GOLD organism and project rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD side inventories.

## Additional Notes

- None.
