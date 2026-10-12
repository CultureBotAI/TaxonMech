# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_salicorniae.yaml`
- Taxon: `NCBITaxon:1337055` (`Ogataea salicorniae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1337055`, label `Ogataea salicorniae`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_salicorniae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_polymorpha.yaml data/taxa/eukaryota/ogataea_populi_albae.yaml data/taxa/eukaryota/ogataea_rishiriensis.yaml data/taxa/eukaryota/ogataea_salicorniae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59530` contains the seeded identifier with reason `attested rule: Ogataea salicorniae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:320400` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:320400` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:8170`, where `NCBITaxon:1337055` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705229` / `Ogataea salicorniae NRRL Y-12834`, linked to project `Gp0831256`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material has 5 culture-from-holotype rows for `NRRL Y-12834` spellings plus 2 `CBS 8071` type-material rows for `Williopsis salicorniae`.
- Exact StrainInfo side inventory found 1 direct record and 9 deposits, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:1337055`.
- Exact NCBI merged-ID side inventory maps old `NCBITaxon:50269` to `NCBITaxon:1337055`, while retained retired old-ID, BacDive, and checked auxiliary source rows were empty; the record correctly has no `replaces` entry and `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, native GOLD, or NCBI merged-ID side inventories.

## Additional Notes

- None.
