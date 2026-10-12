# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_discreta.yaml`
- Taxon: `NCBITaxon:29879` (`Neurospora discreta`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:29879`, label `Neurospora discreta`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_discreta.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_cratophora.yaml data/taxa/eukaryota/neurospora_dictyophora.yaml data/taxa/eukaryota/neurospora_discreta.yaml data/taxa/eukaryota/neurospora_discreta_fgsc_8579.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52219` contains the seeded identifier with reason `attested rule: Neurospora discreta, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:3289` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:3289` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:29918`, where `NCBITaxon:29879` has `organism_count` 88.
- Native GOLD has 88 exact current-taxid organism rows and 90 linked native project rows; no native analyses are linked to those projects in this snapshot.

## Completeness

- A structured exact scan found no rows for `NCBITaxon:29879` in `data/raw/ncbi_type_material.tsv`.
- Exact StrainInfo side inventory found 155 direct records and 159 exact deposit assertions, including sampled designations `ICMP 14007`, `ICMP 14019`, `ICMP 14020`, `ATCC 62167`, `FGSC 3229`, `IMI 305730`, `ATCC 62168`, `FGSC 3228`, and `IMI 305731`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:29879`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact StrainInfo side inventory and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
