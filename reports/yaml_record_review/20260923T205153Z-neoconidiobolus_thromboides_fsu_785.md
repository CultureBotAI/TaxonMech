# YAML Record Review

- Target: `data/taxa/eukaryota/neoconidiobolus_thromboides_fsu_785.yaml`
- Taxon: `NCBITaxon:1314799` (`Neoconidiobolus thromboides FSU 785`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:1314799`, label `Neoconidiobolus thromboides FSU 785`.
- It is grounded exactly under species `NCBITaxon:76012` (`Neoconidiobolus thromboides`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Neoconidiobolus thromboides`.

## Validation

- `just validate data/taxa/eukaryota/neoconidiobolus_thromboides_fsu_785.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neoconidiobolus_thromboides_fsu_785.yaml data/taxa/eukaryota/neocucurbitaria_cava.yaml data/taxa/eukaryota/neodevriesia_sardiniae.yaml data/taxa/eukaryota/neofusicoccum_brasiliense.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59388` contains the seeded identifier with reason `attested rule: Neoconidiobolus thromboides FSU 785, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:312648` matches the YAML identity: parent `NCBITaxon:76012`, rank `STRAIN`, no NCBI synonyms, and genetic code `1`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:312648` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:7699`, where `NCBITaxon:1314799` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0032991` / `Neoconidiobolus thromboides FSU 785`.
- That native organism ID links to projects `Gp0032991` and `Gp0032992`; `Gp0032992` has one native analysis row linked by `AP PROJECT GOLD IDS`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:1314799`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:1314799`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:1314799`.
- The record has no generated local strain rows, and the checked side inventories do not contradict `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains for this taxon.

## Additional Notes

- None.
