# YAML Record Review

- Target: `data/taxa/eukaryota/oleoguttula_mirabilis.yaml`
- Taxon: `NCBITaxon:1507867` (`Oleoguttula mirabilis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1507867`, label `Oleoguttula mirabilis`.
- It is grounded exactly under `NCBITaxon:1507866` (`Oleoguttula`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Oleoguttula`.

## Validation

- `just validate data/taxa/eukaryota/oleoguttula_mirabilis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ogataea_xyloterini.yaml data/taxa/eukaryota/ogataea_zsoltii.yaml data/taxa/eukaryota/oidium_heveae.yaml data/taxa/eukaryota/oleoguttula_mirabilis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60373` contains the seeded identifier with reason `attested rule: Oleoguttula mirabilis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:387249` matches the YAML identity: parent `NCBITaxon:1507866`, rank `SPECIES`, no exact synonyms, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:387249` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:11866`, where `NCBITaxon:1507867` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0583376` / `Oleoguttula mirabilis MNA CCFEE 5522`, linked to projects `Gp0587339` and `Gp0891532`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- Exact NCBI type material has 2 `CCFEE 5523` culture-from-holotype rows plus 2 `CBS 136102` holotype rows for `Oleoguttula mirabilis`.
- Exact StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1507867`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
