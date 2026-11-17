# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_dictyophora.yaml`
- Taxon: `NCBITaxon:241079` (`Neurospora dictyophora`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:241079`, label `Neurospora dictyophora`.
- It is grounded exactly under `NCBITaxon:5140` (`Neurospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neurospora`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_dictyophora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_cratophora.yaml data/taxa/eukaryota/neurospora_dictyophora.yaml data/taxa/eukaryota/neurospora_discreta.yaml data/taxa/eukaryota/neurospora_discreta_fgsc_8579.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54707` contains the seeded identifier with reason `attested rule: Neurospora dictyophora, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:47347` matches the YAML identity: parent `NCBITaxon:5140`, rank `SPECIES`, three synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:47347` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:22001`, where `NCBITaxon:241079` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0651477` / `Neurospora dictyophora FGSC 7798`, linked to two native projects and no native analyses.

## Completeness

- A complete exact scan of `data/raw/ncbi_type_material.tsv` found twelve `type material` rows for `NCBITaxon:241079`: `ATCC 96226`, `ATCC:96226`, `CBS 529.95`, `CBS:529.95`, `FGSC 7798`, `FGSC:7798`, `IMI 364330`, `IMI:364330`, `TRTC 51746`, `TRTC:51746`, `UAMH 7735`, and `UAMH:7735`.
- Exact StrainInfo side inventory found 1 direct record and 5 exact deposit assertions, including `ATCC 96226`, `CBS 529.95`, `FGSC 7798`, `IMI 364330`, and `UAMH 7735`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:241079`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The exact StrainInfo side inventory did not materialize local strain rows; StrainInfo only joins through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
