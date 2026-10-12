# YAML Record Review

- Target: `data/taxa/eukaryota/nigrospora_sphaerica.yaml`
- Taxon: `NCBITaxon:114231` (`Nigrospora sphaerica`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:114231`, label `Nigrospora sphaerica`.
- It is grounded exactly under `NCBITaxon:114230` (`Nigrospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Nigrospora`.

## Validation

- `just validate data/taxa/eukaryota/nigrospora_sphaerica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nigrospora_oryzae.yaml data/taxa/eukaryota/nigrospora_sphaerica.yaml data/taxa/eukaryota/nilaparvata_lugens_yeast_like_symbiont.yaml data/taxa/eukaryota/nitzschia_captiva.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53800` contains the seeded identifier with reason `attested rule: Nigrospora sphaerica, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:20732` matches the YAML identity: parent `NCBITaxon:114230`, rank `SPECIES`, two exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:20732` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:2949`, where `NCBITaxon:114231` has `organism_count` 1.
- Exact scans of the current native GOLD JSONL catalogs found no current exact organism, project, or analysis rows for `NCBITaxon:114231`.

## Completeness

- `data/raw/ncbi_type_material.tsv:9403-9404` has holotype aliases `IMI 103253` and `IMI:103253` under `Trichosporum sphaericum`.
- Exact StrainInfo side inventory found 32 direct records and 40 deposit entries, including sampled designations `IHEM 26038`, `MUCL 2592`, `MUCL 7000`, `MUCL 8367`, `CBS 166.26`, and `MUCL 31966`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1460876` and `NCBITaxon:2047961` into `NCBITaxon:114231`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` generated `replaces` entries.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:114231`; the record correctly has `strain_count: 0`.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or StrainInfo side inventories.

## Additional Notes

- None.
