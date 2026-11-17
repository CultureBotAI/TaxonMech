# YAML Record Review

- Target: `data/taxa/eukaryota/nematodospora_valgi.yaml`
- Taxon: `NCBITaxon:864349` (`Nematodospora valgi`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:864349`, label `Nematodospora valgi`.
- It is grounded exactly under `NCBITaxon:1670620` (`Nematodospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `12`.
- The YAML carries 13 lineage entries from `root` through `Nematodospora`.

## Validation

- `just validate data/taxa/eukaryota/nematodospora_valgi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nematocida_displodere.yaml data/taxa/eukaryota/nematocida_ironsii.yaml data/taxa/eukaryota/nematodospora_anomalae.yaml data/taxa/eukaryota/nematodospora_valgi.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56794` contains the seeded identifier with reason `attested rule: Nematodospora valgi, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:181872` matches the YAML identity: parent `NCBITaxon:1670620`, rank `SPECIES`, nine related synonyms, and genetic code `12`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:181872` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:43463`, where `NCBITaxon:864349` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705046` / `Nematodospora valgi CBS 12562`.
- That native organism ID links to project `Gp0831066`; no native GOLD analysis rows were found for the linked project.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 6 type-material rows for `NCBITaxon:864349`, covering variants of `CBS 12562`, `NBIMCC 8868`, and `D37S`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:864349`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:1286699`, `NCBITaxon:1331965`, `NCBITaxon:1659640`, `NCBITaxon:1659641`, `NCBITaxon:1659642`, `NCBITaxon:864348`, and `NCBITaxon:864350`; they were not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact type-material side inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories, or if the side-inventory merged IDs become retained retired rows.

## Additional Notes

- None.
