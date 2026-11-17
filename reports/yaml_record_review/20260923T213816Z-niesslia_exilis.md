# YAML Record Review

- Target: `data/taxa/eukaryota/niesslia_exilis.yaml`
- Taxon: `NCBITaxon:267680` (`Niesslia exilis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:267680`, label `Niesslia exilis`.
- It is grounded exactly under `NCBITaxon:267679` (`Niesslia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Niesslia`.

## Validation

- `just validate data/taxa/eukaryota/niesslia_exilis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nidularia_deformis.yaml data/taxa/eukaryota/niesslia_exilis.yaml data/taxa/eukaryota/niesslia_gamsii.yaml data/taxa/eukaryota/nigrograna_mackinnonii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54901` contains the seeded identifier with reason `attested rule: Niesslia exilis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:55220` matches the YAML identity: parent `NCBITaxon:267679`, rank `SPECIES`, exact synonym `Sphaeria exilis`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:55220` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:24662`, where `NCBITaxon:267680` has `organism_count` 2.
- Native GOLD has one exact current-taxid organism row, `Go0036359` / `Niesslia exilis CBS 358.70`, linked to projects `Gp0036359` and `Gp0036360`; no native analysis rows linked to those projects.

## Completeness

- Exact StrainInfo side inventory found 7 direct records and 10 deposit entries, including sampled designations `JCM 10162`, `CBS 357.70`, `CBS 358.70`, `MUCL 8386`, `CBS 493.73`, and `CBS 560.74`.
- Exact NCBI type-material, BacDive, generated raw strain rows, generated StrainInfo target rows, NCBI merged-ID side rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:267680`; the record correctly has `strain_count: 0` and no generated `replaces` entries.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; exact rows in the current native GOLD JSONL catalogs can differ from that generated aggregate and do not create local strains without BacDive-derived local strain inventory entries.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or native GOLD side inventories.

## Additional Notes

- None.
