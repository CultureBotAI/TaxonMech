# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_xyloterini.yaml`
- Taxon: `NCBITaxon:641392` (`Ogataea xyloterini`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:641392`, label `Ogataea xyloterini`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_xyloterini.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_xyloterini.yaml data/taxa/eukaryota/ogataea_zsoltii.yaml data/taxa/eukaryota/oidium_heveae.yaml data/taxa/eukaryota/oleoguttula_mirabilis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56205` contains the seeded identifier with reason `attested rule: Ogataea xyloterini, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:147963` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:147963` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40212`, where `NCBITaxon:641392` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705004` / `Candida xyloterini CBS 11547`, linked to project `Gp0831021`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material has 2 `CBS 11547` culture-from-holotype rows and 4 `ATCC 62898` holotype spellings for `Candida xyloterini`.
- Exact StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:641392`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
