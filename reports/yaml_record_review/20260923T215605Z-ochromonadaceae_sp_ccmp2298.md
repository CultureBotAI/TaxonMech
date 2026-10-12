# YAML Record Review

- Target: `data/taxa/eukaryota/ochromonadaceae_sp_ccmp2298.yaml`
- Taxon: `NCBITaxon:483371` (`Ochromonadaceae sp. CCMP2298`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:483371`, label `Ochromonadaceae sp. CCMP2298`.
- It is grounded exactly under `NCBITaxon:372997` (`unclassified Ochromonadaceae`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `unclassified Ochromonadaceae`.

## Validation

- `just validate data/taxa/eukaryota/ochromonadaceae_sp_ccmp2298.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/obelidium_mucronatum.yaml data/taxa/eukaryota/ochromonadaceae_sp_ccmp2298.yaml data/taxa/eukaryota/ochromonas_sp_ccmp1393.yaml data/taxa/eukaryota/octactis_speculum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55802` contains the seeded identifier with reason `attested rule: Ochromonadaceae sp. CCMP2298, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:107955` matches the YAML identity: parent `NCBITaxon:372997`, rank `SPECIES`, two exact synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:107955` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36820`, where `NCBITaxon:483371` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0016967` / `Chrysophyceae sp. CCMP 2298`, linked to projects `Gp0016967` and `Gp0018317`; the local exact native-GOLD scan found no linked analysis rows.

## Completeness

- `data/raw/ncbi_merged_ids.tsv:8134` maps side-inventory old ID `NCBITaxon:1215324` into `NCBITaxon:483371`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` generated a `replaces` entry.
- Exact NCBI type-material, BacDive, generated raw strain rows, exact StrainInfo, generated StrainInfo target rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:483371`; the record correctly has `strain_count: 0`.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from native GOLD side inventories.

## Additional Notes

- None.
