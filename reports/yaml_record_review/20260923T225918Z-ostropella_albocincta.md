# YAML Record Review

- Target: `data/taxa/eukaryota/ostropella_albocincta.yaml`
- Taxon: `NCBITaxon:464915` (`Ostropella albocincta`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:464915`, label `Ostropella albocincta`.
- It is grounded exactly under `NCBITaxon:464913` (`Ostropella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Ostropella`.

## Validation

- `just validate data/taxa/eukaryota/ostropella_albocincta.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/osmozyma_mogii.yaml data/taxa/eukaryota/osmozyma_tolerans.yaml data/taxa/eukaryota/ostropella_albocincta.yaml data/taxa/eukaryota/otidea_leporina.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55744` contains the seeded identifier with reason `attested rule: Ostropella albocincta, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:104161` matches the YAML identity: parent `NCBITaxon:464913`, rank `SPECIES`, one exact synonym, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:104161` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36303`, where `NCBITaxon:464915` has `organism_count` 2.
- The native GOLD exact current-taxid scan found no local organism, project, or analysis rows for `NCBITaxon:464915`.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:464915`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact native GOLD side inventories.

## Additional Notes

- None.
