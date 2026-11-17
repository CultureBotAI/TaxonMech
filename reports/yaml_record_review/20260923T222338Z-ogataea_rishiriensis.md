# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_rishiriensis.yaml`
- Taxon: `NCBITaxon:664898` (`Ogataea rishiriensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:664898`, label `Ogataea rishiriensis`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_rishiriensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_polymorpha.yaml data/taxa/eukaryota/ogataea_populi_albae.yaml data/taxa/eukaryota/ogataea_rishiriensis.yaml data/taxa/eukaryota/ogataea_salicorniae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56311` contains the seeded identifier with reason `attested rule: Ogataea rishiriensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:154135` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:154135` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40767`, where `NCBITaxon:664898` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705188` / `Candida rishiriensis NBRC 105027`, linked to project `Gp0831211`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material has 2 `CBS 11662` culture-from-holotype rows and 4 `NBRC 105027` / `Y07-901-4` holotype rows for `Candida rishiriensis`.
- Exact StrainInfo, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:664898`; no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.
- Exact NCBI merged-ID side inventory maps old `NCBITaxon:564623` to `NCBITaxon:664898`, but the retained retired old-ID source is empty; the record correctly has no `replaces` entry and `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, native GOLD, or NCBI merged-ID side inventories.

## Additional Notes

- None.
