# YAML Record Review

- Target: `data/taxa/eukaryota/paraphaeosphaeria_sporulosa.yaml`
- Taxon: `NCBITaxon:1460663` (`Paraphaeosphaeria sporulosa`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1460663`, label `Paraphaeosphaeria sporulosa`.
- It is grounded exactly under `NCBITaxon:125369` (`Paraphaeosphaeria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Paraphaeosphaeria`.

## Validation

- `just validate data/taxa/eukaryota/paraphaeosphaeria_sporulosa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paranamyces_uniporus.yaml data/taxa/eukaryota/paraphaeosphaeria_minitans.yaml data/taxa/eukaryota/paraphaeosphaeria_sporulosa.yaml data/taxa/eukaryota/paraphoma_chrysanthemicola.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:60226` contains the seeded identifier with reason `attested rule: Paraphaeosphaeria sporulosa, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:371458` matches the YAML identity: parent `NCBITaxon:125369`, rank `SPECIES`, four exact synonyms, four related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:371458` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:11170`, where `NCBITaxon:1460663` has `organism_count` 4.
- The native GOLD exact current-taxid scan found three organism rows, two project rows, and two analysis rows for `NCBITaxon:1460663`.
- Exact StrainInfo side evidence has 26 direct `NCBITaxon:1460663` records and 29 deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1460663`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains two old IDs that now point at `NCBITaxon:1460663`: `NCBITaxon:135649` and `NCBITaxon:1915222`; neither is retained as a retired taxon, so the YAML correctly has no `replaces` entries.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
