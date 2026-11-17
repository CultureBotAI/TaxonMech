# YAML Record Review

- Target: `data/taxa/eukaryota/neophaeosphaeria_agaves.yaml`
- Taxon: `NCBITaxon:1414629` (`Neophaeosphaeria agaves`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1414629`, label `Neophaeosphaeria agaves`.
- It is grounded exactly under `NCBITaxon:364020` (`Neophaeosphaeria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Neophaeosphaeria`.

## Validation

- `just validate data/taxa/eukaryota/neophaeosphaeria_agaves.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neophaeococcomyces_sp.yaml data/taxa/eukaryota/neophaeosphaeria_agaves.yaml data/taxa/eukaryota/neopyrenochaeta_inflorescentiae.yaml data/taxa/eukaryota/neoscytalidium_dimidiatum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60054` contains the seeded identifier with reason `attested rule: Neophaeosphaeria agaves, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:350755` matches the YAML identity: parent `NCBITaxon:364020`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:350755` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:10031`, where `NCBITaxon:1414629` has `organism_count` 1.
- The retained GOLD aggregate supports the generated source attestation; a direct exact scan of the current local native GOLD organism, project, and analysis JSONL snapshots found no rows for current NCBI taxid `1414629`.

## Completeness

- A complete exact scan of `data/raw/ncbi_type_material.tsv` found eight rows for `NCBITaxon:1414629`: culture-from-holotype aliases for `CBS 136429`, `CBS:136429`, `CPC 21264`, `CPC 21265`, `CPC:21264`, and `CPC:21265`, plus holotype aliases `CBS H-21438` and `CBS:H:21438`.
- Exact structured scans found no rows for `NCBITaxon:1414629` in `data/raw/ncbi_merged_ids.tsv`, retained retired NCBI old IDs, exact BacDive, generated raw strain rows, generated StrainInfo target rows, exact StrainInfo side inventory, or checked auxiliary source rows.
- The record correctly has `strain_count: 0` and no generated `replaces` entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation materializes local strains from NCBI type-material or native GOLD side inventories.

## Additional Notes

- `data/raw/gold_organisms.tsv` is a transformed aggregate inventory and can differ from exact current-taxid native GOLD JSONL scans. This record asserts only the retained aggregate organism count.
