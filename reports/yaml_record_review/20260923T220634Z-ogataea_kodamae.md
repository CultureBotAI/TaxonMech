# YAML Record Review

- Target: `data/taxa/eukaryota/ogataea_kodamae.yaml`
- Taxon: `NCBITaxon:50263` (`Ogataea kodamae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:50263`, label `Ogataea kodamae`.
- It is grounded exactly under `NCBITaxon:461281` (`Ogataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Ogataea`.

## Validation

- `just validate data/taxa/eukaryota/ogataea_kodamae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_haglerorum.yaml data/taxa/eukaryota/ogataea_henricii.yaml data/taxa/eukaryota/ogataea_kodamae.yaml data/taxa/eukaryota/ogataea_krabiensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52815` contains the seeded identifier with reason `attested rule: Ogataea kodamae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6323` matches the YAML identity: parent `NCBITaxon:461281`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6323` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37354`, where `NCBITaxon:50263` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0517122` / `Ogataea kodamae NRRL Y-17234`, linked to project `Gp0441160`; one native analysis row links through `Gp0441160`.

## Completeness

- Exact NCBI type material is limited to 12 `Pichia kodamae` designations for `ATCC 56666`, `BCRC 22451` / `CCRC 22451`, `CBS 7081`, `IFO 10090`, and `NRRL Y-17234`.
- Exact StrainInfo side inventory found one direct record and 9 deposit groups, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:50263`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:50263`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
