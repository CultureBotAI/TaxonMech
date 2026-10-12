# YAML Record Review

- Target: `data/taxa/eukaryota/neoboletus_erythropus.yaml`
- Taxon: `NCBITaxon:2268947` (`Neoboletus erythropus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2268947`, label `Neoboletus erythropus`.
- It is grounded exactly under `NCBITaxon:1629869` (`Neoboletus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Neoboletus`.

## Validation

- `just validate data/taxa/eukaryota/neoboletus_erythropus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neoboletus_erythropus.yaml data/taxa/eukaryota/neoboletus_magnificus.yaml data/taxa/eukaryota/neoboletus_subvelutipes.yaml data/taxa/eukaryota/neobulgaria_alba.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62523` contains the seeded identifier with reason `attested rule: Neoboletus erythropus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:522505` matches the YAML identity: parent `NCBITaxon:1629869`, rank `SPECIES`, three synonyms, and genetic code `1`.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:522505` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:21344`, where `NCBITaxon:2268947` has `organism_count` 1.
- A complete scan of the local native GOLD `organisms`, `projects`, and `analyses` snapshots found no exact current-taxid organism rows for `NCBITaxon:2268947`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:2268947`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:2268947`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:121023`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows, and the checked side inventories do not contradict `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if the side-inventory merged ID becomes a retained retired row or if native GOLD rows for this exact current Taxon ID are restored locally.

## Additional Notes

- None.
