# YAML Record Review

- Target: `data/taxa/eukaryota/neotyphodium_sp_fatg_4.yaml`
- Taxon: `NCBITaxon:1326757` (`Neotyphodium sp. FaTG-4`)
- Verdict: pass

## Target

- The record is the seeded NCBI species-rank taxon `NCBITaxon:1326757`, label `Neotyphodium sp. FaTG-4`.
- It is grounded exactly under `NCBITaxon:2644437` (`unclassified Neotyphodium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `unclassified Neotyphodium`.

## Validation

- `just validate data/taxa/eukaryota/neotyphodium_sp_fatg_4.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neospora_caninum.yaml data/taxa/eukaryota/neotessella_volvocina.yaml data/taxa/eukaryota/neotyphodium_sp_fatg_4.yaml data/taxa/eukaryota/nereocystis_luetkeana.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59480` contains the seeded identifier with reason `attested rule: Neotyphodium sp. FaTG-4, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:316530` matches the YAML identity: parent `NCBITaxon:2644437`, rank `SPECIES`, one exact synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:316530` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:7951`, where `NCBITaxon:1326757` has `organism_count` 3.
- The current native GOLD snapshot has one exact current-taxid organism row, `Go0098756` / `Neotyphodium sp. FaTG-4`, linked to four native projects and no native analyses.

## Completeness

- Exact structured scans found no rows for `NCBITaxon:1326757` in `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, retained retired NCBI old IDs, exact BacDive, generated raw strain rows, generated StrainInfo target rows, exact StrainInfo side inventory, or checked auxiliary source rows.
- The record correctly has `strain_count: 0` and no generated `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation adds local strain evidence for `Neotyphodium sp. FaTG-4`.

## Additional Notes

- The retained GOLD aggregate count is three, while the current local native GOLD JSONL snapshot exposes one exact organism row and four exact linked projects; the generated source attestation follows the retained aggregate row.
