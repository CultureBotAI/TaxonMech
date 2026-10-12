# YAML Record Review

- Target: `data/taxa/eukaryota/nilaparvata_lugens_yeast_like_symbiont.yaml`
- Taxon: `NCBITaxon:36927` (`Nilaparvata lugens yeast-like symbiont`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:36927`, label `Nilaparvata lugens yeast-like symbiont`.
- It is grounded exactly under `NCBITaxon:45426` (`unclassified Ascomycota`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 8 lineage entries from `root` through `unclassified Ascomycota`.

## Validation

- `just validate data/taxa/eukaryota/nilaparvata_lugens_yeast_like_symbiont.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nigrospora_oryzae.yaml data/taxa/eukaryota/nigrospora_sphaerica.yaml data/taxa/eukaryota/nilaparvata_lugens_yeast_like_symbiont.yaml data/taxa/eukaryota/nitzschia_captiva.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52364` contains the seeded identifier with reason `attested rule: Nilaparvata lugens yeast-like symbiont, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4193` matches the YAML identity: parent `NCBITaxon:45426`, rank `SPECIES`, exact synonym `Nilaparvata lugens yeast-like symbiote`, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 8 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4193` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33545`, where `NCBITaxon:36927` has `organism_count` 1.
- Native GOLD has two exact current-taxid organism rows, `Go0076238` / `Nilaparvata lugens yeast-like symbiont Hangzhou` and `Go0109084` / `Nilaparvata lugens yeast-like symbiont`; these link to projects `Gp0076238` and `Gp0109084`, and one native analysis links through `Gp0076238`.

## Completeness

- The bounded exact scan found no NCBI type-material rows, no exact StrainInfo rows, and no NCBI merged-ID side rows for `NCBITaxon:36927`; no retained retired old-ID rows were present either.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and checked auxiliary source rows were empty for `NCBITaxon:36927`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD side inventories.

## Additional Notes

- None.
