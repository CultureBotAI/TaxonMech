# YAML Record Review

- Target: `data/taxa/eukaryota/paracorniculantispora_psalliotae.yaml`
- Taxon: `NCBITaxon:73499` (`Paracorniculantispora psalliotae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:73499`, label `Paracorniculantispora psalliotae`.
- It is grounded exactly under `NCBITaxon:3684074` (`Paracorniculantispora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Paracorniculantispora`.

## Validation

- `just validate data/taxa/eukaryota/paracorniculantispora_psalliotae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paracorniculantispora_psalliotae.yaml data/taxa/eukaryota/paraeutypella_vitis.yaml data/taxa/eukaryota/parafenestella_ontariensis.yaml data/taxa/eukaryota/paraglomus_brasilianum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53254` contains the seeded identifier with reason `attested rule: Paracorniculantispora psalliotae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:10317` matches the YAML identity: parent `NCBITaxon:3684074`, rank `SPECIES`, four exact synonyms, four related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:10317` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42059`, where `NCBITaxon:73499` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, one project row, and one analysis row for `Lecanicillium psalliotae HWLR35`.
- Exact StrainInfo side evidence has 64 direct `NCBITaxon:73499` records and 84 deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:73499`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains one old ID that now points at `NCBITaxon:73499`: `NCBITaxon:132166`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
