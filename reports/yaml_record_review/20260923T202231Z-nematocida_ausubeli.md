# YAML Record Review

- Target: `data/taxa/eukaryota/nematocida_ausubeli.yaml`
- Taxon: `NCBITaxon:1913371` (`Nematocida ausubeli`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1913371`, label `Nematocida ausubeli`.
- It is grounded exactly under `NCBITaxon:586132` (`Nematocida`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 9 lineage entries from `root` through `Nematocida`.

## Validation

- `just validate data/taxa/eukaryota/nematocida_ausubeli.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nemania_diffusa.yaml data/taxa/eukaryota/nemania_maritima.yaml data/taxa/eukaryota/nemania_serpens.yaml data/taxa/eukaryota/nematocida_ausubeli.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61588` contains the seeded identifier with reason `attested rule: Nematocida ausubeli, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:493780` matches the YAML identity: parent `NCBITaxon:586132`, rank `SPECIES`, four related synonyms, and genetic code `1`.
- All 9 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:493780` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:17417`, where `NCBITaxon:1913371` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0038029` / `Nematocida ausubeli ERTm2` and `Go0038030` / `Nematocida ausubeli ERTm6`.
- Those two native organism IDs link to projects `Gp0038029` and `Gp0038030`, each with one native analysis row linked by `AP PROJECT GOLD IDS`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 5 type-material rows for `NCBITaxon:1913371`, covering variants of `ATCC PRA-371` and `ERTm2`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1913371`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:1075770`, `NCBITaxon:1138374`, `NCBITaxon:586134`, and `NCBITaxon:944018`; they were not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact type-material side inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories, or if the side-inventory merged IDs become retained retired rows.

## Additional Notes

- None.
