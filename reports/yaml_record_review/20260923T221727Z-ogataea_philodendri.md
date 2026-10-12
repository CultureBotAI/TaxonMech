# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_philodendri.yaml`
- Taxon: `NCBITaxon:1378263` (`Ogataea philodendri`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1378263`, label `Ogataea philodendri`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_philodendri.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_paraovalis.yaml data/taxa/eukaryota/ogataea_parapolymorpha_dl_1.yaml data/taxa/eukaryota/ogataea_philodendri.yaml data/taxa/eukaryota/ogataea_piceae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59702` contains the seeded identifier with reason `attested rule: Ogataea philodendri, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:336115` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, three exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:336115` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:8896`, where `NCBITaxon:1378263` has `organism_count` 7.
- Native GOLD has 7 exact current-taxid organism rows for `NCBITaxon:1378263`; the exact native-GOLD scan found one project and one linked analysis row.

## Completeness

- Exact NCBI type material is limited to eight `Hansenula philodendri` culture-from-type-material rows for `ATCC 58368`, `CBS 6075`, `IFO 1821`, and `NRRL Y-7210`.
- Exact StrainInfo side inventory found one direct record and 6 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:1378263`.
- `data/raw/ncbi_merged_ids.tsv:70550` maps side-inventory old ID `NCBITaxon:34355` into `NCBITaxon:1378263`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact BacDive and checked auxiliary source rows were empty for `NCBITaxon:1378263`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
