# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_hispaniola.yaml`
- Taxon: `NCBITaxon:588809` (`Neurospora hispaniola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:588809`, label `Neurospora hispaniola`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_hispaniola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_heterospora.yaml data/taxa/eukaryota/neurospora_hispaniola.yaml data/taxa/eukaryota/neurospora_indica.yaml data/taxa/eukaryota/neurospora_intermedia.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56116` contains the seeded identifier with reason `attested rule: Neurospora hispaniola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:139299` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:139299` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:39561`, where `NCBITaxon:588809` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0358432` / `Neurospora hispaniola FGSC 10403`, linked to two native projects and one native analysis.

## Completeness

- The NCBI type-material inventory contains five exact holotype rows for `NCBITaxon:588809`: `CV55 `, `FGSC 104032`, `FGSC-104032`, `FGSC104032`, and `FGSC:104032`.
- Exact structured scans found no rows for `NCBITaxon:588809` in `data/raw/ncbi_merged_ids.tsv`, retained retired NCBI old IDs, exact BacDive, generated raw strain rows, generated StrainInfo target rows, exact StrainInfo side inventory, or checked auxiliary source rows.
- The record correctly has `strain_count: 0` and no generated `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation materializes local strains from NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
