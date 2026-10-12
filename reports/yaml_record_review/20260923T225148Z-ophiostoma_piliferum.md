# YAML Record Review

- Target: `data/taxa/eukaryota/ophiostoma_piliferum.yaml`
- Taxon: `NCBITaxon:38032` (`Ophiostoma piliferum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:38032`, label `Ophiostoma piliferum`.
- It is grounded exactly under `NCBITaxon:5159` (`Ophiostoma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Ophiostoma`.

## Validation

- `just validate data/taxa/eukaryota/ophiostoma_piliferum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ophiostoma_montium.yaml data/taxa/eukaryota/ophiostoma_novo_ulmi_subsp_novo_ulmi_h327.yaml data/taxa/eukaryota/ophiostoma_piceae.yaml data/taxa/eukaryota/ophiostoma_piliferum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52384` contains the seeded identifier with reason `attested rule: Ophiostoma piliferum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4324` matches the YAML identity: parent `NCBITaxon:5159`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4324` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33875`, where `NCBITaxon:38032` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0002485` / `Ophiostoma piliferum FCC 55A`, linked to project `Gp0002485` and no analysis rows.
- Exact StrainInfo side evidence has 24 direct `NCBITaxon:38032` records and 25 deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:38032`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD or StrainInfo side inventories.

## Additional Notes

- None.
