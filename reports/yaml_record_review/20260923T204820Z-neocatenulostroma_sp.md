# YAML Record Review

- Target: `data/taxa/eukaryota/neocatenulostroma_sp.yaml`
- Taxon: `NCBITaxon:1917221` (`Neocatenulostroma sp.`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1917221`, label `Neocatenulostroma sp.`.
- It is grounded exactly under `NCBITaxon:2642522` (`unclassified Neocatenulostroma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `unclassified Neocatenulostroma`.

## Validation

- `just validate data/taxa/eukaryota/neocatenulostroma_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neocatenulostroma_sp.yaml data/taxa/eukaryota/neoconidiobolus_osmodes.yaml data/taxa/eukaryota/neoconidiobolus_stromoideus.yaml data/taxa/eukaryota/neoconidiobolus_thromboides.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61608` contains the seeded identifier with reason `attested rule: Neocatenulostroma sp., 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:494837` matches the YAML identity: parent `NCBITaxon:2642522`, rank `SPECIES`, no NCBI synonyms, and genetic code `1`.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:494837` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:17490`, where `NCBITaxon:1917221` has `organism_count` 1.
- A complete scan of the local native GOLD `organisms`, `projects`, and `analyses` snapshots found no exact current-taxid organism rows for `NCBITaxon:1917221`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:1917221`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:1917221`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:1917221`.
- The record has no generated local strain rows, and the checked side inventories do not contradict `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains for this taxon, or if native GOLD rows for this exact current Taxon ID are restored locally.

## Additional Notes

- None.
