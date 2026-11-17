# YAML Record Review

- Target: `data/taxa/eukaryota/opeltia_flavorubescens.yaml`
- Taxon: `NCBITaxon:1301419` (`Opeltia flavorubescens`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1301419`, label `Opeltia flavorubescens`.
- It is grounded exactly under `NCBITaxon:2005610` (`Opeltia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 18 lineage entries from `root` through `Opeltia`.

## Validation

- `just validate data/taxa/eukaryota/opeltia_flavorubescens.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/opeltia_flavorubescens.yaml data/taxa/eukaryota/operculomyces_laminatus.yaml data/taxa/eukaryota/ophidiomyces_ophidiicola.yaml data/taxa/eukaryota/ophiobolus_disseminans.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59290` contains the seeded identifier with reason `attested rule: Opeltia flavorubescens, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:307329` matches the YAML identity: parent `NCBITaxon:2005610`, rank `SPECIES`, three exact synonyms, four related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 18 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:307329` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:7389`, where `NCBITaxon:1301419` has `organism_count` 1.
- The local exact native-GOLD scan found no current-taxid organism, project, or analysis rows for `NCBITaxon:1301419`, so the GOLD attestation rests on the transformed GOLD aggregate rather than matching rows in the local native JSONL snapshot.

## Completeness

- Exact StrainInfo, NCBI type-material, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1301419`; no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.
- Exact NCBI merged-ID side inventory maps old `NCBITaxon:1353255` and `NCBITaxon:140092` to `NCBITaxon:1301419`, but the retained retired old-ID source is empty; the record correctly has no `replaces` entry and `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if a refreshed local native GOLD snapshot materializes exact current-taxid rows for `NCBITaxon:1301419`, or if future curation materializes NCBI merged-ID side inventory.

## Additional Notes

- None.
