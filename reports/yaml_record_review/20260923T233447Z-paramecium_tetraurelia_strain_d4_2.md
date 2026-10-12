# YAML Record Review

- Target: `data/taxa/eukaryota/paramecium_tetraurelia_strain_d4_2.yaml`
- Taxon: `NCBITaxon:412030` (`Paramecium tetraurelia strain d4-2`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:412030`, label `Paramecium tetraurelia strain d4-2`.
- It is grounded exactly under `NCBITaxon:5888` (`Paramecium tetraurelia`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `6`.
- The YAML carries 12 lineage entries from `root` through `Paramecium tetraurelia`.

## Validation

- `just validate data/taxa/eukaryota/paramecium_tetraurelia_strain_d4_2.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/paramecium_tetraurelia_strain_d4_2.yaml data/taxa/eukaryota/paramoeba_aestuarina.yaml data/taxa/eukaryota/paramoeba_atlantica.yaml data/taxa/eukaryota/paramyrothecium_roridum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55554` contains the seeded identifier with reason `attested rule: Paramecium tetraurelia strain d4-2, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:89691` matches the YAML identity: parent `NCBITaxon:5888`, rank `STRAIN`, one exact synonym, genetic code `6`, and the 2026-09-13 taxonomy snapshot.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:89691` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:34759`, where `NCBITaxon:412030` has `organism_count` 3.
- The native GOLD exact current-taxid scan found one organism row for strain `d4-2`, three project rows, and one analysis row.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:412030`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future source refreshes add non-GOLD strain evidence for this identifier.

## Additional Notes

- None.
