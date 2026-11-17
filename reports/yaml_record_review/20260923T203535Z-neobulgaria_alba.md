# YAML Record Review

- Target: `data/taxa/eukaryota/neobulgaria_alba.yaml`
- Taxon: `NCBITaxon:1461596` (`Neobulgaria alba`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1461596`, label `Neobulgaria alba`.
- It is grounded exactly under `NCBITaxon:45424` (`Neobulgaria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Neobulgaria`.

## Validation

- `just validate data/taxa/eukaryota/neobulgaria_alba.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neoboletus_erythropus.yaml data/taxa/eukaryota/neoboletus_magnificus.yaml data/taxa/eukaryota/neoboletus_subvelutipes.yaml data/taxa/eukaryota/neobulgaria_alba.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60227` contains the seeded identifier with reason `attested rule: Neobulgaria alba, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:371697` matches the YAML identity: parent `NCBITaxon:45424`, rank `SPECIES`, four related synonyms, and genetic code `1`.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:371697` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:11195`, where `NCBITaxon:1461596` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0517610` / `Neobulgaria alba D2031`.
- That native organism ID links to project `Gp0441663`, which has one native analysis row linked by `AP PROJECT GOLD IDS`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 4 type-material rows for `NCBITaxon:1461596`, covering variants of `ICMP 18394` and `PDD 91753`.
- Exact StrainInfo side inventory found 14 direct records with 14 exact `ICMP` deposits, including `ICMP 18394` and `ICMP 18395`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:795929`, `NCBITaxon:795930`, and `NCBITaxon:795931`; they were not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:1461596`; the exact StrainInfo and type-material side inventories did not materialize local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if the side-inventory merged IDs become retained retired rows.

## Additional Notes

- None.
