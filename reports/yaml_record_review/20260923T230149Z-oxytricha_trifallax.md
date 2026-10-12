# YAML Record Review

- Target: `data/taxa/eukaryota/oxytricha_trifallax.yaml`
- Taxon: `NCBITaxon:1172189` (`Oxytricha trifallax`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1172189`, label `Oxytricha trifallax`.
- It is grounded exactly under `NCBITaxon:5943` (`Oxytricha`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `6`.
- The YAML carries 13 lineage entries from `root` through `Oxytricha`.

## Validation

- `just validate data/taxa/eukaryota/oxytricha_trifallax.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ovicillium_attenuatum.yaml data/taxa/eukaryota/oxyrrhis_marina.yaml data/taxa/eukaryota/oxytricha_trifallax.yaml data/taxa/eukaryota/pachnocybe_ferruginea.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58175` contains the seeded identifier with reason `attested rule: Oxytricha trifallax, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:259443` matches the YAML identity: parent `NCBITaxon:5943`, rank `SPECIES`, no exact synonyms, one related synonym, genetic code `6`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:259443` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3700`, where `NCBITaxon:1172189` has `organism_count` 1.
- Native GOLD has two exact current-taxid organism rows, three linked projects, and three analysis rows linked through those projects.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1172189`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD side inventories.

## Additional Notes

- None.
