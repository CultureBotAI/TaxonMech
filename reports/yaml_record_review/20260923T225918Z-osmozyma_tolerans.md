# YAML Record Review

- Target: `data/taxa/eukaryota/osmozyma_tolerans.yaml`
- Taxon: `NCBITaxon:85573` (`Osmozyma tolerans`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:85573`, label `Osmozyma tolerans`.
- It is grounded exactly under `NCBITaxon:3315606` (`Osmozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `12`.
- The YAML carries 13 lineage entries from `root` through `Osmozyma`.

## Validation

- `just validate data/taxa/eukaryota/osmozyma_tolerans.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/osmozyma_mogii.yaml data/taxa/eukaryota/osmozyma_tolerans.yaml data/taxa/eukaryota/ostropella_albocincta.yaml data/taxa/eukaryota/otidea_leporina.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53418` contains the seeded identifier with reason `attested rule: Osmozyma tolerans, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:13207` matches the YAML identity: parent `NCBITaxon:3315606`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `12`, and the 2026-09-13 taxonomy snapshot.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:13207` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:43250`, where `NCBITaxon:85573` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705552` / `Osmozyma tolerans NRRL Y-48705`, linked to project `Gp0831595` and no analysis rows.
- Exact StrainInfo side evidence has one direct `NCBITaxon:85573` record, `siID` 179411, and four deposits across that record.

## Completeness

- Exact NCBI type material has nine rows for `NCBITaxon:85573`, covering `NRRL Y-48705` variants and `CBS 8613` or `CBS8613` variants.
- Exact BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:85573`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, native GOLD, or StrainInfo side inventories.

## Additional Notes

- None.
