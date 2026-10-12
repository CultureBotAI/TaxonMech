# YAML Record Review

- Target: `data/taxa/eukaryota/myxozyma_melibiosi.yaml`
- Taxon: `NCBITaxon:54550` (`Myxozyma melibiosi`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:54550`, label `Myxozyma melibiosi`.
- It is grounded exactly under `NCBITaxon:54096` (`Myxozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Myxozyma`.

## Validation

- `just validate data/taxa/eukaryota/myxozyma_melibiosi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myxozyma_lipomycoides.yaml data/taxa/eukaryota/myxozyma_melibiosi.yaml data/taxa/eukaryota/myxozyma_monticola.yaml data/taxa/eukaryota/myxozyma_mucilagina.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52930` contains the seeded identifier with reason `attested rule: Myxozyma melibiosi, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6936` matches the YAML identity: parent `NCBITaxon:54096`, rank `SPECIES`, six exact synonyms, and related synonym `Torulopsis melibiosa Shifrine & Phaff, 1956`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6936` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38402`, where `NCBITaxon:54550` has `organism_count` 2.
- Native GOLD has 2 exact current-taxid organism rows, `Go0357145` / `Myxozyma melibiosi UCDFST 52-87` and `Go0705210` / `Myxozyma melibiosi NRRL Y-11781`, linked to 3 projects and one native analysis for `Myxozyma melibiosi UCDFST 52-87`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 23 type-material rows for `NCBITaxon:54550`, all under `Torulopsis melibiosa` and covering variants of `ATCC 24226`, `BCRC 21484`, `BCRC 22184`, `CBS 2102`, `CCRC 21484`, `CCRC 22184`, `IFO 1871`, `IGC 3939`, `JCM 5194`, `MUCL 30423`, `NRRL Y-11781`, and `UCD 52-87`.
- Exact StrainInfo has 3 direct records and 23 deposit rows for `NCBITaxon:54550`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:54550`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:54550`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.
