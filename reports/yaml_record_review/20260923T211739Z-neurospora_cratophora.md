# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_cratophora.yaml`
- Taxon: `NCBITaxon:303343` (`Neurospora cratophora`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:303343`, label `Neurospora cratophora`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_cratophora.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/neurospora_cratophora.yaml data/taxa/eukaryota/neurospora_dictyophora.yaml data/taxa/eukaryota/neurospora_discreta.yaml data/taxa/eukaryota/neurospora_discreta_fgsc_8579.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55085` contains the seeded identifier with reason `attested rule: Neurospora cratophora, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:62090` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, three synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:62090` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:30362`, where `NCBITaxon:303343` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0651446` / `Neurospora cratophora FGSC 7796`, linked to two native projects and no native analyses.

## Completeness

- A complete exact scan of `data/raw/ncbi_type_material.tsv` found eight `type material` rows for `NCBITaxon:303343`: `CBS 558.94`, `CBS:558.94`, `FGSC 7796`, `FGSC:7796`, `IMI 364328`, `IMI:364328`, `TRTC 51744`, and `TRTC:51744`.
- Exact StrainInfo side inventory found 2 direct records and 9 exact deposit assertions, including `CBS 245.89`, `UAMH 6428`, `ATCC 66227`, `CBS 558.94`, `FGSC 7796`, `IMI 364328`, and `UAMH 7734`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:303343`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact StrainInfo side inventory did not materialize local strain rows; StrainInfo only joins through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
