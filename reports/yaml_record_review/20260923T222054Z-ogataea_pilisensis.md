# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_pilisensis.yaml`
- Taxon: `NCBITaxon:157292` (`Ogataea pilisensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:157292`, label `Ogataea pilisensis`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_pilisensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_pignaliae.yaml data/taxa/eukaryota/ogataea_pilisensis.yaml data/taxa/eukaryota/ogataea_pini.yaml data/taxa/eukaryota/ogataea_pinus.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54139` contains the seeded identifier with reason `attested rule: Ogataea pilisensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:32622` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:32622` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:12670`, where `NCBITaxon:157292` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0517125` / `Ogataea pilisensis NRRL Y-27598`, linked to project `Gp0441163` and one analysis row via that project.

## Completeness

- Exact NCBI type material has 8 duplicated spelling rows for `Ogataea pilisensis`, covering `CBS 9259`, `NCAIM Y-1509` / `NCAIM Y.01509`, and `NRRL Y-27598`.
- Exact StrainInfo side inventory found 1 direct record and 4 deposits, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:157292`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:157292`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
