# YAML Record Review

- Target: `data/taxa/eukaryota/nadsonia_fulvescens.yaml`
- Taxon: `NCBITaxon:45786` (`Nadsonia fulvescens`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:45786`, label `Nadsonia fulvescens`.
- It is grounded exactly under `NCBITaxon:45785` (`Nadsonia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Nadsonia`.

## Validation

- `just validate data/taxa/eukaryota/nadsonia_fulvescens.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myxozyma_udenii.yaml data/taxa/eukaryota/myxozyma_vanderwaltii.yaml data/taxa/eukaryota/nadsonia_commutata.yaml data/taxa/eukaryota/nadsonia_fulvescens.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52688` contains the seeded identifier with reason `attested rule: Nadsonia fulvescens, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:5701` matches the YAML identity: parent `NCBITaxon:45785`, rank `SPECIES`, exact synonym `Guilliermondia fulvescens`, and two related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:5701` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36147`, where `NCBITaxon:45786` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0009966` / `Nadsonia fulvescens elongata DSM 6958`, linked to projects `Gp0009714` and `Gp0009966`; native analysis `Nadsonia fulvescens elongata DSM 6958` links through `AP PROJECT GOLD IDS` `Gp0009966`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 14 type-material rows for `NCBITaxon:45786`, under synonym name `Guilliermondia fulvescens` and covering variants of `ATCC 24236`, `BCRC 21342`, `CBS 2596`, `CCRC 21342`, `DBVPG 6775`, `NRRL Y-12810`, and `UCD 61-44`.
- Exact StrainInfo side inventory has 5 direct rows and 26 deposit entries for `NCBITaxon:45786`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:45786`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- The YAML correctly files only records directly under `NCBITaxon:45786`; descendant taxa are not gathered into this species record.
