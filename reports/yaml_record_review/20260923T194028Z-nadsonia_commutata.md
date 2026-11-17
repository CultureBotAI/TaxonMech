# YAML Record Review

- Target: `data/taxa/eukaryota/nadsonia_commutata.yaml`
- Taxon: `NCBITaxon:53686` (`Nadsonia commutata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:53686`, label `Nadsonia commutata`.
- It is grounded exactly under `NCBITaxon:45785` (`Nadsonia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Nadsonia`.

## Validation

- `just validate data/taxa/eukaryota/nadsonia_commutata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myxozyma_udenii.yaml data/taxa/eukaryota/myxozyma_vanderwaltii.yaml data/taxa/eukaryota/nadsonia_commutata.yaml data/taxa/eukaryota/nadsonia_fulvescens.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52895` contains the seeded identifier with reason `attested rule: Nadsonia commutata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6799` matches the YAML identity: parent `NCBITaxon:45785`, rank `SPECIES`, and related synonym `Nadsonia commutata Golubev, 1973`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6799` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38219`, where `NCBITaxon:53686` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705661` / `Nadsonia commutata NRRL Y-7950`, linked to project `Gp0831711` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 16 type-material rows for `NCBITaxon:53686`, covering variants of `ATCC 58437`, `CBS 6640`, `IFO 10029`, `IGC 4210`, `NRRL Y-7950`, `VKM Y-1573`, and `VKPM Y 1244`.
- Exact StrainInfo side inventory has 4 direct rows and 15 deposit entries for `NCBITaxon:53686`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:53686`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.
