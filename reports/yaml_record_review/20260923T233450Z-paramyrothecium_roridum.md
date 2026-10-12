# YAML Record Review

- Target: `data/taxa/eukaryota/paramyrothecium_roridum.yaml`
- Taxon: `NCBITaxon:1859971` (`Paramyrothecium roridum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1859971`, label `Paramyrothecium roridum`.
- It is grounded exactly under `NCBITaxon:1859940` (`Paramyrothecium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Paramyrothecium`.

## Validation

- `just validate data/taxa/eukaryota/paramyrothecium_roridum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paramecium_tetraurelia_strain_d4_2.yaml data/taxa/eukaryota/paramoeba_aestuarina.yaml data/taxa/eukaryota/paramoeba_atlantica.yaml data/taxa/eukaryota/paramyrothecium_roridum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61377` contains the seeded identifier with reason `attested rule: Paramyrothecium roridum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:486197` matches the YAML identity: parent `NCBITaxon:1859940`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:486197` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:16605`, where `NCBITaxon:1859971` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, one project row, and one analysis row for strain `NRRL 2183`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two culture-from-epitype spellings for `NCBITaxon:1859971` on lines 65529-65530, both under `Myrothecium roridum` and centered on `CBS 357.89`.
- Exact StrainInfo side evidence has 62 direct `NCBITaxon:1859971` records and 78 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1859971`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains one old ID that now points at `NCBITaxon:1859971`: `NCBITaxon:62969`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.
