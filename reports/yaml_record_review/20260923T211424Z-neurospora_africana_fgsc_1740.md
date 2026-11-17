# YAML Record Review

- Target: `data/taxa/eukaryota/neurospora_africana_fgsc_1740.yaml`
- Taxon: `NCBITaxon:1266766` (`Neurospora africana FGSC 1740`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:1266766`, label `Neurospora africana FGSC 1740`.
- It is grounded exactly under `NCBITaxon:5143` (`Neurospora africana`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Neurospora africana`.

## Validation

- `just validate data/taxa/eukaryota/neurospora_africana_fgsc_1740.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/neurospora_africana_fgsc_1740.yaml data/taxa/eukaryota/neurospora_calospora.yaml data/taxa/eukaryota/neurospora_crassa.yaml data/taxa/eukaryota/neurospora_crassa_or74a.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58811` contains the seeded identifier with reason `attested rule: Neurospora africana FGSC 1740, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:293789` matches the YAML identity: parent `NCBITaxon:5143`, rank `STRAIN`, no synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:293789` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:6334`, where `NCBITaxon:1266766` has `organism_count` 4.
- The current native GOLD snapshot has five exact current-taxid organism rows. `Go0080990` / `Neurospora africana FGSC 1740` links to project `Gp0080990` and one native analysis row.

## Completeness

- Exact structured scans found no rows for `NCBITaxon:1266766` in `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, retained retired NCBI old IDs, exact BacDive, generated raw strain rows, generated StrainInfo target rows, exact StrainInfo side inventory, or checked auxiliary source rows.
- The record correctly has `strain_count: 0` and no generated `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation adds local strain evidence for `Neurospora africana FGSC 1740`.

## Additional Notes

- The retained GOLD aggregate count is four, while the current local native GOLD JSONL snapshot exposes five exact organism rows for this NCBI strain ID. The generated source attestation follows the retained aggregate row.
