# YAML Record Review

- Target: `data/taxa/eukaryota/paramoeba_atlantica.yaml`
- Taxon: `NCBITaxon:1077153` (`Paramoeba atlantica`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1077153`, label `Paramoeba atlantica`.
- It is grounded exactly under `NCBITaxon:200890` (`Paramoeba`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 9 lineage entries from `root` through `Paramoeba`.

## Validation

- `just validate data/taxa/eukaryota/paramoeba_atlantica.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/paramecium_tetraurelia_strain_d4_2.yaml data/taxa/eukaryota/paramoeba_aestuarina.yaml data/taxa/eukaryota/paramoeba_atlantica.yaml data/taxa/eukaryota/paramyrothecium_roridum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57541` contains the seeded identifier with reason `attested rule: Paramoeba atlantica, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:230952` matches the YAML identity: parent `NCBITaxon:200890`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 9 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:230952` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1401`, where `NCBITaxon:1077153` has `organism_count` 1.
- The native GOLD exact current-taxid scan found one organism row for strain `621/1 / CCAP 1560/9`; it found no linked project or analysis rows.

## Completeness

- Exact NCBI type-material, StrainInfo, BacDive, NCBI merged-ID, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:1077153`; the record correctly has `strain_count: 0`.
- No BacDive-derived local strain inventory rows generated `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*` rows for this taxon.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future source refreshes add non-GOLD evidence for this species.

## Additional Notes

- None.
