# YAML Record Review

- Target: `data/taxa/eukaryota/neospora_caninum.yaml`
- Taxon: `NCBITaxon:29176` (`Neospora caninum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:29176`, label `Neospora caninum`.
- It is grounded exactly under `NCBITaxon:29175` (`Neospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Neospora`.

## Validation

- `just validate data/taxa/eukaryota/neospora_caninum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/neospora_caninum.yaml data/taxa/eukaryota/neotessella_volvocina.yaml data/taxa/eukaryota/neotyphodium_sp_fatg_4.yaml data/taxa/eukaryota/nereocystis_luetkeana.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52191` contains the seeded identifier with reason `attested rule: Neospora caninum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:3009` matches the YAML identity: parent `NCBITaxon:29175`, rank `SPECIES`, three synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:3009` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:28585`, where `NCBITaxon:29176` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0002411` / `Neospora caninum` and `Go0573655` / `Neospora caninum Uru1`, linked to native projects `Gp0002411` and `Gp0548317`; the Uru1 project has one native analysis linked through `AP PROJECT GOLD IDS`.

## Completeness

- A structured exact scan found no rows for `NCBITaxon:29176` in `data/raw/ncbi_type_material.tsv`.
- Exact StrainInfo side inventory found 7 direct records and 7 exact deposit assertions, including sampled designations `ATCC 50843`, `ATCC 50844`, `ATCC 50845`, type-designated `ATCC 50977`, and `ATCC 50939`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old ID `NCBITaxon:572307` into `NCBITaxon:29176`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points to the target, so the generated record correctly omits `replaces`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and checked auxiliary source rows were empty for `NCBITaxon:29176`; the record correctly has `strain_count: 0`.
- The exact StrainInfo side inventory did not materialize local strain rows; StrainInfo only joins through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
