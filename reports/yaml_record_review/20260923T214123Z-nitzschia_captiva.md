# YAML Record Review

- Target: `data/taxa/eukaryota/nitzschia_captiva.yaml`
- Taxon: `NCBITaxon:2583373` (`Nitzschia captiva`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2583373`, label `Nitzschia captiva`.
- It is grounded exactly under `NCBITaxon:2857` (`Nitzschia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Nitzschia`.

## Validation

- `just validate data/taxa/eukaryota/nitzschia_captiva.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nigrospora_oryzae.yaml data/taxa/eukaryota/nigrospora_sphaerica.yaml data/taxa/eukaryota/nilaparvata_lugens_yeast_like_symbiont.yaml data/taxa/eukaryota/nitzschia_captiva.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62857` contains the seeded identifier with reason `attested rule: Nitzschia captiva, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:533768` matches the YAML identity: parent `NCBITaxon:2857`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:533768` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:23609`, where `NCBITaxon:2583373` has `organism_count` 1.
- Exact scans of the current native GOLD JSONL catalogs found no current exact organism, project, or analysis rows for `NCBITaxon:2583373`.

## Completeness

- `data/raw/ncbi_type_material.tsv:103002-103005` has holotype aliases `E 5899/1`, `E-5899/1`, `E5899/1`, and `E:5899/1` under `Nitzschia captiva`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:2583373`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material side inventories.

## Additional Notes

- None.
