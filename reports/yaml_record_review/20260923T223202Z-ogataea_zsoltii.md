# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_zsoltii.yaml`
- Taxon: `NCBITaxon:169510` (`Ogataea zsoltii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:169510`, label `Ogataea zsoltii`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_zsoltii.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/ogataea_xyloterini.yaml data/taxa/eukaryota/ogataea_zsoltii.yaml data/taxa/eukaryota/oidium_heveae.yaml data/taxa/eukaryota/oleoguttula_mirabilis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54255` contains the seeded identifier with reason `attested rule: Ogataea zsoltii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:34592` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:34592` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:14629`, where `NCBITaxon:169510` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0517130` / `Ogataea zsoltii NRRL Y-27601`, linked to project `Gp0441168` and one analysis row via that project.

## Completeness

- Exact NCBI type material has 12 duplicated spelling rows for `Ogataea zsoltii`, covering `CBS 9262`, `NBRC 101079`, `NCAIM Y.01540` / `NCAIM Y-1540`, and `NRRL Y-27601`.
- Exact StrainInfo side inventory found 1 direct record and 4 deposits, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:169510`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:169510`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
