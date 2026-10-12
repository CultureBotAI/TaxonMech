# YAML Record Review

- Target: `data/taxa/eukaryota/nannochloropsis_oculata.yaml`
- Taxon: `NCBITaxon:43925` (`Nannochloropsis oculata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:43925`, label `Nannochloropsis oculata`.
- It is grounded exactly under `NCBITaxon:5748` (`Nannochloropsis`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Nannochloropsis`.

## Validation

- `just validate data/taxa/eukaryota/nannochloropsis_oculata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nannochloropsis_gaditana_ccmp526.yaml data/taxa/eukaryota/nannochloropsis_oceanica.yaml data/taxa/eukaryota/nannochloropsis_oceanica_strain_imet1.yaml data/taxa/eukaryota/nannochloropsis_oculata.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52545` contains the seeded identifier with reason `attested rule: Nannochloropsis oculata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:5271` matches the YAML identity: parent `NCBITaxon:5748`, rank `SPECIES`, three exact synonyms, three related synonyms, and genetic code `1`.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:5271` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:35498`, where `NCBITaxon:43925` has `organism_count` 1.
- The current native GOLD catalogs have two exact organism rows, `Go0008149` / `Nannochloropsis oculata CCMP 525` and `Go0038536` / `Nannochloropsis oculata`, linked to projects `Gp0008149` and `Gp0038536`.
- No native GOLD analyses are linked to those exact current projects.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for `NCBITaxon:43925`.
- Exact StrainInfo side inventory has 4 direct rows and 12 deposit entries for `NCBITaxon:43925`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:249346`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact StrainInfo side inventory, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventory, or if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv` and differs from the current native GOLD exact-organism count; the native JSONL rows are side evidence only.
