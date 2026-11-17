# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_siamensis.yaml`
- Taxon: `NCBITaxon:246385` (`Ogataea siamensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:246385`, label `Ogataea siamensis`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_siamensis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/ogataea_saltuana.yaml data/taxa/eukaryota/ogataea_siamensis.yaml data/taxa/eukaryota/ogataea_sithepensis.yaml data/taxa/eukaryota/ogataea_sonorensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54742` contains the seeded identifier with reason `attested rule: Ogataea siamensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:48336` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:48336` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:22159`, where `NCBITaxon:246385` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705513` / `Ogataea siamensis NRRL Y-27963`, linked to project `Gp0831556`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material has 16 culture-from-holotype rows covering `ATCC MYA-4464`, `CBS 10095`, `NRRL Y-27963`, and `TISTR 5818`, plus 4 `JCM 12264` holotype spellings.
- Exact StrainInfo side inventory found 1 direct record and 4 deposits, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:246385`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:246385`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
