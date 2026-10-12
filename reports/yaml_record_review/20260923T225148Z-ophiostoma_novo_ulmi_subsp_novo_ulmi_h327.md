# YAML Record Review

- Target: `data/taxa/eukaryota/ophiostoma_novo_ulmi_subsp_novo_ulmi_h327.yaml`
- Taxon: `NCBITaxon:1224258` (`Ophiostoma novo-ulmi subsp. novo-ulmi H327`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:1224258`, label `Ophiostoma novo-ulmi subsp. novo-ulmi H327`.
- It is grounded exactly under `NCBITaxon:170179` (`Ophiostoma novo-ulmi subsp. novo-ulmi`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 18 lineage entries from `root` through `Ophiostoma novo-ulmi subsp. novo-ulmi`.

## Validation

- `just validate data/taxa/eukaryota/ophiostoma_novo_ulmi_subsp_novo_ulmi_h327.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ophiostoma_montium.yaml data/taxa/eukaryota/ophiostoma_novo_ulmi_subsp_novo_ulmi_h327.yaml data/taxa/eukaryota/ophiostoma_piceae.yaml data/taxa/eukaryota/ophiostoma_piliferum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58488` contains the seeded identifier with reason `attested rule: Ophiostoma novo-ulmi subsp. novo-ulmi H327, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:278706` matches the YAML identity: parent `NCBITaxon:170179`, rank `STRAIN`, no exact or related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 18 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:278706` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:5365`, where `NCBITaxon:1224258` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0038489` / `Ophiostoma novo-ulmi novo-ulmi H327`, linked to project `Gp0038489` and one analysis row via that project.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1224258`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD side inventories.

## Additional Notes

- None.
