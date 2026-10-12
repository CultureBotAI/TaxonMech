# YAML Record Review

- Target: `data/taxa/eukaryota/nakaseomyces_uthaithaninus.yaml`
- Taxon: `NCBITaxon:1040648` (`Nakaseomyces uthaithaninus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1040648`, label `Nakaseomyces uthaithaninus`.
- It is grounded exactly under `NCBITaxon:374468` (`Nakaseomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Nakaseomyces`.

## Validation

- `just validate data/taxa/eukaryota/nakaseomyces_uthaithaninus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nakaseomyces_nivariensis_cbs_9983.yaml data/taxa/eukaryota/nakaseomyces_uthaithaninus.yaml data/taxa/eukaryota/nakataea_oryzae.yaml data/taxa/eukaryota/nakazawaea_anatomiae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57266` contains the seeded identifier with reason `attested rule: Nakaseomyces uthaithaninus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:223390` matches the YAML identity: parent `NCBITaxon:374468`, rank `SPECIES`, exact synonym `Candida uthaithanina`, and five related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:223390` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:566`, where `NCBITaxon:1040648` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0704982` / `Nakaseomyces uthaithaninus CBS 10932`, linked to project `Gp0830999` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 4 type-material rows for `NCBITaxon:1040648`, under synonym name `Candida uthaithanina`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1040648`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found 3 side-inventory old IDs now merged into `NCBITaxon:1040648`; none were retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact type-material side inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories, or if any side-inventory merged IDs become retained retired rows.

## Additional Notes

- None.
