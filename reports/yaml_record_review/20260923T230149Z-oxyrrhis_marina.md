# YAML Record Review

- Target: `data/taxa/eukaryota/oxyrrhis_marina.yaml`
- Taxon: `NCBITaxon:2969` (`Oxyrrhis marina`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2969`, label `Oxyrrhis marina`.
- It is grounded exactly under `NCBITaxon:2968` (`Oxyrrhis`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries nine lineage entries from `root` through `Oxyrrhis`.

## Validation

- `just validate data/taxa/eukaryota/oxyrrhis_marina.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ovicillium_attenuatum.yaml data/taxa/eukaryota/oxyrrhis_marina.yaml data/taxa/eukaryota/oxytricha_trifallax.yaml data/taxa/eukaryota/pachnocybe_ferruginea.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51828` contains the seeded identifier with reason `attested rule: Oxyrrhis marina, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2009` matches the YAML identity: parent `NCBITaxon:2968`, rank `SPECIES`, no exact synonyms, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All nine YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2009` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:29640`, where `NCBITaxon:2969` has `organism_count` 3.
- Native GOLD has five exact current-taxid organism rows, one linked project, and no analysis rows for `NCBITaxon:2969`.
- Exact StrainInfo side evidence has 10 direct `NCBITaxon:2969` records and 11 deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:2969`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD or StrainInfo side inventories.

## Additional Notes

- None.
