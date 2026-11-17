# YAML Record Review

- Target: `data/taxa/eukaryota/pachnocybe_ferruginea.yaml`
- Taxon: `NCBITaxon:70604` (`Pachnocybe ferruginea`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:70604`, label `Pachnocybe ferruginea`.
- It is grounded exactly under `NCBITaxon:70603` (`Pachnocybe`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Pachnocybe`.

## Validation

- `just validate data/taxa/eukaryota/pachnocybe_ferruginea.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ovicillium_attenuatum.yaml data/taxa/eukaryota/oxyrrhis_marina.yaml data/taxa/eukaryota/oxytricha_trifallax.yaml data/taxa/eukaryota/pachnocybe_ferruginea.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53212` contains the seeded identifier with reason `attested rule: Pachnocybe ferruginea, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:9933` matches the YAML identity: parent `NCBITaxon:70603`, rank `SPECIES`, no exact synonyms, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:9933` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41704`, where `NCBITaxon:70604` has `organism_count` 1.
- The native GOLD exact current-taxid scan found no local organism, project, or analysis rows for `NCBITaxon:70604`.
- Exact StrainInfo side evidence has 13 direct `NCBITaxon:70604` records and 15 deposits across those records.

## Completeness

- Exact NCBI type-material, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:70604`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
