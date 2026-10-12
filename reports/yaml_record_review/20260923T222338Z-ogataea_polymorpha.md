# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_polymorpha.yaml`
- Taxon: `NCBITaxon:460523` (`Ogataea polymorpha`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:460523`, label `Ogataea polymorpha`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_polymorpha.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_polymorpha.yaml data/taxa/eukaryota/ogataea_populi_albae.yaml data/taxa/eukaryota/ogataea_rishiriensis.yaml data/taxa/eukaryota/ogataea_salicorniae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55737` contains the seeded identifier with reason `attested rule: Ogataea polymorpha, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:103341` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, seven exact synonyms, seven related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:103341` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36212`, where `NCBITaxon:460523` has `organism_count` 14.
- Native GOLD exact current-taxid rows covered 13 organism rows, 13 linked project rows, and 12 linked analysis rows for local `Ogataea polymorpha` projects.

## Completeness

- Exact NCBI type material has 28 rows across `Hansenula polymorpha` culture-from-type-material rows and `Ogataea thermophila` culture-from-holotype or holotype rows, covering `ATCC 34438`, `CBS 4732`, `JCM 3621`, `NCYC 1457`, `NRRL Y-5445`, `CBS 11284`, `KCCM 50661`, `NCAIM Y.01608`, `JCM 10994`, and `Y94`.
- Exact StrainInfo side inventory found 7 direct records and 15 deposits, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:460523`.
- Exact NCBI merged-ID side inventory maps old `NCBITaxon:369265`, `NCBITaxon:416522`, and `NCBITaxon:559302` to `NCBITaxon:460523`, while retained retired old-ID, BacDive, and checked auxiliary source rows were empty; the record correctly has no `replaces` entry and `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, native GOLD, or NCBI merged-ID side inventories.

## Additional Notes

- None.
