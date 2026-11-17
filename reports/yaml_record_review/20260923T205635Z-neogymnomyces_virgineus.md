# YAML Record Review

- Target: `data/taxa/eukaryota/neogymnomyces_virgineus.yaml`
- Taxon: `NCBITaxon:1073324` (`Neogymnomyces virgineus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1073324`, label `Neogymnomyces virgineus`.
- It is grounded exactly under `NCBITaxon:166397` (`Neogymnomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Neogymnomyces`.

## Validation

- `just validate data/taxa/eukaryota/neogymnomyces_virgineus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neofusicoccum_parvum.yaml data/taxa/eukaryota/neogymnomyces_virgineus.yaml data/taxa/eukaryota/neohortaea_acidophila.yaml data/taxa/eukaryota/neonectria_coccinea.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57487` contains the seeded identifier with reason `attested rule: Neogymnomyces virgineus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:230004` matches the YAML identity: parent `NCBITaxon:166397`, rank `SPECIES`, one related synonym, and genetic code `1`.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:230004` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1276`, where `NCBITaxon:1073324` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows: `Go0614125` / `Neogymnomyces virgineus DSM 24930` and `Go0614126` / `Neogymnomyces virgineus DCDSL 7716`.
- No native GOLD project or analysis rows were found for those organism IDs.

## Completeness

- An exact field scan of `data/raw/ncbi_type_material.tsv` found 2 type-material rows for `NCBITaxon:1073324`, covering `DSM 24930`.
- Exact StrainInfo side inventory found one direct record with one exact deposit, `DSM 24930`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:1073324`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:1073324`; the exact StrainInfo and type-material side inventories did not materialize local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.
