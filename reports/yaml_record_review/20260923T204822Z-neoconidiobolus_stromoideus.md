# YAML Record Review

- Target: `data/taxa/eukaryota/neoconidiobolus_stromoideus.yaml`
- Taxon: `NCBITaxon:1167819` (`Neoconidiobolus stromoideus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1167819`, label `Neoconidiobolus stromoideus`.
- It is grounded exactly under `NCBITaxon:2878373` (`Neoconidiobolus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Neoconidiobolus`.

## Validation

- `just validate data/taxa/eukaryota/neoconidiobolus_stromoideus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neocatenulostroma_sp.yaml data/taxa/eukaryota/neoconidiobolus_osmodes.yaml data/taxa/eukaryota/neoconidiobolus_stromoideus.yaml data/taxa/eukaryota/neoconidiobolus_thromboides.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58117` contains the seeded identifier with reason `attested rule: Neoconidiobolus stromoideus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:257998` matches the YAML identity: parent `NCBITaxon:2878373`, rank `SPECIES`, three synonyms, and genetic code `1`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:257998` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3584`, where `NCBITaxon:1167819` has `organism_count` 1.
- A complete scan of the local native GOLD `organisms`, `projects`, and `analyses` snapshots found no exact current-taxid organism rows for `NCBITaxon:1167819`.

## Completeness

- An exact field scan of `data/raw/ncbi_type_material.tsv` found 12 type-material rows for `NCBITaxon:1167819`, covering variants of `ATCC 15430`, `CBS 220.64`, `HACC 126`, `IMI 092298`, and `NRRL 3071`.
- Exact StrainInfo side inventory found 3 direct records and 8 exact deposit assertions, including `CBS 220.64`, `ATCC 15430`, `IMI 092298`, and `NRRL 3071`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:1167819`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:1167819`; the exact StrainInfo and type-material side inventories did not materialize local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if native GOLD rows for this exact current Taxon ID are restored locally.

## Additional Notes

- None.
