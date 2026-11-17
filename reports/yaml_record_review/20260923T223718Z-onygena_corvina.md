# YAML Record Review

- Target: `data/taxa/eukaryota/onygena_corvina.yaml`
- Taxon: `NCBITaxon:180788` (`Onygena corvina`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:180788`, label `Onygena corvina`.
- It is grounded exactly under `NCBITaxon:45432` (`Onygena`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Onygena`.

## Validation

- `just validate data/taxa/eukaryota/onygena_corvina.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/onnia_scaura.yaml data/taxa/eukaryota/onygena_corvina.yaml data/taxa/eukaryota/oomyces_carneoalbus.yaml data/taxa/eukaryota/oosporidium_margaritiferum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54336` contains the seeded identifier with reason `attested rule: Onygena corvina, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:36253` matches the YAML identity: parent `NCBITaxon:45432`, rank `SPECIES`, no exact synonyms, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:36253` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:15927`, where `NCBITaxon:180788` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0114324` / `Onygena corvina CBS 281.48`, linked to project `Gp0118086` and one analysis row via that project.

## Completeness

- Exact NCBI type material has 4 `CBS 152.73` culture-from-neotype rows plus 4 `CBS H-15266` neotype spellings.
- Exact StrainInfo side inventory found 7 direct records and 12 deposits, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:180788`.
- Exact NCBI merged-ID, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:180788`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, or native GOLD side inventories.

## Additional Notes

- None.
