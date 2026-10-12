# YAML Record Review

- Target: `data/taxa/eukaryota/neotessella_volvocina.yaml`
- Taxon: `NCBITaxon:52559` (`Neotessella volvocina`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:52559`, label `Neotessella volvocina`.
- It is grounded exactly under `NCBITaxon:2419521` (`Neotessella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Neotessella`.

## Validation

- `just validate data/taxa/eukaryota/neotessella_volvocina.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neospora_caninum.yaml data/taxa/eukaryota/neotessella_volvocina.yaml data/taxa/eukaryota/neotyphodium_sp_fatg_4.yaml data/taxa/eukaryota/nereocystis_luetkeana.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52865` contains the seeded identifier with reason `attested rule: Neotessella volvocina, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6591` matches the YAML identity: parent `NCBITaxon:2419521`, rank `SPECIES`, five synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6591` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37899`, where `NCBITaxon:52559` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0008157` / `Tessellaria volvocina CCMP 1781`, linked to native project `Gp0008157` and no native analyses.

## Completeness

- A structured exact scan found no rows for `NCBITaxon:52559` in `data/raw/ncbi_type_material.tsv`.
- Exact StrainInfo side inventory found one direct record with one exact deposit assertion, `CCMP1781`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old ID `NCBITaxon:2419522` into `NCBITaxon:52559`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points to the target, so the generated record correctly omits `replaces`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and checked auxiliary source rows were empty for `NCBITaxon:52559`; the record correctly has `strain_count: 0`.
- The exact StrainInfo side inventory did not materialize local strain rows; StrainInfo only joins through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- GOLD's current native organism and project names still use the older `Tessellaria volvocina` spelling while carrying the exact current NCBI taxon ID; the generated YAML follows the NCBI label.
