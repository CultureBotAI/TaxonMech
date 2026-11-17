# YAML Record Review

- Target: `data/taxa/eukaryota/neoboletus_magnificus.yaml`
- Taxon: `NCBITaxon:374759` (`Neoboletus magnificus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:374759`, label `Neoboletus magnificus`.
- It is grounded exactly under `NCBITaxon:1629869` (`Neoboletus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Neoboletus`.

## Validation

- `just validate data/taxa/eukaryota/neoboletus_magnificus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neoboletus_erythropus.yaml data/taxa/eukaryota/neoboletus_magnificus.yaml data/taxa/eukaryota/neoboletus_subvelutipes.yaml data/taxa/eukaryota/neobulgaria_alba.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55403` contains the seeded identifier with reason `attested rule: Neoboletus magnificus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:78565` matches the YAML identity: parent `NCBITaxon:1629869`, rank `SPECIES`, three synonyms, and genetic code `1`.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:78565` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33690`, where `NCBITaxon:374759` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0518044` / `Neoboletus magnificus MG22`.
- That native organism ID links to project `Gp0442113`, which has one native analysis row linked by `AP PROJECT GOLD IDS`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:374759`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:374759`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:374759`.
- The record has no generated local strain rows, and the checked side inventories do not contradict `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains for this taxon.

## Additional Notes

- None.
