# YAML Record Review

- Target: `data/taxa/eukaryota/ovicillium_attenuatum.yaml`
- Taxon: `NCBITaxon:1924279` (`Ovicillium attenuatum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1924279`, label `Ovicillium attenuatum`.
- It is grounded exactly under `NCBITaxon:1924278` (`Ovicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Ovicillium`.

## Validation

- `just validate data/taxa/eukaryota/ovicillium_attenuatum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ovicillium_attenuatum.yaml data/taxa/eukaryota/oxyrrhis_marina.yaml data/taxa/eukaryota/oxytricha_trifallax.yaml data/taxa/eukaryota/pachnocybe_ferruginea.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61625` contains the seeded identifier with reason `attested rule: Ovicillium attenuatum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:495701` matches the YAML identity: parent `NCBITaxon:1924278`, rank `SPECIES`, no exact synonyms, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:495701` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:17590`, where `NCBITaxon:1924279` has `organism_count` 1.
- The native GOLD exact current-taxid scan found no local organism, project, or analysis rows for `NCBITaxon:1924279`.

## Completeness

- Exact NCBI type material has six rows for `NCBITaxon:1924279`, covering `CBS 399.86`, `CBS:399.86`, `CBS_399.86`, `INIFAT C86/59-3`, `CBS H-22409`, and `CBS:H:22409`.
- Exact StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1924279`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material or native GOLD side inventories.

## Additional Notes

- None.
