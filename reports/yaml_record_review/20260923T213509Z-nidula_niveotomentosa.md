# YAML Record Review

- Target: `data/taxa/eukaryota/nidula_niveotomentosa.yaml`
- Taxon: `NCBITaxon:380643` (`Nidula niveotomentosa`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:380643`, label `Nidula niveotomentosa`.
- It is grounded exactly under `NCBITaxon:380642` (`Nidula`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Nidula`.

## Validation

- `just validate data/taxa/eukaryota/nidula_niveotomentosa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neurospora_tetrasperma.yaml data/taxa/eukaryota/neurospora_tetraspora.yaml data/taxa/eukaryota/nia_vibrissa.yaml data/taxa/eukaryota/nidula_niveotomentosa.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55439` contains the seeded identifier with reason `attested rule: Nidula niveotomentosa, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:80030` matches the YAML identity: parent `NCBITaxon:380642`, rank `SPECIES`, two exact synonyms, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:80030` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33886`, where `NCBITaxon:380643` has `organism_count` 2.
- Native GOLD has one exact current-taxid organism row, `Go0551228` / `Nidula niveotomentosa CBS 980.80`, linked to project `Gp0502589`; no native analysis row linked to that project.

## Completeness

- Exact StrainInfo side inventory found 3 direct records and 3 deposit entries: `CBS 380.80`, `CBS 250.84`, and `ATCC 38357`.
- Exact NCBI type-material, BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:380643`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
