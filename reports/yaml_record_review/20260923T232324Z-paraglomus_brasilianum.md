# YAML Record Review

- Target: `data/taxa/eukaryota/paraglomus_brasilianum.yaml`
- Taxon: `NCBITaxon:144538` (`Paraglomus brasilianum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:144538`, label `Paraglomus brasilianum`.
- It is grounded exactly under `NCBITaxon:144537` (`Paraglomus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Paraglomus`.

## Validation

- `just validate data/taxa/eukaryota/paraglomus_brasilianum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/paracorniculantispora_psalliotae.yaml data/taxa/eukaryota/paraeutypella_vitis.yaml data/taxa/eukaryota/parafenestella_ontariensis.yaml data/taxa/eukaryota/paraglomus_brasilianum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54024` contains the seeded identifier with reason `attested rule: Paraglomus brasilianum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:29167` matches the YAML identity: parent `NCBITaxon:144537`, rank `SPECIES`, one exact synonym, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:29167` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:10598`, where `NCBITaxon:144538` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row, one project row, and one analysis row for strain `BR232B`.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:144538`; the record correctly has `strain_count: 0`.
- The NCBI merged-ID side inventory contains one old ID that now points at `NCBITaxon:144538`: `NCBITaxon:83572`; it is not retained as a retired taxon, so the YAML correctly has no `replaces` entry.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future source refreshes add non-GOLD evidence for this species.

## Additional Notes

- None.
