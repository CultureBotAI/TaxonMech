# YAML Record Review

- Target: `data/taxa/eukaryota/nereocystis_luetkeana.yaml`
- Taxon: `NCBITaxon:117523` (`Nereocystis luetkeana`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:117523`, label `Nereocystis luetkeana`.
- It is grounded exactly under `NCBITaxon:117522` (`Nereocystis`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 11 lineage entries from `root` through `Nereocystis`.

## Validation

- `just validate data/taxa/eukaryota/nereocystis_luetkeana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neospora_caninum.yaml data/taxa/eukaryota/neotessella_volvocina.yaml data/taxa/eukaryota/neotyphodium_sp_fatg_4.yaml data/taxa/eukaryota/nereocystis_luetkeana.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53836` contains the seeded identifier with reason `attested rule: Nereocystis luetkeana, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:21907` matches the YAML identity: parent `NCBITaxon:117522`, rank `SPECIES`, three synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 11 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:21907` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3870`, where `NCBITaxon:117523` has `organism_count` 1.
- The retained GOLD aggregate supports the generated source attestation; a direct exact scan of the current local native GOLD organism, project, and analysis JSONL snapshots found no rows for current NCBI taxid `117523`.

## Completeness

- Exact structured scans found no rows for `NCBITaxon:117523` in `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, retained retired NCBI old IDs, exact BacDive, generated raw strain rows, generated StrainInfo target rows, exact StrainInfo side inventory, or checked auxiliary source rows.
- The record correctly has `strain_count: 0` and no generated `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation adds local strain evidence for `Nereocystis luetkeana`.

## Additional Notes

- `data/raw/gold_organisms.tsv` is a transformed aggregate inventory and can differ from exact current-taxid native GOLD JSONL scans. This record asserts only the retained aggregate organism count.
