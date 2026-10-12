# YAML Record Review

- Target: `data/taxa/eukaryota/neonothopanus_nambi.yaml`
- Taxon: `NCBITaxon:71958` (`Neonothopanus nambi`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:71958`, label `Neonothopanus nambi`.
- It is grounded exactly under `NCBITaxon:71957` (`Neonothopanus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Neonothopanus`.

## Validation

- `just validate data/taxa/eukaryota/neonothopanus_nambi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neonectria_punicea.yaml data/taxa/eukaryota/neonectria_sp_b_13.yaml data/taxa/eukaryota/neonothopanus_nambi.yaml data/taxa/eukaryota/neopestalotiopsis_clavispora.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53228` contains the seeded identifier with reason `attested rule: Neonothopanus nambi, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:10072` matches the YAML identity: parent `NCBITaxon:71957`, rank `SPECIES`, four synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:10072` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41953`, where `NCBITaxon:71958` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0519489` / `Neonothopanus nambi BIN 2379`, linked to native project `Gp0443635` and one project-linked native analysis.

## Completeness

- Exact structured scans found no rows for `NCBITaxon:71958` in `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, retained retired NCBI old IDs, exact BacDive, generated raw strain rows, generated StrainInfo target rows, exact StrainInfo side inventory, or checked auxiliary source rows.
- The record correctly has `strain_count: 0` and no generated `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation adds local strain evidence for `Neonothopanus nambi`.

## Additional Notes

- None.
