# YAML Record Review

- Target: `data/taxa/eukaryota/neophaeococcomyces_sp.yaml`
- Taxon: `NCBITaxon:2874731` (`Neophaeococcomyces sp.`)
- Verdict: pass

## Target

- The record is the seeded NCBI species-rank taxon `NCBITaxon:2874731`, label `Neophaeococcomyces sp.`.
- It is grounded exactly under `NCBITaxon:2619597` (`unclassified Neophaeococcomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `unclassified Neophaeococcomyces`.

## Validation

- `just validate data/taxa/eukaryota/neophaeococcomyces_sp.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/neophaeococcomyces_sp.yaml data/taxa/eukaryota/neophaeosphaeria_agaves.yaml data/taxa/eukaryota/neopyrenochaeta_inflorescentiae.yaml data/taxa/eukaryota/neoscytalidium_dimidiatum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63341` contains the seeded identifier with reason `attested rule: Neophaeococcomyces sp., 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:566589` matches the YAML identity: parent `NCBITaxon:2619597`, rank `SPECIES`, no synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:566589` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:27956`, where `NCBITaxon:2874731` has `organism_count` 2.
- The retained GOLD aggregate supports the generated source attestation; a direct exact scan of the current local native GOLD organism, project, and analysis JSONL snapshots found no rows for current NCBI taxid `2874731`.

## Completeness

- Exact structured scans found no rows for `NCBITaxon:2874731` in `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, retained retired NCBI old IDs, exact BacDive, generated raw strain rows, generated StrainInfo target rows, exact StrainInfo side inventory, or checked auxiliary source rows.
- The record correctly has `strain_count: 0` and no generated `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation adds local strain evidence for `Neophaeococcomyces sp.`.

## Additional Notes

- `data/raw/gold_organisms.tsv` is a transformed aggregate inventory and can differ from exact current-taxid native GOLD JSONL scans. This record asserts only the retained aggregate organism count.
