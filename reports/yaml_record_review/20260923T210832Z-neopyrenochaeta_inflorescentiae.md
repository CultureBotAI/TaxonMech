# YAML Record Review

- Target: `data/taxa/eukaryota/neopyrenochaeta_inflorescentiae.yaml`
- Taxon: `NCBITaxon:531899` (`Neopyrenochaeta inflorescentiae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:531899`, label `Neopyrenochaeta inflorescentiae`.
- It is grounded exactly under `NCBITaxon:2078553` (`Neopyrenochaeta`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Neopyrenochaeta`.

## Validation

- `just validate data/taxa/eukaryota/neopyrenochaeta_inflorescentiae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neophaeococcomyces_sp.yaml data/taxa/eukaryota/neophaeosphaeria_agaves.yaml data/taxa/eukaryota/neopyrenochaeta_inflorescentiae.yaml data/taxa/eukaryota/neoscytalidium_dimidiatum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55921` contains the seeded identifier with reason `attested rule: Neopyrenochaeta inflorescentiae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:121709` matches the YAML identity: parent `NCBITaxon:2078553`, rank `SPECIES`, four synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:121709` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38032`, where `NCBITaxon:531899` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0529085` / `Pyrenochaeta inflorescentiae CORFU 0001`, linked to native projects `Gp0457393` and `Gp0466634`; no native analyses are linked to those projects in this snapshot.

## Completeness

- The NCBI type-material inventory contains four exact `culture from type material` rows for `NCBITaxon:531899`: `CBS 119222`, `CBS:119222`, `FMR 15334`, and `FMR:15334`.
- Exact structured scans found no rows for `NCBITaxon:531899` in `data/raw/ncbi_merged_ids.tsv`, retained retired NCBI old IDs, exact BacDive, generated raw strain rows, generated StrainInfo target rows, exact StrainInfo side inventory, or checked auxiliary source rows.
- The record correctly has `strain_count: 0` and no generated `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation materializes local strains from NCBI type-material or native GOLD side inventories.

## Additional Notes

- GOLD's current native organism and project names still use the older `Pyrenochaeta inflorescentiae` spelling while carrying the exact current NCBI taxon ID; the generated YAML follows the NCBI label.
