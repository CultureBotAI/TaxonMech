# YAML Record Review

- Target: `data/taxa/eukaryota/oosporidium_margaritiferum.yaml`
- Taxon: `NCBITaxon:1859950` (`Oosporidium margaritiferum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1859950`, label `Oosporidium margaritiferum`.
- It is grounded exactly under `NCBITaxon:43965` (`Oosporidium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 9 lineage entries from `root` through `Oosporidium`.

## Validation

- `just validate data/taxa/eukaryota/oosporidium_margaritiferum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/onnia_scaura.yaml data/taxa/eukaryota/onygena_corvina.yaml data/taxa/eukaryota/oomyces_carneoalbus.yaml data/taxa/eukaryota/oosporidium_margaritiferum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61376` contains the seeded identifier with reason `attested rule: Oosporidium margaritiferum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:486196` matches the YAML identity: parent `NCBITaxon:43965`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 9 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:486196` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:16604`, where `NCBITaxon:1859950` has `organism_count` 7.
- Native GOLD has 7 exact current-taxid organism rows but no linked project or analysis rows in the local exact scan.

## Completeness

- Exact NCBI type material has 17 duplicated spelling rows for `Trichosporon margaritiferum`, covering `ATCC 10676`, `BCRC` / `CCRC 21536`, `CBS 2531`, `DSM 70351`, `IFO 1208`, `NRRL Y-1519`, and `VKM Y-816`.
- Exact StrainInfo side inventory found 4 direct records and 22 deposits, but no BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for `NCBITaxon:1859950`.
- Exact NCBI merged-ID side inventory maps old `NCBITaxon:43966` to `NCBITaxon:1859950`, while retained retired old-ID, BacDive, and checked auxiliary source rows were empty; the record correctly has no `replaces` entry and `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo, exact NCBI type-material, native GOLD, or NCBI merged-ID side inventories.

## Additional Notes

- None.
